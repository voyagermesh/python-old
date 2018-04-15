# V1beta1IngressSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**IoK8sApiCoreV1Affinity**](IoK8sApiCoreV1Affinity.md) | If specified, the pod&#39;s scheduling constraints | [optional] 
**backend** | [**V1beta1HTTPIngressBackend**](V1beta1HTTPIngressBackend.md) | A default backend capable of servicing requests that don&#39;t match any rule. At least one of &#39;backend&#39; or &#39;rules&#39; must be specified. This field is optional to allow the loadbalancer controller or defaulting logic to specify a global default. | [optional] 
**external_i_ps** | **list[str]** | externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system. | [optional] 
**frontend_rules** | [**list[V1beta1FrontendRule]**](V1beta1FrontendRule.md) | Frontend rules specifies a set of rules that should be applied in HAProxy frontend configuration. The set of keywords are from here https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4.1 Only frontend sections can be applied here. It is up to user to provide valid set of rules. This allows acls or other options in frontend sections in HAProxy config. Frontend rules will be mapped with Ingress Rules according to port. | [optional] 
**image_pull_secrets** | [**list[IoK8sApiCoreV1LocalObjectReference]**](IoK8sApiCoreV1LocalObjectReference.md) | ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod | [optional] 
**load_balancer_source_ranges** | **list[str]** | Optional: If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature. https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/ | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node&#39;s labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ | [optional] 
**resources** | [**IoK8sApiCoreV1ResourceRequirements**](IoK8sApiCoreV1ResourceRequirements.md) | Compute Resources required by the sidecar container. | [optional] 
**rules** | [**list[V1beta1IngressRule]**](V1beta1IngressRule.md) | A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend. | [optional] 
**scheduler_name** | **str** | If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler. | [optional] 
**tls** | [**list[V1beta1IngressTLS]**](V1beta1IngressTLS.md) | TLS is the TLS configuration. Currently the Ingress only supports a single TLS port, 443, and assumes TLS termination. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension. | [optional] 
**tolerations** | [**list[IoK8sApiCoreV1Toleration]**](IoK8sApiCoreV1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


