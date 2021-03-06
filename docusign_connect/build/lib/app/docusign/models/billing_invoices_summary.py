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


class BillingInvoicesSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, billing_invoices=None, past_due_balance=None, payment_allowed=None):
        """
        BillingInvoicesSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'billing_invoices': 'list[BillingInvoice]',
            'past_due_balance': 'str',
            'payment_allowed': 'str'
        }

        self.attribute_map = {
            'billing_invoices': 'billingInvoices',
            'past_due_balance': 'pastDueBalance',
            'payment_allowed': 'paymentAllowed'
        }

        self._billing_invoices = billing_invoices
        self._past_due_balance = past_due_balance
        self._payment_allowed = payment_allowed

    @property
    def billing_invoices(self):
        """
        Gets the billing_invoices of this BillingInvoicesSummary.
        Reserved: TBD

        :return: The billing_invoices of this BillingInvoicesSummary.
        :rtype: list[BillingInvoice]
        """
        return self._billing_invoices

    @billing_invoices.setter
    def billing_invoices(self, billing_invoices):
        """
        Sets the billing_invoices of this BillingInvoicesSummary.
        Reserved: TBD

        :param billing_invoices: The billing_invoices of this BillingInvoicesSummary.
        :type: list[BillingInvoice]
        """

        self._billing_invoices = billing_invoices

    @property
    def past_due_balance(self):
        """
        Gets the past_due_balance of this BillingInvoicesSummary.
        

        :return: The past_due_balance of this BillingInvoicesSummary.
        :rtype: str
        """
        return self._past_due_balance

    @past_due_balance.setter
    def past_due_balance(self, past_due_balance):
        """
        Sets the past_due_balance of this BillingInvoicesSummary.
        

        :param past_due_balance: The past_due_balance of this BillingInvoicesSummary.
        :type: str
        """

        self._past_due_balance = past_due_balance

    @property
    def payment_allowed(self):
        """
        Gets the payment_allowed of this BillingInvoicesSummary.
        

        :return: The payment_allowed of this BillingInvoicesSummary.
        :rtype: str
        """
        return self._payment_allowed

    @payment_allowed.setter
    def payment_allowed(self, payment_allowed):
        """
        Sets the payment_allowed of this BillingInvoicesSummary.
        

        :param payment_allowed: The payment_allowed of this BillingInvoicesSummary.
        :type: str
        """

        self._payment_allowed = payment_allowed

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
