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


class BrandResources(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_by_user_info=None, created_date=None, data_not_saved_not_in_master=None, modified_by_user_info=None, modified_date=None, modified_templates=None, resources_content_type=None, resources_content_uri=None):
        """
        BrandResources - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_by_user_info': 'UserInfo',
            'created_date': 'str',
            'data_not_saved_not_in_master': 'list[str]',
            'modified_by_user_info': 'UserInfo',
            'modified_date': 'str',
            'modified_templates': 'list[str]',
            'resources_content_type': 'str',
            'resources_content_uri': 'str'
        }

        self.attribute_map = {
            'created_by_user_info': 'createdByUserInfo',
            'created_date': 'createdDate',
            'data_not_saved_not_in_master': 'dataNotSavedNotInMaster',
            'modified_by_user_info': 'modifiedByUserInfo',
            'modified_date': 'modifiedDate',
            'modified_templates': 'modifiedTemplates',
            'resources_content_type': 'resourcesContentType',
            'resources_content_uri': 'resourcesContentUri'
        }

        self._created_by_user_info = created_by_user_info
        self._created_date = created_date
        self._data_not_saved_not_in_master = data_not_saved_not_in_master
        self._modified_by_user_info = modified_by_user_info
        self._modified_date = modified_date
        self._modified_templates = modified_templates
        self._resources_content_type = resources_content_type
        self._resources_content_uri = resources_content_uri

    @property
    def created_by_user_info(self):
        """
        Gets the created_by_user_info of this BrandResources.

        :return: The created_by_user_info of this BrandResources.
        :rtype: UserInfo
        """
        return self._created_by_user_info

    @created_by_user_info.setter
    def created_by_user_info(self, created_by_user_info):
        """
        Sets the created_by_user_info of this BrandResources.

        :param created_by_user_info: The created_by_user_info of this BrandResources.
        :type: UserInfo
        """

        self._created_by_user_info = created_by_user_info

    @property
    def created_date(self):
        """
        Gets the created_date of this BrandResources.
        

        :return: The created_date of this BrandResources.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this BrandResources.
        

        :param created_date: The created_date of this BrandResources.
        :type: str
        """

        self._created_date = created_date

    @property
    def data_not_saved_not_in_master(self):
        """
        Gets the data_not_saved_not_in_master of this BrandResources.
        

        :return: The data_not_saved_not_in_master of this BrandResources.
        :rtype: list[str]
        """
        return self._data_not_saved_not_in_master

    @data_not_saved_not_in_master.setter
    def data_not_saved_not_in_master(self, data_not_saved_not_in_master):
        """
        Sets the data_not_saved_not_in_master of this BrandResources.
        

        :param data_not_saved_not_in_master: The data_not_saved_not_in_master of this BrandResources.
        :type: list[str]
        """

        self._data_not_saved_not_in_master = data_not_saved_not_in_master

    @property
    def modified_by_user_info(self):
        """
        Gets the modified_by_user_info of this BrandResources.

        :return: The modified_by_user_info of this BrandResources.
        :rtype: UserInfo
        """
        return self._modified_by_user_info

    @modified_by_user_info.setter
    def modified_by_user_info(self, modified_by_user_info):
        """
        Sets the modified_by_user_info of this BrandResources.

        :param modified_by_user_info: The modified_by_user_info of this BrandResources.
        :type: UserInfo
        """

        self._modified_by_user_info = modified_by_user_info

    @property
    def modified_date(self):
        """
        Gets the modified_date of this BrandResources.
        

        :return: The modified_date of this BrandResources.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this BrandResources.
        

        :param modified_date: The modified_date of this BrandResources.
        :type: str
        """

        self._modified_date = modified_date

    @property
    def modified_templates(self):
        """
        Gets the modified_templates of this BrandResources.
        

        :return: The modified_templates of this BrandResources.
        :rtype: list[str]
        """
        return self._modified_templates

    @modified_templates.setter
    def modified_templates(self, modified_templates):
        """
        Sets the modified_templates of this BrandResources.
        

        :param modified_templates: The modified_templates of this BrandResources.
        :type: list[str]
        """

        self._modified_templates = modified_templates

    @property
    def resources_content_type(self):
        """
        Gets the resources_content_type of this BrandResources.
        

        :return: The resources_content_type of this BrandResources.
        :rtype: str
        """
        return self._resources_content_type

    @resources_content_type.setter
    def resources_content_type(self, resources_content_type):
        """
        Sets the resources_content_type of this BrandResources.
        

        :param resources_content_type: The resources_content_type of this BrandResources.
        :type: str
        """

        self._resources_content_type = resources_content_type

    @property
    def resources_content_uri(self):
        """
        Gets the resources_content_uri of this BrandResources.
        

        :return: The resources_content_uri of this BrandResources.
        :rtype: str
        """
        return self._resources_content_uri

    @resources_content_uri.setter
    def resources_content_uri(self, resources_content_uri):
        """
        Sets the resources_content_uri of this BrandResources.
        

        :param resources_content_uri: The resources_content_uri of this BrandResources.
        :type: str
        """

        self._resources_content_uri = resources_content_uri

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
