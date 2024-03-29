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


class V1beta1FrontendRule(object):
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
        'auth': 'V1beta1AuthOption',
        'port': 'str',
        'rules': 'list[str]'
    }

    attribute_map = {
        'auth': 'auth',
        'port': 'port',
        'rules': 'rules'
    }

    def __init__(self, auth=None, port=None, rules=None):
        """
        V1beta1FrontendRule - a model defined in Swagger
        """

        self._auth = None
        self._port = None
        self._rules = None
        self.discriminator = None

        if auth is not None:
          self.auth = auth
        if port is not None:
          self.port = port
        if rules is not None:
          self.rules = rules

    @property
    def auth(self):
        """
        Gets the auth of this V1beta1FrontendRule.

        :return: The auth of this V1beta1FrontendRule.
        :rtype: V1beta1AuthOption
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """
        Sets the auth of this V1beta1FrontendRule.

        :param auth: The auth of this V1beta1FrontendRule.
        :type: V1beta1AuthOption
        """

        self._auth = auth

    @property
    def port(self):
        """
        Gets the port of this V1beta1FrontendRule.
        Port indicates the frontend port where HAProxy is listening for connection

        :return: The port of this V1beta1FrontendRule.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1beta1FrontendRule.
        Port indicates the frontend port where HAProxy is listening for connection

        :param port: The port of this V1beta1FrontendRule.
        :type: str
        """

        self._port = port

    @property
    def rules(self):
        """
        Gets the rules of this V1beta1FrontendRule.
        Serialized rules

        :return: The rules of this V1beta1FrontendRule.
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this V1beta1FrontendRule.
        Serialized rules

        :param rules: The rules of this V1beta1FrontendRule.
        :type: list[str]
        """

        self._rules = rules

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
        if not isinstance(other, V1beta1FrontendRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
