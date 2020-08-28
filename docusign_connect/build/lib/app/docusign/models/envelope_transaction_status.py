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


class EnvelopeTransactionStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, envelope_id=None, error_details=None, status=None, transaction_id=None):
        """
        EnvelopeTransactionStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'envelope_id': 'str',
            'error_details': 'ErrorDetails',
            'status': 'str',
            'transaction_id': 'str'
        }

        self.attribute_map = {
            'envelope_id': 'envelopeId',
            'error_details': 'errorDetails',
            'status': 'status',
            'transaction_id': 'transactionId'
        }

        self._envelope_id = envelope_id
        self._error_details = error_details
        self._status = status
        self._transaction_id = transaction_id

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this EnvelopeTransactionStatus.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this EnvelopeTransactionStatus.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this EnvelopeTransactionStatus.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this EnvelopeTransactionStatus.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def error_details(self):
        """
        Gets the error_details of this EnvelopeTransactionStatus.

        :return: The error_details of this EnvelopeTransactionStatus.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this EnvelopeTransactionStatus.

        :param error_details: The error_details of this EnvelopeTransactionStatus.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def status(self):
        """
        Gets the status of this EnvelopeTransactionStatus.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this EnvelopeTransactionStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EnvelopeTransactionStatus.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this EnvelopeTransactionStatus.
        :type: str
        """

        self._status = status

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this EnvelopeTransactionStatus.
         Used to identify an envelope. The id is a sender-generated value and is valid in the DocuSign system for 7 days. It is recommended that a transaction ID is used for offline signing to ensure that an envelope is not sent multiple times. The `transactionId` property can be used determine an envelope's status (i.e. was it created or not) in cases where the internet connection was lost before the envelope status was returned.

        :return: The transaction_id of this EnvelopeTransactionStatus.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this EnvelopeTransactionStatus.
         Used to identify an envelope. The id is a sender-generated value and is valid in the DocuSign system for 7 days. It is recommended that a transaction ID is used for offline signing to ensure that an envelope is not sent multiple times. The `transactionId` property can be used determine an envelope's status (i.e. was it created or not) in cases where the internet connection was lost before the envelope status was returned.

        :param transaction_id: The transaction_id of this EnvelopeTransactionStatus.
        :type: str
        """

        self._transaction_id = transaction_id

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