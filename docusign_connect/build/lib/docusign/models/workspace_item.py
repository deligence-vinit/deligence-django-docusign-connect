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


class WorkspaceItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, caller_authorization=None, content_type=None, created=None, created_by_id=None, created_by_information=None, extension=None, file_size=None, file_uri=None, id=None, is_public=None, last_modified=None, last_modified_by_id=None, last_modified_by_information=None, name=None, page_count=None, parent_folder_id=None, parent_folder_uri=None, sha256=None, thumb_height=None, thumbnail=None, thumb_width=None, type=None, uri=None, user_authorization=None):
        """
        WorkspaceItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'caller_authorization': 'WorkspaceUserAuthorization',
            'content_type': 'str',
            'created': 'str',
            'created_by_id': 'str',
            'created_by_information': 'WorkspaceUser',
            'extension': 'str',
            'file_size': 'str',
            'file_uri': 'str',
            'id': 'str',
            'is_public': 'str',
            'last_modified': 'str',
            'last_modified_by_id': 'str',
            'last_modified_by_information': 'WorkspaceUser',
            'name': 'str',
            'page_count': 'str',
            'parent_folder_id': 'str',
            'parent_folder_uri': 'str',
            'sha256': 'str',
            'thumb_height': 'str',
            'thumbnail': 'Page',
            'thumb_width': 'str',
            'type': 'str',
            'uri': 'str',
            'user_authorization': 'WorkspaceUserAuthorization'
        }

        self.attribute_map = {
            'caller_authorization': 'callerAuthorization',
            'content_type': 'contentType',
            'created': 'created',
            'created_by_id': 'createdById',
            'created_by_information': 'createdByInformation',
            'extension': 'extension',
            'file_size': 'fileSize',
            'file_uri': 'fileUri',
            'id': 'id',
            'is_public': 'isPublic',
            'last_modified': 'lastModified',
            'last_modified_by_id': 'lastModifiedById',
            'last_modified_by_information': 'lastModifiedByInformation',
            'name': 'name',
            'page_count': 'pageCount',
            'parent_folder_id': 'parentFolderId',
            'parent_folder_uri': 'parentFolderUri',
            'sha256': 'sha256',
            'thumb_height': 'thumbHeight',
            'thumbnail': 'thumbnail',
            'thumb_width': 'thumbWidth',
            'type': 'type',
            'uri': 'uri',
            'user_authorization': 'userAuthorization'
        }

        self._caller_authorization = caller_authorization
        self._content_type = content_type
        self._created = created
        self._created_by_id = created_by_id
        self._created_by_information = created_by_information
        self._extension = extension
        self._file_size = file_size
        self._file_uri = file_uri
        self._id = id
        self._is_public = is_public
        self._last_modified = last_modified
        self._last_modified_by_id = last_modified_by_id
        self._last_modified_by_information = last_modified_by_information
        self._name = name
        self._page_count = page_count
        self._parent_folder_id = parent_folder_id
        self._parent_folder_uri = parent_folder_uri
        self._sha256 = sha256
        self._thumb_height = thumb_height
        self._thumbnail = thumbnail
        self._thumb_width = thumb_width
        self._type = type
        self._uri = uri
        self._user_authorization = user_authorization

    @property
    def caller_authorization(self):
        """
        Gets the caller_authorization of this WorkspaceItem.

        :return: The caller_authorization of this WorkspaceItem.
        :rtype: WorkspaceUserAuthorization
        """
        return self._caller_authorization

    @caller_authorization.setter
    def caller_authorization(self, caller_authorization):
        """
        Sets the caller_authorization of this WorkspaceItem.

        :param caller_authorization: The caller_authorization of this WorkspaceItem.
        :type: WorkspaceUserAuthorization
        """

        self._caller_authorization = caller_authorization

    @property
    def content_type(self):
        """
        Gets the content_type of this WorkspaceItem.
        

        :return: The content_type of this WorkspaceItem.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this WorkspaceItem.
        

        :param content_type: The content_type of this WorkspaceItem.
        :type: str
        """

        self._content_type = content_type

    @property
    def created(self):
        """
        Gets the created of this WorkspaceItem.
        The UTC DateTime when the workspace item was created.

        :return: The created of this WorkspaceItem.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this WorkspaceItem.
        The UTC DateTime when the workspace item was created.

        :param created: The created of this WorkspaceItem.
        :type: str
        """

        self._created = created

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this WorkspaceItem.
        

        :return: The created_by_id of this WorkspaceItem.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this WorkspaceItem.
        

        :param created_by_id: The created_by_id of this WorkspaceItem.
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_by_information(self):
        """
        Gets the created_by_information of this WorkspaceItem.

        :return: The created_by_information of this WorkspaceItem.
        :rtype: WorkspaceUser
        """
        return self._created_by_information

    @created_by_information.setter
    def created_by_information(self, created_by_information):
        """
        Sets the created_by_information of this WorkspaceItem.

        :param created_by_information: The created_by_information of this WorkspaceItem.
        :type: WorkspaceUser
        """

        self._created_by_information = created_by_information

    @property
    def extension(self):
        """
        Gets the extension of this WorkspaceItem.
        

        :return: The extension of this WorkspaceItem.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this WorkspaceItem.
        

        :param extension: The extension of this WorkspaceItem.
        :type: str
        """

        self._extension = extension

    @property
    def file_size(self):
        """
        Gets the file_size of this WorkspaceItem.
        

        :return: The file_size of this WorkspaceItem.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """
        Sets the file_size of this WorkspaceItem.
        

        :param file_size: The file_size of this WorkspaceItem.
        :type: str
        """

        self._file_size = file_size

    @property
    def file_uri(self):
        """
        Gets the file_uri of this WorkspaceItem.
        

        :return: The file_uri of this WorkspaceItem.
        :rtype: str
        """
        return self._file_uri

    @file_uri.setter
    def file_uri(self, file_uri):
        """
        Sets the file_uri of this WorkspaceItem.
        

        :param file_uri: The file_uri of this WorkspaceItem.
        :type: str
        """

        self._file_uri = file_uri

    @property
    def id(self):
        """
        Gets the id of this WorkspaceItem.
        

        :return: The id of this WorkspaceItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkspaceItem.
        

        :param id: The id of this WorkspaceItem.
        :type: str
        """

        self._id = id

    @property
    def is_public(self):
        """
        Gets the is_public of this WorkspaceItem.
         If true, this supersedes need for bit mask permission with workspaceUserAuthorization

        :return: The is_public of this WorkspaceItem.
        :rtype: str
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this WorkspaceItem.
         If true, this supersedes need for bit mask permission with workspaceUserAuthorization

        :param is_public: The is_public of this WorkspaceItem.
        :type: str
        """

        self._is_public = is_public

    @property
    def last_modified(self):
        """
        Gets the last_modified of this WorkspaceItem.
        

        :return: The last_modified of this WorkspaceItem.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this WorkspaceItem.
        

        :param last_modified: The last_modified of this WorkspaceItem.
        :type: str
        """

        self._last_modified = last_modified

    @property
    def last_modified_by_id(self):
        """
        Gets the last_modified_by_id of this WorkspaceItem.
        Utc date and time the comment was last updated (can only be done by creator)

        :return: The last_modified_by_id of this WorkspaceItem.
        :rtype: str
        """
        return self._last_modified_by_id

    @last_modified_by_id.setter
    def last_modified_by_id(self, last_modified_by_id):
        """
        Sets the last_modified_by_id of this WorkspaceItem.
        Utc date and time the comment was last updated (can only be done by creator)

        :param last_modified_by_id: The last_modified_by_id of this WorkspaceItem.
        :type: str
        """

        self._last_modified_by_id = last_modified_by_id

    @property
    def last_modified_by_information(self):
        """
        Gets the last_modified_by_information of this WorkspaceItem.

        :return: The last_modified_by_information of this WorkspaceItem.
        :rtype: WorkspaceUser
        """
        return self._last_modified_by_information

    @last_modified_by_information.setter
    def last_modified_by_information(self, last_modified_by_information):
        """
        Sets the last_modified_by_information of this WorkspaceItem.

        :param last_modified_by_information: The last_modified_by_information of this WorkspaceItem.
        :type: WorkspaceUser
        """

        self._last_modified_by_information = last_modified_by_information

    @property
    def name(self):
        """
        Gets the name of this WorkspaceItem.
        A simple string description of the item, such as a file name or a folder name.

        :return: The name of this WorkspaceItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkspaceItem.
        A simple string description of the item, such as a file name or a folder name.

        :param name: The name of this WorkspaceItem.
        :type: str
        """

        self._name = name

    @property
    def page_count(self):
        """
        Gets the page_count of this WorkspaceItem.
        

        :return: The page_count of this WorkspaceItem.
        :rtype: str
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this WorkspaceItem.
        

        :param page_count: The page_count of this WorkspaceItem.
        :type: str
        """

        self._page_count = page_count

    @property
    def parent_folder_id(self):
        """
        Gets the parent_folder_id of this WorkspaceItem.
        The ID of the parent folder. This is the GUID of the parent folder, or the special value 'root' for the root folder.

        :return: The parent_folder_id of this WorkspaceItem.
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """
        Sets the parent_folder_id of this WorkspaceItem.
        The ID of the parent folder. This is the GUID of the parent folder, or the special value 'root' for the root folder.

        :param parent_folder_id: The parent_folder_id of this WorkspaceItem.
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def parent_folder_uri(self):
        """
        Gets the parent_folder_uri of this WorkspaceItem.
        

        :return: The parent_folder_uri of this WorkspaceItem.
        :rtype: str
        """
        return self._parent_folder_uri

    @parent_folder_uri.setter
    def parent_folder_uri(self, parent_folder_uri):
        """
        Sets the parent_folder_uri of this WorkspaceItem.
        

        :param parent_folder_uri: The parent_folder_uri of this WorkspaceItem.
        :type: str
        """

        self._parent_folder_uri = parent_folder_uri

    @property
    def sha256(self):
        """
        Gets the sha256 of this WorkspaceItem.
        

        :return: The sha256 of this WorkspaceItem.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """
        Sets the sha256 of this WorkspaceItem.
        

        :param sha256: The sha256 of this WorkspaceItem.
        :type: str
        """

        self._sha256 = sha256

    @property
    def thumb_height(self):
        """
        Gets the thumb_height of this WorkspaceItem.
        

        :return: The thumb_height of this WorkspaceItem.
        :rtype: str
        """
        return self._thumb_height

    @thumb_height.setter
    def thumb_height(self, thumb_height):
        """
        Sets the thumb_height of this WorkspaceItem.
        

        :param thumb_height: The thumb_height of this WorkspaceItem.
        :type: str
        """

        self._thumb_height = thumb_height

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this WorkspaceItem.

        :return: The thumbnail of this WorkspaceItem.
        :rtype: Page
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this WorkspaceItem.

        :param thumbnail: The thumbnail of this WorkspaceItem.
        :type: Page
        """

        self._thumbnail = thumbnail

    @property
    def thumb_width(self):
        """
        Gets the thumb_width of this WorkspaceItem.
        

        :return: The thumb_width of this WorkspaceItem.
        :rtype: str
        """
        return self._thumb_width

    @thumb_width.setter
    def thumb_width(self, thumb_width):
        """
        Sets the thumb_width of this WorkspaceItem.
        

        :param thumb_width: The thumb_width of this WorkspaceItem.
        :type: str
        """

        self._thumb_width = thumb_width

    @property
    def type(self):
        """
        Gets the type of this WorkspaceItem.
        The type of the workspace item. Valid values are file, folder.

        :return: The type of this WorkspaceItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WorkspaceItem.
        The type of the workspace item. Valid values are file, folder.

        :param type: The type of this WorkspaceItem.
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """
        Gets the uri of this WorkspaceItem.
        

        :return: The uri of this WorkspaceItem.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this WorkspaceItem.
        

        :param uri: The uri of this WorkspaceItem.
        :type: str
        """

        self._uri = uri

    @property
    def user_authorization(self):
        """
        Gets the user_authorization of this WorkspaceItem.

        :return: The user_authorization of this WorkspaceItem.
        :rtype: WorkspaceUserAuthorization
        """
        return self._user_authorization

    @user_authorization.setter
    def user_authorization(self, user_authorization):
        """
        Sets the user_authorization of this WorkspaceItem.

        :param user_authorization: The user_authorization of this WorkspaceItem.
        :type: WorkspaceUserAuthorization
        """

        self._user_authorization = user_authorization

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