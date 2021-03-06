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


class BulkSendingListSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bulk_send_list_id=None, created_by_user=None, created_date=None, name=None):
        """
        BulkSendingListSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bulk_send_list_id': 'str',
            'created_by_user': 'str',
            'created_date': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'bulk_send_list_id': 'bulkSendListId',
            'created_by_user': 'createdByUser',
            'created_date': 'createdDate',
            'name': 'name'
        }

        self._bulk_send_list_id = bulk_send_list_id
        self._created_by_user = created_by_user
        self._created_date = created_date
        self._name = name

    @property
    def bulk_send_list_id(self):
        """
        Gets the bulk_send_list_id of this BulkSendingListSummary.
        

        :return: The bulk_send_list_id of this BulkSendingListSummary.
        :rtype: str
        """
        return self._bulk_send_list_id

    @bulk_send_list_id.setter
    def bulk_send_list_id(self, bulk_send_list_id):
        """
        Sets the bulk_send_list_id of this BulkSendingListSummary.
        

        :param bulk_send_list_id: The bulk_send_list_id of this BulkSendingListSummary.
        :type: str
        """

        self._bulk_send_list_id = bulk_send_list_id

    @property
    def created_by_user(self):
        """
        Gets the created_by_user of this BulkSendingListSummary.
        

        :return: The created_by_user of this BulkSendingListSummary.
        :rtype: str
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """
        Sets the created_by_user of this BulkSendingListSummary.
        

        :param created_by_user: The created_by_user of this BulkSendingListSummary.
        :type: str
        """

        self._created_by_user = created_by_user

    @property
    def created_date(self):
        """
        Gets the created_date of this BulkSendingListSummary.
        

        :return: The created_date of this BulkSendingListSummary.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this BulkSendingListSummary.
        

        :param created_date: The created_date of this BulkSendingListSummary.
        :type: str
        """

        self._created_date = created_date

    @property
    def name(self):
        """
        Gets the name of this BulkSendingListSummary.
        

        :return: The name of this BulkSendingListSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BulkSendingListSummary.
        

        :param name: The name of this BulkSendingListSummary.
        :type: str
        """

        self._name = name

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
