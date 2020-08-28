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


class AccountAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address1=None, address2=None, city=None, country=None, email=None, fax=None, first_name=None, last_name=None, phone=None, postal_code=None, state=None, supported_countries=None):
        """
        AccountAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address1': 'str',
            'address2': 'str',
            'city': 'str',
            'country': 'str',
            'email': 'str',
            'fax': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'phone': 'str',
            'postal_code': 'str',
            'state': 'str',
            'supported_countries': 'list[Country]'
        }

        self.attribute_map = {
            'address1': 'address1',
            'address2': 'address2',
            'city': 'city',
            'country': 'country',
            'email': 'email',
            'fax': 'fax',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'phone': 'phone',
            'postal_code': 'postalCode',
            'state': 'state',
            'supported_countries': 'supportedCountries'
        }

        self._address1 = address1
        self._address2 = address2
        self._city = city
        self._country = country
        self._email = email
        self._fax = fax
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._postal_code = postal_code
        self._state = state
        self._supported_countries = supported_countries

    @property
    def address1(self):
        """
        Gets the address1 of this AccountAddress.
        First Line of the address. Maximum length: 100 characters.

        :return: The address1 of this AccountAddress.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this AccountAddress.
        First Line of the address. Maximum length: 100 characters.

        :param address1: The address1 of this AccountAddress.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this AccountAddress.
        Second Line of the address. Maximum length: 100 characters.

        :return: The address2 of this AccountAddress.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this AccountAddress.
        Second Line of the address. Maximum length: 100 characters.

        :param address2: The address2 of this AccountAddress.
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this AccountAddress.
        The city value of the address.

        :return: The city of this AccountAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AccountAddress.
        The city value of the address.

        :param city: The city of this AccountAddress.
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """
        Gets the country of this AccountAddress.
        Specifies the country associated with the address.

        :return: The country of this AccountAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AccountAddress.
        Specifies the country associated with the address.

        :param country: The country of this AccountAddress.
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """
        Gets the email of this AccountAddress.
        

        :return: The email of this AccountAddress.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AccountAddress.
        

        :param email: The email of this AccountAddress.
        :type: str
        """

        self._email = email

    @property
    def fax(self):
        """
        Gets the fax of this AccountAddress.
        

        :return: The fax of this AccountAddress.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this AccountAddress.
        

        :param fax: The fax of this AccountAddress.
        :type: str
        """

        self._fax = fax

    @property
    def first_name(self):
        """
        Gets the first_name of this AccountAddress.
        The user's first name.  Maximum Length: 50 characters.

        :return: The first_name of this AccountAddress.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this AccountAddress.
        The user's first name.  Maximum Length: 50 characters.

        :param first_name: The first_name of this AccountAddress.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this AccountAddress.
        

        :return: The last_name of this AccountAddress.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this AccountAddress.
        

        :param last_name: The last_name of this AccountAddress.
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """
        Gets the phone of this AccountAddress.
        

        :return: The phone of this AccountAddress.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this AccountAddress.
        

        :param phone: The phone of this AccountAddress.
        :type: str
        """

        self._phone = phone

    @property
    def postal_code(self):
        """
        Gets the postal_code of this AccountAddress.
        

        :return: The postal_code of this AccountAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this AccountAddress.
        

        :param postal_code: The postal_code of this AccountAddress.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """
        Gets the state of this AccountAddress.
        The state or province associated with the address.

        :return: The state of this AccountAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AccountAddress.
        The state or province associated with the address.

        :param state: The state of this AccountAddress.
        :type: str
        """

        self._state = state

    @property
    def supported_countries(self):
        """
        Gets the supported_countries of this AccountAddress.
        Contains an array of countries supported by the billing plan.

        :return: The supported_countries of this AccountAddress.
        :rtype: list[Country]
        """
        return self._supported_countries

    @supported_countries.setter
    def supported_countries(self, supported_countries):
        """
        Sets the supported_countries of this AccountAddress.
        Contains an array of countries supported by the billing plan.

        :param supported_countries: The supported_countries of this AccountAddress.
        :type: list[Country]
        """

        self._supported_countries = supported_countries

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