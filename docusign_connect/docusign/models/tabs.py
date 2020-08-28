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


class Tabs(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, approve_tabs=None, checkbox_tabs=None, comment_thread_tabs=None, company_tabs=None, date_signed_tabs=None, date_tabs=None, decline_tabs=None, draw_tabs=None, email_address_tabs=None, email_tabs=None, envelope_id_tabs=None, first_name_tabs=None, formula_tabs=None, full_name_tabs=None, initial_here_tabs=None, last_name_tabs=None, list_tabs=None, notarize_tabs=None, note_tabs=None, number_tabs=None, poly_line_overlay_tabs=None, radio_group_tabs=None, signer_attachment_tabs=None, sign_here_tabs=None, smart_section_tabs=None, ssn_tabs=None, tab_groups=None, text_tabs=None, title_tabs=None, view_tabs=None, zip_tabs=None):
        """
        Tabs - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'approve_tabs': 'list[Approve]',
            'checkbox_tabs': 'list[Checkbox]',
            'comment_thread_tabs': 'list[CommentThread]',
            'company_tabs': 'list[Company]',
            'date_signed_tabs': 'list[DateSigned]',
            'date_tabs': 'list[Date]',
            'decline_tabs': 'list[Decline]',
            'draw_tabs': 'list[Draw]',
            'email_address_tabs': 'list[EmailAddress]',
            'email_tabs': 'list[Email]',
            'envelope_id_tabs': 'list[EnvelopeId]',
            'first_name_tabs': 'list[FirstName]',
            'formula_tabs': 'list[FormulaTab]',
            'full_name_tabs': 'list[FullName]',
            'initial_here_tabs': 'list[InitialHere]',
            'last_name_tabs': 'list[LastName]',
            'list_tabs': 'list[List]',
            'notarize_tabs': 'list[Notarize]',
            'note_tabs': 'list[Note]',
            'number_tabs': 'list[Number]',
            'poly_line_overlay_tabs': 'list[PolyLineOverlay]',
            'radio_group_tabs': 'list[RadioGroup]',
            'signer_attachment_tabs': 'list[SignerAttachment]',
            'sign_here_tabs': 'list[SignHere]',
            'smart_section_tabs': 'list[SmartSection]',
            'ssn_tabs': 'list[Ssn]',
            'tab_groups': 'list[TabGroup]',
            'text_tabs': 'list[Text]',
            'title_tabs': 'list[Title]',
            'view_tabs': 'list[View]',
            'zip_tabs': 'list[Zip]'
        }

        self.attribute_map = {
            'approve_tabs': 'approveTabs',
            'checkbox_tabs': 'checkboxTabs',
            'comment_thread_tabs': 'commentThreadTabs',
            'company_tabs': 'companyTabs',
            'date_signed_tabs': 'dateSignedTabs',
            'date_tabs': 'dateTabs',
            'decline_tabs': 'declineTabs',
            'draw_tabs': 'drawTabs',
            'email_address_tabs': 'emailAddressTabs',
            'email_tabs': 'emailTabs',
            'envelope_id_tabs': 'envelopeIdTabs',
            'first_name_tabs': 'firstNameTabs',
            'formula_tabs': 'formulaTabs',
            'full_name_tabs': 'fullNameTabs',
            'initial_here_tabs': 'initialHereTabs',
            'last_name_tabs': 'lastNameTabs',
            'list_tabs': 'listTabs',
            'notarize_tabs': 'notarizeTabs',
            'note_tabs': 'noteTabs',
            'number_tabs': 'numberTabs',
            'poly_line_overlay_tabs': 'polyLineOverlayTabs',
            'radio_group_tabs': 'radioGroupTabs',
            'signer_attachment_tabs': 'signerAttachmentTabs',
            'sign_here_tabs': 'signHereTabs',
            'smart_section_tabs': 'smartSectionTabs',
            'ssn_tabs': 'ssnTabs',
            'tab_groups': 'tabGroups',
            'text_tabs': 'textTabs',
            'title_tabs': 'titleTabs',
            'view_tabs': 'viewTabs',
            'zip_tabs': 'zipTabs'
        }

        self._approve_tabs = approve_tabs
        self._checkbox_tabs = checkbox_tabs
        self._comment_thread_tabs = comment_thread_tabs
        self._company_tabs = company_tabs
        self._date_signed_tabs = date_signed_tabs
        self._date_tabs = date_tabs
        self._decline_tabs = decline_tabs
        self._draw_tabs = draw_tabs
        self._email_address_tabs = email_address_tabs
        self._email_tabs = email_tabs
        self._envelope_id_tabs = envelope_id_tabs
        self._first_name_tabs = first_name_tabs
        self._formula_tabs = formula_tabs
        self._full_name_tabs = full_name_tabs
        self._initial_here_tabs = initial_here_tabs
        self._last_name_tabs = last_name_tabs
        self._list_tabs = list_tabs
        self._notarize_tabs = notarize_tabs
        self._note_tabs = note_tabs
        self._number_tabs = number_tabs
        self._poly_line_overlay_tabs = poly_line_overlay_tabs
        self._radio_group_tabs = radio_group_tabs
        self._signer_attachment_tabs = signer_attachment_tabs
        self._sign_here_tabs = sign_here_tabs
        self._smart_section_tabs = smart_section_tabs
        self._ssn_tabs = ssn_tabs
        self._tab_groups = tab_groups
        self._text_tabs = text_tabs
        self._title_tabs = title_tabs
        self._view_tabs = view_tabs
        self._zip_tabs = zip_tabs

    @property
    def approve_tabs(self):
        """
        Gets the approve_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to approve documents in an envelope without placing a signature or initials on the document. If the recipient clicks the Approve tag during the signing process, the recipient is considered to have signed the document. No information is shown on the document for the approval, but it is recorded as a signature in the envelope history.

        :return: The approve_tabs of this Tabs.
        :rtype: list[Approve]
        """
        return self._approve_tabs

    @approve_tabs.setter
    def approve_tabs(self, approve_tabs):
        """
        Sets the approve_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to approve documents in an envelope without placing a signature or initials on the document. If the recipient clicks the Approve tag during the signing process, the recipient is considered to have signed the document. No information is shown on the document for the approval, but it is recorded as a signature in the envelope history.

        :param approve_tabs: The approve_tabs of this Tabs.
        :type: list[Approve]
        """

        self._approve_tabs = approve_tabs

    @property
    def checkbox_tabs(self):
        """
        Gets the checkbox_tabs of this Tabs.
        Specifies a tag on the document in a location where the recipient can select an option.

        :return: The checkbox_tabs of this Tabs.
        :rtype: list[Checkbox]
        """
        return self._checkbox_tabs

    @checkbox_tabs.setter
    def checkbox_tabs(self, checkbox_tabs):
        """
        Sets the checkbox_tabs of this Tabs.
        Specifies a tag on the document in a location where the recipient can select an option.

        :param checkbox_tabs: The checkbox_tabs of this Tabs.
        :type: list[Checkbox]
        """

        self._checkbox_tabs = checkbox_tabs

    @property
    def comment_thread_tabs(self):
        """
        Gets the comment_thread_tabs of this Tabs.
        

        :return: The comment_thread_tabs of this Tabs.
        :rtype: list[CommentThread]
        """
        return self._comment_thread_tabs

    @comment_thread_tabs.setter
    def comment_thread_tabs(self, comment_thread_tabs):
        """
        Sets the comment_thread_tabs of this Tabs.
        

        :param comment_thread_tabs: The comment_thread_tabs of this Tabs.
        :type: list[CommentThread]
        """

        self._comment_thread_tabs = comment_thread_tabs

    @property
    def company_tabs(self):
        """
        Gets the company_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient's company name to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :return: The company_tabs of this Tabs.
        :rtype: list[Company]
        """
        return self._company_tabs

    @company_tabs.setter
    def company_tabs(self, company_tabs):
        """
        Sets the company_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient's company name to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :param company_tabs: The company_tabs of this Tabs.
        :type: list[Company]
        """

        self._company_tabs = company_tabs

    @property
    def date_signed_tabs(self):
        """
        Gets the date_signed_tabs of this Tabs.
        Specifies a tab on the document where the date the document was signed will automatically appear.

        :return: The date_signed_tabs of this Tabs.
        :rtype: list[DateSigned]
        """
        return self._date_signed_tabs

    @date_signed_tabs.setter
    def date_signed_tabs(self, date_signed_tabs):
        """
        Sets the date_signed_tabs of this Tabs.
        Specifies a tab on the document where the date the document was signed will automatically appear.

        :param date_signed_tabs: The date_signed_tabs of this Tabs.
        :type: list[DateSigned]
        """

        self._date_signed_tabs = date_signed_tabs

    @property
    def date_tabs(self):
        """
        Gets the date_tabs of this Tabs.
        Specifies a tab on the document where you want the recipient to enter a date. Date tabs are single-line fields that allow date information to be entered in any format. The tooltip for this tab recommends entering the date as MM/DD/YYYY, but this is not enforced. The format entered by the signer is retained.   If you need a particular date format enforced, DocuSign recommends using a Text tab with a Validation Pattern and Validation Message to enforce the format.

        :return: The date_tabs of this Tabs.
        :rtype: list[Date]
        """
        return self._date_tabs

    @date_tabs.setter
    def date_tabs(self, date_tabs):
        """
        Sets the date_tabs of this Tabs.
        Specifies a tab on the document where you want the recipient to enter a date. Date tabs are single-line fields that allow date information to be entered in any format. The tooltip for this tab recommends entering the date as MM/DD/YYYY, but this is not enforced. The format entered by the signer is retained.   If you need a particular date format enforced, DocuSign recommends using a Text tab with a Validation Pattern and Validation Message to enforce the format.

        :param date_tabs: The date_tabs of this Tabs.
        :type: list[Date]
        """

        self._date_tabs = date_tabs

    @property
    def decline_tabs(self):
        """
        Gets the decline_tabs of this Tabs.
        Specifies a tag on the document where you want to give the recipient the option of declining an envelope. If the recipient clicks the Decline tag during the signing process, the envelope is voided.

        :return: The decline_tabs of this Tabs.
        :rtype: list[Decline]
        """
        return self._decline_tabs

    @decline_tabs.setter
    def decline_tabs(self, decline_tabs):
        """
        Sets the decline_tabs of this Tabs.
        Specifies a tag on the document where you want to give the recipient the option of declining an envelope. If the recipient clicks the Decline tag during the signing process, the envelope is voided.

        :param decline_tabs: The decline_tabs of this Tabs.
        :type: list[Decline]
        """

        self._decline_tabs = decline_tabs

    @property
    def draw_tabs(self):
        """
        Gets the draw_tabs of this Tabs.
        

        :return: The draw_tabs of this Tabs.
        :rtype: list[Draw]
        """
        return self._draw_tabs

    @draw_tabs.setter
    def draw_tabs(self, draw_tabs):
        """
        Sets the draw_tabs of this Tabs.
        

        :param draw_tabs: The draw_tabs of this Tabs.
        :type: list[Draw]
        """

        self._draw_tabs = draw_tabs

    @property
    def email_address_tabs(self):
        """
        Gets the email_address_tabs of this Tabs.
        Specifies a location on the document where you want where you want the recipient's email, as entered in the recipient information, to display.

        :return: The email_address_tabs of this Tabs.
        :rtype: list[EmailAddress]
        """
        return self._email_address_tabs

    @email_address_tabs.setter
    def email_address_tabs(self, email_address_tabs):
        """
        Sets the email_address_tabs of this Tabs.
        Specifies a location on the document where you want where you want the recipient's email, as entered in the recipient information, to display.

        :param email_address_tabs: The email_address_tabs of this Tabs.
        :type: list[EmailAddress]
        """

        self._email_address_tabs = email_address_tabs

    @property
    def email_tabs(self):
        """
        Gets the email_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter an email. Email tags are single-line fields that accept any characters. The system checks that a valid email format (i.e. xxx@yyy.zzz) is entered in the tag. It uses the same parameters as a Text tab, with the validation message and pattern set for email information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :return: The email_tabs of this Tabs.
        :rtype: list[Email]
        """
        return self._email_tabs

    @email_tabs.setter
    def email_tabs(self, email_tabs):
        """
        Sets the email_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter an email. Email tags are single-line fields that accept any characters. The system checks that a valid email format (i.e. xxx@yyy.zzz) is entered in the tag. It uses the same parameters as a Text tab, with the validation message and pattern set for email information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :param email_tabs: The email_tabs of this Tabs.
        :type: list[Email]
        """

        self._email_tabs = email_tabs

    @property
    def envelope_id_tabs(self):
        """
        Gets the envelope_id_tabs of this Tabs.
        Specifies a tag on the document where you want the envelope ID for to appear. Recipients cannot enter or change the information in this tab, it is for informational purposes only.

        :return: The envelope_id_tabs of this Tabs.
        :rtype: list[EnvelopeId]
        """
        return self._envelope_id_tabs

    @envelope_id_tabs.setter
    def envelope_id_tabs(self, envelope_id_tabs):
        """
        Sets the envelope_id_tabs of this Tabs.
        Specifies a tag on the document where you want the envelope ID for to appear. Recipients cannot enter or change the information in this tab, it is for informational purposes only.

        :param envelope_id_tabs: The envelope_id_tabs of this Tabs.
        :type: list[EnvelopeId]
        """

        self._envelope_id_tabs = envelope_id_tabs

    @property
    def first_name_tabs(self):
        """
        Gets the first_name_tabs of this Tabs.
        Specifies tag on a document where you want the recipient's first name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the first section as the first name.

        :return: The first_name_tabs of this Tabs.
        :rtype: list[FirstName]
        """
        return self._first_name_tabs

    @first_name_tabs.setter
    def first_name_tabs(self, first_name_tabs):
        """
        Sets the first_name_tabs of this Tabs.
        Specifies tag on a document where you want the recipient's first name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the first section as the first name.

        :param first_name_tabs: The first_name_tabs of this Tabs.
        :type: list[FirstName]
        """

        self._first_name_tabs = first_name_tabs

    @property
    def formula_tabs(self):
        """
        Gets the formula_tabs of this Tabs.
        Specifies a tag that is used to add a calculated field to a document. Envelope recipients cannot directly enter information into the tag; the formula tab calculates and displays a new value when changes are made to the reference tag values. The reference tag information and calculation operations are entered in the \"formula\" element. See the [ML:Using the Calculated Fields Feature] quick start guide or [ML:DocuSign Service User Guide] for more information about formulas.

        :return: The formula_tabs of this Tabs.
        :rtype: list[FormulaTab]
        """
        return self._formula_tabs

    @formula_tabs.setter
    def formula_tabs(self, formula_tabs):
        """
        Sets the formula_tabs of this Tabs.
        Specifies a tag that is used to add a calculated field to a document. Envelope recipients cannot directly enter information into the tag; the formula tab calculates and displays a new value when changes are made to the reference tag values. The reference tag information and calculation operations are entered in the \"formula\" element. See the [ML:Using the Calculated Fields Feature] quick start guide or [ML:DocuSign Service User Guide] for more information about formulas.

        :param formula_tabs: The formula_tabs of this Tabs.
        :type: list[FormulaTab]
        """

        self._formula_tabs = formula_tabs

    @property
    def full_name_tabs(self):
        """
        Gets the full_name_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient's name to appear.

        :return: The full_name_tabs of this Tabs.
        :rtype: list[FullName]
        """
        return self._full_name_tabs

    @full_name_tabs.setter
    def full_name_tabs(self, full_name_tabs):
        """
        Sets the full_name_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient's name to appear.

        :param full_name_tabs: The full_name_tabs of this Tabs.
        :type: list[FullName]
        """

        self._full_name_tabs = full_name_tabs

    @property
    def initial_here_tabs(self):
        """
        Gets the initial_here_tabs of this Tabs.
        Specifies a tag location in the document at which a recipient will place their initials. The `optional` parameter specifies whether the initials are required or optional.

        :return: The initial_here_tabs of this Tabs.
        :rtype: list[InitialHere]
        """
        return self._initial_here_tabs

    @initial_here_tabs.setter
    def initial_here_tabs(self, initial_here_tabs):
        """
        Sets the initial_here_tabs of this Tabs.
        Specifies a tag location in the document at which a recipient will place their initials. The `optional` parameter specifies whether the initials are required or optional.

        :param initial_here_tabs: The initial_here_tabs of this Tabs.
        :type: list[InitialHere]
        """

        self._initial_here_tabs = initial_here_tabs

    @property
    def last_name_tabs(self):
        """
        Gets the last_name_tabs of this Tabs.
        Specifies a tag on a document where you want the recipient's last name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the last section as the last name.

        :return: The last_name_tabs of this Tabs.
        :rtype: list[LastName]
        """
        return self._last_name_tabs

    @last_name_tabs.setter
    def last_name_tabs(self, last_name_tabs):
        """
        Sets the last_name_tabs of this Tabs.
        Specifies a tag on a document where you want the recipient's last name to appear. This tag takes the recipient's name, as entered in the recipient information, splits it into sections based on spaces and uses the last section as the last name.

        :param last_name_tabs: The last_name_tabs of this Tabs.
        :type: list[LastName]
        """

        self._last_name_tabs = last_name_tabs

    @property
    def list_tabs(self):
        """
        Gets the list_tabs of this Tabs.
        Specify this tag to give your recipient a list of options, presented as a drop-down list, from which they can select.

        :return: The list_tabs of this Tabs.
        :rtype: list[List]
        """
        return self._list_tabs

    @list_tabs.setter
    def list_tabs(self, list_tabs):
        """
        Sets the list_tabs of this Tabs.
        Specify this tag to give your recipient a list of options, presented as a drop-down list, from which they can select.

        :param list_tabs: The list_tabs of this Tabs.
        :type: list[List]
        """

        self._list_tabs = list_tabs

    @property
    def notarize_tabs(self):
        """
        Gets the notarize_tabs of this Tabs.
        

        :return: The notarize_tabs of this Tabs.
        :rtype: list[Notarize]
        """
        return self._notarize_tabs

    @notarize_tabs.setter
    def notarize_tabs(self, notarize_tabs):
        """
        Sets the notarize_tabs of this Tabs.
        

        :param notarize_tabs: The notarize_tabs of this Tabs.
        :type: list[Notarize]
        """

        self._notarize_tabs = notarize_tabs

    @property
    def note_tabs(self):
        """
        Gets the note_tabs of this Tabs.
        Specifies a location on the document where you want to place additional information, in the form of a note, for a recipient.

        :return: The note_tabs of this Tabs.
        :rtype: list[Note]
        """
        return self._note_tabs

    @note_tabs.setter
    def note_tabs(self, note_tabs):
        """
        Sets the note_tabs of this Tabs.
        Specifies a location on the document where you want to place additional information, in the form of a note, for a recipient.

        :param note_tabs: The note_tabs of this Tabs.
        :type: list[Note]
        """

        self._note_tabs = note_tabs

    @property
    def number_tabs(self):
        """
        Gets the number_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter a number. It uses the same parameters as a Text tab, with the validation message and pattern set for number information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response. 

        :return: The number_tabs of this Tabs.
        :rtype: list[Number]
        """
        return self._number_tabs

    @number_tabs.setter
    def number_tabs(self, number_tabs):
        """
        Sets the number_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter a number. It uses the same parameters as a Text tab, with the validation message and pattern set for number information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response. 

        :param number_tabs: The number_tabs of this Tabs.
        :type: list[Number]
        """

        self._number_tabs = number_tabs

    @property
    def poly_line_overlay_tabs(self):
        """
        Gets the poly_line_overlay_tabs of this Tabs.
        

        :return: The poly_line_overlay_tabs of this Tabs.
        :rtype: list[PolyLineOverlay]
        """
        return self._poly_line_overlay_tabs

    @poly_line_overlay_tabs.setter
    def poly_line_overlay_tabs(self, poly_line_overlay_tabs):
        """
        Sets the poly_line_overlay_tabs of this Tabs.
        

        :param poly_line_overlay_tabs: The poly_line_overlay_tabs of this Tabs.
        :type: list[PolyLineOverlay]
        """

        self._poly_line_overlay_tabs = poly_line_overlay_tabs

    @property
    def radio_group_tabs(self):
        """
        Gets the radio_group_tabs of this Tabs.
        Specifies a tag on the document in a location where the recipient can select one option from a group of options using a radio button. The radio buttons do not have to be on the same page in a document.

        :return: The radio_group_tabs of this Tabs.
        :rtype: list[RadioGroup]
        """
        return self._radio_group_tabs

    @radio_group_tabs.setter
    def radio_group_tabs(self, radio_group_tabs):
        """
        Sets the radio_group_tabs of this Tabs.
        Specifies a tag on the document in a location where the recipient can select one option from a group of options using a radio button. The radio buttons do not have to be on the same page in a document.

        :param radio_group_tabs: The radio_group_tabs of this Tabs.
        :type: list[RadioGroup]
        """

        self._radio_group_tabs = radio_group_tabs

    @property
    def signer_attachment_tabs(self):
        """
        Gets the signer_attachment_tabs of this Tabs.
        Specifies a tag on the document when you want the recipient to add supporting documents to an envelope.

        :return: The signer_attachment_tabs of this Tabs.
        :rtype: list[SignerAttachment]
        """
        return self._signer_attachment_tabs

    @signer_attachment_tabs.setter
    def signer_attachment_tabs(self, signer_attachment_tabs):
        """
        Sets the signer_attachment_tabs of this Tabs.
        Specifies a tag on the document when you want the recipient to add supporting documents to an envelope.

        :param signer_attachment_tabs: The signer_attachment_tabs of this Tabs.
        :type: list[SignerAttachment]
        """

        self._signer_attachment_tabs = signer_attachment_tabs

    @property
    def sign_here_tabs(self):
        """
        Gets the sign_here_tabs of this Tabs.
        A complex type the contains information about the tag that specifies where the recipient places their signature in the document. The \"optional\" parameter sets if the signature is required or optional. 

        :return: The sign_here_tabs of this Tabs.
        :rtype: list[SignHere]
        """
        return self._sign_here_tabs

    @sign_here_tabs.setter
    def sign_here_tabs(self, sign_here_tabs):
        """
        Sets the sign_here_tabs of this Tabs.
        A complex type the contains information about the tag that specifies where the recipient places their signature in the document. The \"optional\" parameter sets if the signature is required or optional. 

        :param sign_here_tabs: The sign_here_tabs of this Tabs.
        :type: list[SignHere]
        """

        self._sign_here_tabs = sign_here_tabs

    @property
    def smart_section_tabs(self):
        """
        Gets the smart_section_tabs of this Tabs.
        

        :return: The smart_section_tabs of this Tabs.
        :rtype: list[SmartSection]
        """
        return self._smart_section_tabs

    @smart_section_tabs.setter
    def smart_section_tabs(self, smart_section_tabs):
        """
        Sets the smart_section_tabs of this Tabs.
        

        :param smart_section_tabs: The smart_section_tabs of this Tabs.
        :type: list[SmartSection]
        """

        self._smart_section_tabs = smart_section_tabs

    @property
    def ssn_tabs(self):
        """
        Gets the ssn_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter a Social Security Number (SSN). A SSN can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for SSN information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :return: The ssn_tabs of this Tabs.
        :rtype: list[Ssn]
        """
        return self._ssn_tabs

    @ssn_tabs.setter
    def ssn_tabs(self, ssn_tabs):
        """
        Sets the ssn_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter a Social Security Number (SSN). A SSN can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for SSN information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :param ssn_tabs: The ssn_tabs of this Tabs.
        :type: list[Ssn]
        """

        self._ssn_tabs = ssn_tabs

    @property
    def tab_groups(self):
        """
        Gets the tab_groups of this Tabs.
        

        :return: The tab_groups of this Tabs.
        :rtype: list[TabGroup]
        """
        return self._tab_groups

    @tab_groups.setter
    def tab_groups(self, tab_groups):
        """
        Sets the tab_groups of this Tabs.
        

        :param tab_groups: The tab_groups of this Tabs.
        :type: list[TabGroup]
        """

        self._tab_groups = tab_groups

    @property
    def text_tabs(self):
        """
        Gets the text_tabs of this Tabs.
        Specifies a that that is an adaptable field that allows the recipient to enter different text information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :return: The text_tabs of this Tabs.
        :rtype: list[Text]
        """
        return self._text_tabs

    @text_tabs.setter
    def text_tabs(self, text_tabs):
        """
        Sets the text_tabs of this Tabs.
        Specifies a that that is an adaptable field that allows the recipient to enter different text information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :param text_tabs: The text_tabs of this Tabs.
        :type: list[Text]
        """

        self._text_tabs = text_tabs

    @property
    def title_tabs(self):
        """
        Gets the title_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient's title to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :return: The title_tabs of this Tabs.
        :rtype: list[Title]
        """
        return self._title_tabs

    @title_tabs.setter
    def title_tabs(self, title_tabs):
        """
        Sets the title_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient's title to appear.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :param title_tabs: The title_tabs of this Tabs.
        :type: list[Title]
        """

        self._title_tabs = title_tabs

    @property
    def view_tabs(self):
        """
        Gets the view_tabs of this Tabs.
        

        :return: The view_tabs of this Tabs.
        :rtype: list[View]
        """
        return self._view_tabs

    @view_tabs.setter
    def view_tabs(self, view_tabs):
        """
        Sets the view_tabs of this Tabs.
        

        :param view_tabs: The view_tabs of this Tabs.
        :type: list[View]
        """

        self._view_tabs = view_tabs

    @property
    def zip_tabs(self):
        """
        Gets the zip_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter a ZIP code. The ZIP code can be a five numbers or the ZIP+4 format with nine numbers. The zip code can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for ZIP code information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :return: The zip_tabs of this Tabs.
        :rtype: list[Zip]
        """
        return self._zip_tabs

    @zip_tabs.setter
    def zip_tabs(self, zip_tabs):
        """
        Sets the zip_tabs of this Tabs.
        Specifies a tag on the document where you want the recipient to enter a ZIP code. The ZIP code can be a five numbers or the ZIP+4 format with nine numbers. The zip code can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for ZIP code information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.

        :param zip_tabs: The zip_tabs of this Tabs.
        :type: list[Zip]
        """

        self._zip_tabs = zip_tabs

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
