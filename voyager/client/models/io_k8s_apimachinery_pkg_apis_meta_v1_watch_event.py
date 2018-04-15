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


class IoK8sApimachineryPkgApisMetaV1WatchEvent(object):
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
        'object': 'IoK8sApimachineryPkgRuntimeRawExtension',
        'type': 'str'
    }

    attribute_map = {
        'object': 'object',
        'type': 'type'
    }

    def __init__(self, object=None, type=None):
        """
        IoK8sApimachineryPkgApisMetaV1WatchEvent - a model defined in Swagger
        """

        self._object = None
        self._type = None
        self.discriminator = None

        self.object = object
        self.type = type

    @property
    def object(self):
        """
        Gets the object of this IoK8sApimachineryPkgApisMetaV1WatchEvent.
        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context.

        :return: The object of this IoK8sApimachineryPkgApisMetaV1WatchEvent.
        :rtype: IoK8sApimachineryPkgRuntimeRawExtension
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this IoK8sApimachineryPkgApisMetaV1WatchEvent.
        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context.

        :param object: The object of this IoK8sApimachineryPkgApisMetaV1WatchEvent.
        :type: IoK8sApimachineryPkgRuntimeRawExtension
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")

        self._object = object

    @property
    def type(self):
        """
        Gets the type of this IoK8sApimachineryPkgApisMetaV1WatchEvent.

        :return: The type of this IoK8sApimachineryPkgApisMetaV1WatchEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IoK8sApimachineryPkgApisMetaV1WatchEvent.

        :param type: The type of this IoK8sApimachineryPkgApisMetaV1WatchEvent.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1WatchEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
