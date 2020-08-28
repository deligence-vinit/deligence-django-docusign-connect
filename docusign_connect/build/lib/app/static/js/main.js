function viewfile(){
   var file_name= document.getElementById('file-data').textContent;
    document.getElementById('pdf_view').src=`/getfile/?file=${file_name}`
   document.getElementById('title').innerHTML=`${file_name}`
}

function clearsearch(){
   document.getElementById('sub').click();
}