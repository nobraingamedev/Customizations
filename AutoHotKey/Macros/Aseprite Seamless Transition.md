### To create a Seamless Transition

- Just copy the code below into any `.ahk` file, and run it .
- Make the pattern in Aseprite.
- Double Click the `.ahk` file to open the GUI App.
- Enter the Parameters.
- Click on Submit.
- Click on Exit after the Job done to close the app.

```autohotkey
Gui, Font, s10, Bahnschrift ; Set a custom font size and type
Gui, Color, White       ; Set the background color of the GUI

; Adding a subtle border
Gui, +Border

; Adding colored text and controls
Gui, Add, Text, x10 y10 w200 cBlack, Enter size of canvas:
Gui, Add, Edit, x220 y10 w150 vSizeOfCanvas BackgroundGray, 32

Gui, Add, Text, x10 y40 w200 cBlack, Enter number of pixel shift:
Gui, Add, Edit, x220 y40 w150 vNumberOfPixelShift BackgroundGray, 2

Gui, Add, Text, x10 y70 w200 cBlack, Direction of pixel shift:

; Align radio buttons horizontally using the x and y position for control
Gui, Add, Radio, x220 y70 w80 vDirectionLeft gDirectionChanged, Left
Gui, Add, Radio, x310 y70 w80 vDirectionRight gDirectionChanged, Right
Gui, Add, Radio, x220 y90 w80 vDirectionUp gDirectionChanged, Up
Gui, Add, Radio, x310 y90 w80 vDirectionDown gDirectionChanged, Down

; Styled buttons with different background and text colors
Gui, Add, Button, x10 y130 w150 cWhite BackgroundBlue gSubmit, Submit
Gui, Add, Button, x220 y130 w150 cWhite BackgroundRed gExitApp, Exit

Gui, Show, w400 h180, Pixel Shift Animation Setup
return

DirectionChanged:
    ; This function is triggered when a direction is selected
    Gui, Submit, NoHide
    return

Submit:
    Gui, Submit, NoHide
    global sizeOfCanvas := SizeOfCanvas
    global numberOfPixelShift := NumberOfPixelShift
    global sleepTimer := 100 ; Default sleep timer value

    ; Map the user-friendly direction to internal values
    if (DirectionLeft)
        directionOfPixelShift := "l"
    else if (DirectionRight)
        directionOfPixelShift := "r"
    else if (DirectionUp)
        directionOfPixelShift := "u"
    else if (DirectionDown)
        directionOfPixelShift := "d"

    ; Combined message box with both instructions
    MsgBox, 4, Done!, Parameters set! Press OK to close this window, then switch to Aseprite and use the F10 hotkey to start the animation process.
    return

F10::
    numberOfLoop := (sizeOfCanvas / numberOfPixelShift) - 1
    Loop, %numberOfLoop%
    {
        Send, !n ; create new frame copy of current frame
        Send, ^a ; select all
        
        loop, %numberOfPixelShift%
        {
            Send, !e ; open edit panel
            Sleep, sleepTimer
            Send, s ; open shift option panel
            Send, %directionOfPixelShift%
        }
    }
    return

ExitApp:
GuiClose:
GuiEscape:
    ExitApp
```
