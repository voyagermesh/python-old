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


class V1beta1TLSAuth(object):
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
        'error_page': 'str',
        'headers': 'dict(str, str)',
        'secret_name': 'str',
        'verify_client': 'str'
    }

    attribute_map = {
        'error_page': 'errorPage',
        'headers': 'headers',
        'secret_name': 'secretName',
        'verify_client': 'verifyClient'
    }

    def __init__(self, error_page=None, headers=None, secret_name=None, verify_client=None):
        """
        V1beta1TLSAuth - a model defined in Swagger
        """

        self._error_page = None
        self._headers = None
        self._secret_name = None
        self._verify_client = None
        self.discriminator = None

        if error_page is not None:
          self.error_page = error_page
        if headers is not None:
          self.headers = headers
        if secret_name is not None:
          self.secret_name = secret_name
        if verify_client is not None:
          self.verify_client = verify_client

    @property
    def error_page(self):
        """
        Gets the error_page of this V1beta1TLSAuth.

        :return: The error_page of this V1beta1TLSAuth.
        :rtype: str
        """
        return self._error_page

    @error_page.setter
    def error_page(self, error_page):
        """
        Sets the error_page of this V1beta1TLSAuth.

        :param error_page: The error_page of this V1beta1TLSAuth.
        :type: str
        """

        self._error_page = error_page

    @property
    def headers(self):
        """
        Gets the headers of this V1beta1TLSAuth.

        :return: The headers of this V1beta1TLSAuth.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this V1beta1TLSAuth.

        :param headers: The headers of this V1beta1TLSAuth.
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def secret_name(self):
        """
        Gets the secret_name of this V1beta1TLSAuth.

        :return: The secret_name of this V1beta1TLSAuth.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """
        Sets the secret_name of this V1beta1TLSAuth.

        :param secret_name: The secret_name of this V1beta1TLSAuth.
        :type: str
        """

        self._secret_name = secret_name

    @property
    def verify_client(self):
        """
        Gets the verify_client of this V1beta1TLSAuth.

        :return: The verify_client of this V1beta1TLSAuth.
        :rtype: str
        """
        return self._verify_client

    @verify_client.setter
    def verify_client(self, verify_client):
        """
        Sets the verify_client of this V1beta1TLSAuth.

        :param verify_client: The verify_client of this V1beta1TLSAuth.
        :type: str
        """

        self._verify_client = verify_client

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
        if not isinstance(other, V1beta1TLSAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
