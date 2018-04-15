# V1beta1HTTPIngressRuleValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The network address to listen HTTP(s) connections on. | [optional] 
**no_tls** | **bool** | Set noTLS &#x3D; true to force plain text. Else, auto detect like present | [optional] 
**node_port** | **str** | Specifies the node port of the referenced service. | [optional] 
**paths** | [**list[V1beta1HTTPIngressPath]**](V1beta1HTTPIngressPath.md) | A collection of paths that map requests to backends. | 
**port** | **str** | port to listen http(s) connections. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


