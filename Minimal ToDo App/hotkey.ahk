; Set the path to the Todo app - change only this line when needed
global todoAppPath := "C:\Users\shiva\Downloads\Minimal ToDo App\app.pyw"

; Manual hotkey: Alt+T to run the todo app
!t::RunTodoApp()

; Run the app when the script starts
RunTodoApp()

; Auto-run the todo app every 30 minutes
SetTimer(RunTodoApp, 1800000)

; Function to run the todo app
RunTodoApp() {
    global todoAppPath
    Run(todoAppPath)
}

; Show tray tip on script start
TrayTip("Todo Auto-Runner", "Script started - Todo app will auto-run every 30 minutes")
