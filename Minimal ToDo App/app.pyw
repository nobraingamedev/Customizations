import tkinter as tk
from tkinter import ttk
import json
import os
from datetime import datetime

class OverlayTodoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.tasks = []
        self.tasks_file = "tasks.json"
        self.is_visible = True
        self.dragged_task = None
        self.drag_start_y = 0
        
        self.setup_window()
        self.create_widgets()
        self.load_tasks()
        self.bind_events()
        
    def setup_window(self):
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate 30% of screen size
        width = int(screen_width * 0.3)
        height = int(screen_height * 0.3)
        
        # Position in bottom-right corner
        x = screen_width - width - 20
        y = screen_height - height - 60  # 60px from bottom to account for taskbar
        
        # Configure window - with minimal title bar
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Minimal ToDo")  # Set window title
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.85)
        self.root.configure(bg='#2b2b2b')
        
        # Keep the title bar but make it minimal - remove overrideredirect
        # This will make it visible in Alt+Tab menu
        
    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Input box FIRST (at bottom)
        self.task_entry = tk.Entry(self.main_frame, 
                                  font=('Cascadia Mono', 12), 
                                  bg='#555555', fg='white',  # Lighter gray for visibility
                                  insertbackground='white',
                                  relief=tk.RAISED, bd=2,
                                  highlightthickness=2,
                                  highlightcolor='#777777',
                                  highlightbackground='#555555')
        self.task_entry.pack(side=tk.BOTTOM, fill=tk.X, pady=(5, 0), ipady=3)  # Reduced from 8 to 3
        
        # Tasks frame with scrollbar (fills remaining space)
        tasks_frame = tk.Frame(self.main_frame, bg='#2b2b2b')
        tasks_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # Create scrollable frame
        canvas = tk.Canvas(tasks_frame, bg='#2b2b2b', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tasks_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg='#2b2b2b')
        
        # Store scrollbar and canvas for dynamic show/hide
        self.canvas = canvas
        self.scrollbar = scrollbar
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.update_scrollbar()
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Initially pack only canvas (no scrollbar)
        canvas.pack(side="left", fill="both", expand=True)
        
        # Focus on the input box when app starts
        self.root.after(100, lambda: self.task_entry.focus_set())
        
    def bind_events(self):
        self.task_entry.bind('<Return>', self.add_task)
        self.task_entry.bind('<KP_Enter>', self.add_task)  # Also bind numpad Enter
        # Removed Ctrl+T hotkey as requested
        
        # Add Alt+T to close the app
        self.root.bind('<Alt-t>', lambda e: self.root.quit())
        self.root.bind('<Alt-T>', lambda e: self.root.quit())  # Handle both cases
        
        # Add Ctrl+Backspace for deleting whole words
        self.task_entry.bind('<Control-BackSpace>', self.delete_word_backward)
        self.task_entry.bind('<Control-Delete>', self.delete_word_forward)
        
        # Bind mouse wheel to ALL components for scrolling
        def _on_mousewheel(event):
            # Only scroll if there's content to scroll
            if self.scrollable_frame.winfo_reqheight() > self.canvas.winfo_height():
                self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # Bind mousewheel to root window so it works everywhere
        self.root.bind("<MouseWheel>", _on_mousewheel)
        
    def add_task(self, event=None):
        task_text = self.task_entry.get().strip()
        if not task_text:
            return
            
        task = {
            'id': len(self.tasks),
            'text': task_text,
            'completed': False,
            'created': datetime.now().isoformat()
        }
        
        self.tasks.append(task)
        self.task_entry.delete(0, tk.END)
        self.refresh_tasks()
        self.save_tasks()
        
        # Focus back to entry box for quick adding
        self.task_entry.focus_set()
        
    def create_task_widget(self, task):
        task_frame = tk.Frame(self.scrollable_frame, bg='#3a3a3a')
        task_frame.pack(fill=tk.X, pady=1, padx=1)
        
        # Complete button (small)
        complete_text = "✓" if not task['completed'] else "↶"
        complete_color = "#4CAF50" if not task['completed'] else "#FFC107"
        complete_hover_color = "#5CBF60" if not task['completed'] else "#FFD54F"  # Lighter versions
        
        btn_font_size = 6 if task['completed'] else 8
        btn_width = 2
        
        complete_btn = tk.Button(task_frame, text=complete_text,
                               command=lambda: self.toggle_complete(task['id']),
                               font=('Cascadia Mono', btn_font_size), 
                               bg=complete_color, fg='white',
                               relief=tk.FLAT, width=btn_width, height=1,
                               activebackground=complete_hover_color,
                               activeforeground='white')
        complete_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Add hover effects to complete button
        def on_complete_enter(event):
            complete_btn.configure(bg=complete_hover_color, cursor="hand2")
        def on_complete_leave(event):
            complete_btn.configure(bg=complete_color, cursor="")
        
        complete_btn.bind("<Enter>", on_complete_enter)
        complete_btn.bind("<Leave>", on_complete_leave)
        
        # Delete button (small)
        delete_btn = tk.Button(task_frame, text="✕",
                             command=lambda: self.delete_task(task['id']),
                             font=('Cascadia Mono', btn_font_size), 
                             bg='#f44336', fg='white',
                             relief=tk.FLAT, width=btn_width, height=1,
                             activebackground='#f66356',  # Lighter red
                             activeforeground='white')
        delete_btn.pack(side=tk.LEFT, padx=(0, 5), pady=2)
        
        # Add hover effects to delete button
        def on_delete_enter(event):
            delete_btn.configure(bg='#f66356', cursor="hand2")
        def on_delete_leave(event):
            delete_btn.configure(bg='#f44336', cursor="")
        
        delete_btn.bind("<Enter>", on_delete_enter)
        delete_btn.bind("<Leave>", on_delete_leave)
        
        # Drag handle (≡ symbol)
        drag_handle = tk.Label(task_frame, text="≡", 
                              font=('Cascadia Mono', 10), fg='#888888', bg='#3a3a3a',
                              cursor="hand2")
        drag_handle.pack(side=tk.LEFT, padx=(0, 5), pady=2)
        
        # Add hover effects to drag handle
        def on_drag_enter(event):
            drag_handle.configure(fg='#aaaaaa', bg='#454545')
        def on_drag_leave(event):
            drag_handle.configure(fg='#888888', bg='#3a3a3a')
        
        drag_handle.bind("<Enter>", on_drag_enter)
        drag_handle.bind("<Leave>", on_drag_leave)
        
        # Task text
        font_style = ('Cascadia Mono', 11, 'overstrike') if task['completed'] else ('Cascadia Mono', 13, 'normal')
        text_color = '#888888' if task['completed'] else '#ffffff'
        
        task_label = tk.Label(task_frame, text=task['text'], 
                             font=font_style, fg=text_color, bg='#3a3a3a', 
                             anchor='nw', justify='left', wraplength=320,  # Reduced from 360 to make room for drag handle
                             cursor="hand2")
        task_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=3)
        
        # Add subtle hover effect to task text area
        def on_task_enter(event):
            if not task['completed']:  # Only hover effect for active tasks
                task_label.configure(bg='#454545')
                task_frame.configure(bg='#454545')
        def on_task_leave(event):
            task_label.configure(bg='#3a3a3a')
            task_frame.configure(bg='#3a3a3a')
        
        task_label.bind("<Enter>", on_task_enter)
        task_label.bind("<Leave>", on_task_leave)
        task_frame.bind("<Enter>", on_task_enter)  # Also bind to frame for better coverage
        task_frame.bind("<Leave>", on_task_leave)
        
        # Store task reference in the frame for drag operations
        task_frame.task_id = task['id']
        
        # Enable mouse wheel scrolling on task elements
        def _on_mousewheel_task(event):
            if self.scrollable_frame.winfo_reqheight() > self.canvas.winfo_height():
                self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        task_frame.bind("<MouseWheel>", _on_mousewheel_task)
        task_label.bind("<MouseWheel>", _on_mousewheel_task)
        drag_handle.bind("<MouseWheel>", _on_mousewheel_task)
        
        # Double-click to edit task
        def start_edit(event):
            self.edit_task(task['id'], task_label, task_frame)
        
        task_label.bind("<Double-Button-1>", start_edit)
        
        # Drag and drop functionality for reordering
        def start_drag(event):
            self.dragged_task = task_frame
            self.drag_start_y = event.y_root
            task_frame.configure(bg='#4a4a4a')  # Visual feedback
            
        def on_drag(event):
            if self.dragged_task:
                # Calculate which task we're hovering over
                canvas_y = self.root.winfo_rooty() + self.canvas.winfo_y()
                relative_y = event.y_root - canvas_y
                
                # Find the task frame we're hovering over
                for child in self.scrollable_frame.winfo_children():
                    if child != self.dragged_task:
                        child_top = child.winfo_y()
                        child_bottom = child_top + child.winfo_height()
                        if child_top <= relative_y <= child_bottom:
                            # Insert before this child
                            self.reorder_task(self.dragged_task.task_id, child.task_id)
                            break
        
        def end_drag(event):
            if self.dragged_task:
                self.dragged_task.configure(bg='#3a3a3a')  # Reset visual feedback
                self.dragged_task = None
                
        # Bind drag events to drag handle
        drag_handle.bind("<Button-1>", start_drag)
        drag_handle.bind("<B1-Motion>", on_drag)
        drag_handle.bind("<ButtonRelease-1>", end_drag)
        
    def toggle_complete(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
        self.refresh_tasks()
        self.save_tasks()
        
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.refresh_tasks()
        self.save_tasks()
    
    def edit_task(self, task_id, task_label, task_frame):
        # Find the task
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if not task:
            return
            
        # Create entry widget to replace label
        entry = tk.Entry(task_frame, font=('Cascadia Mono', 13), 
                        bg='#555555', fg='white',
                        insertbackground='white')
        entry.insert(0, task['text'])
        
        # Replace label with entry
        task_label.pack_forget()
        entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=3)
        entry.focus_set()
        entry.select_range(0, tk.END)
        
        def save_edit(event=None):
            new_text = entry.get().strip()
            if new_text:
                task['text'] = new_text
                self.save_tasks()
            self.refresh_tasks()
            
        def cancel_edit(event=None):
            self.refresh_tasks()
            
        # Add word deletion shortcuts to edit entry too
        entry.bind('<Control-BackSpace>', self.delete_word_backward)
        entry.bind('<Control-Delete>', self.delete_word_forward)
        entry.bind('<Return>', save_edit)
        entry.bind('<KP_Enter>', save_edit)
        entry.bind('<Escape>', cancel_edit)
        entry.bind('<FocusOut>', save_edit)
    
    def reorder_task(self, dragged_id, target_id):
        # Find indices
        dragged_idx = next((i for i, t in enumerate(self.tasks) if t['id'] == dragged_id), -1)
        target_idx = next((i for i, t in enumerate(self.tasks) if t['id'] == target_id), -1)
        
        if dragged_idx != -1 and target_idx != -1 and dragged_idx != target_idx:
            # Remove dragged task and insert it before target
            dragged_task = self.tasks.pop(dragged_idx)
            
            # Adjust target index if we removed an item before it
            if dragged_idx < target_idx:
                target_idx -= 1
                
            self.tasks.insert(target_idx, dragged_task)
            self.refresh_tasks()
            self.save_tasks()
    
    def delete_word_backward(self, event):
        """Delete word backward from cursor position (Ctrl+Backspace)"""
        entry = event.widget
        cursor_pos = entry.index(tk.INSERT)
        text = entry.get()
        
        if cursor_pos == 0:
            return "break"
        
        # Find the start of the current word
        start_pos = cursor_pos - 1
        
        # Skip trailing spaces
        while start_pos >= 0 and text[start_pos] == ' ':
            start_pos -= 1
        
        # Find word boundary
        while start_pos >= 0 and text[start_pos] != ' ':
            start_pos -= 1
        
        start_pos += 1  # Move to first character of word
        
        # Delete the word
        entry.delete(start_pos, cursor_pos)
        return "break"  # Prevent default behavior
    
    def delete_word_forward(self, event):
        """Delete word forward from cursor position (Ctrl+Delete)"""
        entry = event.widget
        cursor_pos = entry.index(tk.INSERT)
        text = entry.get()
        
        if cursor_pos >= len(text):
            return "break"
        
        # Find the end of the current word
        end_pos = cursor_pos
        
        # Skip leading spaces
        while end_pos < len(text) and text[end_pos] == ' ':
            end_pos += 1
        
        # Find word boundary
        while end_pos < len(text) and text[end_pos] != ' ':
            end_pos += 1
        
        # Delete the word
        entry.delete(cursor_pos, end_pos)
        return "break"  # Prevent default behavior
        
    def update_scrollbar(self):
        # Update canvas scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        # Check if scrollbar is needed
        canvas_height = self.canvas.winfo_height()
        content_height = self.scrollable_frame.winfo_reqheight()
        
        if content_height > canvas_height and canvas_height > 1:
            # Show scrollbar
            if not self.scrollbar.winfo_ismapped():
                self.scrollbar.pack(side="right", fill="y")
        else:
            # Hide scrollbar
            if self.scrollbar.winfo_ismapped():
                self.scrollbar.pack_forget()
    
    def refresh_tasks(self):
        # Clear existing task widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        # Add all tasks
        for task in self.tasks:
            self.create_task_widget(task)
            
        # Update scrollbar visibility after a short delay
        self.root.after(10, self.update_scrollbar)
            
    def save_tasks(self):
        try:
            with open(self.tasks_file, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
            
    def load_tasks(self):
        try:
            if os.path.exists(self.tasks_file):
                with open(self.tasks_file, 'r') as f:
                    self.tasks = json.load(f)
                self.refresh_tasks()
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = OverlayTodoApp()
    app.run()