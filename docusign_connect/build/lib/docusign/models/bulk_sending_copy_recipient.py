# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BulkSendingCopyRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_code=None, client_user_id=None, custom_fields=None, delivery_method=None, email=None, email_notification=None, embedded_recipient_start_url=None, fax_number=None, id_check_configuration_name=None, id_check_information_input=None, identification_method=None, name=None, note=None, phone_authentication=None, recipient_id=None, recipient_signature_providers=None, role_name=None, sms_authentication=None, social_authentications=None, tabs=None):
        """
        BulkSendingCopyRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_code': 'str',
            'client_user_id': 'str',
            'custom_fields': 'list[str]',
            'delivery_method': 'str',
            'email': 'str',
            'email_notification': 'RecipientEmailNotification',
            'embedded_recipient_start_url': 'str',
            'fax_number': 'str',
            'id_check_configuration_name': 'str',
            'id_check_information_input': 'IdCheckInformationInput',
            'identification_method': 'str',
            'name': 'str',
            'note': 'str',
            'phone_authentication': 'RecipientPhoneAuthentication',
            'recipient_id': 'str',
            'recipient_signature_providers': 'list[RecipientSignatureProvider]',
            'role_name': 'str',
            'sms_authentication': 'RecipientSMSAuthentication',
            'social_authentications': 'list[SocialAuthentication]',
            'tabs': 'list[BulkSendingCopyTab]'
        }

        self.attribute_map = {
            'access_code': 'accessCode',
            'client_user_id': 'clientUserId',
            'custom_fields': 'customFields',
            'delivery_method': 'deliveryMethod',
            'email': 'email',
            'email_notification': 'emailNotification',
            'embedded_recipient_start_url': 'embeddedRecipientStartURL',
            'fax_number': 'faxNumber',
            'id_check_configuration_name': 'idCheckConfigurationName',
            'id_check_information_input': 'idCheckInformationInput',
            'identification_method': 'identificationMethod',
            'name': 'name',
            'note': 'note',
            'phone_authentication': 'phoneAuthentication',
            'recipient_id': 'recipientId',
            'recipient_signature_providers': 'recipientSignatureProviders',
            'role_name': 'roleName',
            'sms_authentication': 'smsAuthentication',
            'social_authentications': 'socialAuthentications',
            'tabs': 'tabs'
        }

        self._access_code = access_code
        self._client_user_id = client_user_id
        self._custom_fields = custom_fields
        self._delivery_method = delivery_method
        self._email = email
        self._email_notification = email_notification
        self._embedded_recipient_start_url = embedded_recipient_start_url
        self._fax_number = fax_number
        self._id_check_configuration_name = id_check_configuration_name
        self._id_check_information_input = id_check_information_input
        self._identification_method = identification_method
        self._name = name
        self._note = note
        self._phone_authentication = phone_authentication
        self._recipient_id = recipient_id
        self._recipient_signature_providers = recipient_signature_providers
        self._role_name = role_name
        self._sms_authentication = sms_authentication
        self._social_authentications = social_authentications
        self._tabs = tabs

    @property
    def access_code(self):
        """
        Gets the access_code of this BulkSendingCopyRecipient.
        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.

        :return: The access_code of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """
        Sets the access_code of this BulkSendingCopyRecipient.
        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.

        :param access_code: The access_code of this BulkSendingCopyRecipient.
        :type: str
        """

        self._access_code = access_code

    @property
    def client_user_id(self):
        """
        Gets the client_user_id of this BulkSendingCopyRecipient.
        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters. 

        :return: The client_user_id of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """
        Sets the client_user_id of this BulkSendingCopyRecipient.
        Specifies whether the recipient is embedded or remote.   If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to  **true**, an error is generated on sending.ng.   Maximum length: 100 characters. 

        :param client_user_id: The client_user_id of this BulkSendingCopyRecipient.
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this BulkSendingCopyRecipient.
        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.

        :return: The custom_fields of this BulkSendingCopyRecipient.
        :rtype: list[str]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this BulkSendingCopyRecipient.
        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.

        :param custom_fields: The custom_fields of this BulkSendingCopyRecipient.
        :type: list[str]
        """

        self._custom_fields = custom_fields

    @property
    def delivery_method(self):
        """
        Gets the delivery_method of this BulkSendingCopyRecipient.
        Reserved: For DocuSign use only.

        :return: The delivery_method of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """
        Sets the delivery_method of this BulkSendingCopyRecipient.
        Reserved: For DocuSign use only.

        :param delivery_method: The delivery_method of this BulkSendingCopyRecipient.
        :type: str
        """

        self._delivery_method = delivery_method

    @property
    def email(self):
        """
        Gets the email of this BulkSendingCopyRecipient.
        

        :return: The email of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this BulkSendingCopyRecipient.
        

        :param email: The email of this BulkSendingCopyRecipient.
        :type: str
        """

        self._email = email

    @property
    def email_notification(self):
        """
        Gets the email_notification of this BulkSendingCopyRecipient.

        :return: The email_notification of this BulkSendingCopyRecipient.
        :rtype: RecipientEmailNotification
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """
        Sets the email_notification of this BulkSendingCopyRecipient.

        :param email_notification: The email_notification of this BulkSendingCopyRecipient.
        :type: RecipientEmailNotification
        """

        self._email_notification = email_notification

    @property
    def embedded_recipient_start_url(self):
        """
        Gets the embedded_recipient_start_url of this BulkSendingCopyRecipient.
        Specifies a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from DocuSign, just as a remote recipient would. When the document link in the email is clicked the recipient is redirected, through DocuSign, to the supplied URL to complete their actions. When routing to the URL, the sender's system (the server responding to the URL) must request a recipient token to launch a signing session.   If set to `SIGN_AT_DOCUSIGN`, the recipient is directed to an embedded signing or viewing process directly at DocuSign. The signing or viewing action is initiated by the DocuSign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that is launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application, DocuSign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets `EmbeddedRecipientStartURL=SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, DocuSign recommends that you use one of the normal DocuSign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) to verify the identity of the recipient.  If the `clientUserId` property is NOT set, and the `embeddedRecipientStartURL` is set, DocuSign will ignore the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the embedded recipient start URL using merge fields. The available merge fields items are: envelopeId, recipientId, recipientName, recipientEmail, and customFields. The `customFields` property must be set fort the recipient or envelope. The merge fields are enclosed in double brackets.   *Example*:   `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]` 

        :return: The embedded_recipient_start_url of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._embedded_recipient_start_url

    @embedded_recipient_start_url.setter
    def embedded_recipient_start_url(self, embedded_recipient_start_url):
        """
        Sets the embedded_recipient_start_url of this BulkSendingCopyRecipient.
        Specifies a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from DocuSign, just as a remote recipient would. When the document link in the email is clicked the recipient is redirected, through DocuSign, to the supplied URL to complete their actions. When routing to the URL, the sender's system (the server responding to the URL) must request a recipient token to launch a signing session.   If set to `SIGN_AT_DOCUSIGN`, the recipient is directed to an embedded signing or viewing process directly at DocuSign. The signing or viewing action is initiated by the DocuSign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that is launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application, DocuSign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets `EmbeddedRecipientStartURL=SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, DocuSign recommends that you use one of the normal DocuSign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) to verify the identity of the recipient.  If the `clientUserId` property is NOT set, and the `embeddedRecipientStartURL` is set, DocuSign will ignore the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the embedded recipient start URL using merge fields. The available merge fields items are: envelopeId, recipientId, recipientName, recipientEmail, and customFields. The `customFields` property must be set fort the recipient or envelope. The merge fields are enclosed in double brackets.   *Example*:   `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]` 

        :param embedded_recipient_start_url: The embedded_recipient_start_url of this BulkSendingCopyRecipient.
        :type: str
        """

        self._embedded_recipient_start_url = embedded_recipient_start_url

    @property
    def fax_number(self):
        """
        Gets the fax_number of this BulkSendingCopyRecipient.
        Reserved:

        :return: The fax_number of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """
        Sets the fax_number of this BulkSendingCopyRecipient.
        Reserved:

        :param fax_number: The fax_number of this BulkSendingCopyRecipient.
        :type: str
        """

        self._fax_number = fax_number

    @property
    def id_check_configuration_name(self):
        """
        Gets the id_check_configuration_name of this BulkSendingCopyRecipient.
        Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient,) This overrides any default authentication setting.  *Example*: Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an envelope, the idCheckConfigurationName should be 'ID Check '. If you wanted to use SMS, it would be 'SMS Auth $' and you would need to add you would need to add phone number information to the `smsAuthentication` node.

        :return: The id_check_configuration_name of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._id_check_configuration_name

    @id_check_configuration_name.setter
    def id_check_configuration_name(self, id_check_configuration_name):
        """
        Sets the id_check_configuration_name of this BulkSendingCopyRecipient.
        Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient,) This overrides any default authentication setting.  *Example*: Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an envelope, the idCheckConfigurationName should be 'ID Check '. If you wanted to use SMS, it would be 'SMS Auth $' and you would need to add you would need to add phone number information to the `smsAuthentication` node.

        :param id_check_configuration_name: The id_check_configuration_name of this BulkSendingCopyRecipient.
        :type: str
        """

        self._id_check_configuration_name = id_check_configuration_name

    @property
    def id_check_information_input(self):
        """
        Gets the id_check_information_input of this BulkSendingCopyRecipient.

        :return: The id_check_information_input of this BulkSendingCopyRecipient.
        :rtype: IdCheckInformationInput
        """
        return self._id_check_information_input

    @id_check_information_input.setter
    def id_check_information_input(self, id_check_information_input):
        """
        Sets the id_check_information_input of this BulkSendingCopyRecipient.

        :param id_check_information_input: The id_check_information_input of this BulkSendingCopyRecipient.
        :type: IdCheckInformationInput
        """

        self._id_check_information_input = id_check_information_input

    @property
    def identification_method(self):
        """
        Gets the identification_method of this BulkSendingCopyRecipient.
        

        :return: The identification_method of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._identification_method

    @identification_method.setter
    def identification_method(self, identification_method):
        """
        Sets the identification_method of this BulkSendingCopyRecipient.
        

        :param identification_method: The identification_method of this BulkSendingCopyRecipient.
        :type: str
        """

        self._identification_method = identification_method

    @property
    def name(self):
        """
        Gets the name of this BulkSendingCopyRecipient.
        

        :return: The name of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BulkSendingCopyRecipient.
        

        :param name: The name of this BulkSendingCopyRecipient.
        :type: str
        """

        self._name = name

    @property
    def note(self):
        """
        Gets the note of this BulkSendingCopyRecipient.
        Specifies a note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen.  Maximum Length: 1000 characters.

        :return: The note of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this BulkSendingCopyRecipient.
        Specifies a note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen.  Maximum Length: 1000 characters.

        :param note: The note of this BulkSendingCopyRecipient.
        :type: str
        """

        self._note = note

    @property
    def phone_authentication(self):
        """
        Gets the phone_authentication of this BulkSendingCopyRecipient.

        :return: The phone_authentication of this BulkSendingCopyRecipient.
        :rtype: RecipientPhoneAuthentication
        """
        return self._phone_authentication

    @phone_authentication.setter
    def phone_authentication(self, phone_authentication):
        """
        Sets the phone_authentication of this BulkSendingCopyRecipient.

        :param phone_authentication: The phone_authentication of this BulkSendingCopyRecipient.
        :type: RecipientPhoneAuthentication
        """

        self._phone_authentication = phone_authentication

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this BulkSendingCopyRecipient.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :return: The recipient_id of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this BulkSendingCopyRecipient.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :param recipient_id: The recipient_id of this BulkSendingCopyRecipient.
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def recipient_signature_providers(self):
        """
        Gets the recipient_signature_providers of this BulkSendingCopyRecipient.
        

        :return: The recipient_signature_providers of this BulkSendingCopyRecipient.
        :rtype: list[RecipientSignatureProvider]
        """
        return self._recipient_signature_providers

    @recipient_signature_providers.setter
    def recipient_signature_providers(self, recipient_signature_providers):
        """
        Sets the recipient_signature_providers of this BulkSendingCopyRecipient.
        

        :param recipient_signature_providers: The recipient_signature_providers of this BulkSendingCopyRecipient.
        :type: list[RecipientSignatureProvider]
        """

        self._recipient_signature_providers = recipient_signature_providers

    @property
    def role_name(self):
        """
        Gets the role_name of this BulkSendingCopyRecipient.
        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.

        :return: The role_name of this BulkSendingCopyRecipient.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """
        Sets the role_name of this BulkSendingCopyRecipient.
        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.

        :param role_name: The role_name of this BulkSendingCopyRecipient.
        :type: str
        """

        self._role_name = role_name

    @property
    def sms_authentication(self):
        """
        Gets the sms_authentication of this BulkSendingCopyRecipient.

        :return: The sms_authentication of this BulkSendingCopyRecipient.
        :rtype: RecipientSMSAuthentication
        """
        return self._sms_authentication

    @sms_authentication.setter
    def sms_authentication(self, sms_authentication):
        """
        Sets the sms_authentication of this BulkSendingCopyRecipient.

        :param sms_authentication: The sms_authentication of this BulkSendingCopyRecipient.
        :type: RecipientSMSAuthentication
        """

        self._sms_authentication = sms_authentication

    @property
    def social_authentications(self):
        """
        Gets the social_authentications of this BulkSendingCopyRecipient.
         Lists the social ID type that can be used for recipient authentication.

        :return: The social_authentications of this BulkSendingCopyRecipient.
        :rtype: list[SocialAuthentication]
        """
        return self._social_authentications

    @social_authentications.setter
    def social_authentications(self, social_authentications):
        """
        Sets the social_authentications of this BulkSendingCopyRecipient.
         Lists the social ID type that can be used for recipient authentication.

        :param social_authentications: The social_authentications of this BulkSendingCopyRecipient.
        :type: list[SocialAuthentication]
        """

        self._social_authentications = social_authentications

    @property
    def tabs(self):
        """
        Gets the tabs of this BulkSendingCopyRecipient.
        

        :return: The tabs of this BulkSendingCopyRecipient.
        :rtype: list[BulkSendingCopyTab]
        """
        return self._tabs

    @tabs.setter
    def tabs(self, tabs):
        """
        Sets the tabs of this BulkSendingCopyRecipient.
        

        :param tabs: The tabs of this BulkSendingCopyRecipient.
        :type: list[BulkSendingCopyTab]
        """

        self._tabs = tabs

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
