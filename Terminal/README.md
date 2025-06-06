### $PROFILE

```pwsh
Set-Alias npp "C:\Program Files\Notepad++\notepad++.exe"

# fzf window appearance change
$env:FZF_DEFAULT_OPTS = '--multi --height 60% --layout=reverse --border --color=fg:#d0d0d0,bg:#1e1e1e,hl:#ffa500,fg+:#ffffff,bg+:#44475a,hl+:#ffcc00,info:#8be9fd,prompt:#50fa7b,pointer:#ff5555,marker:#f1fa8c,spinner:#bd93f9,header:#6272a4'

# oh-my-posh default theme to lead
oh-my-posh init pwsh --config "C:\Users\shiva\AppData\Local\Programs\oh-my-posh\themes\gruvbox-edited.omp.json" | Invoke-Expression

# PSReadLine options
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows

# Take Me There
function tmt {
    $dir = fd --type d | fzf
    if ($dir) {
        Set-Location $dir
    }
}

# Open file in default Program
function of {
    $file = fd --type f | fzf
    if ($file) {
        Invoke-Item $file
    }
}

# Take Me To File's directory
function tmfd {
    $file = fd --type f | fzf
    if ($file) {
        Set-Location (Split-Path $file -Parent)
    }
}

# Open current working directory in filepilot 
function fp {
	param([string]$path = ".")

    & "C:\Users\shiva\AppData\Local\Voidstar\FilePilot\FPilot.exe" $path
}

# Open the chosen file in notepad++
function npf {
    $files = fd --type f | fzf --multi
    if ($files) {
        # $files can be multiple lines if --multi is used, so split by newline and open each
        $files -split "`n" | ForEach-Object { npp $_ }
    }
}

# Open the commands 
function hp {
	$line = "---------------------------------------------"
	Write-Host "tmt" -NoNewLine -ForegroundColor Cyan
	Write-Host " -> cd to chosen directory" -ForegroundColor Cyan
	Write-Host "tmfd" -NoNewLine -ForegroundColor Cyan
	Write-Host " -> Take me to chosen file's directory" -ForegroundColor Cyan
	Write-Host $line -ForegroundColor Cyan 
	Write-Host "of" -NoNewLine -ForegroundColor Cyan
	Write-Host 	" -> Open File in Default Program" -ForegroundColor Cyan
	Write-Host "npf" -NoNewLine -ForegroundColor Cyan
	Write-Host " -> Open the chosen file in Notepad++" -ForegroundColor Cyan
	Write-Host $line -ForegroundColor Cyan 
	Write-Host "fp" -NoNewLine -ForegroundColor Cyan
	Write-Host " -> Open FilePilot in current directory" -ForegroundColor Cyan
	Write-Host "npp" -NoNewLine -ForegroundColor Cyan
	Write-Host " -> Notepad++" -ForegroundColor Cyan
	Write-Host $line -ForegroundColor Cyan 
	Write-Host "hp" -NoNewLine -ForegroundColor Cyan
	Write-Host " -> HELP - Print all these commands" -ForegroundColor Cyan
}

# Printing the help commands at the start of terminal
hp

```	    	    
