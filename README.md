# ansible-yaml-doc

Minimal Python script to convert an ansible role `defaults/main.yml` file
to a Markdown table content.

## How to use

Write Markdown code in yaml comment blocks (lines starting with `# `).
The script will parse each comment block preceding a default variable, and generates a description in .md content.
Variables that are grouped together without a white line will share the same description.

Any real yaml code is wrapped with ` ```yaml `
Raw links are formatted in .md links. (The line may only contain the http(s) link)


## Example:

This defaults/main.yml code

```
---
# Name and ID of the SQL Server instance
mssql_instance: MSSQLSERVER

# Hides logs of tasks that contain sensitive data
# !! Turning it off will display secrets in plain text
mssql_hide_log: true

# This parameter can only be used together with the module SqlServer v22.x (minimum v22.0.49-preview). The parameter will be ignored if an older major versions of the module SqlServer is used. Encryption is mandatory by default, which generates the following exception when the correct certificates are not present:
# A connection was successfully established with the server, but then
# an error occurred during the login process. (provider: SSL Provider,
# error: 0 - The certificate chain was issued by an authority that is
# not trusted.)
# Options: Mandatory, Optional, Strict
mssql_encrypt: Optional

# The only time that DTC needs to be used is when more than one physical computer is going to be involved in an explicit distributed transaction.
# If you are going from one instance to another on the same server DTC will not be needed.
# If you are going from one instance to another within a cluster you will want to have DTC available as you may have to go between nodes of the cluster as you have no guarantee that the instances will be on the same physical node.
mssql_enable_msdtc: true

# Required. This value sets the installation for a single instance or high available instance
# Values: `'single','ha'`
mssql_install_type: 'single'

```

will be converted to this .md code

```
| Options and defaults | Description 
| :-------- | :---- | 
|`mssql_instance: MSSQLSERVER`<br/>|<br/>Name and ID of the SQL Server instance|
|`mssql_hide_log: true`<br/>|<br/>Hides logs of tasks that contain sensitive data<br/>!! Turning it off will display secrets in plain text|
|`mssql_encrypt: Optional`<br/>|<br/>This parameter can only be used together with the module SqlServer v22.x (minimum v22.0.49-preview). The parameter will be ignored if an older major versions of the module SqlServer is used. Encryption is mandatory by default, which generates the following exception when the correct certificates are not present:<br/>A connection was successfully established with the server, but then<br/>an error occurred during the login process. (provider: SSL Provider,<br/>error: 0 - The certificate chain was issued by an authority that is<br/>not trusted.)<br/>Options: Mandatory, Optional, Strict|
|`mssql_enable_msdtc: true`<br/>|<br/>The only time that DTC needs to be used is when more than one physical computer is going to be involved in an explicit distributed transaction.<br/>If you are going from one instance to another on the same server DTC will not be needed.<br/>If you are going from one instance to another within a cluster you will want to have DTC available as you may have to go between nodes of the cluster as you have no guarantee that the instances will be on the same physical node.|
|`mssql_install_type: 'single'`<br/>|<br/>Required. This value sets the installation for a single instance or high available instance<br/>Values: `'single','ha'`|
```

which will render like this
----
| Options and defaults | Description 
| :-------- | :---- | 
|`mssql_instance: MSSQLSERVER`<br/>|<br/>Name and ID of the SQL Server instance|
|`mssql_hide_log: true`<br/>|<br/>Hides logs of tasks that contain sensitive data<br/>!! Turning it off will display secrets in plain text|
|`mssql_encrypt: Optional`<br/>|<br/>This parameter can only be used together with the module SqlServer v22.x (minimum v22.0.49-preview). The parameter will be ignored if an older major versions of the module SqlServer is used. Encryption is mandatory by default, which generates the following exception when the correct certificates are not present:<br/>A connection was successfully established with the server, but then<br/>an error occurred during the login process. (provider: SSL Provider,<br/>error: 0 - The certificate chain was issued by an authority that is<br/>not trusted.)<br/>Options: Mandatory, Optional, Strict|
|`mssql_enable_msdtc: true`<br/>|<br/>The only time that DTC needs to be used is when more than one physical computer is going to be involved in an explicit distributed transaction.<br/>If you are going from one instance to another on the same server DTC will not be needed.<br/>If you are going from one instance to another within a cluster you will want to have DTC available as you may have to go between nodes of the cluster as you have no guarantee that the instances will be on the same physical node.|
|`mssql_install_type: 'single'`<br/>|<br/>Required. This value sets the installation for a single instance or high available instance<br/>Values: `'single','ha'`|
----
