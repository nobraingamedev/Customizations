- Just create a `.ini` file anywhere 
- Copy and Paste the Code in the `.ini` file
- Locate it from the Rainmeter App from Windows System Tray
- And Load the File

## Battery Percentage

```ini
[Rainmeter]
Author=mailmerge (analities.com) edited by riliaf@seznam.cz
BackgroundMode=0
Update=2
AlwaysOnTop=1

[Metadata]
Name=BatteryCorner
Author=mailmerge (analities.com) edited by riliaf@seznam.cz
Information=Before edit: Shows battery level and percentage in one color. After edit: Provides multiple useful features to monitor status of your notebook battery and change its power plans which are color distinguished. Also its only south east corner available now.
License=
Version=V2.1

;====================================================================VARIABLES==

[Variables]
Low=0.2
AC=0
Text=0
Font=Times New Roman

;=====================================================================MEASURES==

[MeasureAC]
Measure=Plugin
Plugin=PowerPlugin
PowerState=ACLINE
Substitute="1":"~","0":" "

[MeasurePercent]
Measure=Plugin
Plugin=PowerPlugin
PowerState=PERCENT

;=======================================================================METERS==

[MeterPercent]
Meter=String
MeasureName=MeasurePercent
Text=%1%
AntiAlias=1
FontColor=178,244,251,255
;FontFace=namaku
StringStyle=bold
;StringAlign=CENTER
FontSize=20
X=160r
Y=0r
;W=50
H=30
SolidColor=0,0,0,150

;=======================================================================METERS==

```

## Clock

```ini
[Rainmeter]
Update=1000
BackgroundMode=0
AccurateText=1

[Variables]
Font=Times New Roman
Opacity=150
FontColor=255,255,0,255  ; Yellow color
BackgroundColor=0,0,0,150  ; 150 opacity black

[MeasureTime]
Measure=Time
Format=%d-%b ~ %H:%M:%S

;%d-%b-%y for date like 21-Sep-24
;%d-%m-%y for date like 21-10-24
;%I:%M:%S %p for 12 hour format
;%H:%M:%S for 24 hour format
;%p is for AM or PM

;================== Background Meter =====================
[MeterBackground]
Meter=Shape

;================== Time Display Meter =====================
[MeterTime]
Meter=String
MeasureName=MeasureTime
FontColor=255,255,0,255
;FontFace=Harlow Solid
FontSize=20
W=220
H=30
AntiAlias=1
SolidColor=0,0,0,150  ; 150 is opacity of black background
;255 is 100% opacity and 0 is 0% opacity

```