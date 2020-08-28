import io,os,base64,string,random,uuid
APP_PATH = os.path.dirname(os.path.abspath(__file__)) #current directory path
import sys
sys.path.append(f"../{APP_PATH}")
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser
import json,os
from django.http import HttpResponse,Http404,FileResponse
from app.models import signedData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from docusign.client.api_client import ApiClient
from docusign.client.api_exception import ApiException
from docusign.apis.envelopes_api import EnvelopesApi
from docusign.models.envelope_definition import EnvelopeDefinition
from docusign.models.signer import Signer
from docusign.models.sign_here import SignHere
from docusign.models.tabs import Tabs
from docusign.models.recipients import Recipients
from docusign.models.document import Document
from docusign.models.recipient_view_request import RecipientViewRequest
from xhtml2pdf import pisa
import time
import json
from django.http import HttpResponse,Http404,FileResponse
from . models import signedData
from django.contrib import messages

access_token = '' # auto generated 
# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture. 
f = open(os.path.join(APP_PATH, "../", "config.json"), "rb")
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 

account_id = data.get('account_id')

# The document you wish to send. Path is relative to the root directory of this repo.
user_id= data.get('user_id') #add your user id

# The url of this web application
base_url = data.get('base_url')

# base_url is patient infomation form page url
consent_redirect_url  = data.get('consent_redirect_url')   #url to redirect after consent on first time use
auth_server= data.get('auth_server') #for production use https://account.docusign.com

client_user_id = data.get('integration_key') #integration key

# Used to indicate that the signer will use an embedded
                       # Signing Ceremony. Represents the signer's userId within
                       # your application.
authentication_method = 'None' # How is this application authenticating
                               # the signer? See the `authenticationMethod' definition
                               # https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeViews/createRecipient

# The API base_path
base_path = data.get('base_path')

api_client=None #auto do not change
_token_received = False #auto do not change
expiresTimestamp= 0 #auto do not change

#private key
s = "\n"
private_key=s.join(data.get('private_key'))
TOKEN_REPLACEMENT_IN_SECONDS= 10*60 #auto do not change
TOKEN_EXPIRATION_IN_SECONDS= 3600 #auto do not change

redirect_url='' #auto do not change
consent_scopes = "signature%20impersonation" #auto do not change
# Constants
def random_char():  #function to genrate random string
    return ''.join(random.choice(string.ascii_letters) for x in range(5))



