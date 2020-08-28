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


class TabAccountSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allow_tab_order=None, allow_tab_order_metadata=None, approve_decline_tabs_enabled=None, approve_decline_tabs_metadata=None, calculated_fields_enabled=None, calculated_fields_metadata=None, checkbox_tabs_enabled=None, check_box_tabs_metadata=None, data_field_regex_enabled=None, data_field_regex_metadata=None, data_field_size_enabled=None, data_field_size_metadata=None, draw_tabs_enabled=None, draw_tabs_metadata=None, first_last_email_tabs_enabled=None, first_last_email_tabs_metadata=None, list_tabs_enabled=None, list_tabs_metadata=None, note_tabs_enabled=None, note_tabs_metadata=None, radio_tabs_enabled=None, radio_tabs_metadata=None, saving_custom_tabs_enabled=None, saving_custom_tabs_metadata=None, sender_to_change_tab_assignments_enabled=None, sender_to_change_tab_assignments_metadata=None, shared_custom_tabs_enabled=None, shared_custom_tabs_metadata=None, tab_data_label_enabled=None, tab_data_label_metadata=None, tab_location_enabled=None, tab_location_metadata=None, tab_locking_enabled=None, tab_locking_metadata=None, tab_scale_enabled=None, tab_scale_metadata=None, tab_text_formatting_enabled=None, tab_text_formatting_metadata=None, text_tabs_enabled=None, text_tabs_metadata=None):
        """
        TabAccountSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allow_tab_order': 'str',
            'allow_tab_order_metadata': 'SettingsMetadata',
            'approve_decline_tabs_enabled': 'str',
            'approve_decline_tabs_metadata': 'SettingsMetadata',
            'calculated_fields_enabled': 'str',
            'calculated_fields_metadata': 'SettingsMetadata',
            'checkbox_tabs_enabled': 'str',
            'check_box_tabs_metadata': 'SettingsMetadata',
            'data_field_regex_enabled': 'str',
            'data_field_regex_metadata': 'SettingsMetadata',
            'data_field_size_enabled': 'str',
            'data_field_size_metadata': 'SettingsMetadata',
            'draw_tabs_enabled': 'str',
            'draw_tabs_metadata': 'SettingsMetadata',
            'first_last_email_tabs_enabled': 'str',
            'first_last_email_tabs_metadata': 'SettingsMetadata',
            'list_tabs_enabled': 'str',
            'list_tabs_metadata': 'SettingsMetadata',
            'note_tabs_enabled': 'str',
            'note_tabs_metadata': 'SettingsMetadata',
            'radio_tabs_enabled': 'str',
            'radio_tabs_metadata': 'SettingsMetadata',
            'saving_custom_tabs_enabled': 'str',
            'saving_custom_tabs_metadata': 'SettingsMetadata',
            'sender_to_change_tab_assignments_enabled': 'str',
            'sender_to_change_tab_assignments_metadata': 'SettingsMetadata',
            'shared_custom_tabs_enabled': 'str',
            'shared_custom_tabs_metadata': 'SettingsMetadata',
            'tab_data_label_enabled': 'str',
            'tab_data_label_metadata': 'SettingsMetadata',
            'tab_location_enabled': 'str',
            'tab_location_metadata': 'SettingsMetadata',
            'tab_locking_enabled': 'str',
            'tab_locking_metadata': 'SettingsMetadata',
            'tab_scale_enabled': 'str',
            'tab_scale_metadata': 'SettingsMetadata',
            'tab_text_formatting_enabled': 'str',
            'tab_text_formatting_metadata': 'SettingsMetadata',
            'text_tabs_enabled': 'str',
            'text_tabs_metadata': 'SettingsMetadata'
        }

        self.attribute_map = {
            'allow_tab_order': 'allowTabOrder',
            'allow_tab_order_metadata': 'allowTabOrderMetadata',
            'approve_decline_tabs_enabled': 'approveDeclineTabsEnabled',
            'approve_decline_tabs_metadata': 'approveDeclineTabsMetadata',
            'calculated_fields_enabled': 'calculatedFieldsEnabled',
            'calculated_fields_metadata': 'calculatedFieldsMetadata',
            'checkbox_tabs_enabled': 'checkboxTabsEnabled',
            'check_box_tabs_metadata': 'checkBoxTabsMetadata',
            'data_field_regex_enabled': 'dataFieldRegexEnabled',
            'data_field_regex_metadata': 'dataFieldRegexMetadata',
            'data_field_size_enabled': 'dataFieldSizeEnabled',
            'data_field_size_metadata': 'dataFieldSizeMetadata',
            'draw_tabs_enabled': 'drawTabsEnabled',
            'draw_tabs_metadata': 'drawTabsMetadata',
            'first_last_email_tabs_enabled': 'firstLastEmailTabsEnabled',
            'first_last_email_tabs_metadata': 'firstLastEmailTabsMetadata',
            'list_tabs_enabled': 'listTabsEnabled',
            'list_tabs_metadata': 'listTabsMetadata',
            'note_tabs_enabled': 'noteTabsEnabled',
            'note_tabs_metadata': 'noteTabsMetadata',
            'radio_tabs_enabled': 'radioTabsEnabled',
            'radio_tabs_metadata': 'radioTabsMetadata',
            'saving_custom_tabs_enabled': 'savingCustomTabsEnabled',
            'saving_custom_tabs_metadata': 'savingCustomTabsMetadata',
            'sender_to_change_tab_assignments_enabled': 'senderToChangeTabAssignmentsEnabled',
            'sender_to_change_tab_assignments_metadata': 'senderToChangeTabAssignmentsMetadata',
            'shared_custom_tabs_enabled': 'sharedCustomTabsEnabled',
            'shared_custom_tabs_metadata': 'sharedCustomTabsMetadata',
            'tab_data_label_enabled': 'tabDataLabelEnabled',
            'tab_data_label_metadata': 'tabDataLabelMetadata',
            'tab_location_enabled': 'tabLocationEnabled',
            'tab_location_metadata': 'tabLocationMetadata',
            'tab_locking_enabled': 'tabLockingEnabled',
            'tab_locking_metadata': 'tabLockingMetadata',
            'tab_scale_enabled': 'tabScaleEnabled',
            'tab_scale_metadata': 'tabScaleMetadata',
            'tab_text_formatting_enabled': 'tabTextFormattingEnabled',
            'tab_text_formatting_metadata': 'tabTextFormattingMetadata',
            'text_tabs_enabled': 'textTabsEnabled',
            'text_tabs_metadata': 'textTabsMetadata'
        }

        self._allow_tab_order = allow_tab_order
        self._allow_tab_order_metadata = allow_tab_order_metadata
        self._approve_decline_tabs_enabled = approve_decline_tabs_enabled
        self._approve_decline_tabs_metadata = approve_decline_tabs_metadata
        self._calculated_fields_enabled = calculated_fields_enabled
        self._calculated_fields_metadata = calculated_fields_metadata
        self._checkbox_tabs_enabled = checkbox_tabs_enabled
        self._check_box_tabs_metadata = check_box_tabs_metadata
        self._data_field_regex_enabled = data_field_regex_enabled
        self._data_field_regex_metadata = data_field_regex_metadata
        self._data_field_size_enabled = data_field_size_enabled
        self._data_field_size_metadata = data_field_size_metadata
        self._draw_tabs_enabled = draw_tabs_enabled
        self._draw_tabs_metadata = draw_tabs_metadata
        self._first_last_email_tabs_enabled = first_last_email_tabs_enabled
        self._first_last_email_tabs_metadata = first_last_email_tabs_metadata
        self._list_tabs_enabled = list_tabs_enabled
        self._list_tabs_metadata = list_tabs_metadata
        self._note_tabs_enabled = note_tabs_enabled
        self._note_tabs_metadata = note_tabs_metadata
        self._radio_tabs_enabled = radio_tabs_enabled
        self._radio_tabs_metadata = radio_tabs_metadata
        self._saving_custom_tabs_enabled = saving_custom_tabs_enabled
        self._saving_custom_tabs_metadata = saving_custom_tabs_metadata
        self._sender_to_change_tab_assignments_enabled = sender_to_change_tab_assignments_enabled
        self._sender_to_change_tab_assignments_metadata = sender_to_change_tab_assignments_metadata
        self._shared_custom_tabs_enabled = shared_custom_tabs_enabled
        self._shared_custom_tabs_metadata = shared_custom_tabs_metadata
        self._tab_data_label_enabled = tab_data_label_enabled
        self._tab_data_label_metadata = tab_data_label_metadata
        self._tab_location_enabled = tab_location_enabled
        self._tab_location_metadata = tab_location_metadata
        self._tab_locking_enabled = tab_locking_enabled
        self._tab_locking_metadata = tab_locking_metadata
        self._tab_scale_enabled = tab_scale_enabled
        self._tab_scale_metadata = tab_scale_metadata
        self._tab_text_formatting_enabled = tab_text_formatting_enabled
        self._tab_text_formatting_metadata = tab_text_formatting_metadata
        self._text_tabs_enabled = text_tabs_enabled
        self._text_tabs_metadata = text_tabs_metadata

    @property
    def allow_tab_order(self):
        """
        Gets the allow_tab_order of this TabAccountSettings.
        

        :return: The allow_tab_order of this TabAccountSettings.
        :rtype: str
        """
        return self._allow_tab_order

    @allow_tab_order.setter
    def allow_tab_order(self, allow_tab_order):
        """
        Sets the allow_tab_order of this TabAccountSettings.
        

        :param allow_tab_order: The allow_tab_order of this TabAccountSettings.
        :type: str
        """

        self._allow_tab_order = allow_tab_order

    @property
    def allow_tab_order_metadata(self):
        """
        Gets the allow_tab_order_metadata of this TabAccountSettings.

        :return: The allow_tab_order_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._allow_tab_order_metadata

    @allow_tab_order_metadata.setter
    def allow_tab_order_metadata(self, allow_tab_order_metadata):
        """
        Sets the allow_tab_order_metadata of this TabAccountSettings.

        :param allow_tab_order_metadata: The allow_tab_order_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._allow_tab_order_metadata = allow_tab_order_metadata

    @property
    def approve_decline_tabs_enabled(self):
        """
        Gets the approve_decline_tabs_enabled of this TabAccountSettings.
        

        :return: The approve_decline_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._approve_decline_tabs_enabled

    @approve_decline_tabs_enabled.setter
    def approve_decline_tabs_enabled(self, approve_decline_tabs_enabled):
        """
        Sets the approve_decline_tabs_enabled of this TabAccountSettings.
        

        :param approve_decline_tabs_enabled: The approve_decline_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._approve_decline_tabs_enabled = approve_decline_tabs_enabled

    @property
    def approve_decline_tabs_metadata(self):
        """
        Gets the approve_decline_tabs_metadata of this TabAccountSettings.

        :return: The approve_decline_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._approve_decline_tabs_metadata

    @approve_decline_tabs_metadata.setter
    def approve_decline_tabs_metadata(self, approve_decline_tabs_metadata):
        """
        Sets the approve_decline_tabs_metadata of this TabAccountSettings.

        :param approve_decline_tabs_metadata: The approve_decline_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._approve_decline_tabs_metadata = approve_decline_tabs_metadata

    @property
    def calculated_fields_enabled(self):
        """
        Gets the calculated_fields_enabled of this TabAccountSettings.
        

        :return: The calculated_fields_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._calculated_fields_enabled

    @calculated_fields_enabled.setter
    def calculated_fields_enabled(self, calculated_fields_enabled):
        """
        Sets the calculated_fields_enabled of this TabAccountSettings.
        

        :param calculated_fields_enabled: The calculated_fields_enabled of this TabAccountSettings.
        :type: str
        """

        self._calculated_fields_enabled = calculated_fields_enabled

    @property
    def calculated_fields_metadata(self):
        """
        Gets the calculated_fields_metadata of this TabAccountSettings.

        :return: The calculated_fields_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._calculated_fields_metadata

    @calculated_fields_metadata.setter
    def calculated_fields_metadata(self, calculated_fields_metadata):
        """
        Sets the calculated_fields_metadata of this TabAccountSettings.

        :param calculated_fields_metadata: The calculated_fields_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._calculated_fields_metadata = calculated_fields_metadata

    @property
    def checkbox_tabs_enabled(self):
        """
        Gets the checkbox_tabs_enabled of this TabAccountSettings.
        

        :return: The checkbox_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._checkbox_tabs_enabled

    @checkbox_tabs_enabled.setter
    def checkbox_tabs_enabled(self, checkbox_tabs_enabled):
        """
        Sets the checkbox_tabs_enabled of this TabAccountSettings.
        

        :param checkbox_tabs_enabled: The checkbox_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._checkbox_tabs_enabled = checkbox_tabs_enabled

    @property
    def check_box_tabs_metadata(self):
        """
        Gets the check_box_tabs_metadata of this TabAccountSettings.

        :return: The check_box_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._check_box_tabs_metadata

    @check_box_tabs_metadata.setter
    def check_box_tabs_metadata(self, check_box_tabs_metadata):
        """
        Sets the check_box_tabs_metadata of this TabAccountSettings.

        :param check_box_tabs_metadata: The check_box_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._check_box_tabs_metadata = check_box_tabs_metadata

    @property
    def data_field_regex_enabled(self):
        """
        Gets the data_field_regex_enabled of this TabAccountSettings.
        

        :return: The data_field_regex_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._data_field_regex_enabled

    @data_field_regex_enabled.setter
    def data_field_regex_enabled(self, data_field_regex_enabled):
        """
        Sets the data_field_regex_enabled of this TabAccountSettings.
        

        :param data_field_regex_enabled: The data_field_regex_enabled of this TabAccountSettings.
        :type: str
        """

        self._data_field_regex_enabled = data_field_regex_enabled

    @property
    def data_field_regex_metadata(self):
        """
        Gets the data_field_regex_metadata of this TabAccountSettings.

        :return: The data_field_regex_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._data_field_regex_metadata

    @data_field_regex_metadata.setter
    def data_field_regex_metadata(self, data_field_regex_metadata):
        """
        Sets the data_field_regex_metadata of this TabAccountSettings.

        :param data_field_regex_metadata: The data_field_regex_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._data_field_regex_metadata = data_field_regex_metadata

    @property
    def data_field_size_enabled(self):
        """
        Gets the data_field_size_enabled of this TabAccountSettings.
        

        :return: The data_field_size_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._data_field_size_enabled

    @data_field_size_enabled.setter
    def data_field_size_enabled(self, data_field_size_enabled):
        """
        Sets the data_field_size_enabled of this TabAccountSettings.
        

        :param data_field_size_enabled: The data_field_size_enabled of this TabAccountSettings.
        :type: str
        """

        self._data_field_size_enabled = data_field_size_enabled

    @property
    def data_field_size_metadata(self):
        """
        Gets the data_field_size_metadata of this TabAccountSettings.

        :return: The data_field_size_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._data_field_size_metadata

    @data_field_size_metadata.setter
    def data_field_size_metadata(self, data_field_size_metadata):
        """
        Sets the data_field_size_metadata of this TabAccountSettings.

        :param data_field_size_metadata: The data_field_size_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._data_field_size_metadata = data_field_size_metadata

    @property
    def draw_tabs_enabled(self):
        """
        Gets the draw_tabs_enabled of this TabAccountSettings.
        

        :return: The draw_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._draw_tabs_enabled

    @draw_tabs_enabled.setter
    def draw_tabs_enabled(self, draw_tabs_enabled):
        """
        Sets the draw_tabs_enabled of this TabAccountSettings.
        

        :param draw_tabs_enabled: The draw_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._draw_tabs_enabled = draw_tabs_enabled

    @property
    def draw_tabs_metadata(self):
        """
        Gets the draw_tabs_metadata of this TabAccountSettings.

        :return: The draw_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._draw_tabs_metadata

    @draw_tabs_metadata.setter
    def draw_tabs_metadata(self, draw_tabs_metadata):
        """
        Sets the draw_tabs_metadata of this TabAccountSettings.

        :param draw_tabs_metadata: The draw_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._draw_tabs_metadata = draw_tabs_metadata

    @property
    def first_last_email_tabs_enabled(self):
        """
        Gets the first_last_email_tabs_enabled of this TabAccountSettings.
        

        :return: The first_last_email_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._first_last_email_tabs_enabled

    @first_last_email_tabs_enabled.setter
    def first_last_email_tabs_enabled(self, first_last_email_tabs_enabled):
        """
        Sets the first_last_email_tabs_enabled of this TabAccountSettings.
        

        :param first_last_email_tabs_enabled: The first_last_email_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._first_last_email_tabs_enabled = first_last_email_tabs_enabled

    @property
    def first_last_email_tabs_metadata(self):
        """
        Gets the first_last_email_tabs_metadata of this TabAccountSettings.

        :return: The first_last_email_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._first_last_email_tabs_metadata

    @first_last_email_tabs_metadata.setter
    def first_last_email_tabs_metadata(self, first_last_email_tabs_metadata):
        """
        Sets the first_last_email_tabs_metadata of this TabAccountSettings.

        :param first_last_email_tabs_metadata: The first_last_email_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._first_last_email_tabs_metadata = first_last_email_tabs_metadata

    @property
    def list_tabs_enabled(self):
        """
        Gets the list_tabs_enabled of this TabAccountSettings.
        

        :return: The list_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._list_tabs_enabled

    @list_tabs_enabled.setter
    def list_tabs_enabled(self, list_tabs_enabled):
        """
        Sets the list_tabs_enabled of this TabAccountSettings.
        

        :param list_tabs_enabled: The list_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._list_tabs_enabled = list_tabs_enabled

    @property
    def list_tabs_metadata(self):
        """
        Gets the list_tabs_metadata of this TabAccountSettings.

        :return: The list_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._list_tabs_metadata

    @list_tabs_metadata.setter
    def list_tabs_metadata(self, list_tabs_metadata):
        """
        Sets the list_tabs_metadata of this TabAccountSettings.

        :param list_tabs_metadata: The list_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._list_tabs_metadata = list_tabs_metadata

    @property
    def note_tabs_enabled(self):
        """
        Gets the note_tabs_enabled of this TabAccountSettings.
        

        :return: The note_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._note_tabs_enabled

    @note_tabs_enabled.setter
    def note_tabs_enabled(self, note_tabs_enabled):
        """
        Sets the note_tabs_enabled of this TabAccountSettings.
        

        :param note_tabs_enabled: The note_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._note_tabs_enabled = note_tabs_enabled

    @property
    def note_tabs_metadata(self):
        """
        Gets the note_tabs_metadata of this TabAccountSettings.

        :return: The note_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._note_tabs_metadata

    @note_tabs_metadata.setter
    def note_tabs_metadata(self, note_tabs_metadata):
        """
        Sets the note_tabs_metadata of this TabAccountSettings.

        :param note_tabs_metadata: The note_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._note_tabs_metadata = note_tabs_metadata

    @property
    def radio_tabs_enabled(self):
        """
        Gets the radio_tabs_enabled of this TabAccountSettings.
        

        :return: The radio_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._radio_tabs_enabled

    @radio_tabs_enabled.setter
    def radio_tabs_enabled(self, radio_tabs_enabled):
        """
        Sets the radio_tabs_enabled of this TabAccountSettings.
        

        :param radio_tabs_enabled: The radio_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._radio_tabs_enabled = radio_tabs_enabled

    @property
    def radio_tabs_metadata(self):
        """
        Gets the radio_tabs_metadata of this TabAccountSettings.

        :return: The radio_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._radio_tabs_metadata

    @radio_tabs_metadata.setter
    def radio_tabs_metadata(self, radio_tabs_metadata):
        """
        Sets the radio_tabs_metadata of this TabAccountSettings.

        :param radio_tabs_metadata: The radio_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._radio_tabs_metadata = radio_tabs_metadata

    @property
    def saving_custom_tabs_enabled(self):
        """
        Gets the saving_custom_tabs_enabled of this TabAccountSettings.
        

        :return: The saving_custom_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._saving_custom_tabs_enabled

    @saving_custom_tabs_enabled.setter
    def saving_custom_tabs_enabled(self, saving_custom_tabs_enabled):
        """
        Sets the saving_custom_tabs_enabled of this TabAccountSettings.
        

        :param saving_custom_tabs_enabled: The saving_custom_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._saving_custom_tabs_enabled = saving_custom_tabs_enabled

    @property
    def saving_custom_tabs_metadata(self):
        """
        Gets the saving_custom_tabs_metadata of this TabAccountSettings.

        :return: The saving_custom_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._saving_custom_tabs_metadata

    @saving_custom_tabs_metadata.setter
    def saving_custom_tabs_metadata(self, saving_custom_tabs_metadata):
        """
        Sets the saving_custom_tabs_metadata of this TabAccountSettings.

        :param saving_custom_tabs_metadata: The saving_custom_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._saving_custom_tabs_metadata = saving_custom_tabs_metadata

    @property
    def sender_to_change_tab_assignments_enabled(self):
        """
        Gets the sender_to_change_tab_assignments_enabled of this TabAccountSettings.
        

        :return: The sender_to_change_tab_assignments_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._sender_to_change_tab_assignments_enabled

    @sender_to_change_tab_assignments_enabled.setter
    def sender_to_change_tab_assignments_enabled(self, sender_to_change_tab_assignments_enabled):
        """
        Sets the sender_to_change_tab_assignments_enabled of this TabAccountSettings.
        

        :param sender_to_change_tab_assignments_enabled: The sender_to_change_tab_assignments_enabled of this TabAccountSettings.
        :type: str
        """

        self._sender_to_change_tab_assignments_enabled = sender_to_change_tab_assignments_enabled

    @property
    def sender_to_change_tab_assignments_metadata(self):
        """
        Gets the sender_to_change_tab_assignments_metadata of this TabAccountSettings.

        :return: The sender_to_change_tab_assignments_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._sender_to_change_tab_assignments_metadata

    @sender_to_change_tab_assignments_metadata.setter
    def sender_to_change_tab_assignments_metadata(self, sender_to_change_tab_assignments_metadata):
        """
        Sets the sender_to_change_tab_assignments_metadata of this TabAccountSettings.

        :param sender_to_change_tab_assignments_metadata: The sender_to_change_tab_assignments_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._sender_to_change_tab_assignments_metadata = sender_to_change_tab_assignments_metadata

    @property
    def shared_custom_tabs_enabled(self):
        """
        Gets the shared_custom_tabs_enabled of this TabAccountSettings.
        

        :return: The shared_custom_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._shared_custom_tabs_enabled

    @shared_custom_tabs_enabled.setter
    def shared_custom_tabs_enabled(self, shared_custom_tabs_enabled):
        """
        Sets the shared_custom_tabs_enabled of this TabAccountSettings.
        

        :param shared_custom_tabs_enabled: The shared_custom_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._shared_custom_tabs_enabled = shared_custom_tabs_enabled

    @property
    def shared_custom_tabs_metadata(self):
        """
        Gets the shared_custom_tabs_metadata of this TabAccountSettings.

        :return: The shared_custom_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._shared_custom_tabs_metadata

    @shared_custom_tabs_metadata.setter
    def shared_custom_tabs_metadata(self, shared_custom_tabs_metadata):
        """
        Sets the shared_custom_tabs_metadata of this TabAccountSettings.

        :param shared_custom_tabs_metadata: The shared_custom_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._shared_custom_tabs_metadata = shared_custom_tabs_metadata

    @property
    def tab_data_label_enabled(self):
        """
        Gets the tab_data_label_enabled of this TabAccountSettings.
        

        :return: The tab_data_label_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._tab_data_label_enabled

    @tab_data_label_enabled.setter
    def tab_data_label_enabled(self, tab_data_label_enabled):
        """
        Sets the tab_data_label_enabled of this TabAccountSettings.
        

        :param tab_data_label_enabled: The tab_data_label_enabled of this TabAccountSettings.
        :type: str
        """

        self._tab_data_label_enabled = tab_data_label_enabled

    @property
    def tab_data_label_metadata(self):
        """
        Gets the tab_data_label_metadata of this TabAccountSettings.

        :return: The tab_data_label_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._tab_data_label_metadata

    @tab_data_label_metadata.setter
    def tab_data_label_metadata(self, tab_data_label_metadata):
        """
        Sets the tab_data_label_metadata of this TabAccountSettings.

        :param tab_data_label_metadata: The tab_data_label_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._tab_data_label_metadata = tab_data_label_metadata

    @property
    def tab_location_enabled(self):
        """
        Gets the tab_location_enabled of this TabAccountSettings.
        

        :return: The tab_location_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._tab_location_enabled

    @tab_location_enabled.setter
    def tab_location_enabled(self, tab_location_enabled):
        """
        Sets the tab_location_enabled of this TabAccountSettings.
        

        :param tab_location_enabled: The tab_location_enabled of this TabAccountSettings.
        :type: str
        """

        self._tab_location_enabled = tab_location_enabled

    @property
    def tab_location_metadata(self):
        """
        Gets the tab_location_metadata of this TabAccountSettings.

        :return: The tab_location_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._tab_location_metadata

    @tab_location_metadata.setter
    def tab_location_metadata(self, tab_location_metadata):
        """
        Sets the tab_location_metadata of this TabAccountSettings.

        :param tab_location_metadata: The tab_location_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._tab_location_metadata = tab_location_metadata

    @property
    def tab_locking_enabled(self):
        """
        Gets the tab_locking_enabled of this TabAccountSettings.
        

        :return: The tab_locking_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._tab_locking_enabled

    @tab_locking_enabled.setter
    def tab_locking_enabled(self, tab_locking_enabled):
        """
        Sets the tab_locking_enabled of this TabAccountSettings.
        

        :param tab_locking_enabled: The tab_locking_enabled of this TabAccountSettings.
        :type: str
        """

        self._tab_locking_enabled = tab_locking_enabled

    @property
    def tab_locking_metadata(self):
        """
        Gets the tab_locking_metadata of this TabAccountSettings.

        :return: The tab_locking_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._tab_locking_metadata

    @tab_locking_metadata.setter
    def tab_locking_metadata(self, tab_locking_metadata):
        """
        Sets the tab_locking_metadata of this TabAccountSettings.

        :param tab_locking_metadata: The tab_locking_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._tab_locking_metadata = tab_locking_metadata

    @property
    def tab_scale_enabled(self):
        """
        Gets the tab_scale_enabled of this TabAccountSettings.
        

        :return: The tab_scale_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._tab_scale_enabled

    @tab_scale_enabled.setter
    def tab_scale_enabled(self, tab_scale_enabled):
        """
        Sets the tab_scale_enabled of this TabAccountSettings.
        

        :param tab_scale_enabled: The tab_scale_enabled of this TabAccountSettings.
        :type: str
        """

        self._tab_scale_enabled = tab_scale_enabled

    @property
    def tab_scale_metadata(self):
        """
        Gets the tab_scale_metadata of this TabAccountSettings.

        :return: The tab_scale_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._tab_scale_metadata

    @tab_scale_metadata.setter
    def tab_scale_metadata(self, tab_scale_metadata):
        """
        Sets the tab_scale_metadata of this TabAccountSettings.

        :param tab_scale_metadata: The tab_scale_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._tab_scale_metadata = tab_scale_metadata

    @property
    def tab_text_formatting_enabled(self):
        """
        Gets the tab_text_formatting_enabled of this TabAccountSettings.
        

        :return: The tab_text_formatting_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._tab_text_formatting_enabled

    @tab_text_formatting_enabled.setter
    def tab_text_formatting_enabled(self, tab_text_formatting_enabled):
        """
        Sets the tab_text_formatting_enabled of this TabAccountSettings.
        

        :param tab_text_formatting_enabled: The tab_text_formatting_enabled of this TabAccountSettings.
        :type: str
        """

        self._tab_text_formatting_enabled = tab_text_formatting_enabled

    @property
    def tab_text_formatting_metadata(self):
        """
        Gets the tab_text_formatting_metadata of this TabAccountSettings.

        :return: The tab_text_formatting_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._tab_text_formatting_metadata

    @tab_text_formatting_metadata.setter
    def tab_text_formatting_metadata(self, tab_text_formatting_metadata):
        """
        Sets the tab_text_formatting_metadata of this TabAccountSettings.

        :param tab_text_formatting_metadata: The tab_text_formatting_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._tab_text_formatting_metadata = tab_text_formatting_metadata

    @property
    def text_tabs_enabled(self):
        """
        Gets the text_tabs_enabled of this TabAccountSettings.
        

        :return: The text_tabs_enabled of this TabAccountSettings.
        :rtype: str
        """
        return self._text_tabs_enabled

    @text_tabs_enabled.setter
    def text_tabs_enabled(self, text_tabs_enabled):
        """
        Sets the text_tabs_enabled of this TabAccountSettings.
        

        :param text_tabs_enabled: The text_tabs_enabled of this TabAccountSettings.
        :type: str
        """

        self._text_tabs_enabled = text_tabs_enabled

    @property
    def text_tabs_metadata(self):
        """
        Gets the text_tabs_metadata of this TabAccountSettings.

        :return: The text_tabs_metadata of this TabAccountSettings.
        :rtype: SettingsMetadata
        """
        return self._text_tabs_metadata

    @text_tabs_metadata.setter
    def text_tabs_metadata(self, text_tabs_metadata):
        """
        Sets the text_tabs_metadata of this TabAccountSettings.

        :param text_tabs_metadata: The text_tabs_metadata of this TabAccountSettings.
        :type: SettingsMetadata
        """

        self._text_tabs_metadata = text_tabs_metadata

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
