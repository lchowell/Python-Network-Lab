# Common Commands For PowerShell

## Getting Started with PowerShell
$PSVersionTable
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

## Setting the Execution Policy
Get-ExecutionPolicy
Get-ExecutionPolicy -List
Set-ExecutionPolicy -ExecutionPolicy AllSigned
Get-ExecutionPolicy -List
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Get-ExecutionPolicy -List
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Undefined

## Finding and Using Commands
Get-Service
Get-Service - (use tab autofill to find paraeter)
Get-Service -Name WinRM 
Get-Service -Name win*

Get-Service | Get-Member
Get-Service 
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-Service | Where-Object {$_.Status -eq "Running"} |Select-Object DisplayName, Status
Get-NetIPAddress | Where-Object {$_.AddressFamily -eq "ipv4"} | Select-Object InterfaceAlias, IPAddress

Get-Command -Name *time*
timedate.cpl
Get-Command -Noun *time*
