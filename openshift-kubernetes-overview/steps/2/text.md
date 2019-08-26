Kubernetes key concepts
Like any complex system, a Kubernetes cluster can be viewed from multiple perspectives. From the infrastructure perspective, it comprises two sets of nodes; they can be bare-metal servers as well as VMs:

Masters:
This type of node is responsible for cluster management, network allocation, quota enforcement, synchronization, and communication. Master nodes act as the main point of contact for clients—be it actual people or some external system. In the simplest setup, there can be only one master, but highly available clusters require at least two to prevent common fail situations. The most important service that masters run is the API.

Nodes:
Nodes do the actual work of hosting Docker containers. More specifically, nodes provide a runtime environment for running pods, which are described later in this book. These servers run the kubelet service to manage pods:


 Kubernetes architecture

Logically, the Kubernetes API provides a number of resources that allow you to use various mechanisms provided by Kubernetes while abstracting some low-level implementation details. These resources can be defined in either YAML or JSON format. Here are some of them:

Namespaces: These resources serve the purpose of separating organizational units of users and their projects in a multitenant environment. Moreover, they are used for more fine-grained access control and quota enforcement. Almost all Kubernetes resources, except Volumes and Namespaces themselves, are namespaced, which means their names must be unique in any given namespace.
Pods: Pods represent a collection of containers and each pod serves as a basic management unit in Kubernetes. All containers in a pod share the same storage volumes and network.
Services: They represent an interface between clients and the actual application running in pods. A service is an IP:port pair which forwards traffic to backend pods in a round-robin fashion. Having a consistent address and port saves clients having to keep up with any transient changes in the cluster.
Replication Controllers (RC): In a nutshell, these resources define how many pods must be replicated. Their definitions include pod templates that describe pods to be launched, and one of the parameters each RC contains is the number of replicas to be maintained. If for some reason one or more of the pods go down, Kubernetes will launch new ones to satisfy this number.
Persistent Volumes (PV): These resources abstract actual physical storage systems, be it NFS, iSCSI, or something else. Typically, they are created by a cluster administrator and can be mounted inside a pod using the PVC binding mechanism, which is mentioned later.
Persistent Volume Claims (PVC): PVC represents a request for storage resources. Pod definitions don't use PVs directly; instead, they rely on binding PVs to PVCs, performed by Kubernetes.
Secrets: Used for passing sensitive data such as keys, tokens, and passwords inside pods.
Labels: Labels provide a mechanism for scoping a set of resources using selectors. For example, services use selectors to specify what pods to forward incoming traffic to. When new pods are started with the same label, they are dynamically associated with the service that has their label specified as a selector in its definition.
Here is a sample scenario with two teams residing in Denver and Phoenix, with separate namespaces. Selectors, labels, and a number of replicas are specified using the same notation as in actual YAML definitions of services, pods, and replication controllers, respectively:


Kubernetes resources

From a service point of view, Kubernetes can be represented as a set of interacting services:

These services typically run on masters:
etcd: This is a distributed key-value configuration store that holds all metadata and  cluster resources. Due to its quorum model, you are advised to run an uneven number of etcd nodes, starting from three in a highly available setup.
kube-apiserver: Service that exposes the Kubernetes API to clients. Its stateless nature enables it to be deployed in a highly available configuration by scaling horizontally.
kube-scheduler: Component that governs the placement of newly created pods on nodes. This procedure takes into account such factors as hardware/policy limitations, data locality, and affinity rules. It is worth noting that from the cluster point of view, masters are no different from any other node and thus can be eligible for running pods, although best practices suggest not putting additional strain on master nodes and dedicating them only to management functions.
kube-controller-manager: The component that runs various controllers—some of them are replication controllers that maintain the required number of running pods, node controllers for discovering nodes that went down, a volume controller for binding PVs to PVCs, and an endpoints controller that binds services and pods together.
cloud-controller-manager: Service that provides integration with underlying cloud providers, such as DigitalOcean and Oracle Cloud Infrastructure.
These services typically run on nodes:

kubelet: This service uses a pod specification to manage its pods and conduct periodic health checks.
kubeproxy: This component implements service abstraction by providing TCP and UDP forwarding capabilities across a set of backend pods.
Container runtime environment: This component is represented in Kubernetes by an underlying container technology. At the time of writing, Kubernetes supports docker and rkt as runtimes:

Kubernetes services

