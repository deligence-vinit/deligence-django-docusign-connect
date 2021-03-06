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


class PayPalLegacySettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currency=None, partner=None, password=None, user_name=None, vendor=None):
        """
        PayPalLegacySettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency': 'str',
            'partner': 'str',
            'password': 'str',
            'user_name': 'str',
            'vendor': 'str'
        }

        self.attribute_map = {
            'currency': 'currency',
            'partner': 'partner',
            'password': 'password',
            'user_name': 'userName',
            'vendor': 'vendor'
        }

        self._currency = currency
        self._partner = partner
        self._password = password
        self._user_name = user_name
        self._vendor = vendor

    @property
    def currency(self):
        """
        Gets the currency of this PayPalLegacySettings.
        

        :return: The currency of this PayPalLegacySettings.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PayPalLegacySettings.
        

        :param currency: The currency of this PayPalLegacySettings.
        :type: str
        """

        self._currency = currency

    @property
    def partner(self):
        """
        Gets the partner of this PayPalLegacySettings.
        

        :return: The partner of this PayPalLegacySettings.
        :rtype: str
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """
        Sets the partner of this PayPalLegacySettings.
        

        :param partner: The partner of this PayPalLegacySettings.
        :type: str
        """

        self._partner = partner

    @property
    def password(self):
        """
        Gets the password of this PayPalLegacySettings.
        

        :return: The password of this PayPalLegacySettings.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this PayPalLegacySettings.
        

        :param password: The password of this PayPalLegacySettings.
        :type: str
        """

        self._password = password

    @property
    def user_name(self):
        """
        Gets the user_name of this PayPalLegacySettings.
        

        :return: The user_name of this PayPalLegacySettings.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this PayPalLegacySettings.
        

        :param user_name: The user_name of this PayPalLegacySettings.
        :type: str
        """

        self._user_name = user_name

    @property
    def vendor(self):
        """
        Gets the vendor of this PayPalLegacySettings.
        

        :return: The vendor of this PayPalLegacySettings.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this PayPalLegacySettings.
        

        :param vendor: The vendor of this PayPalLegacySettings.
        :type: str
        """

        self._vendor = vendor

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
