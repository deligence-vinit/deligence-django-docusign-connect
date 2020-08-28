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


class DisplayApplianceRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cfr_part11=None, company=None, custom_field2=None, digital_signature_base64=None, digital_signatures_pending=None, email=None, first_name=None, full_name=None, initials_base64=None, in_person_email=None, is_notary=None, is_notary_transaction=None, job_title=None, last_name=None, notary_seal_base64=None, phone_number=None, recipient_complete_count=None, recipient_guid_id=None, recipient_id=None, recipient_status=None, recipient_type=None, require_signer_certificate=None, row_state=None, signature_base64=None, signature_image_id=None, signed=None, signer_apply_tabs=None, signer_attachment_base64=None, user_id=None, user_name=None):
        """
        DisplayApplianceRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cfr_part11': 'bool',
            'company': 'str',
            'custom_field2': 'str',
            'digital_signature_base64': 'str',
            'digital_signatures_pending': 'str',
            'email': 'str',
            'first_name': 'str',
            'full_name': 'str',
            'initials_base64': 'str',
            'in_person_email': 'str',
            'is_notary': 'bool',
            'is_notary_transaction': 'bool',
            'job_title': 'str',
            'last_name': 'str',
            'notary_seal_base64': 'str',
            'phone_number': 'str',
            'recipient_complete_count': 'int',
            'recipient_guid_id': 'str',
            'recipient_id': 'str',
            'recipient_status': 'str',
            'recipient_type': 'str',
            'require_signer_certificate': 'str',
            'row_state': 'str',
            'signature_base64': 'str',
            'signature_image_id': 'str',
            'signed': 'bool',
            'signer_apply_tabs': 'bool',
            'signer_attachment_base64': 'str',
            'user_id': 'str',
            'user_name': 'str'
        }

        self.attribute_map = {
            'cfr_part11': 'cfrPart11',
            'company': 'company',
            'custom_field2': 'customField2',
            'digital_signature_base64': 'digitalSignatureBase64',
            'digital_signatures_pending': 'digitalSignaturesPending',
            'email': 'email',
            'first_name': 'firstName',
            'full_name': 'fullName',
            'initials_base64': 'initialsBase64',
            'in_person_email': 'inPersonEmail',
            'is_notary': 'isNotary',
            'is_notary_transaction': 'isNotaryTransaction',
            'job_title': 'jobTitle',
            'last_name': 'lastName',
            'notary_seal_base64': 'notarySealBase64',
            'phone_number': 'phoneNumber',
            'recipient_complete_count': 'recipientCompleteCount',
            'recipient_guid_id': 'recipientGuidId',
            'recipient_id': 'recipientId',
            'recipient_status': 'recipientStatus',
            'recipient_type': 'recipientType',
            'require_signer_certificate': 'requireSignerCertificate',
            'row_state': 'rowState',
            'signature_base64': 'signatureBase64',
            'signature_image_id': 'signatureImageId',
            'signed': 'signed',
            'signer_apply_tabs': 'signerApplyTabs',
            'signer_attachment_base64': 'signerAttachmentBase64',
            'user_id': 'userId',
            'user_name': 'userName'
        }

        self._cfr_part11 = cfr_part11
        self._company = company
        self._custom_field2 = custom_field2
        self._digital_signature_base64 = digital_signature_base64
        self._digital_signatures_pending = digital_signatures_pending
        self._email = email
        self._first_name = first_name
        self._full_name = full_name
        self._initials_base64 = initials_base64
        self._in_person_email = in_person_email
        self._is_notary = is_notary
        self._is_notary_transaction = is_notary_transaction
        self._job_title = job_title
        self._last_name = last_name
        self._notary_seal_base64 = notary_seal_base64
        self._phone_number = phone_number
        self._recipient_complete_count = recipient_complete_count
        self._recipient_guid_id = recipient_guid_id
        self._recipient_id = recipient_id
        self._recipient_status = recipient_status
        self._recipient_type = recipient_type
        self._require_signer_certificate = require_signer_certificate
        self._row_state = row_state
        self._signature_base64 = signature_base64
        self._signature_image_id = signature_image_id
        self._signed = signed
        self._signer_apply_tabs = signer_apply_tabs
        self._signer_attachment_base64 = signer_attachment_base64
        self._user_id = user_id
        self._user_name = user_name

    @property
    def cfr_part11(self):
        """
        Gets the cfr_part11 of this DisplayApplianceRecipient.
        

        :return: The cfr_part11 of this DisplayApplianceRecipient.
        :rtype: bool
        """
        return self._cfr_part11

    @cfr_part11.setter
    def cfr_part11(self, cfr_part11):
        """
        Sets the cfr_part11 of this DisplayApplianceRecipient.
        

        :param cfr_part11: The cfr_part11 of this DisplayApplianceRecipient.
        :type: bool
        """

        self._cfr_part11 = cfr_part11

    @property
    def company(self):
        """
        Gets the company of this DisplayApplianceRecipient.
        

        :return: The company of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this DisplayApplianceRecipient.
        

        :param company: The company of this DisplayApplianceRecipient.
        :type: str
        """

        self._company = company

    @property
    def custom_field2(self):
        """
        Gets the custom_field2 of this DisplayApplianceRecipient.
        

        :return: The custom_field2 of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._custom_field2

    @custom_field2.setter
    def custom_field2(self, custom_field2):
        """
        Sets the custom_field2 of this DisplayApplianceRecipient.
        

        :param custom_field2: The custom_field2 of this DisplayApplianceRecipient.
        :type: str
        """

        self._custom_field2 = custom_field2

    @property
    def digital_signature_base64(self):
        """
        Gets the digital_signature_base64 of this DisplayApplianceRecipient.
        

        :return: The digital_signature_base64 of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._digital_signature_base64

    @digital_signature_base64.setter
    def digital_signature_base64(self, digital_signature_base64):
        """
        Sets the digital_signature_base64 of this DisplayApplianceRecipient.
        

        :param digital_signature_base64: The digital_signature_base64 of this DisplayApplianceRecipient.
        :type: str
        """

        self._digital_signature_base64 = digital_signature_base64

    @property
    def digital_signatures_pending(self):
        """
        Gets the digital_signatures_pending of this DisplayApplianceRecipient.
        

        :return: The digital_signatures_pending of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._digital_signatures_pending

    @digital_signatures_pending.setter
    def digital_signatures_pending(self, digital_signatures_pending):
        """
        Sets the digital_signatures_pending of this DisplayApplianceRecipient.
        

        :param digital_signatures_pending: The digital_signatures_pending of this DisplayApplianceRecipient.
        :type: str
        """

        self._digital_signatures_pending = digital_signatures_pending

    @property
    def email(self):
        """
        Gets the email of this DisplayApplianceRecipient.
        

        :return: The email of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this DisplayApplianceRecipient.
        

        :param email: The email of this DisplayApplianceRecipient.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this DisplayApplianceRecipient.
        The user's first name.  Maximum Length: 50 characters.

        :return: The first_name of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this DisplayApplianceRecipient.
        The user's first name.  Maximum Length: 50 characters.

        :param first_name: The first_name of this DisplayApplianceRecipient.
        :type: str
        """

        self._first_name = first_name

    @property
    def full_name(self):
        """
        Gets the full_name of this DisplayApplianceRecipient.
        

        :return: The full_name of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this DisplayApplianceRecipient.
        

        :param full_name: The full_name of this DisplayApplianceRecipient.
        :type: str
        """

        self._full_name = full_name

    @property
    def initials_base64(self):
        """
        Gets the initials_base64 of this DisplayApplianceRecipient.
        

        :return: The initials_base64 of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._initials_base64

    @initials_base64.setter
    def initials_base64(self, initials_base64):
        """
        Sets the initials_base64 of this DisplayApplianceRecipient.
        

        :param initials_base64: The initials_base64 of this DisplayApplianceRecipient.
        :type: str
        """

        self._initials_base64 = initials_base64

    @property
    def in_person_email(self):
        """
        Gets the in_person_email of this DisplayApplianceRecipient.
        

        :return: The in_person_email of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._in_person_email

    @in_person_email.setter
    def in_person_email(self, in_person_email):
        """
        Sets the in_person_email of this DisplayApplianceRecipient.
        

        :param in_person_email: The in_person_email of this DisplayApplianceRecipient.
        :type: str
        """

        self._in_person_email = in_person_email

    @property
    def is_notary(self):
        """
        Gets the is_notary of this DisplayApplianceRecipient.
        

        :return: The is_notary of this DisplayApplianceRecipient.
        :rtype: bool
        """
        return self._is_notary

    @is_notary.setter
    def is_notary(self, is_notary):
        """
        Sets the is_notary of this DisplayApplianceRecipient.
        

        :param is_notary: The is_notary of this DisplayApplianceRecipient.
        :type: bool
        """

        self._is_notary = is_notary

    @property
    def is_notary_transaction(self):
        """
        Gets the is_notary_transaction of this DisplayApplianceRecipient.
        

        :return: The is_notary_transaction of this DisplayApplianceRecipient.
        :rtype: bool
        """
        return self._is_notary_transaction

    @is_notary_transaction.setter
    def is_notary_transaction(self, is_notary_transaction):
        """
        Sets the is_notary_transaction of this DisplayApplianceRecipient.
        

        :param is_notary_transaction: The is_notary_transaction of this DisplayApplianceRecipient.
        :type: bool
        """

        self._is_notary_transaction = is_notary_transaction

    @property
    def job_title(self):
        """
        Gets the job_title of this DisplayApplianceRecipient.
        

        :return: The job_title of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """
        Sets the job_title of this DisplayApplianceRecipient.
        

        :param job_title: The job_title of this DisplayApplianceRecipient.
        :type: str
        """

        self._job_title = job_title

    @property
    def last_name(self):
        """
        Gets the last_name of this DisplayApplianceRecipient.
        

        :return: The last_name of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this DisplayApplianceRecipient.
        

        :param last_name: The last_name of this DisplayApplianceRecipient.
        :type: str
        """

        self._last_name = last_name

    @property
    def notary_seal_base64(self):
        """
        Gets the notary_seal_base64 of this DisplayApplianceRecipient.
        

        :return: The notary_seal_base64 of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._notary_seal_base64

    @notary_seal_base64.setter
    def notary_seal_base64(self, notary_seal_base64):
        """
        Sets the notary_seal_base64 of this DisplayApplianceRecipient.
        

        :param notary_seal_base64: The notary_seal_base64 of this DisplayApplianceRecipient.
        :type: str
        """

        self._notary_seal_base64 = notary_seal_base64

    @property
    def phone_number(self):
        """
        Gets the phone_number of this DisplayApplianceRecipient.
        

        :return: The phone_number of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this DisplayApplianceRecipient.
        

        :param phone_number: The phone_number of this DisplayApplianceRecipient.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def recipient_complete_count(self):
        """
        Gets the recipient_complete_count of this DisplayApplianceRecipient.
        

        :return: The recipient_complete_count of this DisplayApplianceRecipient.
        :rtype: int
        """
        return self._recipient_complete_count

    @recipient_complete_count.setter
    def recipient_complete_count(self, recipient_complete_count):
        """
        Sets the recipient_complete_count of this DisplayApplianceRecipient.
        

        :param recipient_complete_count: The recipient_complete_count of this DisplayApplianceRecipient.
        :type: int
        """

        self._recipient_complete_count = recipient_complete_count

    @property
    def recipient_guid_id(self):
        """
        Gets the recipient_guid_id of this DisplayApplianceRecipient.
        

        :return: The recipient_guid_id of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._recipient_guid_id

    @recipient_guid_id.setter
    def recipient_guid_id(self, recipient_guid_id):
        """
        Sets the recipient_guid_id of this DisplayApplianceRecipient.
        

        :param recipient_guid_id: The recipient_guid_id of this DisplayApplianceRecipient.
        :type: str
        """

        self._recipient_guid_id = recipient_guid_id

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this DisplayApplianceRecipient.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :return: The recipient_id of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this DisplayApplianceRecipient.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :param recipient_id: The recipient_id of this DisplayApplianceRecipient.
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def recipient_status(self):
        """
        Gets the recipient_status of this DisplayApplianceRecipient.
        

        :return: The recipient_status of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._recipient_status

    @recipient_status.setter
    def recipient_status(self, recipient_status):
        """
        Sets the recipient_status of this DisplayApplianceRecipient.
        

        :param recipient_status: The recipient_status of this DisplayApplianceRecipient.
        :type: str
        """

        self._recipient_status = recipient_status

    @property
    def recipient_type(self):
        """
        Gets the recipient_type of this DisplayApplianceRecipient.
        

        :return: The recipient_type of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type):
        """
        Sets the recipient_type of this DisplayApplianceRecipient.
        

        :param recipient_type: The recipient_type of this DisplayApplianceRecipient.
        :type: str
        """

        self._recipient_type = recipient_type

    @property
    def require_signer_certificate(self):
        """
        Gets the require_signer_certificate of this DisplayApplianceRecipient.
        

        :return: The require_signer_certificate of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._require_signer_certificate

    @require_signer_certificate.setter
    def require_signer_certificate(self, require_signer_certificate):
        """
        Sets the require_signer_certificate of this DisplayApplianceRecipient.
        

        :param require_signer_certificate: The require_signer_certificate of this DisplayApplianceRecipient.
        :type: str
        """

        self._require_signer_certificate = require_signer_certificate

    @property
    def row_state(self):
        """
        Gets the row_state of this DisplayApplianceRecipient.
        

        :return: The row_state of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._row_state

    @row_state.setter
    def row_state(self, row_state):
        """
        Sets the row_state of this DisplayApplianceRecipient.
        

        :param row_state: The row_state of this DisplayApplianceRecipient.
        :type: str
        """

        self._row_state = row_state

    @property
    def signature_base64(self):
        """
        Gets the signature_base64 of this DisplayApplianceRecipient.
        

        :return: The signature_base64 of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._signature_base64

    @signature_base64.setter
    def signature_base64(self, signature_base64):
        """
        Sets the signature_base64 of this DisplayApplianceRecipient.
        

        :param signature_base64: The signature_base64 of this DisplayApplianceRecipient.
        :type: str
        """

        self._signature_base64 = signature_base64

    @property
    def signature_image_id(self):
        """
        Gets the signature_image_id of this DisplayApplianceRecipient.
        

        :return: The signature_image_id of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._signature_image_id

    @signature_image_id.setter
    def signature_image_id(self, signature_image_id):
        """
        Sets the signature_image_id of this DisplayApplianceRecipient.
        

        :param signature_image_id: The signature_image_id of this DisplayApplianceRecipient.
        :type: str
        """

        self._signature_image_id = signature_image_id

    @property
    def signed(self):
        """
        Gets the signed of this DisplayApplianceRecipient.
        

        :return: The signed of this DisplayApplianceRecipient.
        :rtype: bool
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        """
        Sets the signed of this DisplayApplianceRecipient.
        

        :param signed: The signed of this DisplayApplianceRecipient.
        :type: bool
        """

        self._signed = signed

    @property
    def signer_apply_tabs(self):
        """
        Gets the signer_apply_tabs of this DisplayApplianceRecipient.
        

        :return: The signer_apply_tabs of this DisplayApplianceRecipient.
        :rtype: bool
        """
        return self._signer_apply_tabs

    @signer_apply_tabs.setter
    def signer_apply_tabs(self, signer_apply_tabs):
        """
        Sets the signer_apply_tabs of this DisplayApplianceRecipient.
        

        :param signer_apply_tabs: The signer_apply_tabs of this DisplayApplianceRecipient.
        :type: bool
        """

        self._signer_apply_tabs = signer_apply_tabs

    @property
    def signer_attachment_base64(self):
        """
        Gets the signer_attachment_base64 of this DisplayApplianceRecipient.
        

        :return: The signer_attachment_base64 of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._signer_attachment_base64

    @signer_attachment_base64.setter
    def signer_attachment_base64(self, signer_attachment_base64):
        """
        Sets the signer_attachment_base64 of this DisplayApplianceRecipient.
        

        :param signer_attachment_base64: The signer_attachment_base64 of this DisplayApplianceRecipient.
        :type: str
        """

        self._signer_attachment_base64 = signer_attachment_base64

    @property
    def user_id(self):
        """
        Gets the user_id of this DisplayApplianceRecipient.
        

        :return: The user_id of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this DisplayApplianceRecipient.
        

        :param user_id: The user_id of this DisplayApplianceRecipient.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """
        Gets the user_name of this DisplayApplianceRecipient.
        

        :return: The user_name of this DisplayApplianceRecipient.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DisplayApplianceRecipient.
        

        :param user_name: The user_name of this DisplayApplianceRecipient.
        :type: str
        """

        self._user_name = user_name

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
