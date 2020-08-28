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


class EnvelopesInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, continuation_token=None, end_position=None, envelopes=None, envelope_transaction_statuses=None, folders=None, last_queried_date_time=None, next_uri=None, previous_uri=None, result_set_size=None, start_position=None, total_set_size=None):
        """
        EnvelopesInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'continuation_token': 'str',
            'end_position': 'str',
            'envelopes': 'list[Envelope]',
            'envelope_transaction_statuses': 'list[EnvelopeTransactionStatus]',
            'folders': 'list[Folder]',
            'last_queried_date_time': 'str',
            'next_uri': 'str',
            'previous_uri': 'str',
            'result_set_size': 'str',
            'start_position': 'str',
            'total_set_size': 'str'
        }

        self.attribute_map = {
            'continuation_token': 'continuationToken',
            'end_position': 'endPosition',
            'envelopes': 'envelopes',
            'envelope_transaction_statuses': 'envelopeTransactionStatuses',
            'folders': 'folders',
            'last_queried_date_time': 'lastQueriedDateTime',
            'next_uri': 'nextUri',
            'previous_uri': 'previousUri',
            'result_set_size': 'resultSetSize',
            'start_position': 'startPosition',
            'total_set_size': 'totalSetSize'
        }

        self._continuation_token = continuation_token
        self._end_position = end_position
        self._envelopes = envelopes
        self._envelope_transaction_statuses = envelope_transaction_statuses
        self._folders = folders
        self._last_queried_date_time = last_queried_date_time
        self._next_uri = next_uri
        self._previous_uri = previous_uri
        self._result_set_size = result_set_size
        self._start_position = start_position
        self._total_set_size = total_set_size

    @property
    def continuation_token(self):
        """
        Gets the continuation_token of this EnvelopesInformation.
        

        :return: The continuation_token of this EnvelopesInformation.
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """
        Sets the continuation_token of this EnvelopesInformation.
        

        :param continuation_token: The continuation_token of this EnvelopesInformation.
        :type: str
        """

        self._continuation_token = continuation_token

    @property
    def end_position(self):
        """
        Gets the end_position of this EnvelopesInformation.
        The last position in the result set. 

        :return: The end_position of this EnvelopesInformation.
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """
        Sets the end_position of this EnvelopesInformation.
        The last position in the result set. 

        :param end_position: The end_position of this EnvelopesInformation.
        :type: str
        """

        self._end_position = end_position

    @property
    def envelopes(self):
        """
        Gets the envelopes of this EnvelopesInformation.
        

        :return: The envelopes of this EnvelopesInformation.
        :rtype: list[Envelope]
        """
        return self._envelopes

    @envelopes.setter
    def envelopes(self, envelopes):
        """
        Sets the envelopes of this EnvelopesInformation.
        

        :param envelopes: The envelopes of this EnvelopesInformation.
        :type: list[Envelope]
        """

        self._envelopes = envelopes

    @property
    def envelope_transaction_statuses(self):
        """
        Gets the envelope_transaction_statuses of this EnvelopesInformation.
        

        :return: The envelope_transaction_statuses of this EnvelopesInformation.
        :rtype: list[EnvelopeTransactionStatus]
        """
        return self._envelope_transaction_statuses

    @envelope_transaction_statuses.setter
    def envelope_transaction_statuses(self, envelope_transaction_statuses):
        """
        Sets the envelope_transaction_statuses of this EnvelopesInformation.
        

        :param envelope_transaction_statuses: The envelope_transaction_statuses of this EnvelopesInformation.
        :type: list[EnvelopeTransactionStatus]
        """

        self._envelope_transaction_statuses = envelope_transaction_statuses

    @property
    def folders(self):
        """
        Gets the folders of this EnvelopesInformation.
        

        :return: The folders of this EnvelopesInformation.
        :rtype: list[Folder]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """
        Sets the folders of this EnvelopesInformation.
        

        :param folders: The folders of this EnvelopesInformation.
        :type: list[Folder]
        """

        self._folders = folders

    @property
    def last_queried_date_time(self):
        """
        Gets the last_queried_date_time of this EnvelopesInformation.
        

        :return: The last_queried_date_time of this EnvelopesInformation.
        :rtype: str
        """
        return self._last_queried_date_time

    @last_queried_date_time.setter
    def last_queried_date_time(self, last_queried_date_time):
        """
        Sets the last_queried_date_time of this EnvelopesInformation.
        

        :param last_queried_date_time: The last_queried_date_time of this EnvelopesInformation.
        :type: str
        """

        self._last_queried_date_time = last_queried_date_time

    @property
    def next_uri(self):
        """
        Gets the next_uri of this EnvelopesInformation.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :return: The next_uri of this EnvelopesInformation.
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """
        Sets the next_uri of this EnvelopesInformation.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :param next_uri: The next_uri of this EnvelopesInformation.
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """
        Gets the previous_uri of this EnvelopesInformation.
        The postal code for the billing address.

        :return: The previous_uri of this EnvelopesInformation.
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """
        Sets the previous_uri of this EnvelopesInformation.
        The postal code for the billing address.

        :param previous_uri: The previous_uri of this EnvelopesInformation.
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """
        Gets the result_set_size of this EnvelopesInformation.
        The number of results returned in this response. 

        :return: The result_set_size of this EnvelopesInformation.
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """
        Sets the result_set_size of this EnvelopesInformation.
        The number of results returned in this response. 

        :param result_set_size: The result_set_size of this EnvelopesInformation.
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """
        Gets the start_position of this EnvelopesInformation.
        Starting position of the current result set.

        :return: The start_position of this EnvelopesInformation.
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """
        Sets the start_position of this EnvelopesInformation.
        Starting position of the current result set.

        :param start_position: The start_position of this EnvelopesInformation.
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """
        Gets the total_set_size of this EnvelopesInformation.
        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.

        :return: The total_set_size of this EnvelopesInformation.
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """
        Sets the total_set_size of this EnvelopesInformation.
        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.

        :param total_set_size: The total_set_size of this EnvelopesInformation.
        :type: str
        """

        self._total_set_size = total_set_size

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