def sign(request):
    global account_id
    global user_id
    global base_url
    global consent_redirect_url
    global auth_server
    global client_user_id
    global base_path
    global private_key
    f = open(os.path.join(APP_PATH, "../", "config.json"), "rb")
    data = json.load(f) 
    account_id = data.get('account_id')
    user_id= data.get('user_id')
    base_url = data.get('base_url')
    consent_redirect_url  = data.get('consent_redirect_url')
    auth_server= data.get('auth_server')
    client_user_id = data.get('integration_key') 
    base_path = data.get('base_path')
    s = "\n"
    private_key=s.join(data.get('private_key'))
    if request.method== 'POST':
        first_name=request.POST.get('first_name')  #sample from fields
        last_name=request.POST.get('last_name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
       #Generate html template from form fields
        message = f"""<html>
        <head>
        </head>
<body>
<br><br>
<br>
  <br>
        <table style="font-size:150%">
        <tr>
                <td style="width:300px;">Name:</td><td style="max-width:400px; white-space:pre-wrap; word-wrap:break-word">{first_name}&nbsp;&nbsp;{last_name}</td></tr>
                <tr><td style="width:300px;">Phone:</td><td style="max-width:400px; white-space:pre-wrap; word-wrap:break-word">{phone}</td></tr>
                <tr><td style="width:300px;">Email:</td><td style="max-width:400px; white-space:pre-wrap; word-wrap:break-word">{email}</td></tr>
                <tr><td style="width:300px;">Address:</td><td style="max-width:400px; white-space:pre-wrap; word-wrap:break-word">{address}</td></tr>
        </table>  
            </body>
        </html>"""
        file_name=f'{first_name}_{random_char()}'  #genrate unique file name
        resultFile = open(os.path.join(APP_PATH, "../docusign/tempf/", f'{file_name}.pdf'), "w+b")  #create  pdf
        pisaStatus = pisa.CreatePDF(message,resultFile) #convert above html to pdf 
        resultFile.close()                              #save pdf file to docusign/tempf folder
              
        doc = f'{file_name}.pdf'            #Generated pdf file name
        """
        The document <file_name> will be signed by <signer_name> via an
        embedded signing ceremony.
        """
        access_token =check_token()         #check for access token
        if access_token == 'exception':
            return redirect(f"{auth_server}/oauth/auth?response_type=code&scope={consent_scopes}&client_id={client_user_id}&redirect_uri={consent_redirect_url}")
        # Recipient Information:
        signer_name = f'{first_name} {last_name}'   
        signer_email = f'{email}'
        #
        # Step 1. The envelope definition is created.
        #         One signHere tab is added.
        #         The document path supplied is relative to the working directory
        #
        # Create the component objects for the envelope definition...
        with open(os.path.join(APP_PATH, "../docusign/tempf/", doc), "rb") as file:      #read pdf file from docusign/tempf folder
            content_bytes = file.read()
        base64_file_content = base64.b64encode(content_bytes).decode('ascii')
        #add pdf to Document
        document = Document( # create the DocuSign document object 
            document_base64 = base64_file_content, 
            name = doc, # can be different from actual file name
            file_extension = 'pdf', # many different document types are accepted
            document_id = 1 # a label used to reference the doc
        )
        #Delete unsinged file after adding to document
        try:
            os.remove(os.path.join(APP_PATH, "../docusign/tempf/", doc))    

        except:
            pass

        # Create the signer recipient model 
        signer = Signer( # The signer
            email = signer_email, name = signer_name, recipient_id = "1", routing_order = "1",
            client_user_id = client_user_id, # Setting the client_user_id marks the signer as embedded
        )

        sign_here = SignHere( # DocuSign SignHere field/tab change position x & y to show sign here tab on page.
            document_id = '1', page_number = '1', recipient_id = '1', tab_label = 'SignHereTab',
            x_position = '350', y_position = '600')

        # Add the tabs model (including the sign_here tab) to the signer
        signer.tabs = Tabs(sign_here_tabs = [sign_here]) # The Tabs object wants arrays of the different field/tab types

        # Next, create the top level envelope definition and populate it.
        envelope_definition = EnvelopeDefinition(
            email_subject = "Please sign this Document",
            documents = [document], # The order in the docs array determines the order in the envelope
            recipients = Recipients(signers = [signer]), # The Recipients object wants arrays for each recipient type
            status = "sent" # requests that the envelope be created and sent.
        )
    #
        #  Step 2. Create/send the envelope.
        #
        api_client = ApiClient()
        api_client.host = base_path
        api_client.set_default_header("Authorization", "Bearer " + access_token)

        envelope_api = EnvelopesApi(api_client)
        results = envelope_api.create_envelope(account_id, envelope_definition=envelope_definition)

        #
        # Step 3. The envelope has been created.
        #         Request a Recipient View URL (the Signing Cdjango_docusign.CustomUsereremony URL)
        name=base64.urlsafe_b64encode(signer_name.encode('utf-8'))
        envelope_id = results.envelope_id
        recipient_view_request = RecipientViewRequest(
            authentication_method = authentication_method,client_user_id = client_user_id,
            recipient_id = '1', return_url = base_url + f'/getpdf/?envelope_id={envelope_id}&name={name}',
            user_name = signer_name, email = signer_email
        )

        results = envelope_api.create_recipient_view(account_id, envelope_id,
            recipient_view_request = recipient_view_request)
        
        #
        # Step 4. The Recipient View URL (the Signing Ceremony URL) has been received.
        #         Redirect the user's browser to it.
        #
        return redirect(results.url)
    return render(request,'form.html')

def get_pdf(request):
    """
    1. Call the envelope get method
    """
    envelope_id=request.GET.get('envelope_id')
    temp_name=request.GET.get('name')
    temp_name=temp_name.replace("b", '').replace("'", '')
    if envelope_id and temp_name:
        name=base64.urlsafe_b64decode(temp_name)
        name=name.decode('utf-8')
        access_token =check_token()
        api_client = ApiClient()
        api_client.host = base_path
        api_client.set_default_header("Authorization", "Bearer " + access_token)
        envelope_api = EnvelopesApi(api_client)
        document_id = 1
        # The SDK always stores the received file as a temp file
        if envelope_id != 0:
            temp_file = envelope_api.get_document(account_id, document_id, envelope_id)
            file_name=os.path.basename(temp_file)
            obj=signedData.objects.create(name=name,file_name=file_name)
            obj.save()
            messages.success(request,'signed')
            return render(request,"done.html",{"file_name":file_name})
        else:
            return HttpResponse("Some error Occured")


def check_token():
    global _token_received
    global access_token
    current_time = int(round(time.time()))
    if not _token_received \
        or ((current_time + TOKEN_REPLACEMENT_IN_SECONDS) >expiresTimestamp):
        access_token=update_token()
    else:
        access_token=access_token
    return access_token

def aud():
    if 'https://' in auth_server:
        aud = auth_server[8:]
    else:
        aud = auth_server[7:]
    return aud

def update_token():
    global _token_received
    global expiresTimestamp
    client = ApiClient()
    try:
        # print("Requesting an access token via JWT grant...")
        client.set_base_path(aud())
        response=client.request_jwt_user_token(client_user_id,
        user_id,
        aud(),
        private_key,
        TOKEN_EXPIRATION_IN_SECONDS)
        access_token=(json.loads(json.dumps(response.__dict__)).get('_access_token'))
        _token_received = True
        expiresTimestamp = (int(round(time.time())) + TOKEN_EXPIRATION_IN_SECONDS)
        # print("Done. Continuing...")
        return access_token
    except ApiException as err:
        print ("\n\nDocuSign Exception!")
        # Special handling for consent_required
        body = err.body.decode('utf8')
        if "consent_required" in body:
            
            return 'exception'
        else:
            print (f" Reason: {err.reason}")
            print (f" Error response: {err.body.decode('utf8')}")

            print("\nDone.\n")
            return 'exception'
    
def download_pdf(request):
    file_name=request.GET.get('file')
    if file_name:
        response=FileResponse(open(os.path.join(APP_PATH, "../docusign/tempf/", file_name), 'rb'))
        return response
    else:
        raise Http404 
        
APP_PATH = os.path.dirname(os.path.abspath(__file__))

def homepage(request):
    return redirect('/form')

def manage(request):
    next=request.GET.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                obj=CustomUser.objects.get(username=username)
                if obj:
                    login(request, user)
                    if next:
                        return redirect(next)
                    else:
                        return redirect('/files/')
                else:
                    messages.error(request, "You are not admin")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})

