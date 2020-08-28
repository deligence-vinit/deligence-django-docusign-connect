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


class BrandLink(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, link_text=None, link_type=None, show_link=None, url_or_mail_to=None):
        """
        BrandLink - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'link_text': 'str',
            'link_type': 'str',
            'show_link': 'str',
            'url_or_mail_to': 'str'
        }

        self.attribute_map = {
            'link_text': 'linkText',
            'link_type': 'linkType',
            'show_link': 'showLink',
            'url_or_mail_to': 'urlOrMailTo'
        }

        self._link_text = link_text
        self._link_type = link_type
        self._show_link = show_link
        self._url_or_mail_to = url_or_mail_to

    @property
    def link_text(self):
        """
        Gets the link_text of this BrandLink.
        

        :return: The link_text of this BrandLink.
        :rtype: str
        """
        return self._link_text

    @link_text.setter
    def link_text(self, link_text):
        """
        Sets the link_text of this BrandLink.
        

        :param link_text: The link_text of this BrandLink.
        :type: str
        """

        self._link_text = link_text

    @property
    def link_type(self):
        """
        Gets the link_type of this BrandLink.
        

        :return: The link_type of this BrandLink.
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """
        Sets the link_type of this BrandLink.
        

        :param link_type: The link_type of this BrandLink.
        :type: str
        """

        self._link_type = link_type

    @property
    def show_link(self):
        """
        Gets the show_link of this BrandLink.
        

        :return: The show_link of this BrandLink.
        :rtype: str
        """
        return self._show_link

    @show_link.setter
    def show_link(self, show_link):
        """
        Sets the show_link of this BrandLink.
        

        :param show_link: The show_link of this BrandLink.
        :type: str
        """

        self._show_link = show_link

    @property
    def url_or_mail_to(self):
        """
        Gets the url_or_mail_to of this BrandLink.
        

        :return: The url_or_mail_to of this BrandLink.
        :rtype: str
        """
        return self._url_or_mail_to

    @url_or_mail_to.setter
    def url_or_mail_to(self, url_or_mail_to):
        """
        Sets the url_or_mail_to of this BrandLink.
        

        :param url_or_mail_to: The url_or_mail_to of this BrandLink.
        :type: str
        """

        self._url_or_mail_to = url_or_mail_to

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
