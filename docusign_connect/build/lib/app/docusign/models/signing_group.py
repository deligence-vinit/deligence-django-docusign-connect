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


class SigningGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, created_by=None, error_details=None, group_email=None, group_name=None, group_type=None, modified=None, modified_by=None, signing_group_id=None, users=None):
        """
        SigningGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'str',
            'created_by': 'str',
            'error_details': 'ErrorDetails',
            'group_email': 'str',
            'group_name': 'str',
            'group_type': 'str',
            'modified': 'str',
            'modified_by': 'str',
            'signing_group_id': 'str',
            'users': 'list[SigningGroupUser]'
        }

        self.attribute_map = {
            'created': 'created',
            'created_by': 'createdBy',
            'error_details': 'errorDetails',
            'group_email': 'groupEmail',
            'group_name': 'groupName',
            'group_type': 'groupType',
            'modified': 'modified',
            'modified_by': 'modifiedBy',
            'signing_group_id': 'signingGroupId',
            'users': 'users'
        }

        self._created = created
        self._created_by = created_by
        self._error_details = error_details
        self._group_email = group_email
        self._group_name = group_name
        self._group_type = group_type
        self._modified = modified
        self._modified_by = modified_by
        self._signing_group_id = signing_group_id
        self._users = users

    @property
    def created(self):
        """
        Gets the created of this SigningGroup.
        

        :return: The created of this SigningGroup.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this SigningGroup.
        

        :param created: The created of this SigningGroup.
        :type: str
        """

        self._created = created

    @property
    def created_by(self):
        """
        Gets the created_by of this SigningGroup.
        

        :return: The created_by of this SigningGroup.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this SigningGroup.
        

        :param created_by: The created_by of this SigningGroup.
        :type: str
        """

        self._created_by = created_by

    @property
    def error_details(self):
        """
        Gets the error_details of this SigningGroup.

        :return: The error_details of this SigningGroup.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this SigningGroup.

        :param error_details: The error_details of this SigningGroup.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def group_email(self):
        """
        Gets the group_email of this SigningGroup.
        

        :return: The group_email of this SigningGroup.
        :rtype: str
        """
        return self._group_email

    @group_email.setter
    def group_email(self, group_email):
        """
        Sets the group_email of this SigningGroup.
        

        :param group_email: The group_email of this SigningGroup.
        :type: str
        """

        self._group_email = group_email

    @property
    def group_name(self):
        """
        Gets the group_name of this SigningGroup.
        The name of the group.

        :return: The group_name of this SigningGroup.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this SigningGroup.
        The name of the group.

        :param group_name: The group_name of this SigningGroup.
        :type: str
        """

        self._group_name = group_name

    @property
    def group_type(self):
        """
        Gets the group_type of this SigningGroup.
        

        :return: The group_type of this SigningGroup.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """
        Sets the group_type of this SigningGroup.
        

        :param group_type: The group_type of this SigningGroup.
        :type: str
        """

        self._group_type = group_type

    @property
    def modified(self):
        """
        Gets the modified of this SigningGroup.
        

        :return: The modified of this SigningGroup.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this SigningGroup.
        

        :param modified: The modified of this SigningGroup.
        :type: str
        """

        self._modified = modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this SigningGroup.
        

        :return: The modified_by of this SigningGroup.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this SigningGroup.
        

        :param modified_by: The modified_by of this SigningGroup.
        :type: str
        """

        self._modified_by = modified_by

    @property
    def signing_group_id(self):
        """
        Gets the signing_group_id of this SigningGroup.
        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).

        :return: The signing_group_id of this SigningGroup.
        :rtype: str
        """
        return self._signing_group_id

    @signing_group_id.setter
    def signing_group_id(self, signing_group_id):
        """
        Sets the signing_group_id of this SigningGroup.
        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).

        :param signing_group_id: The signing_group_id of this SigningGroup.
        :type: str
        """

        self._signing_group_id = signing_group_id

    @property
    def users(self):
        """
        Gets the users of this SigningGroup.
        

        :return: The users of this SigningGroup.
        :rtype: list[SigningGroupUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this SigningGroup.
        

        :param users: The users of this SigningGroup.
        :type: list[SigningGroupUser]
        """

        self._users = users

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
