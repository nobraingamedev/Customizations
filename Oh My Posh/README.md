### Download the Font from the [Link](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip) >>> Extract >>> Install All 

### Restart the Terminal >>> Settings >>> Defaults >>> Appearance >>> Change the Font Face to Fira Code

### Install `WinGet` from the Store and `winget install JanDeDobbeleer.OhMyPosh -s winget` to install Oh My Posh

### Run `oh-my-posh` to see whether it is installed properly or not.

### Open the Oh My Posh themes folder and create a new file called `gruvbox-edited.omp.json` 
Path to folder is `C:\Users\<username>\AppData\Local\Programs\oh-my-posh\themes\`

### Paste the below code in the file and save it.
<details>
<summary> Click to expand the code.</summary>
<pre><code>
{
  "$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
  "blocks": [
    {
      "alignment": "left",
      "segments": [
        {
          "background": "#3A3A3A",
          "foreground": "#ffffff",
          "style": "powerline",
          "template": "{{ if .WSL }}WSL at{{ end }} {{.Icon}} ",
          "type": "os"
        },
        {
          "background": "#458588",
          "foreground": "#ffffff",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "style": "full"
          },
          "style": "powerline",
          "template": " {{ .Path }} ",
          "type": "path"
        },
        {
          "background": "#98971A",
          "background_templates": [
            "{{ if or (.Working.Changed) (.Staging.Changed) }}#FF9248{{ end }}",
            "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#ff4500{{ end }}",
            "{{ if gt .Ahead 0 }}#B388FF{{ end }}",
            "{{ if gt .Behind 0 }}#B388FF{{ end }}"
          ],
          "foreground": "#ffffff",
          "leading_diamond": "\ue0b6",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "branch_template": "{{ trunc 25 .Branch }}",
            "fetch_stash_count": true,
            "fetch_status": true,
            "branch_icon": "\uE0A0 ",
            "branch_identical_icon": "\u25CF"
          },
          "style": "powerline",
          "template": " {{ .HEAD }}{{if .BranchStatus }} {{ .BranchStatus }}{{ end }}{{ if .Working.Changed }} \uf044 {{ .Working.String }}{{ end }}{{ if and (.Working.Changed) (.Staging.Changed) }} |{{ end }}{{ if .Staging.Changed }} \uf046 {{ .Staging.String }}{{ end }}{{ if gt .StashCount 0 }} \ueb4b {{ .StashCount }}{{ end }} ",
          "trailing_diamond": "\ue0b4",
          "type": "git"
        },
        {
          "background": "#8ED1F7",
          "foreground": "#111111",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "fetch_version": true
          },
          "style": "powerline",
          "template": " \ue626 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "type": "go"
        },
        {
          "background": "#4063D8",
          "foreground": "#111111",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "fetch_version": true
          },
          "style": "powerline",
          "template": " \ue624 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "type": "julia"
        },
        {
          "background": "#FFDE57",
          "foreground": "#111111",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "display_mode": "files",
            "fetch_virtual_env": false
          },
          "style": "powerline",
          "template": " \ue235 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "type": "python"
        },
        {
          "background": "#AE1401",
          "foreground": "#ffffff",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "display_mode": "files",
            "fetch_version": true
          },
          "style": "powerline",
          "template": " \ue791 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "type": "ruby"
        },
        {
          "background": "#FEAC19",
          "foreground": "#ffffff",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "display_mode": "files",
            "fetch_version": false
          },
          "style": "powerline",
          "template": " \uf0e7{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
          "type": "azfunc"
        },
        {
          "background_templates": [
            "{{if contains \"default\" .Profile}}#FFA400{{end}}",
            "{{if contains \"jan\" .Profile}}#f1184c{{end}}"
          ],
          "foreground": "#ffffff",
          "powerline_symbol": "\ue0b0",
          "properties": {
            "display_default": false
          },
          "style": "powerline",
          "template": " \ue7ad {{ .Profile }}{{ if .Region }}@{{ .Region }}{{ end }} ",
          "type": "aws"
        },
        {
          "background": "#ffff66",
          "foreground": "#111111",
          "powerline_symbol": "\ue0b0",
          "style": "powerline",
          "template": " \uf0ad ",
          "type": "root"
        }
      ],
      "type": "prompt"
    }
  ],
  "console_title_template": "{{ .Folder }}",
  "final_space": true,
  "version": 3
}
</code><pre>
</details>

### Run `notepad $PROFILE` 

### Paste the following command in the File and restart the terminal.
```pwsh
oh-my-posh init pwsh --config "C:\Users\shiva\AppData\Local\Programs\oh-my-posh\themes\gruvbox-edited.omp.json" | Invoke-Expression
```









