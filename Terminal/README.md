### $PROFILE

```pwsh
oh-my-posh init pwsh --config "C:\Users\shiva\AppData\Local\Programs\oh-my-posh\themes\gruvbox-edited.omp.json" | Invoke-Expression

Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows

# function to ease fzf use
function tmt {
	Set-Location (Get-ChildItem -Directory -Recurse | Select-Object -ExpandProperty FullName | fzf)
}
function ftf {
	Get-ChildItem -File -Recurse | Select-Object -ExpandProperty FullName | fzf
}

# function to open any directory in filepilot 
function filepilot { & "C:\Users\shiva\AppData\Local\Voidstar\FilePilot\FPilot.exe" $args }

```	    	    
