# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.5.2
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CurrencyPair(object):
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
        'id': 'str',
        'base': 'str',
        'quote': 'str',
        'fee': 'str',
        'min_base_amount': 'str',
        'min_quote_amount': 'str',
        'precision': 'int'
    }

    attribute_map = {
        'id': 'id',
        'base': 'base',
        'quote': 'quote',
        'fee': 'fee',
        'min_base_amount': 'min_base_amount',
        'min_quote_amount': 'min_quote_amount',
        'precision': 'precision'
    }

    def __init__(self, id=None, base=None, quote=None, fee=None, min_base_amount=None, min_quote_amount=None, precision=None):  # noqa: E501
        """CurrencyPair - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._base = None
        self._quote = None
        self._fee = None
        self._min_base_amount = None
        self._min_quote_amount = None
        self._precision = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if base is not None:
            self.base = base
        if quote is not None:
            self.quote = quote
        if fee is not None:
            self.fee = fee
        if min_base_amount is not None:
            self.min_base_amount = min_base_amount
        if min_quote_amount is not None:
            self.min_quote_amount = min_quote_amount
        if precision is not None:
            self.precision = precision

    @property
    def id(self):
        """Gets the id of this CurrencyPair.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The id of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrencyPair.

        Currency pair  # noqa: E501

        :param id: The id of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def base(self):
        """Gets the base of this CurrencyPair.  # noqa: E501

        Base currency  # noqa: E501

        :return: The base of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this CurrencyPair.

        Base currency  # noqa: E501

        :param base: The base of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def quote(self):
        """Gets the quote of this CurrencyPair.  # noqa: E501

        Quote currency  # noqa: E501

        :return: The quote of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this CurrencyPair.

        Quote currency  # noqa: E501

        :param quote: The quote of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._quote = quote

    @property
    def fee(self):
        """Gets the fee of this CurrencyPair.  # noqa: E501

        Trading fee  # noqa: E501

        :return: The fee of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this CurrencyPair.

        Trading fee  # noqa: E501

        :param fee: The fee of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._fee = fee

    @property
    def min_base_amount(self):
        """Gets the min_base_amount of this CurrencyPair.  # noqa: E501

        Minimum amount of base currency to trade, `null` means no limit  # noqa: E501

        :return: The min_base_amount of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._min_base_amount

    @min_base_amount.setter
    def min_base_amount(self, min_base_amount):
        """Sets the min_base_amount of this CurrencyPair.

        Minimum amount of base currency to trade, `null` means no limit  # noqa: E501

        :param min_base_amount: The min_base_amount of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._min_base_amount = min_base_amount

    @property
    def min_quote_amount(self):
        """Gets the min_quote_amount of this CurrencyPair.  # noqa: E501

        Minimum amount of quote currency to trade, `null` means no limit  # noqa: E501

        :return: The min_quote_amount of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._min_quote_amount

    @min_quote_amount.setter
    def min_quote_amount(self, min_quote_amount):
        """Sets the min_quote_amount of this CurrencyPair.

        Minimum amount of quote currency to trade, `null` means no limit  # noqa: E501

        :param min_quote_amount: The min_quote_amount of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._min_quote_amount = min_quote_amount

    @property
    def precision(self):
        """Gets the precision of this CurrencyPair.  # noqa: E501

        Price scale  # noqa: E501

        :return: The precision of this CurrencyPair.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this CurrencyPair.

        Price scale  # noqa: E501

        :param precision: The precision of this CurrencyPair.  # noqa: E501
        :type: int
        """

        self._precision = precision

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
        if not isinstance(other, CurrencyPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other