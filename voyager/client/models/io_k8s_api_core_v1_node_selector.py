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


class IoK8sApiCoreV1NodeSelector(object):
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
        'node_selector_terms': 'list[IoK8sApiCoreV1NodeSelectorTerm]'
    }

    attribute_map = {
        'node_selector_terms': 'nodeSelectorTerms'
    }

    def __init__(self, node_selector_terms=None):
        """
        IoK8sApiCoreV1NodeSelector - a model defined in Swagger
        """

        self._node_selector_terms = None
        self.discriminator = None

        self.node_selector_terms = node_selector_terms

    @property
    def node_selector_terms(self):
        """
        Gets the node_selector_terms of this IoK8sApiCoreV1NodeSelector.
        Required. A list of node selector terms. The terms are ORed.

        :return: The node_selector_terms of this IoK8sApiCoreV1NodeSelector.
        :rtype: list[IoK8sApiCoreV1NodeSelectorTerm]
        """
        return self._node_selector_terms

    @node_selector_terms.setter
    def node_selector_terms(self, node_selector_terms):
        """
        Sets the node_selector_terms of this IoK8sApiCoreV1NodeSelector.
        Required. A list of node selector terms. The terms are ORed.

        :param node_selector_terms: The node_selector_terms of this IoK8sApiCoreV1NodeSelector.
        :type: list[IoK8sApiCoreV1NodeSelectorTerm]
        """
        if node_selector_terms is None:
            raise ValueError("Invalid value for `node_selector_terms`, must not be `None`")

        self._node_selector_terms = node_selector_terms

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
        if not isinstance(other, IoK8sApiCoreV1NodeSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
