
;TO CONTROL VOLUME WITH SCROLL WHEEL
;+WheelUp::Send {WheelLeft}
;+WheelDown::Send {WheelRight}
#WheelUp::Volume_Up
#WheelDown::Volume_Down
#Numpad5::Volume_Up
#Numpad2::Volume_Down

SetCapsLockState, AlwaysOff

CapsLock::
    Send, {Media_Play_Pause}
return


!i:: Run, wt.exe
return
;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

;WINDOW + SHIFT + y
#+y::
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Coding - Brave.lnk" "https://www.youtube.com/"
return

;WINDOW + CONTROL + y
#^y:: 
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Coding - Brave.lnk" --incognito https://www.youtube.com
return

;CONTROL + SHIFT + ALT + Y
^!+y::
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Kridachetra - Brave.lnk"
return    

;Shift + Alt + Ctrl + O
^+!o::
    Run,"C:\Program Files\Notepad++\notepad++.exe" "C:\Users\shiva\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Shortcuts.ahk"
return

;Window + E
#e::
    Run, "C:\Users\shiva\AppData\Local\Voidstar\FilePilot\FPilot.exe"

;Window + Alt + Ctrl + R
^+!r::
    Reload
return

#+s::Send {PrintScreen}	


#s:: Run, "C:\Program Files\Everything\Everything.exe"

; @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
;OPENING SOME WEBSITES in SOME profiles USING Shortcuts

^!g::
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Coding - Brave.lnk" "https://chatgpt.com/?temporary-chat=true"
return

^!p::
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Coding - Brave.lnk" "https://www.perplexity.ai/"
return 

^!o::
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Coding - Brave.lnk" "C:\Users\shiva\Desktop\Links.html"
return

^!m::
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Coding - Brave.lnk" "https://claude.ai/new"
return

^!b::
    Run, "C:\Users\shiva\OneDrive\Pictures\Apps\Brave Profiles\Coding - Brave.lnk" "https://gemini.google.com/u/0/app"
return

; @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

;SO THAT F1 and F2 DO NOT LOSE ITS OWN FUNCTIONALITY
F1::
    KeyWait, F1
    if (A_PriorKey = "F1") {
        Send {F1}
    }
    return
F2::
    KeyWait, F2
    if (A_PriorKey = "F2") {
        Send {F2}
    }
    return

F2 & Up:: ; F2 + Arrow Up
    Send, {WheelUp 1} ; Scrolls up
    return

; Scroll down using F2 + Arrow
F2 & Down:: ; F2 + Arrow Down
    Send, {WheelDown 1} ; Scrolls down
    return

F2 & Left:: ; F2 + Arrow Down
    Send, {WheelLeft 1} ; Scrolls down
    return

F2 & Right:: ; F2 + Arrow Down
    Send, {WheelRight 1} ; Scrolls down
    return

; @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

; Jump up 5 lines 
F1 & Up:: ; F1 + Arrow Up
    SendInput, {Up 5} ; Moves up 5 lines in one action
    return

; Jump down 5 lines 
F1 & Down:: ; F1 + Arrow Down
    SendInput, {Down 5} ; Moves down 5 lines in one action
    return

; @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

 RAlt & Numpad2::
  AdjustScreenBrightness(-5)
  Return
RAlt & Numpad5::
  AdjustScreenBrightness(5)
  Return
RAlt & WheelDown::
  AdjustScreenBrightness(-10)
  Return
RAlt & WheelUp::
  AdjustScreenBrightness(10)
  Return
AdjustScreenBrightness(step) {
    service := "winmgmts:{impersonationLevel=impersonate}!\\.\root\WMI"
    monitors := ComObjGet(service).ExecQuery("SELECT * FROM WmiMonitorBrightness WHERE Active=TRUE")
    monMethods := ComObjGet(service).ExecQuery("SELECT * FROM wmiMonitorBrightNessMethods WHERE Active=TRUE")
    minBrightness := 5  ; level below this is identical to this
    for i in monitors {
        curt := i.CurrentBrightness
        break
    }
    if (curt < minBrightness)  ; parenthesis is necessary here
        curt := minBrightness
    toSet := curt + step
    if (toSet > 100)
        return
    if (toSet < minBrightness)
        toSet := minBrightness
    for i in monMethods {
        i.WmiSetBrightness(1, toSet)
        break
    }
}
;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
