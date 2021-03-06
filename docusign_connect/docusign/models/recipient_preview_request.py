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


class RecipientPreviewRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, assertion_id=None, authentication_instant=None, authentication_method=None, ping_frequency=None, ping_url=None, recipient_id=None, return_url=None, security_domain=None, x_frame_options=None, x_frame_options_allow_from_url=None):
        """
        RecipientPreviewRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'assertion_id': 'str',
            'authentication_instant': 'str',
            'authentication_method': 'str',
            'ping_frequency': 'str',
            'ping_url': 'str',
            'recipient_id': 'str',
            'return_url': 'str',
            'security_domain': 'str',
            'x_frame_options': 'str',
            'x_frame_options_allow_from_url': 'str'
        }

        self.attribute_map = {
            'assertion_id': 'assertionId',
            'authentication_instant': 'authenticationInstant',
            'authentication_method': 'authenticationMethod',
            'ping_frequency': 'pingFrequency',
            'ping_url': 'pingUrl',
            'recipient_id': 'recipientId',
            'return_url': 'returnUrl',
            'security_domain': 'securityDomain',
            'x_frame_options': 'xFrameOptions',
            'x_frame_options_allow_from_url': 'xFrameOptionsAllowFromUrl'
        }

        self._assertion_id = assertion_id
        self._authentication_instant = authentication_instant
        self._authentication_method = authentication_method
        self._ping_frequency = ping_frequency
        self._ping_url = ping_url
        self._recipient_id = recipient_id
        self._return_url = return_url
        self._security_domain = security_domain
        self._x_frame_options = x_frame_options
        self._x_frame_options_allow_from_url = x_frame_options_allow_from_url

    @property
    def assertion_id(self):
        """
        Gets the assertion_id of this RecipientPreviewRequest.
        

        :return: The assertion_id of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._assertion_id

    @assertion_id.setter
    def assertion_id(self, assertion_id):
        """
        Sets the assertion_id of this RecipientPreviewRequest.
        

        :param assertion_id: The assertion_id of this RecipientPreviewRequest.
        :type: str
        """

        self._assertion_id = assertion_id

    @property
    def authentication_instant(self):
        """
        Gets the authentication_instant of this RecipientPreviewRequest.
        

        :return: The authentication_instant of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._authentication_instant

    @authentication_instant.setter
    def authentication_instant(self, authentication_instant):
        """
        Sets the authentication_instant of this RecipientPreviewRequest.
        

        :param authentication_instant: The authentication_instant of this RecipientPreviewRequest.
        :type: str
        """

        self._authentication_instant = authentication_instant

    @property
    def authentication_method(self):
        """
        Gets the authentication_method of this RecipientPreviewRequest.
        

        :return: The authentication_method of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """
        Sets the authentication_method of this RecipientPreviewRequest.
        

        :param authentication_method: The authentication_method of this RecipientPreviewRequest.
        :type: str
        """

        self._authentication_method = authentication_method

    @property
    def ping_frequency(self):
        """
        Gets the ping_frequency of this RecipientPreviewRequest.
        

        :return: The ping_frequency of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._ping_frequency

    @ping_frequency.setter
    def ping_frequency(self, ping_frequency):
        """
        Sets the ping_frequency of this RecipientPreviewRequest.
        

        :param ping_frequency: The ping_frequency of this RecipientPreviewRequest.
        :type: str
        """

        self._ping_frequency = ping_frequency

    @property
    def ping_url(self):
        """
        Gets the ping_url of this RecipientPreviewRequest.
        

        :return: The ping_url of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._ping_url

    @ping_url.setter
    def ping_url(self, ping_url):
        """
        Sets the ping_url of this RecipientPreviewRequest.
        

        :param ping_url: The ping_url of this RecipientPreviewRequest.
        :type: str
        """

        self._ping_url = ping_url

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this RecipientPreviewRequest.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :return: The recipient_id of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this RecipientPreviewRequest.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :param recipient_id: The recipient_id of this RecipientPreviewRequest.
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def return_url(self):
        """
        Gets the return_url of this RecipientPreviewRequest.
        

        :return: The return_url of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """
        Sets the return_url of this RecipientPreviewRequest.
        

        :param return_url: The return_url of this RecipientPreviewRequest.
        :type: str
        """

        self._return_url = return_url

    @property
    def security_domain(self):
        """
        Gets the security_domain of this RecipientPreviewRequest.
        

        :return: The security_domain of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._security_domain

    @security_domain.setter
    def security_domain(self, security_domain):
        """
        Sets the security_domain of this RecipientPreviewRequest.
        

        :param security_domain: The security_domain of this RecipientPreviewRequest.
        :type: str
        """

        self._security_domain = security_domain

    @property
    def x_frame_options(self):
        """
        Gets the x_frame_options of this RecipientPreviewRequest.
        

        :return: The x_frame_options of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._x_frame_options

    @x_frame_options.setter
    def x_frame_options(self, x_frame_options):
        """
        Sets the x_frame_options of this RecipientPreviewRequest.
        

        :param x_frame_options: The x_frame_options of this RecipientPreviewRequest.
        :type: str
        """

        self._x_frame_options = x_frame_options

    @property
    def x_frame_options_allow_from_url(self):
        """
        Gets the x_frame_options_allow_from_url of this RecipientPreviewRequest.
        

        :return: The x_frame_options_allow_from_url of this RecipientPreviewRequest.
        :rtype: str
        """
        return self._x_frame_options_allow_from_url

    @x_frame_options_allow_from_url.setter
    def x_frame_options_allow_from_url(self, x_frame_options_allow_from_url):
        """
        Sets the x_frame_options_allow_from_url of this RecipientPreviewRequest.
        

        :param x_frame_options_allow_from_url: The x_frame_options_allow_from_url of this RecipientPreviewRequest.
        :type: str
        """

        self._x_frame_options_allow_from_url = x_frame_options_allow_from_url

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
