# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CancelOrder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency_pair': 'str',
        'id': 'str'
    }

    attribute_map = {
        'currency_pair': 'currency_pair',
        'id': 'id'
    }

    def __init__(self, currency_pair=None, id=None):  # noqa: E501
        """CancelOrder - a model defined in OpenAPI"""  # noqa: E501

        self._currency_pair = None
        self._id = None
        self.discriminator = None

        self.currency_pair = currency_pair
        self.id = id

    @property
    def currency_pair(self):
        """Gets the currency_pair of this CancelOrder.  # noqa: E501

        Order currency pair  # noqa: E501

        :return: The currency_pair of this CancelOrder.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this CancelOrder.

        Order currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this CancelOrder.  # noqa: E501
        :type: str
        """
        if currency_pair is None:
            raise ValueError("Invalid value for `currency_pair`, must not be `None`")  # noqa: E501

        self._currency_pair = currency_pair

    @property
    def id(self):
        """Gets the id of this CancelOrder.  # noqa: E501

        Order ID  # noqa: E501

        :return: The id of this CancelOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CancelOrder.

        Order ID  # noqa: E501

        :param id: The id of this CancelOrder.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CancelOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other