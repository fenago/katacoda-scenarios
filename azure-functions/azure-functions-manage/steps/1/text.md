
In Azure Functions, a function app provides the execution context for your individual functions. Function app behaviors apply to all functions hosted by a given function app. All functions in a function app must be of the same language.

Individual functions in a function app are deployed together and are scaled together. All functions in the same function app share resources, per instance, as the function app scales.

Connection strings, environment variables, and other application settings are defined separately for each function app. Any data that must be shared between function apps should be stored externally in a persisted store.

This scenario describes how to configure and manage your function apps.

**Tip:** Many configuration options can also be managed by using the Azure CLI.