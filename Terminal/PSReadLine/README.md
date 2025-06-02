### Check if PSReadLine is installed or not

`Get-Module -ListAvailable PSReadLine`

### If not installed, run the command below and check again

`Install-Module -Name PSReadLine -Scope CurrentUser`

### In `notepad $PROFILE`, paste the three lines given below 

```pwsh
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows
```