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


class PaymentGatewayAccountsInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, payment_gateway_accounts=None):
        """
        PaymentGatewayAccountsInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'payment_gateway_accounts': 'list[PaymentGatewayAccount]'
        }

        self.attribute_map = {
            'payment_gateway_accounts': 'paymentGatewayAccounts'
        }

        self._payment_gateway_accounts = payment_gateway_accounts

    @property
    def payment_gateway_accounts(self):
        """
        Gets the payment_gateway_accounts of this PaymentGatewayAccountsInfo.
        

        :return: The payment_gateway_accounts of this PaymentGatewayAccountsInfo.
        :rtype: list[PaymentGatewayAccount]
        """
        return self._payment_gateway_accounts

    @payment_gateway_accounts.setter
    def payment_gateway_accounts(self, payment_gateway_accounts):
        """
        Sets the payment_gateway_accounts of this PaymentGatewayAccountsInfo.
        

        :param payment_gateway_accounts: The payment_gateway_accounts of this PaymentGatewayAccountsInfo.
        :type: list[PaymentGatewayAccount]
        """

        self._payment_gateway_accounts = payment_gateway_accounts

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