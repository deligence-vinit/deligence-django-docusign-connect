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


class TemplateCustomFields(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, list_custom_fields=None, text_custom_fields=None):
        """
        TemplateCustomFields - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'list_custom_fields': 'list[ListCustomField]',
            'text_custom_fields': 'list[TextCustomField]'
        }

        self.attribute_map = {
            'list_custom_fields': 'listCustomFields',
            'text_custom_fields': 'textCustomFields'
        }

        self._list_custom_fields = list_custom_fields
        self._text_custom_fields = text_custom_fields

    @property
    def list_custom_fields(self):
        """
        Gets the list_custom_fields of this TemplateCustomFields.
        An array of list custom fields.

        :return: The list_custom_fields of this TemplateCustomFields.
        :rtype: list[ListCustomField]
        """
        return self._list_custom_fields

    @list_custom_fields.setter
    def list_custom_fields(self, list_custom_fields):
        """
        Sets the list_custom_fields of this TemplateCustomFields.
        An array of list custom fields.

        :param list_custom_fields: The list_custom_fields of this TemplateCustomFields.
        :type: list[ListCustomField]
        """

        self._list_custom_fields = list_custom_fields

    @property
    def text_custom_fields(self):
        """
        Gets the text_custom_fields of this TemplateCustomFields.
        An array of text custom fields.

        :return: The text_custom_fields of this TemplateCustomFields.
        :rtype: list[TextCustomField]
        """
        return self._text_custom_fields

    @text_custom_fields.setter
    def text_custom_fields(self, text_custom_fields):
        """
        Sets the text_custom_fields of this TemplateCustomFields.
        An array of text custom fields.

        :param text_custom_fields: The text_custom_fields of this TemplateCustomFields.
        :type: list[TextCustomField]
        """

        self._text_custom_fields = text_custom_fields

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
