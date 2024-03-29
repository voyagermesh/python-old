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


class V1beta1HTTPIngressBackend(object):
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
        'backend_rules': 'list[str]',
        'header_rules': 'list[str]',
        'host_names': 'list[str]',
        'name': 'str',
        'rewrite_rules': 'list[str]',
        'service_name': 'str',
        'service_port': 'str'
    }

    attribute_map = {
        'backend_rules': 'backendRules',
        'header_rules': 'headerRules',
        'host_names': 'hostNames',
        'name': 'name',
        'rewrite_rules': 'rewriteRules',
        'service_name': 'serviceName',
        'service_port': 'servicePort'
    }

    def __init__(self, backend_rules=None, header_rules=None, host_names=None, name=None, rewrite_rules=None, service_name=None, service_port=None):
        """
        V1beta1HTTPIngressBackend - a model defined in Swagger
        """

        self._backend_rules = None
        self._header_rules = None
        self._host_names = None
        self._name = None
        self._rewrite_rules = None
        self._service_name = None
        self._service_port = None
        self.discriminator = None

        if backend_rules is not None:
          self.backend_rules = backend_rules
        if header_rules is not None:
          self.header_rules = header_rules
        if host_names is not None:
          self.host_names = host_names
        if name is not None:
          self.name = name
        if rewrite_rules is not None:
          self.rewrite_rules = rewrite_rules
        if service_name is not None:
          self.service_name = service_name
        if service_port is not None:
          self.service_port = service_port

    @property
    def backend_rules(self):
        """
        Gets the backend_rules of this V1beta1HTTPIngressBackend.
        Serialized HAProxy rules to apply on server backend including request, response or header rewrite. acls also can be used. https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#1

        :return: The backend_rules of this V1beta1HTTPIngressBackend.
        :rtype: list[str]
        """
        return self._backend_rules

    @backend_rules.setter
    def backend_rules(self, backend_rules):
        """
        Sets the backend_rules of this V1beta1HTTPIngressBackend.
        Serialized HAProxy rules to apply on server backend including request, response or header rewrite. acls also can be used. https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#1

        :param backend_rules: The backend_rules of this V1beta1HTTPIngressBackend.
        :type: list[str]
        """

        self._backend_rules = backend_rules

    @property
    def header_rules(self):
        """
        Gets the header_rules of this V1beta1HTTPIngressBackend.
        Header rules to modifies the header.  Deprecated: Use backendRule, will be removed.

        :return: The header_rules of this V1beta1HTTPIngressBackend.
        :rtype: list[str]
        """
        return self._header_rules

    @header_rules.setter
    def header_rules(self, header_rules):
        """
        Sets the header_rules of this V1beta1HTTPIngressBackend.
        Header rules to modifies the header.  Deprecated: Use backendRule, will be removed.

        :param header_rules: The header_rules of this V1beta1HTTPIngressBackend.
        :type: list[str]
        """

        self._header_rules = header_rules

    @property
    def host_names(self):
        """
        Gets the host_names of this V1beta1HTTPIngressBackend.
        Host names to forward traffic to. If empty traffic will be forwarded to all subsets instance. If set only matched hosts will get the traffic. This is an handy way to send traffic to Specific StatefulSet pod. IE. Setting [web-0] will send traffic to only web-0 host for this StatefulSet, https://kubernetes.io/docs/tasks/stateful-application/basic-stateful-set/#creating-a-statefulset

        :return: The host_names of this V1beta1HTTPIngressBackend.
        :rtype: list[str]
        """
        return self._host_names

    @host_names.setter
    def host_names(self, host_names):
        """
        Sets the host_names of this V1beta1HTTPIngressBackend.
        Host names to forward traffic to. If empty traffic will be forwarded to all subsets instance. If set only matched hosts will get the traffic. This is an handy way to send traffic to Specific StatefulSet pod. IE. Setting [web-0] will send traffic to only web-0 host for this StatefulSet, https://kubernetes.io/docs/tasks/stateful-application/basic-stateful-set/#creating-a-statefulset

        :param host_names: The host_names of this V1beta1HTTPIngressBackend.
        :type: list[str]
        """

        self._host_names = host_names

    @property
    def name(self):
        """
        Gets the name of this V1beta1HTTPIngressBackend.
        User can specify backend name for using it with custom acl Otherwise it will be generated

        :return: The name of this V1beta1HTTPIngressBackend.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1HTTPIngressBackend.
        User can specify backend name for using it with custom acl Otherwise it will be generated

        :param name: The name of this V1beta1HTTPIngressBackend.
        :type: str
        """

        self._name = name

    @property
    def rewrite_rules(self):
        """
        Gets the rewrite_rules of this V1beta1HTTPIngressBackend.
        Path rewrite rules with haproxy formatted regex.  Deprecated: Use backendRule, will be removed.

        :return: The rewrite_rules of this V1beta1HTTPIngressBackend.
        :rtype: list[str]
        """
        return self._rewrite_rules

    @rewrite_rules.setter
    def rewrite_rules(self, rewrite_rules):
        """
        Sets the rewrite_rules of this V1beta1HTTPIngressBackend.
        Path rewrite rules with haproxy formatted regex.  Deprecated: Use backendRule, will be removed.

        :param rewrite_rules: The rewrite_rules of this V1beta1HTTPIngressBackend.
        :type: list[str]
        """

        self._rewrite_rules = rewrite_rules

    @property
    def service_name(self):
        """
        Gets the service_name of this V1beta1HTTPIngressBackend.
        Specifies the name of the referenced service.

        :return: The service_name of this V1beta1HTTPIngressBackend.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this V1beta1HTTPIngressBackend.
        Specifies the name of the referenced service.

        :param service_name: The service_name of this V1beta1HTTPIngressBackend.
        :type: str
        """

        self._service_name = service_name

    @property
    def service_port(self):
        """
        Gets the service_port of this V1beta1HTTPIngressBackend.
        Specifies the port of the referenced service.

        :return: The service_port of this V1beta1HTTPIngressBackend.
        :rtype: str
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        """
        Sets the service_port of this V1beta1HTTPIngressBackend.
        Specifies the port of the referenced service.

        :param service_port: The service_port of this V1beta1HTTPIngressBackend.
        :type: str
        """

        self._service_port = service_port

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
        if not isinstance(other, V1beta1HTTPIngressBackend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
