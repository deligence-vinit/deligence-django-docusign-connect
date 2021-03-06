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


class PathExtendedElement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, type=None, type_name=None):
        """
        PathExtendedElement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'type_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'type_name': 'typeName'
        }

        self._name = name
        self._type = type
        self._type_name = type_name

    @property
    def name(self):
        """
        Gets the name of this PathExtendedElement.
        

        :return: The name of this PathExtendedElement.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PathExtendedElement.
        

        :param name: The name of this PathExtendedElement.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this PathExtendedElement.
        

        :return: The type of this PathExtendedElement.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PathExtendedElement.
        

        :param type: The type of this PathExtendedElement.
        :type: str
        """

        self._type = type

    @property
    def type_name(self):
        """
        Gets the type_name of this PathExtendedElement.
        

        :return: The type_name of this PathExtendedElement.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this PathExtendedElement.
        

        :param type_name: The type_name of this PathExtendedElement.
        :type: str
        """

        self._type_name = type_name

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
