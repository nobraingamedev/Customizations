; Manual hotkey: Alt+T to run todo app
!t::Run "C:\Users\shiva\OneDrive\Desktop\Py Todo\todo_working.pyw"

;Run the app when the app is started 
RunTodoApp()

; Auto-run the todo app every 30 minutes
SetTimer(() => RunTodoApp(), 1800000)

; Function to run the todo app
RunTodoApp() {
    Run "C:\Users\shiva\OneDrive\Desktop\Py Todo\todo_working.pyw"
}

; Show tray tip on script start
TrayTip "Todo Auto-Runner", "Script started - Todo app will auto-run every 30 minutes"
