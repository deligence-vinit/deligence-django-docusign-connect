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


class UserPasswordInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, current_password=None, email=None, forgotten_password_info=None, new_password=None):
        """
        UserPasswordInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current_password': 'str',
            'email': 'str',
            'forgotten_password_info': 'ForgottenPasswordInformation',
            'new_password': 'str'
        }

        self.attribute_map = {
            'current_password': 'currentPassword',
            'email': 'email',
            'forgotten_password_info': 'forgottenPasswordInfo',
            'new_password': 'newPassword'
        }

        self._current_password = current_password
        self._email = email
        self._forgotten_password_info = forgotten_password_info
        self._new_password = new_password

    @property
    def current_password(self):
        """
        Gets the current_password of this UserPasswordInformation.
        The user's current password to be changed.

        :return: The current_password of this UserPasswordInformation.
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """
        Sets the current_password of this UserPasswordInformation.
        The user's current password to be changed.

        :param current_password: The current_password of this UserPasswordInformation.
        :type: str
        """

        self._current_password = current_password

    @property
    def email(self):
        """
        Gets the email of this UserPasswordInformation.
        The user's email address for the associated account.

        :return: The email of this UserPasswordInformation.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserPasswordInformation.
        The user's email address for the associated account.

        :param email: The email of this UserPasswordInformation.
        :type: str
        """

        self._email = email

    @property
    def forgotten_password_info(self):
        """
        Gets the forgotten_password_info of this UserPasswordInformation.

        :return: The forgotten_password_info of this UserPasswordInformation.
        :rtype: ForgottenPasswordInformation
        """
        return self._forgotten_password_info

    @forgotten_password_info.setter
    def forgotten_password_info(self, forgotten_password_info):
        """
        Sets the forgotten_password_info of this UserPasswordInformation.

        :param forgotten_password_info: The forgotten_password_info of this UserPasswordInformation.
        :type: ForgottenPasswordInformation
        """

        self._forgotten_password_info = forgotten_password_info

    @property
    def new_password(self):
        """
        Gets the new_password of this UserPasswordInformation.
        The user's new password.

        :return: The new_password of this UserPasswordInformation.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """
        Sets the new_password of this UserPasswordInformation.
        The user's new password.

        :param new_password: The new_password of this UserPasswordInformation.
        :type: str
        """

        self._new_password = new_password

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