```autohotkey

; AHK Script: Hold D + move stylus (mouse) horizontally = scroll simulation with clean GUI
#Persistent
#InstallMouseHook
CoordMode, Mouse, Screen
SetTimer, CheckDandMove, 10

; === GUI Setup ===
Gui, +Border 
Gui, Font, s15, Bahnschrift  ; Clean modern font
Gui, Color, F0F0F0        ; White background

; GUI Elements
Gui, Add, Text, x20 y20 w360 h40 cBlack Center, Aseprite Brush Resize Tool is Running
Gui, Add, Button, x150 y80 w100 h40 cWhite BackgroundRed gCloseScript, Close

Gui, Show, w400 h150, Aseprite Helper Tool
return

CheckDandMove:
    ; If D is held down
    if GetKeyState("d", "P")
    {
        MouseGetPos, xNow, yNow

        if (!xPrev)
        {
            xPrev := xNow
            return
        }

        diff := xNow - xPrev

        ; Sensitivity threshold to avoid tiny jitters
        if (Abs(diff) > 15)
        {
            ; Scroll right = increase brush size
            ; Scroll left = decrease brush size
            if (diff > 0)
            {
                Send ^{WheelUp}
            }
            else
            {
                Send ^{WheelDown}
            }
            xPrev := xNow
        }
    }
    else
    {
        xPrev := ""
    }
return

CloseScript:
GuiClose:
ExitApp

```