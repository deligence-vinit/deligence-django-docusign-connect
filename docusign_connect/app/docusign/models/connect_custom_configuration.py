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


class ConnectCustomConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allow_envelope_publish=None, allow_salesforce_publish=None, all_users=None, configuration_type=None, connect_id=None, enable_log=None, envelope_events=None, event_data=None, external_folder_id=None, external_folder_label=None, include_certificate_of_completion=None, include_cert_soap_header=None, include_document_fields=None, include_documents=None, include_envelope_void_reason=None, include_hmac=None, include_sender_accountas_custom_field=None, include_time_zone_information=None, name=None, password=None, recipient_events=None, require_mutual_tls=None, requires_acknowledgement=None, salesforce_api_version=None, salesforce_authcode=None, salesforce_call_back_url=None, salesforce_documents_as_content_files=None, sender_override=None, sender_selectable_items=None, sf_objects=None, sign_message_with_x509_certificate=None, soap_namespace=None, url_to_publish_to=None, user_ids=None, user_name=None, use_soap_interface=None):
        """
        ConnectCustomConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allow_envelope_publish': 'str',
            'allow_salesforce_publish': 'str',
            'all_users': 'str',
            'configuration_type': 'str',
            'connect_id': 'str',
            'enable_log': 'str',
            'envelope_events': 'list[str]',
            'event_data': 'ConnectEventData',
            'external_folder_id': 'str',
            'external_folder_label': 'str',
            'include_certificate_of_completion': 'str',
            'include_cert_soap_header': 'str',
            'include_document_fields': 'str',
            'include_documents': 'str',
            'include_envelope_void_reason': 'str',
            'include_hmac': 'str',
            'include_sender_accountas_custom_field': 'str',
            'include_time_zone_information': 'str',
            'name': 'str',
            'password': 'str',
            'recipient_events': 'list[str]',
            'require_mutual_tls': 'str',
            'requires_acknowledgement': 'str',
            'salesforce_api_version': 'str',
            'salesforce_authcode': 'str',
            'salesforce_call_back_url': 'str',
            'salesforce_documents_as_content_files': 'str',
            'sender_override': 'str',
            'sender_selectable_items': 'list[str]',
            'sf_objects': 'list[ConnectSalesforceObject]',
            'sign_message_with_x509_certificate': 'str',
            'soap_namespace': 'str',
            'url_to_publish_to': 'str',
            'user_ids': 'list[str]',
            'user_name': 'str',
            'use_soap_interface': 'str'
        }

        self.attribute_map = {
            'allow_envelope_publish': 'allowEnvelopePublish',
            'allow_salesforce_publish': 'allowSalesforcePublish',
            'all_users': 'allUsers',
            'configuration_type': 'configurationType',
            'connect_id': 'connectId',
            'enable_log': 'enableLog',
            'envelope_events': 'envelopeEvents',
            'event_data': 'eventData',
            'external_folder_id': 'externalFolderId',
            'external_folder_label': 'externalFolderLabel',
            'include_certificate_of_completion': 'includeCertificateOfCompletion',
            'include_cert_soap_header': 'includeCertSoapHeader',
            'include_document_fields': 'includeDocumentFields',
            'include_documents': 'includeDocuments',
            'include_envelope_void_reason': 'includeEnvelopeVoidReason',
            'include_hmac': 'includeHMAC',
            'include_sender_accountas_custom_field': 'includeSenderAccountasCustomField',
            'include_time_zone_information': 'includeTimeZoneInformation',
            'name': 'name',
            'password': 'password',
            'recipient_events': 'recipientEvents',
            'require_mutual_tls': 'requireMutualTls',
            'requires_acknowledgement': 'requiresAcknowledgement',
            'salesforce_api_version': 'salesforceApiVersion',
            'salesforce_authcode': 'salesforceAuthcode',
            'salesforce_call_back_url': 'salesforceCallBackUrl',
            'salesforce_documents_as_content_files': 'salesforceDocumentsAsContentFiles',
            'sender_override': 'senderOverride',
            'sender_selectable_items': 'senderSelectableItems',
            'sf_objects': 'sfObjects',
            'sign_message_with_x509_certificate': 'signMessageWithX509Certificate',
            'soap_namespace': 'soapNamespace',
            'url_to_publish_to': 'urlToPublishTo',
            'user_ids': 'userIds',
            'user_name': 'userName',
            'use_soap_interface': 'useSoapInterface'
        }

        self._allow_envelope_publish = allow_envelope_publish
        self._allow_salesforce_publish = allow_salesforce_publish
        self._all_users = all_users
        self._configuration_type = configuration_type
        self._connect_id = connect_id
        self._enable_log = enable_log
        self._envelope_events = envelope_events
        self._event_data = event_data
        self._external_folder_id = external_folder_id
        self._external_folder_label = external_folder_label
        self._include_certificate_of_completion = include_certificate_of_completion
        self._include_cert_soap_header = include_cert_soap_header
        self._include_document_fields = include_document_fields
        self._include_documents = include_documents
        self._include_envelope_void_reason = include_envelope_void_reason
        self._include_hmac = include_hmac
        self._include_sender_accountas_custom_field = include_sender_accountas_custom_field
        self._include_time_zone_information = include_time_zone_information
        self._name = name
        self._password = password
        self._recipient_events = recipient_events
        self._require_mutual_tls = require_mutual_tls
        self._requires_acknowledgement = requires_acknowledgement
        self._salesforce_api_version = salesforce_api_version
        self._salesforce_authcode = salesforce_authcode
        self._salesforce_call_back_url = salesforce_call_back_url
        self._salesforce_documents_as_content_files = salesforce_documents_as_content_files
        self._sender_override = sender_override
        self._sender_selectable_items = sender_selectable_items
        self._sf_objects = sf_objects
        self._sign_message_with_x509_certificate = sign_message_with_x509_certificate
        self._soap_namespace = soap_namespace
        self._url_to_publish_to = url_to_publish_to
        self._user_ids = user_ids
        self._user_name = user_name
        self._use_soap_interface = use_soap_interface

    @property
    def allow_envelope_publish(self):
        """
        Gets the allow_envelope_publish of this ConnectCustomConfiguration.
        When set to **true**, data is sent to the urlToPublishTo web address. This option can be set to false to stop sending data while maintaining the Connect configuration information.

        :return: The allow_envelope_publish of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._allow_envelope_publish

    @allow_envelope_publish.setter
    def allow_envelope_publish(self, allow_envelope_publish):
        """
        Sets the allow_envelope_publish of this ConnectCustomConfiguration.
        When set to **true**, data is sent to the urlToPublishTo web address. This option can be set to false to stop sending data while maintaining the Connect configuration information.

        :param allow_envelope_publish: The allow_envelope_publish of this ConnectCustomConfiguration.
        :type: str
        """

        self._allow_envelope_publish = allow_envelope_publish

    @property
    def allow_salesforce_publish(self):
        """
        Gets the allow_salesforce_publish of this ConnectCustomConfiguration.
        

        :return: The allow_salesforce_publish of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._allow_salesforce_publish

    @allow_salesforce_publish.setter
    def allow_salesforce_publish(self, allow_salesforce_publish):
        """
        Sets the allow_salesforce_publish of this ConnectCustomConfiguration.
        

        :param allow_salesforce_publish: The allow_salesforce_publish of this ConnectCustomConfiguration.
        :type: str
        """

        self._allow_salesforce_publish = allow_salesforce_publish

    @property
    def all_users(self):
        """
        Gets the all_users of this ConnectCustomConfiguration.
        When set to **true**, the tracked envelope and recipient events for all users, including users that are added a later time, are sent through Connect.

        :return: The all_users of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._all_users

    @all_users.setter
    def all_users(self, all_users):
        """
        Sets the all_users of this ConnectCustomConfiguration.
        When set to **true**, the tracked envelope and recipient events for all users, including users that are added a later time, are sent through Connect.

        :param all_users: The all_users of this ConnectCustomConfiguration.
        :type: str
        """

        self._all_users = all_users

    @property
    def configuration_type(self):
        """
        Gets the configuration_type of this ConnectCustomConfiguration.
        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.

        :return: The configuration_type of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """
        Sets the configuration_type of this ConnectCustomConfiguration.
        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.

        :param configuration_type: The configuration_type of this ConnectCustomConfiguration.
        :type: str
        """

        self._configuration_type = configuration_type

    @property
    def connect_id(self):
        """
        Gets the connect_id of this ConnectCustomConfiguration.
         Specifies the DocuSign generated ID for the Connect configuration.  

        :return: The connect_id of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._connect_id

    @connect_id.setter
    def connect_id(self, connect_id):
        """
        Sets the connect_id of this ConnectCustomConfiguration.
         Specifies the DocuSign generated ID for the Connect configuration.  

        :param connect_id: The connect_id of this ConnectCustomConfiguration.
        :type: str
        """

        self._connect_id = connect_id

    @property
    def enable_log(self):
        """
        Gets the enable_log of this ConnectCustomConfiguration.
        This turns Connect logging on or off. When set to **true**, logging is turned on.

        :return: The enable_log of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._enable_log

    @enable_log.setter
    def enable_log(self, enable_log):
        """
        Sets the enable_log of this ConnectCustomConfiguration.
        This turns Connect logging on or off. When set to **true**, logging is turned on.

        :param enable_log: The enable_log of this ConnectCustomConfiguration.
        :type: str
        """

        self._enable_log = enable_log

    @property
    def envelope_events(self):
        """
        Gets the envelope_events of this ConnectCustomConfiguration.
        A comma separated list of Ã¯Â¿Â½EnvelopeÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, and Voided.

        :return: The envelope_events of this ConnectCustomConfiguration.
        :rtype: list[str]
        """
        return self._envelope_events

    @envelope_events.setter
    def envelope_events(self, envelope_events):
        """
        Sets the envelope_events of this ConnectCustomConfiguration.
        A comma separated list of Ã¯Â¿Â½EnvelopeÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, and Voided.

        :param envelope_events: The envelope_events of this ConnectCustomConfiguration.
        :type: list[str]
        """

        self._envelope_events = envelope_events

    @property
    def event_data(self):
        """
        Gets the event_data of this ConnectCustomConfiguration.

        :return: The event_data of this ConnectCustomConfiguration.
        :rtype: ConnectEventData
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """
        Sets the event_data of this ConnectCustomConfiguration.

        :param event_data: The event_data of this ConnectCustomConfiguration.
        :type: ConnectEventData
        """

        self._event_data = event_data

    @property
    def external_folder_id(self):
        """
        Gets the external_folder_id of this ConnectCustomConfiguration.
        

        :return: The external_folder_id of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._external_folder_id

    @external_folder_id.setter
    def external_folder_id(self, external_folder_id):
        """
        Sets the external_folder_id of this ConnectCustomConfiguration.
        

        :param external_folder_id: The external_folder_id of this ConnectCustomConfiguration.
        :type: str
        """

        self._external_folder_id = external_folder_id

    @property
    def external_folder_label(self):
        """
        Gets the external_folder_label of this ConnectCustomConfiguration.
        

        :return: The external_folder_label of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._external_folder_label

    @external_folder_label.setter
    def external_folder_label(self, external_folder_label):
        """
        Sets the external_folder_label of this ConnectCustomConfiguration.
        

        :param external_folder_label: The external_folder_label of this ConnectCustomConfiguration.
        :type: str
        """

        self._external_folder_label = external_folder_label

    @property
    def include_certificate_of_completion(self):
        """
        Gets the include_certificate_of_completion of this ConnectCustomConfiguration.
        When set to **true**, the Connect Service includes the Certificate of Completion with completed envelopes. 

        :return: The include_certificate_of_completion of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_certificate_of_completion

    @include_certificate_of_completion.setter
    def include_certificate_of_completion(self, include_certificate_of_completion):
        """
        Sets the include_certificate_of_completion of this ConnectCustomConfiguration.
        When set to **true**, the Connect Service includes the Certificate of Completion with completed envelopes. 

        :param include_certificate_of_completion: The include_certificate_of_completion of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_certificate_of_completion = include_certificate_of_completion

    @property
    def include_cert_soap_header(self):
        """
        Gets the include_cert_soap_header of this ConnectCustomConfiguration.
        

        :return: The include_cert_soap_header of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_cert_soap_header

    @include_cert_soap_header.setter
    def include_cert_soap_header(self, include_cert_soap_header):
        """
        Sets the include_cert_soap_header of this ConnectCustomConfiguration.
        

        :param include_cert_soap_header: The include_cert_soap_header of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_cert_soap_header = include_cert_soap_header

    @property
    def include_document_fields(self):
        """
        Gets the include_document_fields of this ConnectCustomConfiguration.
        When set to **true**, the Document Fields associated with envelope documents are included in the data. Document Fields are optional custom name-value pairs added to documents using the API. 

        :return: The include_document_fields of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_document_fields

    @include_document_fields.setter
    def include_document_fields(self, include_document_fields):
        """
        Sets the include_document_fields of this ConnectCustomConfiguration.
        When set to **true**, the Document Fields associated with envelope documents are included in the data. Document Fields are optional custom name-value pairs added to documents using the API. 

        :param include_document_fields: The include_document_fields of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_document_fields = include_document_fields

    @property
    def include_documents(self):
        """
        Gets the include_documents of this ConnectCustomConfiguration.
        When set to **true**, Connect will send the PDF document along with the update XML.

        :return: The include_documents of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_documents

    @include_documents.setter
    def include_documents(self, include_documents):
        """
        Sets the include_documents of this ConnectCustomConfiguration.
        When set to **true**, Connect will send the PDF document along with the update XML.

        :param include_documents: The include_documents of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_documents = include_documents

    @property
    def include_envelope_void_reason(self):
        """
        Gets the include_envelope_void_reason of this ConnectCustomConfiguration.
        When set to **true**, Connect will include the voidedReason for voided envelopes.

        :return: The include_envelope_void_reason of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_envelope_void_reason

    @include_envelope_void_reason.setter
    def include_envelope_void_reason(self, include_envelope_void_reason):
        """
        Sets the include_envelope_void_reason of this ConnectCustomConfiguration.
        When set to **true**, Connect will include the voidedReason for voided envelopes.

        :param include_envelope_void_reason: The include_envelope_void_reason of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_envelope_void_reason = include_envelope_void_reason

    @property
    def include_hmac(self):
        """
        Gets the include_hmac of this ConnectCustomConfiguration.
        

        :return: The include_hmac of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_hmac

    @include_hmac.setter
    def include_hmac(self, include_hmac):
        """
        Sets the include_hmac of this ConnectCustomConfiguration.
        

        :param include_hmac: The include_hmac of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_hmac = include_hmac

    @property
    def include_sender_accountas_custom_field(self):
        """
        Gets the include_sender_accountas_custom_field of this ConnectCustomConfiguration.
        When set to **true**, Connect will include the sender account as Custom Field in the data.

        :return: The include_sender_accountas_custom_field of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_sender_accountas_custom_field

    @include_sender_accountas_custom_field.setter
    def include_sender_accountas_custom_field(self, include_sender_accountas_custom_field):
        """
        Sets the include_sender_accountas_custom_field of this ConnectCustomConfiguration.
        When set to **true**, Connect will include the sender account as Custom Field in the data.

        :param include_sender_accountas_custom_field: The include_sender_accountas_custom_field of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_sender_accountas_custom_field = include_sender_accountas_custom_field

    @property
    def include_time_zone_information(self):
        """
        Gets the include_time_zone_information of this ConnectCustomConfiguration.
        When set to **true**, Connect will include the envelope time zone information.

        :return: The include_time_zone_information of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._include_time_zone_information

    @include_time_zone_information.setter
    def include_time_zone_information(self, include_time_zone_information):
        """
        Sets the include_time_zone_information of this ConnectCustomConfiguration.
        When set to **true**, Connect will include the envelope time zone information.

        :param include_time_zone_information: The include_time_zone_information of this ConnectCustomConfiguration.
        :type: str
        """

        self._include_time_zone_information = include_time_zone_information

    @property
    def name(self):
        """
        Gets the name of this ConnectCustomConfiguration.
        The name of the Connect configuration. The name helps identify the configuration in the list.

        :return: The name of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectCustomConfiguration.
        The name of the Connect configuration. The name helps identify the configuration in the list.

        :param name: The name of this ConnectCustomConfiguration.
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """
        Gets the password of this ConnectCustomConfiguration.
        

        :return: The password of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ConnectCustomConfiguration.
        

        :param password: The password of this ConnectCustomConfiguration.
        :type: str
        """

        self._password = password

    @property
    def recipient_events(self):
        """
        Gets the recipient_events of this ConnectCustomConfiguration.
        A comma separated list of Ã¯Â¿Â½RecipientÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded.

        :return: The recipient_events of this ConnectCustomConfiguration.
        :rtype: list[str]
        """
        return self._recipient_events

    @recipient_events.setter
    def recipient_events(self, recipient_events):
        """
        Sets the recipient_events of this ConnectCustomConfiguration.
        A comma separated list of Ã¯Â¿Â½RecipientÃ¯Â¿Â½ related events that are tracked through Connect. The possible event values are: Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded.

        :param recipient_events: The recipient_events of this ConnectCustomConfiguration.
        :type: list[str]
        """

        self._recipient_events = recipient_events

    @property
    def require_mutual_tls(self):
        """
        Gets the require_mutual_tls of this ConnectCustomConfiguration.
        

        :return: The require_mutual_tls of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._require_mutual_tls

    @require_mutual_tls.setter
    def require_mutual_tls(self, require_mutual_tls):
        """
        Sets the require_mutual_tls of this ConnectCustomConfiguration.
        

        :param require_mutual_tls: The require_mutual_tls of this ConnectCustomConfiguration.
        :type: str
        """

        self._require_mutual_tls = require_mutual_tls

    @property
    def requires_acknowledgement(self):
        """
        Gets the requires_acknowledgement of this ConnectCustomConfiguration.
        When set to **true**, and a publication message fails to be acknowledged, the message goes back into the queue and the system will retry delivery after a successful acknowledgement is received. If the delivery fails a second time, the message is not returned to the queue for sending until Connect receives a successful acknowledgement and it has been at least 24 hours since the previous retry. There is a maximum of ten retries Alternately, you can use Republish Connect Information to manually republish the envelope information.

        :return: The requires_acknowledgement of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._requires_acknowledgement

    @requires_acknowledgement.setter
    def requires_acknowledgement(self, requires_acknowledgement):
        """
        Sets the requires_acknowledgement of this ConnectCustomConfiguration.
        When set to **true**, and a publication message fails to be acknowledged, the message goes back into the queue and the system will retry delivery after a successful acknowledgement is received. If the delivery fails a second time, the message is not returned to the queue for sending until Connect receives a successful acknowledgement and it has been at least 24 hours since the previous retry. There is a maximum of ten retries Alternately, you can use Republish Connect Information to manually republish the envelope information.

        :param requires_acknowledgement: The requires_acknowledgement of this ConnectCustomConfiguration.
        :type: str
        """

        self._requires_acknowledgement = requires_acknowledgement

    @property
    def salesforce_api_version(self):
        """
        Gets the salesforce_api_version of this ConnectCustomConfiguration.
        

        :return: The salesforce_api_version of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._salesforce_api_version

    @salesforce_api_version.setter
    def salesforce_api_version(self, salesforce_api_version):
        """
        Sets the salesforce_api_version of this ConnectCustomConfiguration.
        

        :param salesforce_api_version: The salesforce_api_version of this ConnectCustomConfiguration.
        :type: str
        """

        self._salesforce_api_version = salesforce_api_version

    @property
    def salesforce_authcode(self):
        """
        Gets the salesforce_authcode of this ConnectCustomConfiguration.
        

        :return: The salesforce_authcode of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._salesforce_authcode

    @salesforce_authcode.setter
    def salesforce_authcode(self, salesforce_authcode):
        """
        Sets the salesforce_authcode of this ConnectCustomConfiguration.
        

        :param salesforce_authcode: The salesforce_authcode of this ConnectCustomConfiguration.
        :type: str
        """

        self._salesforce_authcode = salesforce_authcode

    @property
    def salesforce_call_back_url(self):
        """
        Gets the salesforce_call_back_url of this ConnectCustomConfiguration.
        

        :return: The salesforce_call_back_url of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._salesforce_call_back_url

    @salesforce_call_back_url.setter
    def salesforce_call_back_url(self, salesforce_call_back_url):
        """
        Sets the salesforce_call_back_url of this ConnectCustomConfiguration.
        

        :param salesforce_call_back_url: The salesforce_call_back_url of this ConnectCustomConfiguration.
        :type: str
        """

        self._salesforce_call_back_url = salesforce_call_back_url

    @property
    def salesforce_documents_as_content_files(self):
        """
        Gets the salesforce_documents_as_content_files of this ConnectCustomConfiguration.
        

        :return: The salesforce_documents_as_content_files of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._salesforce_documents_as_content_files

    @salesforce_documents_as_content_files.setter
    def salesforce_documents_as_content_files(self, salesforce_documents_as_content_files):
        """
        Sets the salesforce_documents_as_content_files of this ConnectCustomConfiguration.
        

        :param salesforce_documents_as_content_files: The salesforce_documents_as_content_files of this ConnectCustomConfiguration.
        :type: str
        """

        self._salesforce_documents_as_content_files = salesforce_documents_as_content_files

    @property
    def sender_override(self):
        """
        Gets the sender_override of this ConnectCustomConfiguration.
        

        :return: The sender_override of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._sender_override

    @sender_override.setter
    def sender_override(self, sender_override):
        """
        Sets the sender_override of this ConnectCustomConfiguration.
        

        :param sender_override: The sender_override of this ConnectCustomConfiguration.
        :type: str
        """

        self._sender_override = sender_override

    @property
    def sender_selectable_items(self):
        """
        Gets the sender_selectable_items of this ConnectCustomConfiguration.
        

        :return: The sender_selectable_items of this ConnectCustomConfiguration.
        :rtype: list[str]
        """
        return self._sender_selectable_items

    @sender_selectable_items.setter
    def sender_selectable_items(self, sender_selectable_items):
        """
        Sets the sender_selectable_items of this ConnectCustomConfiguration.
        

        :param sender_selectable_items: The sender_selectable_items of this ConnectCustomConfiguration.
        :type: list[str]
        """

        self._sender_selectable_items = sender_selectable_items

    @property
    def sf_objects(self):
        """
        Gets the sf_objects of this ConnectCustomConfiguration.
        

        :return: The sf_objects of this ConnectCustomConfiguration.
        :rtype: list[ConnectSalesforceObject]
        """
        return self._sf_objects

    @sf_objects.setter
    def sf_objects(self, sf_objects):
        """
        Sets the sf_objects of this ConnectCustomConfiguration.
        

        :param sf_objects: The sf_objects of this ConnectCustomConfiguration.
        :type: list[ConnectSalesforceObject]
        """

        self._sf_objects = sf_objects

    @property
    def sign_message_with_x509_certificate(self):
        """
        Gets the sign_message_with_x509_certificate of this ConnectCustomConfiguration.
        When set to **true**, Connect messages are signed with an X509 certificate. This provides support for 2-way SSL.

        :return: The sign_message_with_x509_certificate of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._sign_message_with_x509_certificate

    @sign_message_with_x509_certificate.setter
    def sign_message_with_x509_certificate(self, sign_message_with_x509_certificate):
        """
        Sets the sign_message_with_x509_certificate of this ConnectCustomConfiguration.
        When set to **true**, Connect messages are signed with an X509 certificate. This provides support for 2-way SSL.

        :param sign_message_with_x509_certificate: The sign_message_with_x509_certificate of this ConnectCustomConfiguration.
        :type: str
        """

        self._sign_message_with_x509_certificate = sign_message_with_x509_certificate

    @property
    def soap_namespace(self):
        """
        Gets the soap_namespace of this ConnectCustomConfiguration.
        The namespace of the SOAP interface.  The namespace value must be set if useSoapInterface is set to true.

        :return: The soap_namespace of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._soap_namespace

    @soap_namespace.setter
    def soap_namespace(self, soap_namespace):
        """
        Sets the soap_namespace of this ConnectCustomConfiguration.
        The namespace of the SOAP interface.  The namespace value must be set if useSoapInterface is set to true.

        :param soap_namespace: The soap_namespace of this ConnectCustomConfiguration.
        :type: str
        """

        self._soap_namespace = soap_namespace

    @property
    def url_to_publish_to(self):
        """
        Gets the url_to_publish_to of this ConnectCustomConfiguration.
        This is the web address and name of your listener or Retrieving Service endpoint. You need to include HTTPS:// in the web address.

        :return: The url_to_publish_to of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._url_to_publish_to

    @url_to_publish_to.setter
    def url_to_publish_to(self, url_to_publish_to):
        """
        Sets the url_to_publish_to of this ConnectCustomConfiguration.
        This is the web address and name of your listener or Retrieving Service endpoint. You need to include HTTPS:// in the web address.

        :param url_to_publish_to: The url_to_publish_to of this ConnectCustomConfiguration.
        :type: str
        """

        self._url_to_publish_to = url_to_publish_to

    @property
    def user_ids(self):
        """
        Gets the user_ids of this ConnectCustomConfiguration.
        A comma separated list of userIds. This sets the users associated with the tracked envelope and recipient events. When one of the event occurs for a set user, the information is sent through Connect.   ###### Note: If allUsers is set to Ã¯Â¿Â½falseÃ¯Â¿Â½ then you must provide a list of user idÃ¯Â¿Â½s.

        :return: The user_ids of this ConnectCustomConfiguration.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """
        Sets the user_ids of this ConnectCustomConfiguration.
        A comma separated list of userIds. This sets the users associated with the tracked envelope and recipient events. When one of the event occurs for a set user, the information is sent through Connect.   ###### Note: If allUsers is set to Ã¯Â¿Â½falseÃ¯Â¿Â½ then you must provide a list of user idÃ¯Â¿Â½s.

        :param user_ids: The user_ids of this ConnectCustomConfiguration.
        :type: list[str]
        """

        self._user_ids = user_ids

    @property
    def user_name(self):
        """
        Gets the user_name of this ConnectCustomConfiguration.
        

        :return: The user_name of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this ConnectCustomConfiguration.
        

        :param user_name: The user_name of this ConnectCustomConfiguration.
        :type: str
        """

        self._user_name = user_name

    @property
    def use_soap_interface(self):
        """
        Gets the use_soap_interface of this ConnectCustomConfiguration.
        When set to **true**, indicates that the `urlToPublishTo` property contains a SOAP endpoint.

        :return: The use_soap_interface of this ConnectCustomConfiguration.
        :rtype: str
        """
        return self._use_soap_interface

    @use_soap_interface.setter
    def use_soap_interface(self, use_soap_interface):
        """
        Sets the use_soap_interface of this ConnectCustomConfiguration.
        When set to **true**, indicates that the `urlToPublishTo` property contains a SOAP endpoint.

        :param use_soap_interface: The use_soap_interface of this ConnectCustomConfiguration.
        :type: str
        """

        self._use_soap_interface = use_soap_interface

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
