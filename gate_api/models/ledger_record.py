# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class LedgerRecord(object):
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
        'txid': 'str',
        'timestamp': 'str',
        'amount': 'str',
        'currency': 'str',
        'address': 'str',
        'memo': 'str',
        'status': 'str',
        'chain': 'str',
        'fee': 'str',
    }

    attribute_map = {
        'id': 'id',
        'txid': 'txid',
        'timestamp': 'timestamp',
        'amount': 'amount',
        'currency': 'currency',
        'address': 'address',
        'memo': 'memo',
        'status': 'status',
        'chain': 'chain',
        'fee': 'fee',
    }

    def __init__(
        self,
        id=None,
        txid=None,
        timestamp=None,
        amount=None,
        currency=None,
        address=None,
        memo=None,
        status=None,
        chain=None,
        fee=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, str, str, Configuration) -> None
        """LedgerRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._txid = None
        self._timestamp = None
        self._amount = None
        self._currency = None
        self._address = None
        self._memo = None
        self._status = None
        self._chain = None
        self._fee = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if txid is not None:
            self.txid = txid
        if timestamp is not None:
            self.timestamp = timestamp
        self.amount = amount
        self.currency = currency
        if address is not None:
            self.address = address
        if memo is not None:
            self.memo = memo
        if status is not None:
            self.status = status
        if chain is not None:
            self.chain = chain
        if fee is not None:
            self.fee = fee

    @property
    def id(self):
        """Gets the id of this LedgerRecord.  # noqa: E501

        Record ID  # noqa: E501

        :return: The id of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LedgerRecord.

        Record ID  # noqa: E501

        :param id: The id of this LedgerRecord.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def txid(self):
        """Gets the txid of this LedgerRecord.  # noqa: E501

        Hash record of the withdrawal  # noqa: E501

        :return: The txid of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this LedgerRecord.

        Hash record of the withdrawal  # noqa: E501

        :param txid: The txid of this LedgerRecord.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def timestamp(self):
        """Gets the timestamp of this LedgerRecord.  # noqa: E501

        Operation time  # noqa: E501

        :return: The timestamp of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this LedgerRecord.

        Operation time  # noqa: E501

        :param timestamp: The timestamp of this LedgerRecord.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def amount(self):
        """Gets the amount of this LedgerRecord.  # noqa: E501

        Currency amount  # noqa: E501

        :return: The amount of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LedgerRecord.

        Currency amount  # noqa: E501

        :param amount: The amount of this LedgerRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this LedgerRecord.  # noqa: E501

        Currency name  # noqa: E501

        :return: The currency of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this LedgerRecord.

        Currency name  # noqa: E501

        :param currency: The currency of this LedgerRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def address(self):
        """Gets the address of this LedgerRecord.  # noqa: E501

        Withdrawal address. Required for withdrawals  # noqa: E501

        :return: The address of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this LedgerRecord.

        Withdrawal address. Required for withdrawals  # noqa: E501

        :param address: The address of this LedgerRecord.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def memo(self):
        """Gets the memo of this LedgerRecord.  # noqa: E501

        Additional remarks with regards to the withdrawal  # noqa: E501

        :return: The memo of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this LedgerRecord.

        Additional remarks with regards to the withdrawal  # noqa: E501

        :param memo: The memo of this LedgerRecord.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def status(self):
        """Gets the status of this LedgerRecord.  # noqa: E501

        Record status.  - DONE: done - CANCEL: cancelled - REQUEST: requesting - MANUAL: pending manual approval - BCODE: GateCode operation - EXTPEND: pending confirm after sending - FAIL: pending confirm when fail - INVALID: invalid order - VERIFY: verifying - PROCES: processing - PEND: pending - DMOVE: required manual approval - SPLITPEND: the order is automatically split due to large amount  # noqa: E501

        :return: The status of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LedgerRecord.

        Record status.  - DONE: done - CANCEL: cancelled - REQUEST: requesting - MANUAL: pending manual approval - BCODE: GateCode operation - EXTPEND: pending confirm after sending - FAIL: pending confirm when fail - INVALID: invalid order - VERIFY: verifying - PROCES: processing - PEND: pending - DMOVE: required manual approval - SPLITPEND: the order is automatically split due to large amount  # noqa: E501

        :param status: The status of this LedgerRecord.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DONE",
            "CANCEL",
            "REQUEST",
            "MANUAL",
            "BCODE",
            "EXTPEND",
            "FAIL",
            "INVALID",
            "VERIFY",
            "PROCES",
            "PEND",
            "DMOVE",
            "SPLITPEND",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values)  # noqa: E501
            )

        self._status = status

    @property
    def chain(self):
        """Gets the chain of this LedgerRecord.  # noqa: E501

        Name of the chain used in withdrawals  # noqa: E501

        :return: The chain of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this LedgerRecord.

        Name of the chain used in withdrawals  # noqa: E501

        :param chain: The chain of this LedgerRecord.  # noqa: E501
        :type: str
        """

        self._chain = chain

    @property
    def fee(self):
        """Gets the fee of this LedgerRecord.  # noqa: E501

        Fee  # noqa: E501

        :return: The fee of this LedgerRecord.  # noqa: E501
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this LedgerRecord.

        Fee  # noqa: E501

        :param fee: The fee of this LedgerRecord.  # noqa: E501
        :type: str
        """

        self._fee = fee

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, LedgerRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LedgerRecord):
            return True

        return self.to_dict() != other.to_dict()
