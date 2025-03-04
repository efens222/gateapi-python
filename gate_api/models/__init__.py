# coding: utf-8

# flake8: noqa
"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from gate_api.models.account_balance import AccountBalance
from gate_api.models.auto_repay_setting import AutoRepaySetting
from gate_api.models.batch_order import BatchOrder
from gate_api.models.cancel_order import CancelOrder
from gate_api.models.cancel_order_result import CancelOrderResult
from gate_api.models.contract import Contract
from gate_api.models.contract_stat import ContractStat
from gate_api.models.cross_margin_account import CrossMarginAccount
from gate_api.models.cross_margin_account_book import CrossMarginAccountBook
from gate_api.models.cross_margin_balance import CrossMarginBalance
from gate_api.models.cross_margin_borrowable import CrossMarginBorrowable
from gate_api.models.cross_margin_currency import CrossMarginCurrency
from gate_api.models.cross_margin_loan import CrossMarginLoan
from gate_api.models.cross_margin_repay_request import CrossMarginRepayRequest
from gate_api.models.cross_margin_repayment import CrossMarginRepayment
from gate_api.models.cross_margin_transferable import CrossMarginTransferable
from gate_api.models.currency import Currency
from gate_api.models.currency_chain import CurrencyChain
from gate_api.models.currency_pair import CurrencyPair
from gate_api.models.delivery_contract import DeliveryContract
from gate_api.models.delivery_settlement import DeliverySettlement
from gate_api.models.deposit_address import DepositAddress
from gate_api.models.flash_swap_currency import FlashSwapCurrency
from gate_api.models.flash_swap_order import FlashSwapOrder
from gate_api.models.flash_swap_order_preview import FlashSwapOrderPreview
from gate_api.models.flash_swap_order_request import FlashSwapOrderRequest
from gate_api.models.funding_account import FundingAccount
from gate_api.models.funding_book_item import FundingBookItem
from gate_api.models.funding_rate_record import FundingRateRecord
from gate_api.models.futures_account import FuturesAccount
from gate_api.models.futures_account_book import FuturesAccountBook
from gate_api.models.futures_account_history import FuturesAccountHistory
from gate_api.models.futures_candlestick import FuturesCandlestick
from gate_api.models.futures_index_constituents import FuturesIndexConstituents
from gate_api.models.futures_initial_order import FuturesInitialOrder
from gate_api.models.futures_liquidate import FuturesLiquidate
from gate_api.models.futures_order import FuturesOrder
from gate_api.models.futures_order_amendment import FuturesOrderAmendment
from gate_api.models.futures_order_book import FuturesOrderBook
from gate_api.models.futures_order_book_item import FuturesOrderBookItem
from gate_api.models.futures_price_trigger import FuturesPriceTrigger
from gate_api.models.futures_price_triggered_order import FuturesPriceTriggeredOrder
from gate_api.models.futures_ticker import FuturesTicker
from gate_api.models.futures_trade import FuturesTrade
from gate_api.models.index_constituent import IndexConstituent
from gate_api.models.insurance_record import InsuranceRecord
from gate_api.models.ledger_record import LedgerRecord
from gate_api.models.liquidate_order import LiquidateOrder
from gate_api.models.loan import Loan
from gate_api.models.loan_patch import LoanPatch
from gate_api.models.loan_record import LoanRecord
from gate_api.models.margin_account import MarginAccount
from gate_api.models.margin_account_book import MarginAccountBook
from gate_api.models.margin_account_currency import MarginAccountCurrency
from gate_api.models.margin_borrowable import MarginBorrowable
from gate_api.models.margin_currency_pair import MarginCurrencyPair
from gate_api.models.margin_transferable import MarginTransferable
from gate_api.models.multi_chain_address_item import MultiChainAddressItem
from gate_api.models.my_futures_trade import MyFuturesTrade
from gate_api.models.open_orders import OpenOrders
from gate_api.models.options_account import OptionsAccount
from gate_api.models.options_account_book import OptionsAccountBook
from gate_api.models.options_contract import OptionsContract
from gate_api.models.options_my_settlements import OptionsMySettlements
from gate_api.models.options_my_trade import OptionsMyTrade
from gate_api.models.options_order import OptionsOrder
from gate_api.models.options_position import OptionsPosition
from gate_api.models.options_position_close import OptionsPositionClose
from gate_api.models.options_settlement import OptionsSettlement
from gate_api.models.options_ticker import OptionsTicker
from gate_api.models.options_underlying import OptionsUnderlying
from gate_api.models.options_underlying_ticker import OptionsUnderlyingTicker
from gate_api.models.order import Order
from gate_api.models.order_book import OrderBook
from gate_api.models.position import Position
from gate_api.models.position_close import PositionClose
from gate_api.models.position_close_order import PositionCloseOrder
from gate_api.models.repay_request import RepayRequest
from gate_api.models.repayment import Repayment
from gate_api.models.saved_address import SavedAddress
from gate_api.models.spot_account import SpotAccount
from gate_api.models.spot_price_put_order import SpotPricePutOrder
from gate_api.models.spot_price_trigger import SpotPriceTrigger
from gate_api.models.spot_price_triggered_order import SpotPriceTriggeredOrder
from gate_api.models.sub_account_balance import SubAccountBalance
from gate_api.models.sub_account_cross_margin_balance import SubAccountCrossMarginBalance
from gate_api.models.sub_account_futures_balance import SubAccountFuturesBalance
from gate_api.models.sub_account_margin_balance import SubAccountMarginBalance
from gate_api.models.sub_account_transfer import SubAccountTransfer
from gate_api.models.sub_cross_margin_account import SubCrossMarginAccount
from gate_api.models.system_time import SystemTime
from gate_api.models.ticker import Ticker
from gate_api.models.total_balance import TotalBalance
from gate_api.models.trade import Trade
from gate_api.models.trade_fee import TradeFee
from gate_api.models.transaction_id import TransactionID
from gate_api.models.transfer import Transfer
from gate_api.models.trigger_order_response import TriggerOrderResponse
from gate_api.models.withdraw_status import WithdrawStatus