@login_required(login_url='/manage/')
def detailedView(request):
    f = open(os.path.join(APP_PATH, "../", "config.json"), "rb")
    data = json.load(f) 
    record_per_page=data.get('record_per_page')
    account_id = data.get('account_id')
    user_id= data.get('user_id')
    base_url = data.get('base_url')
    consent_redirect_url  = data.get('consent_redirect_url')
    auth_server= data.get('auth_server')
    integration_key = data.get('integration_key')
    base_path = data.get('base_path')
    s = "\n"
    private_key=s.join(data.get('private_key'))
    if request.method == 'POST':
        post_data=[]
        temp_record_per_page=request.POST.get('record_per_page')
        temp_account_id = request.POST.get('account_id')
        temp_user_id= request.POST.get('user_id')
        temp_base_url = request.POST.get('base_url')
        temp_consent_redirect_url  = request.POST.get('consent_redirect_url')
        temp_auth_server= request.POST.get('auth_server')
        temp_integration_key = request.POST.get('integration_key')
        temp_base_path = request.POST.get('base_path')
        temp_private_key=request.POST.get('private_key')
        temp_private_key=temp_private_key.splitlines()
        temp_data={ "record_per_page":temp_record_per_page,
                    "account_id":temp_account_id,
                    "user_id":temp_user_id,
                    "base_url":temp_base_url,
                    "consent_redirect_url":temp_consent_redirect_url,
                    "auth_server":temp_auth_server,
                    "integration_key":temp_integration_key,
                    "base_path":temp_base_path,
                    "private_key":temp_private_key
                            }
        with open(os.path.join(APP_PATH, "../", "config.json"), 'w') as f1:
            json.dump(temp_data, f1)
            f1.close()
        messages.success(request,'success') 
        return redirect('/detailedView')
    return render(request,'config.html',{'record_per_page':record_per_page,'account_id':account_id,'user_id':user_id,'base_url':base_url,'consent_redirect_url':consent_redirect_url,'auth_server':auth_server,'integration_key':integration_key,'base_path':base_path,'private_key':private_key})

@login_required(login_url='/manage/')
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/manage/')

@login_required(login_url='/manage/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'success')
            return redirect('/detailedView')
        else:
            messages.error(request, 'error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form
    })

@login_required(login_url='/manage/')
def get_file(request):
    file_list=[]
    modal='deactivate'
    search=request.GET.get('search')
    page=request.GET.get('page')
    f = open(os.path.join(APP_PATH, "../", "config.json"), "rb")
    data = json.load(f) 
    record_per_page=data.get('record_per_page')
    if search:
        data_list=signedData.objects.filter(name__icontains=search)
    else:
        data_list=signedData.objects.all()
    paginator = Paginator(data_list, record_per_page)
    try:
        pg_data_list = paginator.page(page)
    except PageNotAnInteger:
        pg_data_list = paginator.page(1)
    except EmptyPage:
        pg_data_list = paginator.page(paginator.num_pages)
    event=request.GET.get('event')
    file_name=request.GET.get('file')
    if (event == 'view' and file_name):
        modal='activate'
    if (event == 'delete' and file_name):
        try:
            obj=signedData.objects.filter(file_name=file_name)
            obj.delete()
            os.remove(os.path.join(APP_PATH, "../docusign/tempf/", file_name))
            messages.success(request,'deleted')    
        except:
            messages.error(request,'file_not_found')
        if search or page:
            return redirect(f'/files/?page={page}&search={search}')
        else:
            return redirect('/files')
    return render(request,'file_list.html',{'file_list':pg_data_list,'search':search,'page':page,'modal':modal,'file_name':file_name})

@login_required(login_url='/manage/')
def download_pdf(request):
    file_name=request.GET.get('file')
    if file_name:
        response=FileResponse(open(os.path.join(APP_PATH, "../docusign/tempf/", file_name), 'rb'))
        return response
    else:
        raise Http404
