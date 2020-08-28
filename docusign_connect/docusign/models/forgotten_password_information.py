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


class ForgottenPasswordInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, forgotten_password_answer1=None, forgotten_password_answer2=None, forgotten_password_answer3=None, forgotten_password_answer4=None, forgotten_password_question1=None, forgotten_password_question2=None, forgotten_password_question3=None, forgotten_password_question4=None):
        """
        ForgottenPasswordInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'forgotten_password_answer1': 'str',
            'forgotten_password_answer2': 'str',
            'forgotten_password_answer3': 'str',
            'forgotten_password_answer4': 'str',
            'forgotten_password_question1': 'str',
            'forgotten_password_question2': 'str',
            'forgotten_password_question3': 'str',
            'forgotten_password_question4': 'str'
        }

        self.attribute_map = {
            'forgotten_password_answer1': 'forgottenPasswordAnswer1',
            'forgotten_password_answer2': 'forgottenPasswordAnswer2',
            'forgotten_password_answer3': 'forgottenPasswordAnswer3',
            'forgotten_password_answer4': 'forgottenPasswordAnswer4',
            'forgotten_password_question1': 'forgottenPasswordQuestion1',
            'forgotten_password_question2': 'forgottenPasswordQuestion2',
            'forgotten_password_question3': 'forgottenPasswordQuestion3',
            'forgotten_password_question4': 'forgottenPasswordQuestion4'
        }

        self._forgotten_password_answer1 = forgotten_password_answer1
        self._forgotten_password_answer2 = forgotten_password_answer2
        self._forgotten_password_answer3 = forgotten_password_answer3
        self._forgotten_password_answer4 = forgotten_password_answer4
        self._forgotten_password_question1 = forgotten_password_question1
        self._forgotten_password_question2 = forgotten_password_question2
        self._forgotten_password_question3 = forgotten_password_question3
        self._forgotten_password_question4 = forgotten_password_question4

    @property
    def forgotten_password_answer1(self):
        """
        Gets the forgotten_password_answer1 of this ForgottenPasswordInformation.
        The answer to the first forgotten password challenge question.

        :return: The forgotten_password_answer1 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_answer1

    @forgotten_password_answer1.setter
    def forgotten_password_answer1(self, forgotten_password_answer1):
        """
        Sets the forgotten_password_answer1 of this ForgottenPasswordInformation.
        The answer to the first forgotten password challenge question.

        :param forgotten_password_answer1: The forgotten_password_answer1 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_answer1 = forgotten_password_answer1

    @property
    def forgotten_password_answer2(self):
        """
        Gets the forgotten_password_answer2 of this ForgottenPasswordInformation.
        The answer to the second forgotten password challenge question.

        :return: The forgotten_password_answer2 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_answer2

    @forgotten_password_answer2.setter
    def forgotten_password_answer2(self, forgotten_password_answer2):
        """
        Sets the forgotten_password_answer2 of this ForgottenPasswordInformation.
        The answer to the second forgotten password challenge question.

        :param forgotten_password_answer2: The forgotten_password_answer2 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_answer2 = forgotten_password_answer2

    @property
    def forgotten_password_answer3(self):
        """
        Gets the forgotten_password_answer3 of this ForgottenPasswordInformation.
        The answer to the third forgotten password challenge question.

        :return: The forgotten_password_answer3 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_answer3

    @forgotten_password_answer3.setter
    def forgotten_password_answer3(self, forgotten_password_answer3):
        """
        Sets the forgotten_password_answer3 of this ForgottenPasswordInformation.
        The answer to the third forgotten password challenge question.

        :param forgotten_password_answer3: The forgotten_password_answer3 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_answer3 = forgotten_password_answer3

    @property
    def forgotten_password_answer4(self):
        """
        Gets the forgotten_password_answer4 of this ForgottenPasswordInformation.
        The answer to the fourth forgotten password challenge question.

        :return: The forgotten_password_answer4 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_answer4

    @forgotten_password_answer4.setter
    def forgotten_password_answer4(self, forgotten_password_answer4):
        """
        Sets the forgotten_password_answer4 of this ForgottenPasswordInformation.
        The answer to the fourth forgotten password challenge question.

        :param forgotten_password_answer4: The forgotten_password_answer4 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_answer4 = forgotten_password_answer4

    @property
    def forgotten_password_question1(self):
        """
        Gets the forgotten_password_question1 of this ForgottenPasswordInformation.
        The first challenge question presented to a user who has forgotten their password.

        :return: The forgotten_password_question1 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_question1

    @forgotten_password_question1.setter
    def forgotten_password_question1(self, forgotten_password_question1):
        """
        Sets the forgotten_password_question1 of this ForgottenPasswordInformation.
        The first challenge question presented to a user who has forgotten their password.

        :param forgotten_password_question1: The forgotten_password_question1 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_question1 = forgotten_password_question1

    @property
    def forgotten_password_question2(self):
        """
        Gets the forgotten_password_question2 of this ForgottenPasswordInformation.
        The second challenge question presented to a user who has forgotten their password.

        :return: The forgotten_password_question2 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_question2

    @forgotten_password_question2.setter
    def forgotten_password_question2(self, forgotten_password_question2):
        """
        Sets the forgotten_password_question2 of this ForgottenPasswordInformation.
        The second challenge question presented to a user who has forgotten their password.

        :param forgotten_password_question2: The forgotten_password_question2 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_question2 = forgotten_password_question2

    @property
    def forgotten_password_question3(self):
        """
        Gets the forgotten_password_question3 of this ForgottenPasswordInformation.
        The third challenge question presented to a user who has forgotten their password.

        :return: The forgotten_password_question3 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_question3

    @forgotten_password_question3.setter
    def forgotten_password_question3(self, forgotten_password_question3):
        """
        Sets the forgotten_password_question3 of this ForgottenPasswordInformation.
        The third challenge question presented to a user who has forgotten their password.

        :param forgotten_password_question3: The forgotten_password_question3 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_question3 = forgotten_password_question3

    @property
    def forgotten_password_question4(self):
        """
        Gets the forgotten_password_question4 of this ForgottenPasswordInformation.
        The fourth challenge question presented to a user who has forgotten their password.

        :return: The forgotten_password_question4 of this ForgottenPasswordInformation.
        :rtype: str
        """
        return self._forgotten_password_question4

    @forgotten_password_question4.setter
    def forgotten_password_question4(self, forgotten_password_question4):
        """
        Sets the forgotten_password_question4 of this ForgottenPasswordInformation.
        The fourth challenge question presented to a user who has forgotten their password.

        :param forgotten_password_question4: The forgotten_password_question4 of this ForgottenPasswordInformation.
        :type: str
        """

        self._forgotten_password_question4 = forgotten_password_question4

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
