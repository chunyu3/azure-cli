# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az storage|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az storage` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az storage table|Table|[commands](#CommandsInTable)|

## COMMANDS
### <a name="CommandsInTable">Commands in `az storage table` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az storage table delete](#TableDelete)|Delete|[Parameters](#ParametersTableDelete)|[Example](#ExamplesTableDelete)|


## COMMAND DETAILS

### group `az storage table`
#### <a name="TableDelete">Command `az storage table delete`</a>

##### <a name="ExamplesTableDelete">Example</a>
```
az storage table delete --account-name "sto328" --resource-group "res3376" --name "table6185"
```
##### <a name="ParametersTableDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group within the user's subscription. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.|account_name|accountName|
|**--table-name**|string|A table name must be unique within a storage account and must be between 3 and 63 characters.The name must comprise of only alphanumeric characters and it cannot begin with a numeric character.|table_name|tableName|
