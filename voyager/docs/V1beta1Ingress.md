# V1beta1Ingress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) | Standard object&#39;s metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata | [optional] 
**spec** | [**V1beta1IngressSpec**](V1beta1IngressSpec.md) | Spec is the desired state of the Ingress. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#spec-and-status | [optional] 
**status** | [**V1beta1IngressStatus**](V1beta1IngressStatus.md) | Status is the current state of the Ingress. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#spec-and-status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


