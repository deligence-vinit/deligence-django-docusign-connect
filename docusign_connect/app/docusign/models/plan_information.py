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


class PlanInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, add_ons=None, currency_code=None, free_trial_days_override=None, plan_feature_sets=None, plan_id=None, recipient_domains=None):
        """
        PlanInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'add_ons': 'list[AddOn]',
            'currency_code': 'str',
            'free_trial_days_override': 'str',
            'plan_feature_sets': 'list[FeatureSet]',
            'plan_id': 'str',
            'recipient_domains': 'list[RecipientDomain]'
        }

        self.attribute_map = {
            'add_ons': 'addOns',
            'currency_code': 'currencyCode',
            'free_trial_days_override': 'freeTrialDaysOverride',
            'plan_feature_sets': 'planFeatureSets',
            'plan_id': 'planId',
            'recipient_domains': 'recipientDomains'
        }

        self._add_ons = add_ons
        self._currency_code = currency_code
        self._free_trial_days_override = free_trial_days_override
        self._plan_feature_sets = plan_feature_sets
        self._plan_id = plan_id
        self._recipient_domains = recipient_domains

    @property
    def add_ons(self):
        """
        Gets the add_ons of this PlanInformation.
        Reserved:

        :return: The add_ons of this PlanInformation.
        :rtype: list[AddOn]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """
        Sets the add_ons of this PlanInformation.
        Reserved:

        :param add_ons: The add_ons of this PlanInformation.
        :type: list[AddOn]
        """

        self._add_ons = add_ons

    @property
    def currency_code(self):
        """
        Gets the currency_code of this PlanInformation.
        Specifies the ISO currency code for the account.

        :return: The currency_code of this PlanInformation.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this PlanInformation.
        Specifies the ISO currency code for the account.

        :param currency_code: The currency_code of this PlanInformation.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def free_trial_days_override(self):
        """
        Gets the free_trial_days_override of this PlanInformation.
        Reserved for DocuSign use only.

        :return: The free_trial_days_override of this PlanInformation.
        :rtype: str
        """
        return self._free_trial_days_override

    @free_trial_days_override.setter
    def free_trial_days_override(self, free_trial_days_override):
        """
        Sets the free_trial_days_override of this PlanInformation.
        Reserved for DocuSign use only.

        :param free_trial_days_override: The free_trial_days_override of this PlanInformation.
        :type: str
        """

        self._free_trial_days_override = free_trial_days_override

    @property
    def plan_feature_sets(self):
        """
        Gets the plan_feature_sets of this PlanInformation.
        A complex type that sets the feature sets for the account.

        :return: The plan_feature_sets of this PlanInformation.
        :rtype: list[FeatureSet]
        """
        return self._plan_feature_sets

    @plan_feature_sets.setter
    def plan_feature_sets(self, plan_feature_sets):
        """
        Sets the plan_feature_sets of this PlanInformation.
        A complex type that sets the feature sets for the account.

        :param plan_feature_sets: The plan_feature_sets of this PlanInformation.
        :type: list[FeatureSet]
        """

        self._plan_feature_sets = plan_feature_sets

    @property
    def plan_id(self):
        """
        Gets the plan_id of this PlanInformation.
        The DocuSign Plan ID for the account.

        :return: The plan_id of this PlanInformation.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this PlanInformation.
        The DocuSign Plan ID for the account.

        :param plan_id: The plan_id of this PlanInformation.
        :type: str
        """

        self._plan_id = plan_id

    @property
    def recipient_domains(self):
        """
        Gets the recipient_domains of this PlanInformation.
        

        :return: The recipient_domains of this PlanInformation.
        :rtype: list[RecipientDomain]
        """
        return self._recipient_domains

    @recipient_domains.setter
    def recipient_domains(self, recipient_domains):
        """
        Sets the recipient_domains of this PlanInformation.
        

        :param recipient_domains: The recipient_domains of this PlanInformation.
        :type: list[RecipientDomain]
        """

        self._recipient_domains = recipient_domains

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
