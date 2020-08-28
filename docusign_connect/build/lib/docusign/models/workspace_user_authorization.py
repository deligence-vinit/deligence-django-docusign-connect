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


class WorkspaceUserAuthorization(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, can_delete=None, can_move=None, can_transact=None, can_view=None, created=None, created_by_id=None, error_details=None, modified=None, modified_by_id=None, workspace_user_id=None, workspace_user_information=None):
        """
        WorkspaceUserAuthorization - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'can_delete': 'str',
            'can_move': 'str',
            'can_transact': 'str',
            'can_view': 'str',
            'created': 'str',
            'created_by_id': 'str',
            'error_details': 'ErrorDetails',
            'modified': 'str',
            'modified_by_id': 'str',
            'workspace_user_id': 'str',
            'workspace_user_information': 'WorkspaceUser'
        }

        self.attribute_map = {
            'can_delete': 'canDelete',
            'can_move': 'canMove',
            'can_transact': 'canTransact',
            'can_view': 'canView',
            'created': 'created',
            'created_by_id': 'createdById',
            'error_details': 'errorDetails',
            'modified': 'modified',
            'modified_by_id': 'modifiedById',
            'workspace_user_id': 'workspaceUserId',
            'workspace_user_information': 'workspaceUserInformation'
        }

        self._can_delete = can_delete
        self._can_move = can_move
        self._can_transact = can_transact
        self._can_view = can_view
        self._created = created
        self._created_by_id = created_by_id
        self._error_details = error_details
        self._modified = modified
        self._modified_by_id = modified_by_id
        self._workspace_user_id = workspace_user_id
        self._workspace_user_information = workspace_user_information

    @property
    def can_delete(self):
        """
        Gets the can_delete of this WorkspaceUserAuthorization.
        

        :return: The can_delete of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """
        Sets the can_delete of this WorkspaceUserAuthorization.
        

        :param can_delete: The can_delete of this WorkspaceUserAuthorization.
        :type: str
        """

        self._can_delete = can_delete

    @property
    def can_move(self):
        """
        Gets the can_move of this WorkspaceUserAuthorization.
        

        :return: The can_move of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._can_move

    @can_move.setter
    def can_move(self, can_move):
        """
        Sets the can_move of this WorkspaceUserAuthorization.
        

        :param can_move: The can_move of this WorkspaceUserAuthorization.
        :type: str
        """

        self._can_move = can_move

    @property
    def can_transact(self):
        """
        Gets the can_transact of this WorkspaceUserAuthorization.
        

        :return: The can_transact of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._can_transact

    @can_transact.setter
    def can_transact(self, can_transact):
        """
        Sets the can_transact of this WorkspaceUserAuthorization.
        

        :param can_transact: The can_transact of this WorkspaceUserAuthorization.
        :type: str
        """

        self._can_transact = can_transact

    @property
    def can_view(self):
        """
        Gets the can_view of this WorkspaceUserAuthorization.
        

        :return: The can_view of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        """
        Sets the can_view of this WorkspaceUserAuthorization.
        

        :param can_view: The can_view of this WorkspaceUserAuthorization.
        :type: str
        """

        self._can_view = can_view

    @property
    def created(self):
        """
        Gets the created of this WorkspaceUserAuthorization.
        The UTC DateTime when the workspace user authorization was created.

        :return: The created of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this WorkspaceUserAuthorization.
        The UTC DateTime when the workspace user authorization was created.

        :param created: The created of this WorkspaceUserAuthorization.
        :type: str
        """

        self._created = created

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this WorkspaceUserAuthorization.
        

        :return: The created_by_id of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this WorkspaceUserAuthorization.
        

        :param created_by_id: The created_by_id of this WorkspaceUserAuthorization.
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def error_details(self):
        """
        Gets the error_details of this WorkspaceUserAuthorization.

        :return: The error_details of this WorkspaceUserAuthorization.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this WorkspaceUserAuthorization.

        :param error_details: The error_details of this WorkspaceUserAuthorization.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def modified(self):
        """
        Gets the modified of this WorkspaceUserAuthorization.
        

        :return: The modified of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this WorkspaceUserAuthorization.
        

        :param modified: The modified of this WorkspaceUserAuthorization.
        :type: str
        """

        self._modified = modified

    @property
    def modified_by_id(self):
        """
        Gets the modified_by_id of this WorkspaceUserAuthorization.
        

        :return: The modified_by_id of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """
        Sets the modified_by_id of this WorkspaceUserAuthorization.
        

        :param modified_by_id: The modified_by_id of this WorkspaceUserAuthorization.
        :type: str
        """

        self._modified_by_id = modified_by_id

    @property
    def workspace_user_id(self):
        """
        Gets the workspace_user_id of this WorkspaceUserAuthorization.
        

        :return: The workspace_user_id of this WorkspaceUserAuthorization.
        :rtype: str
        """
        return self._workspace_user_id

    @workspace_user_id.setter
    def workspace_user_id(self, workspace_user_id):
        """
        Sets the workspace_user_id of this WorkspaceUserAuthorization.
        

        :param workspace_user_id: The workspace_user_id of this WorkspaceUserAuthorization.
        :type: str
        """

        self._workspace_user_id = workspace_user_id

    @property
    def workspace_user_information(self):
        """
        Gets the workspace_user_information of this WorkspaceUserAuthorization.

        :return: The workspace_user_information of this WorkspaceUserAuthorization.
        :rtype: WorkspaceUser
        """
        return self._workspace_user_information

    @workspace_user_information.setter
    def workspace_user_information(self, workspace_user_information):
        """
        Sets the workspace_user_information of this WorkspaceUserAuthorization.

        :param workspace_user_information: The workspace_user_information of this WorkspaceUserAuthorization.
        :type: WorkspaceUser
        """

        self._workspace_user_information = workspace_user_information

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
