By using the advanced option, you can associate existing resources. When selecting a Cloud Shell region you must select a backing storage account co-located in the same region. For example, if your assigned region is West US than you must associate a file share that resides within West US as well.

When the storage setup prompt appears, select Show advanced settings to view additional options. The populated storage options filter for locally redundant storage (LRS), geo-redundant storage (GRS), and zone-redundant storage (ZRS) accounts.

**Note:**
Using GRS or ZRS storage accounts are recommended for additional resiliency for your backing file share. Which type of redundancy depends on your goals and price preference. Learn more about replication options for Azure Storage accounts.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/persist-files-azure-shell/steps/3/1.png)
