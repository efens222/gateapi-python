# gate-api
APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 4.18.1
- Package version: 4.18.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.gate.io/page/contacts](https://www.gate.io/page/contacts)

## Versioning

Trying our best to follow the [semantic versioning](https://semver.org/), while enjoying recent features
provided by programming language and libraries, from 4.15.2, one major versioning difference will be
introduced:

If extra code rewrite is required when you upgrade the SDK, such as:

- some outdated programming language version support is dropped
- API method signature has breaking changes.

**the MAJOR version will be incremented, but the MINOR and PATCH version are still following REST API's
instead of resetting to 0**, so that you can recognize it has some breaking changes, but still getting
the idea of from which REST API version the change is introduced.

For example, the previous REST API and SDK version are both 4.14.0. But if we decide to introduce
some breaking changes in SDK along with REST API 4.15.2 upgrade, then the version of next SDK release
will be 5.15.2(the MAJOR version is incremented to denote breaking changes, but the MINOR and PATCH
version are identical to REST API's instead of resetting them to 0)

If MAJOR version is incremented, make sure you read the release note on
[Releases](https://github.com/gateio/gateapi-python/releases)
page

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/gateio/gateapi-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/gateio/gateapi-python.git`)

Then import the package:
```python
import gate_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gate_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import gate_api
from gate_api.exceptions import ApiException, GateApiException

# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)


api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency

try:
    # List all futures contracts
    api_response = api_instance.list_delivery_contracts(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_contracts: %s\n" % e)

```

For a more complete API usage example, refer to the demo application in [example](example) directory

## Documentation for API Endpoints

All URIs are relative to *https://api.gateio.ws/api/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeliveryApi* | [**list_delivery_contracts**](docs/DeliveryApi.md#list_delivery_contracts) | **GET** /delivery/{settle}/contracts | List all futures contracts
*DeliveryApi* | [**get_delivery_contract**](docs/DeliveryApi.md#get_delivery_contract) | **GET** /delivery/{settle}/contracts/{contract} | Get a single contract
*DeliveryApi* | [**list_delivery_order_book**](docs/DeliveryApi.md#list_delivery_order_book) | **GET** /delivery/{settle}/order_book | Futures order book
*DeliveryApi* | [**list_delivery_trades**](docs/DeliveryApi.md#list_delivery_trades) | **GET** /delivery/{settle}/trades | Futures trading history
*DeliveryApi* | [**list_delivery_candlesticks**](docs/DeliveryApi.md#list_delivery_candlesticks) | **GET** /delivery/{settle}/candlesticks | Get futures candlesticks
*DeliveryApi* | [**list_delivery_tickers**](docs/DeliveryApi.md#list_delivery_tickers) | **GET** /delivery/{settle}/tickers | List futures tickers
*DeliveryApi* | [**list_delivery_insurance_ledger**](docs/DeliveryApi.md#list_delivery_insurance_ledger) | **GET** /delivery/{settle}/insurance | Futures insurance balance history
*DeliveryApi* | [**list_delivery_accounts**](docs/DeliveryApi.md#list_delivery_accounts) | **GET** /delivery/{settle}/accounts | Query futures account
*DeliveryApi* | [**list_delivery_account_book**](docs/DeliveryApi.md#list_delivery_account_book) | **GET** /delivery/{settle}/account_book | Query account book
*DeliveryApi* | [**list_delivery_positions**](docs/DeliveryApi.md#list_delivery_positions) | **GET** /delivery/{settle}/positions | List all positions of a user
*DeliveryApi* | [**get_delivery_position**](docs/DeliveryApi.md#get_delivery_position) | **GET** /delivery/{settle}/positions/{contract} | Get single position
*DeliveryApi* | [**update_delivery_position_margin**](docs/DeliveryApi.md#update_delivery_position_margin) | **POST** /delivery/{settle}/positions/{contract}/margin | Update position margin
*DeliveryApi* | [**update_delivery_position_leverage**](docs/DeliveryApi.md#update_delivery_position_leverage) | **POST** /delivery/{settle}/positions/{contract}/leverage | Update position leverage
*DeliveryApi* | [**update_delivery_position_risk_limit**](docs/DeliveryApi.md#update_delivery_position_risk_limit) | **POST** /delivery/{settle}/positions/{contract}/risk_limit | Update position risk limit
*DeliveryApi* | [**list_delivery_orders**](docs/DeliveryApi.md#list_delivery_orders) | **GET** /delivery/{settle}/orders | List futures orders
*DeliveryApi* | [**create_delivery_order**](docs/DeliveryApi.md#create_delivery_order) | **POST** /delivery/{settle}/orders | Create a futures order
*DeliveryApi* | [**cancel_delivery_orders**](docs/DeliveryApi.md#cancel_delivery_orders) | **DELETE** /delivery/{settle}/orders | Cancel all &#x60;open&#x60; orders matched
*DeliveryApi* | [**get_delivery_order**](docs/DeliveryApi.md#get_delivery_order) | **GET** /delivery/{settle}/orders/{order_id} | Get a single order
*DeliveryApi* | [**cancel_delivery_order**](docs/DeliveryApi.md#cancel_delivery_order) | **DELETE** /delivery/{settle}/orders/{order_id} | Cancel a single order
*DeliveryApi* | [**get_my_delivery_trades**](docs/DeliveryApi.md#get_my_delivery_trades) | **GET** /delivery/{settle}/my_trades | List personal trading history
*DeliveryApi* | [**list_delivery_position_close**](docs/DeliveryApi.md#list_delivery_position_close) | **GET** /delivery/{settle}/position_close | List position close history
*DeliveryApi* | [**list_delivery_liquidates**](docs/DeliveryApi.md#list_delivery_liquidates) | **GET** /delivery/{settle}/liquidates | List liquidation history
*DeliveryApi* | [**list_delivery_settlements**](docs/DeliveryApi.md#list_delivery_settlements) | **GET** /delivery/{settle}/settlements | List settlement history
*DeliveryApi* | [**list_price_triggered_delivery_orders**](docs/DeliveryApi.md#list_price_triggered_delivery_orders) | **GET** /delivery/{settle}/price_orders | List all auto orders
*DeliveryApi* | [**create_price_triggered_delivery_order**](docs/DeliveryApi.md#create_price_triggered_delivery_order) | **POST** /delivery/{settle}/price_orders | Create a price-triggered order
*DeliveryApi* | [**cancel_price_triggered_delivery_order_list**](docs/DeliveryApi.md#cancel_price_triggered_delivery_order_list) | **DELETE** /delivery/{settle}/price_orders | Cancel all open orders
*DeliveryApi* | [**get_price_triggered_delivery_order**](docs/DeliveryApi.md#get_price_triggered_delivery_order) | **GET** /delivery/{settle}/price_orders/{order_id} | Get a single order
*DeliveryApi* | [**cancel_price_triggered_delivery_order**](docs/DeliveryApi.md#cancel_price_triggered_delivery_order) | **DELETE** /delivery/{settle}/price_orders/{order_id} | Cancel a single order
*FuturesApi* | [**list_futures_contracts**](docs/FuturesApi.md#list_futures_contracts) | **GET** /futures/{settle}/contracts | List all futures contracts
*FuturesApi* | [**get_futures_contract**](docs/FuturesApi.md#get_futures_contract) | **GET** /futures/{settle}/contracts/{contract} | Get a single contract
*FuturesApi* | [**list_futures_order_book**](docs/FuturesApi.md#list_futures_order_book) | **GET** /futures/{settle}/order_book | Futures order book
*FuturesApi* | [**list_futures_trades**](docs/FuturesApi.md#list_futures_trades) | **GET** /futures/{settle}/trades | Futures trading history
*FuturesApi* | [**list_futures_candlesticks**](docs/FuturesApi.md#list_futures_candlesticks) | **GET** /futures/{settle}/candlesticks | Get futures candlesticks
*FuturesApi* | [**list_futures_tickers**](docs/FuturesApi.md#list_futures_tickers) | **GET** /futures/{settle}/tickers | List futures tickers
*FuturesApi* | [**list_futures_funding_rate_history**](docs/FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/{settle}/funding_rate | Funding rate history
*FuturesApi* | [**list_futures_insurance_ledger**](docs/FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/{settle}/insurance | Futures insurance balance history
*FuturesApi* | [**list_contract_stats**](docs/FuturesApi.md#list_contract_stats) | **GET** /futures/{settle}/contract_stats | Futures stats
*FuturesApi* | [**list_liquidated_orders**](docs/FuturesApi.md#list_liquidated_orders) | **GET** /futures/{settle}/liq_orders | Retrieve liquidation history
*FuturesApi* | [**list_futures_accounts**](docs/FuturesApi.md#list_futures_accounts) | **GET** /futures/{settle}/accounts | Query futures account
*FuturesApi* | [**list_futures_account_book**](docs/FuturesApi.md#list_futures_account_book) | **GET** /futures/{settle}/account_book | Query account book
*FuturesApi* | [**list_positions**](docs/FuturesApi.md#list_positions) | **GET** /futures/{settle}/positions | List all positions of a user
*FuturesApi* | [**get_position**](docs/FuturesApi.md#get_position) | **GET** /futures/{settle}/positions/{contract} | Get single position
*FuturesApi* | [**update_position_margin**](docs/FuturesApi.md#update_position_margin) | **POST** /futures/{settle}/positions/{contract}/margin | Update position margin
*FuturesApi* | [**update_position_leverage**](docs/FuturesApi.md#update_position_leverage) | **POST** /futures/{settle}/positions/{contract}/leverage | Update position leverage
*FuturesApi* | [**update_position_risk_limit**](docs/FuturesApi.md#update_position_risk_limit) | **POST** /futures/{settle}/positions/{contract}/risk_limit | Update position risk limit
*FuturesApi* | [**set_dual_mode**](docs/FuturesApi.md#set_dual_mode) | **POST** /futures/{settle}/dual_mode | Enable or disable dual mode
*FuturesApi* | [**get_dual_mode_position**](docs/FuturesApi.md#get_dual_mode_position) | **GET** /futures/{settle}/dual_comp/positions/{contract} | Retrieve position detail in dual mode
*FuturesApi* | [**update_dual_mode_position_margin**](docs/FuturesApi.md#update_dual_mode_position_margin) | **POST** /futures/{settle}/dual_comp/positions/{contract}/margin | Update position margin in dual mode
*FuturesApi* | [**update_dual_mode_position_leverage**](docs/FuturesApi.md#update_dual_mode_position_leverage) | **POST** /futures/{settle}/dual_comp/positions/{contract}/leverage | Update position leverage in dual mode
*FuturesApi* | [**update_dual_mode_position_risk_limit**](docs/FuturesApi.md#update_dual_mode_position_risk_limit) | **POST** /futures/{settle}/dual_comp/positions/{contract}/risk_limit | Update position risk limit in dual mode
*FuturesApi* | [**list_futures_orders**](docs/FuturesApi.md#list_futures_orders) | **GET** /futures/{settle}/orders | List futures orders
*FuturesApi* | [**create_futures_order**](docs/FuturesApi.md#create_futures_order) | **POST** /futures/{settle}/orders | Create a futures order
*FuturesApi* | [**cancel_futures_orders**](docs/FuturesApi.md#cancel_futures_orders) | **DELETE** /futures/{settle}/orders | Cancel all &#x60;open&#x60; orders matched
*FuturesApi* | [**get_futures_order**](docs/FuturesApi.md#get_futures_order) | **GET** /futures/{settle}/orders/{order_id} | Get a single order
*FuturesApi* | [**cancel_futures_order**](docs/FuturesApi.md#cancel_futures_order) | **DELETE** /futures/{settle}/orders/{order_id} | Cancel a single order
*FuturesApi* | [**get_my_trades**](docs/FuturesApi.md#get_my_trades) | **GET** /futures/{settle}/my_trades | List personal trading history
*FuturesApi* | [**list_position_close**](docs/FuturesApi.md#list_position_close) | **GET** /futures/{settle}/position_close | List position close history
*FuturesApi* | [**list_liquidates**](docs/FuturesApi.md#list_liquidates) | **GET** /futures/{settle}/liquidates | List liquidation history
*FuturesApi* | [**list_price_triggered_orders**](docs/FuturesApi.md#list_price_triggered_orders) | **GET** /futures/{settle}/price_orders | List all auto orders
*FuturesApi* | [**create_price_triggered_order**](docs/FuturesApi.md#create_price_triggered_order) | **POST** /futures/{settle}/price_orders | Create a price-triggered order
*FuturesApi* | [**cancel_price_triggered_order_list**](docs/FuturesApi.md#cancel_price_triggered_order_list) | **DELETE** /futures/{settle}/price_orders | Cancel all open orders
*FuturesApi* | [**get_price_triggered_order**](docs/FuturesApi.md#get_price_triggered_order) | **GET** /futures/{settle}/price_orders/{order_id} | Get a single order
*FuturesApi* | [**cancel_price_triggered_order**](docs/FuturesApi.md#cancel_price_triggered_order) | **DELETE** /futures/{settle}/price_orders/{order_id} | Cancel a single order
*MarginApi* | [**list_margin_currency_pairs**](docs/MarginApi.md#list_margin_currency_pairs) | **GET** /margin/currency_pairs | List all supported currency pairs supported in margin trading
*MarginApi* | [**get_margin_currency_pair**](docs/MarginApi.md#get_margin_currency_pair) | **GET** /margin/currency_pairs/{currency_pair} | Query one single margin currency pair
*MarginApi* | [**list_funding_book**](docs/MarginApi.md#list_funding_book) | **GET** /margin/funding_book | Order book of lending loans
*MarginApi* | [**list_margin_accounts**](docs/MarginApi.md#list_margin_accounts) | **GET** /margin/accounts | Margin account list
*MarginApi* | [**list_margin_account_book**](docs/MarginApi.md#list_margin_account_book) | **GET** /margin/account_book | List margin account balance change history
*MarginApi* | [**list_funding_accounts**](docs/MarginApi.md#list_funding_accounts) | **GET** /margin/funding_accounts | Funding account list
*MarginApi* | [**list_loans**](docs/MarginApi.md#list_loans) | **GET** /margin/loans | List all loans
*MarginApi* | [**create_loan**](docs/MarginApi.md#create_loan) | **POST** /margin/loans | Lend or borrow
*MarginApi* | [**merge_loans**](docs/MarginApi.md#merge_loans) | **POST** /margin/merged_loans | Merge multiple lending loans
*MarginApi* | [**get_loan**](docs/MarginApi.md#get_loan) | **GET** /margin/loans/{loan_id} | Retrieve one single loan detail
*MarginApi* | [**cancel_loan**](docs/MarginApi.md#cancel_loan) | **DELETE** /margin/loans/{loan_id} | Cancel lending loan
*MarginApi* | [**update_loan**](docs/MarginApi.md#update_loan) | **PATCH** /margin/loans/{loan_id} | Modify a loan
*MarginApi* | [**list_loan_repayments**](docs/MarginApi.md#list_loan_repayments) | **GET** /margin/loans/{loan_id}/repayment | List loan repayment records
*MarginApi* | [**repay_loan**](docs/MarginApi.md#repay_loan) | **POST** /margin/loans/{loan_id}/repayment | Repay a loan
*MarginApi* | [**list_loan_records**](docs/MarginApi.md#list_loan_records) | **GET** /margin/loan_records | List repayment records of specified loan
*MarginApi* | [**get_loan_record**](docs/MarginApi.md#get_loan_record) | **GET** /margin/loan_records/{loan_record_id} | Get one single loan record
*MarginApi* | [**update_loan_record**](docs/MarginApi.md#update_loan_record) | **PATCH** /margin/loan_records/{loan_record_id} | Modify a loan record
*SpotApi* | [**list_currencies**](docs/SpotApi.md#list_currencies) | **GET** /spot/currencies | List all currencies&#39; detail
*SpotApi* | [**get_currency**](docs/SpotApi.md#get_currency) | **GET** /spot/currencies/{currency} | Get detail of one particular currency
*SpotApi* | [**list_currency_pairs**](docs/SpotApi.md#list_currency_pairs) | **GET** /spot/currency_pairs | List all currency pairs supported
*SpotApi* | [**get_currency_pair**](docs/SpotApi.md#get_currency_pair) | **GET** /spot/currency_pairs/{currency_pair} | Get detail of one single order
*SpotApi* | [**list_tickers**](docs/SpotApi.md#list_tickers) | **GET** /spot/tickers | Retrieve ticker information
*SpotApi* | [**list_order_book**](docs/SpotApi.md#list_order_book) | **GET** /spot/order_book | Retrieve order book
*SpotApi* | [**list_trades**](docs/SpotApi.md#list_trades) | **GET** /spot/trades | Retrieve market trades
*SpotApi* | [**list_candlesticks**](docs/SpotApi.md#list_candlesticks) | **GET** /spot/candlesticks | Market candlesticks
*SpotApi* | [**get_fee**](docs/SpotApi.md#get_fee) | **GET** /spot/fee | Query user trading fee rates
*SpotApi* | [**list_spot_accounts**](docs/SpotApi.md#list_spot_accounts) | **GET** /spot/accounts | List spot accounts
*SpotApi* | [**create_batch_orders**](docs/SpotApi.md#create_batch_orders) | **POST** /spot/batch_orders | Create a batch of orders
*SpotApi* | [**list_all_open_orders**](docs/SpotApi.md#list_all_open_orders) | **GET** /spot/open_orders | List all open orders
*SpotApi* | [**list_orders**](docs/SpotApi.md#list_orders) | **GET** /spot/orders | List orders
*SpotApi* | [**create_order**](docs/SpotApi.md#create_order) | **POST** /spot/orders | Create an order
*SpotApi* | [**cancel_orders**](docs/SpotApi.md#cancel_orders) | **DELETE** /spot/orders | Cancel all &#x60;open&#x60; orders in specified currency pair
*SpotApi* | [**cancel_batch_orders**](docs/SpotApi.md#cancel_batch_orders) | **POST** /spot/cancel_batch_orders | Cancel a batch of orders with an ID list
*SpotApi* | [**get_order**](docs/SpotApi.md#get_order) | **GET** /spot/orders/{order_id} | Get a single order
*SpotApi* | [**cancel_order**](docs/SpotApi.md#cancel_order) | **DELETE** /spot/orders/{order_id} | Cancel a single order
*SpotApi* | [**list_my_trades**](docs/SpotApi.md#list_my_trades) | **GET** /spot/my_trades | List personal trading history
*WalletApi* | [**get_deposit_address**](docs/WalletApi.md#get_deposit_address) | **GET** /wallet/deposit_address | Generate currency deposit address
*WalletApi* | [**list_withdrawals**](docs/WalletApi.md#list_withdrawals) | **GET** /wallet/withdrawals | Retrieve withdrawal records
*WalletApi* | [**list_deposits**](docs/WalletApi.md#list_deposits) | **GET** /wallet/deposits | Retrieve deposit records
*WalletApi* | [**transfer**](docs/WalletApi.md#transfer) | **POST** /wallet/transfers | Transfer between trading accounts
*WalletApi* | [**list_sub_account_transfers**](docs/WalletApi.md#list_sub_account_transfers) | **GET** /wallet/sub_account_transfers | Transfer records between main and sub accounts
*WalletApi* | [**transfer_with_sub_account**](docs/WalletApi.md#transfer_with_sub_account) | **POST** /wallet/sub_account_transfers | Transfer between main and sub accounts
*WalletApi* | [**list_withdraw_status**](docs/WalletApi.md#list_withdraw_status) | **GET** /wallet/withdraw_status | Retrieve withdrawal status
*WalletApi* | [**list_sub_account_balances**](docs/WalletApi.md#list_sub_account_balances) | **GET** /wallet/sub_account_balances | Retrieve sub account balances
*WithdrawalApi* | [**withdraw**](docs/WithdrawalApi.md#withdraw) | **POST** /withdrawals | Withdraw


## Documentation For Models

 - [BatchOrder](docs/BatchOrder.md)
 - [CancelOrder](docs/CancelOrder.md)
 - [CancelOrderResult](docs/CancelOrderResult.md)
 - [Contract](docs/Contract.md)
 - [ContractStat](docs/ContractStat.md)
 - [Currency](docs/Currency.md)
 - [CurrencyPair](docs/CurrencyPair.md)
 - [DeliveryContract](docs/DeliveryContract.md)
 - [DeliverySettlement](docs/DeliverySettlement.md)
 - [DepositAddress](docs/DepositAddress.md)
 - [FundingAccount](docs/FundingAccount.md)
 - [FundingBookItem](docs/FundingBookItem.md)
 - [FundingRateRecord](docs/FundingRateRecord.md)
 - [FuturesAccount](docs/FuturesAccount.md)
 - [FuturesAccountBook](docs/FuturesAccountBook.md)
 - [FuturesCandlestick](docs/FuturesCandlestick.md)
 - [FuturesInitialOrder](docs/FuturesInitialOrder.md)
 - [FuturesLiquidate](docs/FuturesLiquidate.md)
 - [FuturesOrder](docs/FuturesOrder.md)
 - [FuturesOrderBook](docs/FuturesOrderBook.md)
 - [FuturesOrderBookItem](docs/FuturesOrderBookItem.md)
 - [FuturesPriceTrigger](docs/FuturesPriceTrigger.md)
 - [FuturesPriceTriggeredOrder](docs/FuturesPriceTriggeredOrder.md)
 - [FuturesTicker](docs/FuturesTicker.md)
 - [FuturesTrade](docs/FuturesTrade.md)
 - [InsuranceRecord](docs/InsuranceRecord.md)
 - [LedgerRecord](docs/LedgerRecord.md)
 - [Loan](docs/Loan.md)
 - [LoanPatch](docs/LoanPatch.md)
 - [LoanRecord](docs/LoanRecord.md)
 - [MarginAccount](docs/MarginAccount.md)
 - [MarginAccountBook](docs/MarginAccountBook.md)
 - [MarginAccountCurrency](docs/MarginAccountCurrency.md)
 - [MarginCurrencyPair](docs/MarginCurrencyPair.md)
 - [MyFuturesTrade](docs/MyFuturesTrade.md)
 - [OpenOrders](docs/OpenOrders.md)
 - [Order](docs/Order.md)
 - [OrderBook](docs/OrderBook.md)
 - [Position](docs/Position.md)
 - [PositionClose](docs/PositionClose.md)
 - [PositionCloseOrder](docs/PositionCloseOrder.md)
 - [RepayRequest](docs/RepayRequest.md)
 - [Repayment](docs/Repayment.md)
 - [SpotAccount](docs/SpotAccount.md)
 - [SubAccountBalance](docs/SubAccountBalance.md)
 - [SubAccountTransfer](docs/SubAccountTransfer.md)
 - [Ticker](docs/Ticker.md)
 - [Trade](docs/Trade.md)
 - [TradeFee](docs/TradeFee.md)
 - [Transfer](docs/Transfer.md)
 - [TriggerOrderResponse](docs/TriggerOrderResponse.md)
 - [WithdrawStatus](docs/WithdrawStatus.md)


## Documentation For Authorization


## apiv4

Authentication with APIv4 key and secret

For details, refer to:
[APIv4 signed request requirements](https://www.gate.io/docs/apiv4/en/index.html#apiv4-signed-request-requirements)


## Author

support@mail.gate.io


