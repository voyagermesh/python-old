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


class IoK8sApimachineryPkgApisMetaV1StatusCause(object):
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
        'field': 'str',
        'message': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'field': 'field',
        'message': 'message',
        'reason': 'reason'
    }

    def __init__(self, field=None, message=None, reason=None):
        """
        IoK8sApimachineryPkgApisMetaV1StatusCause - a model defined in Swagger
        """

        self._field = None
        self._message = None
        self._reason = None
        self.discriminator = None

        if field is not None:
          self.field = field
        if message is not None:
          self.message = message
        if reason is not None:
          self.reason = reason

    @property
    def field(self):
        """
        Gets the field of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.  Examples:   \"name\" - the field \"name\" on the current resource   \"items[0].name\" - the field \"name\" on the first array entry in \"items\"

        :return: The field of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.  Examples:   \"name\" - the field \"name\" on the current resource   \"items[0].name\" - the field \"name\" on the first array entry in \"items\"

        :param field: The field of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        :type: str
        """

        self._field = field

    @property
    def message(self):
        """
        Gets the message of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        A human-readable description of the cause of the error.  This field may be presented as-is to a reader.

        :return: The message of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        A human-readable description of the cause of the error.  This field may be presented as-is to a reader.

        :param message: The message of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        A machine-readable description of the cause of the error. If this value is empty there is no information available.

        :return: The reason of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        A machine-readable description of the cause of the error. If this value is empty there is no information available.

        :param reason: The reason of this IoK8sApimachineryPkgApisMetaV1StatusCause.
        :type: str
        """

        self._reason = reason

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
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1StatusCause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
