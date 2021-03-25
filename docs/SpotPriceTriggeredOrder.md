# SpotPriceTriggeredOrder

Spot order detail
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | [**SpotPriceTrigger**](SpotPriceTrigger.md) |  | 
**put** | [**SpotPricePutOrder**](SpotPricePutOrder.md) |  | 
**id** | **int** | Auto order ID | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**market** | **str** | Currency pair | 
**ctime** | **float** | Creation time | [optional] [readonly] 
**ftime** | **float** | Finished time | [optional] [readonly] 
**fired_order_id** | **int** | ID of the newly created order on condition triggered | [optional] [readonly] 
**status** | **str** | Status  - open: open - cancelled: being manually cancelled - finish: successfully executed - failed: failed to execute - expired - expired  | [optional] [readonly] 
**reason** | **str** | Extra messages of how order is finished | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

