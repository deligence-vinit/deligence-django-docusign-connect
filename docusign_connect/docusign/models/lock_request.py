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


class LockRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, lock_duration_in_seconds=None, locked_by_app=None, lock_type=None, template_password=None, use_scratch_pad=None):
        """
        LockRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'lock_duration_in_seconds': 'str',
            'locked_by_app': 'str',
            'lock_type': 'str',
            'template_password': 'str',
            'use_scratch_pad': 'str'
        }

        self.attribute_map = {
            'lock_duration_in_seconds': 'lockDurationInSeconds',
            'locked_by_app': 'lockedByApp',
            'lock_type': 'lockType',
            'template_password': 'templatePassword',
            'use_scratch_pad': 'useScratchPad'
        }

        self._lock_duration_in_seconds = lock_duration_in_seconds
        self._locked_by_app = locked_by_app
        self._lock_type = lock_type
        self._template_password = template_password
        self._use_scratch_pad = use_scratch_pad

    @property
    def lock_duration_in_seconds(self):
        """
        Gets the lock_duration_in_seconds of this LockRequest.
        The number of seconds to lock the envelope for editing.  Must be greater than 0 seconds.

        :return: The lock_duration_in_seconds of this LockRequest.
        :rtype: str
        """
        return self._lock_duration_in_seconds

    @lock_duration_in_seconds.setter
    def lock_duration_in_seconds(self, lock_duration_in_seconds):
        """
        Sets the lock_duration_in_seconds of this LockRequest.
        The number of seconds to lock the envelope for editing.  Must be greater than 0 seconds.

        :param lock_duration_in_seconds: The lock_duration_in_seconds of this LockRequest.
        :type: str
        """

        self._lock_duration_in_seconds = lock_duration_in_seconds

    @property
    def locked_by_app(self):
        """
        Gets the locked_by_app of this LockRequest.
        A friendly name of the application used to lock the envelope.  Will be used in error messages to the user when lock conflicts occur.

        :return: The locked_by_app of this LockRequest.
        :rtype: str
        """
        return self._locked_by_app

    @locked_by_app.setter
    def locked_by_app(self, locked_by_app):
        """
        Sets the locked_by_app of this LockRequest.
        A friendly name of the application used to lock the envelope.  Will be used in error messages to the user when lock conflicts occur.

        :param locked_by_app: The locked_by_app of this LockRequest.
        :type: str
        """

        self._locked_by_app = locked_by_app

    @property
    def lock_type(self):
        """
        Gets the lock_type of this LockRequest.
        The type of envelope lock.  Currently \"edit\" is the only supported type.

        :return: The lock_type of this LockRequest.
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        """
        Sets the lock_type of this LockRequest.
        The type of envelope lock.  Currently \"edit\" is the only supported type.

        :param lock_type: The lock_type of this LockRequest.
        :type: str
        """

        self._lock_type = lock_type

    @property
    def template_password(self):
        """
        Gets the template_password of this LockRequest.
        

        :return: The template_password of this LockRequest.
        :rtype: str
        """
        return self._template_password

    @template_password.setter
    def template_password(self, template_password):
        """
        Sets the template_password of this LockRequest.
        

        :param template_password: The template_password of this LockRequest.
        :type: str
        """

        self._template_password = template_password

    @property
    def use_scratch_pad(self):
        """
        Gets the use_scratch_pad of this LockRequest.
        Reserved for future use.  Indicates whether a scratchpad is used for editing information.  

        :return: The use_scratch_pad of this LockRequest.
        :rtype: str
        """
        return self._use_scratch_pad

    @use_scratch_pad.setter
    def use_scratch_pad(self, use_scratch_pad):
        """
        Sets the use_scratch_pad of this LockRequest.
        Reserved for future use.  Indicates whether a scratchpad is used for editing information.  

        :param use_scratch_pad: The use_scratch_pad of this LockRequest.
        :type: str
        """

        self._use_scratch_pad = use_scratch_pad

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