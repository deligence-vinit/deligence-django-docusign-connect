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


class PowerFormFormDataEnvelope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, envelope_id=None, recipients=None):
        """
        PowerFormFormDataEnvelope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'envelope_id': 'str',
            'recipients': 'list[PowerFormFormDataRecipient]'
        }

        self.attribute_map = {
            'envelope_id': 'envelopeId',
            'recipients': 'recipients'
        }

        self._envelope_id = envelope_id
        self._recipients = recipients

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this PowerFormFormDataEnvelope.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this PowerFormFormDataEnvelope.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this PowerFormFormDataEnvelope.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this PowerFormFormDataEnvelope.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def recipients(self):
        """
        Gets the recipients of this PowerFormFormDataEnvelope.
        An array of powerform recipients.

        :return: The recipients of this PowerFormFormDataEnvelope.
        :rtype: list[PowerFormFormDataRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this PowerFormFormDataEnvelope.
        An array of powerform recipients.

        :param recipients: The recipients of this PowerFormFormDataEnvelope.
        :type: list[PowerFormFormDataRecipient]
        """

        self._recipients = recipients

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
