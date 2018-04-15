# coding: utf-8

"""
    Voyager

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v6.0.0
    Contact: hello@appscode.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CertificateDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_ref': 'str',
        'cert_stable_url': 'str',
        'cert_url': 'str',
        'not_after': 'datetime',
        'not_before': 'datetime',
        'serial_number': 'str'
    }

    attribute_map = {
        'account_ref': 'accountRef',
        'cert_stable_url': 'certStableURL',
        'cert_url': 'certURL',
        'not_after': 'notAfter',
        'not_before': 'notBefore',
        'serial_number': 'serialNumber'
    }

    def __init__(self, account_ref=None, cert_stable_url=None, cert_url=None, not_after=None, not_before=None, serial_number=None):
        """
        V1beta1CertificateDetails - a model defined in Swagger
        """

        self._account_ref = None
        self._cert_stable_url = None
        self._cert_url = None
        self._not_after = None
        self._not_before = None
        self._serial_number = None
        self.discriminator = None

        if account_ref is not None:
          self.account_ref = account_ref
        self.cert_stable_url = cert_stable_url
        self.cert_url = cert_url
        if not_after is not None:
          self.not_after = not_after
        if not_before is not None:
          self.not_before = not_before
        if serial_number is not None:
          self.serial_number = serial_number

    @property
    def account_ref(self):
        """
        Gets the account_ref of this V1beta1CertificateDetails.

        :return: The account_ref of this V1beta1CertificateDetails.
        :rtype: str
        """
        return self._account_ref

    @account_ref.setter
    def account_ref(self, account_ref):
        """
        Sets the account_ref of this V1beta1CertificateDetails.

        :param account_ref: The account_ref of this V1beta1CertificateDetails.
        :type: str
        """

        self._account_ref = account_ref

    @property
    def cert_stable_url(self):
        """
        Gets the cert_stable_url of this V1beta1CertificateDetails.

        :return: The cert_stable_url of this V1beta1CertificateDetails.
        :rtype: str
        """
        return self._cert_stable_url

    @cert_stable_url.setter
    def cert_stable_url(self, cert_stable_url):
        """
        Sets the cert_stable_url of this V1beta1CertificateDetails.

        :param cert_stable_url: The cert_stable_url of this V1beta1CertificateDetails.
        :type: str
        """
        if cert_stable_url is None:
            raise ValueError("Invalid value for `cert_stable_url`, must not be `None`")

        self._cert_stable_url = cert_stable_url

    @property
    def cert_url(self):
        """
        Gets the cert_url of this V1beta1CertificateDetails.

        :return: The cert_url of this V1beta1CertificateDetails.
        :rtype: str
        """
        return self._cert_url

    @cert_url.setter
    def cert_url(self, cert_url):
        """
        Sets the cert_url of this V1beta1CertificateDetails.

        :param cert_url: The cert_url of this V1beta1CertificateDetails.
        :type: str
        """
        if cert_url is None:
            raise ValueError("Invalid value for `cert_url`, must not be `None`")

        self._cert_url = cert_url

    @property
    def not_after(self):
        """
        Gets the not_after of this V1beta1CertificateDetails.

        :return: The not_after of this V1beta1CertificateDetails.
        :rtype: datetime
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """
        Sets the not_after of this V1beta1CertificateDetails.

        :param not_after: The not_after of this V1beta1CertificateDetails.
        :type: datetime
        """

        self._not_after = not_after

    @property
    def not_before(self):
        """
        Gets the not_before of this V1beta1CertificateDetails.

        :return: The not_before of this V1beta1CertificateDetails.
        :rtype: datetime
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """
        Sets the not_before of this V1beta1CertificateDetails.

        :param not_before: The not_before of this V1beta1CertificateDetails.
        :type: datetime
        """

        self._not_before = not_before

    @property
    def serial_number(self):
        """
        Gets the serial_number of this V1beta1CertificateDetails.

        :return: The serial_number of this V1beta1CertificateDetails.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this V1beta1CertificateDetails.

        :param serial_number: The serial_number of this V1beta1CertificateDetails.
        :type: str
        """

        self._serial_number = serial_number

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
        if not isinstance(other, V1beta1CertificateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
