# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FolderItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, completed_date_time=None, created_date_time=None, custom_fields=None, description=None, envelope_id=None, envelope_uri=None, is21_cfr_part11=None, is_signature_provider_envelope=None, last_modified=None, name=None, owner_name=None, page_count=None, password=None, sender_email=None, sender_name=None, sent_date_time=None, shared=None, status=None, subject=None, template_id=None, uri=None):
        """
        FolderItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'completed_date_time': 'str',
            'created_date_time': 'str',
            'custom_fields': 'list[CustomFieldV2]',
            'description': 'str',
            'envelope_id': 'str',
            'envelope_uri': 'str',
            'is21_cfr_part11': 'str',
            'is_signature_provider_envelope': 'str',
            'last_modified': 'str',
            'name': 'str',
            'owner_name': 'str',
            'page_count': 'int',
            'password': 'str',
            'sender_email': 'str',
            'sender_name': 'str',
            'sent_date_time': 'str',
            'shared': 'str',
            'status': 'str',
            'subject': 'str',
            'template_id': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'completed_date_time': 'completedDateTime',
            'created_date_time': 'createdDateTime',
            'custom_fields': 'customFields',
            'description': 'description',
            'envelope_id': 'envelopeId',
            'envelope_uri': 'envelopeUri',
            'is21_cfr_part11': 'is21CFRPart11',
            'is_signature_provider_envelope': 'isSignatureProviderEnvelope',
            'last_modified': 'lastModified',
            'name': 'name',
            'owner_name': 'ownerName',
            'page_count': 'pageCount',
            'password': 'password',
            'sender_email': 'senderEmail',
            'sender_name': 'senderName',
            'sent_date_time': 'sentDateTime',
            'shared': 'shared',
            'status': 'status',
            'subject': 'subject',
            'template_id': 'templateId',
            'uri': 'uri'
        }

        self._completed_date_time = completed_date_time
        self._created_date_time = created_date_time
        self._custom_fields = custom_fields
        self._description = description
        self._envelope_id = envelope_id
        self._envelope_uri = envelope_uri
        self._is21_cfr_part11 = is21_cfr_part11
        self._is_signature_provider_envelope = is_signature_provider_envelope
        self._last_modified = last_modified
        self._name = name
        self._owner_name = owner_name
        self._page_count = page_count
        self._password = password
        self._sender_email = sender_email
        self._sender_name = sender_name
        self._sent_date_time = sent_date_time
        self._shared = shared
        self._status = status
        self._subject = subject
        self._template_id = template_id
        self._uri = uri

    @property
    def completed_date_time(self):
        """
        Gets the completed_date_time of this FolderItem.
        Specifies the date and time this item was completed.

        :return: The completed_date_time of this FolderItem.
        :rtype: str
        """
        return self._completed_date_time

    @completed_date_time.setter
    def completed_date_time(self, completed_date_time):
        """
        Sets the completed_date_time of this FolderItem.
        Specifies the date and time this item was completed.

        :param completed_date_time: The completed_date_time of this FolderItem.
        :type: str
        """

        self._completed_date_time = completed_date_time

    @property
    def created_date_time(self):
        """
        Gets the created_date_time of this FolderItem.
        Indicates the date and time the item was created.

        :return: The created_date_time of this FolderItem.
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """
        Sets the created_date_time of this FolderItem.
        Indicates the date and time the item was created.

        :param created_date_time: The created_date_time of this FolderItem.
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this FolderItem.
        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.

        :return: The custom_fields of this FolderItem.
        :rtype: list[CustomFieldV2]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this FolderItem.
        An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each customField string can be a maximum of 100 characters.

        :param custom_fields: The custom_fields of this FolderItem.
        :type: list[CustomFieldV2]
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """
        Gets the description of this FolderItem.
        

        :return: The description of this FolderItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FolderItem.
        

        :param description: The description of this FolderItem.
        :type: str
        """

        self._description = description

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this FolderItem.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this FolderItem.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this FolderItem.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this FolderItem.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def envelope_uri(self):
        """
        Gets the envelope_uri of this FolderItem.
        Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes.

        :return: The envelope_uri of this FolderItem.
        :rtype: str
        """
        return self._envelope_uri

    @envelope_uri.setter
    def envelope_uri(self, envelope_uri):
        """
        Sets the envelope_uri of this FolderItem.
        Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes.

        :param envelope_uri: The envelope_uri of this FolderItem.
        :type: str
        """

        self._envelope_uri = envelope_uri

    @property
    def is21_cfr_part11(self):
        """
        Gets the is21_cfr_part11 of this FolderItem.
        When set to **true**, indicates that this module is enabled on the account.

        :return: The is21_cfr_part11 of this FolderItem.
        :rtype: str
        """
        return self._is21_cfr_part11

    @is21_cfr_part11.setter
    def is21_cfr_part11(self, is21_cfr_part11):
        """
        Sets the is21_cfr_part11 of this FolderItem.
        When set to **true**, indicates that this module is enabled on the account.

        :param is21_cfr_part11: The is21_cfr_part11 of this FolderItem.
        :type: str
        """

        self._is21_cfr_part11 = is21_cfr_part11

    @property
    def is_signature_provider_envelope(self):
        """
        Gets the is_signature_provider_envelope of this FolderItem.
        

        :return: The is_signature_provider_envelope of this FolderItem.
        :rtype: str
        """
        return self._is_signature_provider_envelope

    @is_signature_provider_envelope.setter
    def is_signature_provider_envelope(self, is_signature_provider_envelope):
        """
        Sets the is_signature_provider_envelope of this FolderItem.
        

        :param is_signature_provider_envelope: The is_signature_provider_envelope of this FolderItem.
        :type: str
        """

        self._is_signature_provider_envelope = is_signature_provider_envelope

    @property
    def last_modified(self):
        """
        Gets the last_modified of this FolderItem.
        

        :return: The last_modified of this FolderItem.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this FolderItem.
        

        :param last_modified: The last_modified of this FolderItem.
        :type: str
        """

        self._last_modified = last_modified

    @property
    def name(self):
        """
        Gets the name of this FolderItem.
        

        :return: The name of this FolderItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FolderItem.
        

        :param name: The name of this FolderItem.
        :type: str
        """

        self._name = name

    @property
    def owner_name(self):
        """
        Gets the owner_name of this FolderItem.
        Name of the envelope owner.

        :return: The owner_name of this FolderItem.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """
        Sets the owner_name of this FolderItem.
        Name of the envelope owner.

        :param owner_name: The owner_name of this FolderItem.
        :type: str
        """

        self._owner_name = owner_name

    @property
    def page_count(self):
        """
        Gets the page_count of this FolderItem.
        

        :return: The page_count of this FolderItem.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this FolderItem.
        

        :param page_count: The page_count of this FolderItem.
        :type: int
        """

        self._page_count = page_count

    @property
    def password(self):
        """
        Gets the password of this FolderItem.
        

        :return: The password of this FolderItem.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this FolderItem.
        

        :param password: The password of this FolderItem.
        :type: str
        """

        self._password = password

    @property
    def sender_email(self):
        """
        Gets the sender_email of this FolderItem.
        

        :return: The sender_email of this FolderItem.
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """
        Sets the sender_email of this FolderItem.
        

        :param sender_email: The sender_email of this FolderItem.
        :type: str
        """

        self._sender_email = sender_email

    @property
    def sender_name(self):
        """
        Gets the sender_name of this FolderItem.
        Name of the envelope sender.

        :return: The sender_name of this FolderItem.
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """
        Sets the sender_name of this FolderItem.
        Name of the envelope sender.

        :param sender_name: The sender_name of this FolderItem.
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sent_date_time(self):
        """
        Gets the sent_date_time of this FolderItem.
        The date and time the envelope was sent.

        :return: The sent_date_time of this FolderItem.
        :rtype: str
        """
        return self._sent_date_time

    @sent_date_time.setter
    def sent_date_time(self, sent_date_time):
        """
        Sets the sent_date_time of this FolderItem.
        The date and time the envelope was sent.

        :param sent_date_time: The sent_date_time of this FolderItem.
        :type: str
        """

        self._sent_date_time = sent_date_time

    @property
    def shared(self):
        """
        Gets the shared of this FolderItem.
        When set to **true**, this custom tab is shared.

        :return: The shared of this FolderItem.
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this FolderItem.
        When set to **true**, this custom tab is shared.

        :param shared: The shared of this FolderItem.
        :type: str
        """

        self._shared = shared

    @property
    def status(self):
        """
        Gets the status of this FolderItem.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this FolderItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FolderItem.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this FolderItem.
        :type: str
        """

        self._status = status

    @property
    def subject(self):
        """
        Gets the subject of this FolderItem.
        

        :return: The subject of this FolderItem.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this FolderItem.
        

        :param subject: The subject of this FolderItem.
        :type: str
        """

        self._subject = subject

    @property
    def template_id(self):
        """
        Gets the template_id of this FolderItem.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :return: The template_id of this FolderItem.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this FolderItem.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :param template_id: The template_id of this FolderItem.
        :type: str
        """

        self._template_id = template_id

    @property
    def uri(self):
        """
        Gets the uri of this FolderItem.
        

        :return: The uri of this FolderItem.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this FolderItem.
        

        :param uri: The uri of this FolderItem.
        :type: str
        """

        self._uri = uri

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