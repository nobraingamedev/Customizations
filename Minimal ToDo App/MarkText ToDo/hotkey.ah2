; Set paths to MarkText executable and Markdown file
global markTextAppPath := "C:\Users\shiva\AppData\Local\Programs\MarkText\MarkText.exe"
global markdownFilePath := "C:\Users\shiva\Downloads\Tasks-Todo\Tasks.md"

; Manual hotkey: Alt+T to toggle MarkText (open or minimize)
!t::ToggleMarkdownApp()

; Run the app when the script starts
RunMarkdownApp()

; Auto-run the markdown app every 15 minutes (900000 ms)
SetTimer(RunMarkdownApp, 900000)

; Function to toggle MarkText - open if not active, hide if active
ToggleMarkdownApp() {
    ; Check if MarkText window exists and is active
    if WinExist("ahk_exe MarkText.exe") {
        if WinActive("ahk_exe MarkText.exe") {
            ; If MarkText is the active window, hide it completely
            HideMarkTextWindow()
        } else {
            ; If MarkText exists but isn't active, bring it to front and restore visibility
            ShowMarkTextWindow()
            WinActivate("ahk_exe MarkText.exe")
        }
    } else {
        ; If MarkText doesn't exist, run it
        RunMarkdownApp()
    }
}

; Function to hide MarkText from taskbar and Alt+Tab
HideMarkTextWindow() {
    hwnd := WinExist("ahk_exe MarkText.exe")
    if (hwnd) {
        ; Hide from taskbar by removing WS_EX_APPWINDOW and adding WS_EX_TOOLWINDOW
        WinSetExStyle("+0x80 -0x40000", hwnd)  ; +WS_EX_TOOLWINDOW -WS_EX_APPWINDOW
        WinHide(hwnd)
    }
}

; Function to show MarkText in taskbar and Alt+Tab
ShowMarkTextWindow() {
    hwnd := WinExist("ahk_exe MarkText.exe")
    if (hwnd) {
        ; Show in taskbar by adding WS_EX_APPWINDOW and removing WS_EX_TOOLWINDOW
        WinSetExStyle("-0x80 +0x40000", hwnd)  ; -WS_EX_TOOLWINDOW +WS_EX_APPWINDOW
        WinShow(hwnd)
    }
}

; Function to run MarkText with the markdown file
RunMarkdownApp() {
    global markTextAppPath, markdownFilePath
    Run('"' markTextAppPath '" "' markdownFilePath '"')
}

; Show tray tip on script start
TrayTip("Todo Auto-Runner", "Tasks.md will open in MarkText every 15 minutes. Use Alt+T to toggle (hides from taskbar when minimized).")