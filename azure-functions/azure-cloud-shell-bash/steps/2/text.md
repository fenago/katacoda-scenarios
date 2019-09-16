Check that the environment drop-down from the left-hand side of shell window says Bash.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-cloud-shell-bash/steps/2/1.png)

#### Set your subscription

List subscriptions you have access to.
`az account list`{{copy}}

Set your preferred subscription:
`az account set --subscription 'my-subscription-name'`{{copy}}

**Tip:** Your subscription will be remembered for future sessions using `/home/<user>/.azure/azureProfile.json`.