import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    
    PADDING = 10
    
    BUTTON_CAPTIONS = [
        "C", "+/-", "%", "/",
        7, 8, 9, "*",
        4, 5, 6, "-",
        1, 2, 3, "+",
        0, ".", "="
    ]
    
    BUTTONS_PER_ROW = 4
    
    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller
        
        self.entry_variable = tk.StringVar()
        
        self.title("Python Calculator")
        
        self._create_main_frame()
        self._create_entry()
        self._create_buttons()
        self._center_window()
    
    def _create_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PADDING, pady=self.PADDING)
    
    def _create_entry(self):
        entry = ttk.Entry(self.main_frame, justify="right", textvariable=self.entry_variable, state="disabled")
        entry.pack(fill="x")
    
    def _create_buttons(self):
        outer_buttons_frame = ttk.Frame(self.main_frame)
        outer_buttons_frame.pack()
        
        row_frame = ttk.Frame(outer_buttons_frame)
        row_frame.pack()
        
        buttons_in_row = 0
        
        for caption in self.BUTTON_CAPTIONS:
            if buttons_in_row == self.BUTTONS_PER_ROW:
                row_frame = ttk.Frame(outer_buttons_frame)
                row_frame.pack()
                buttons_in_row = 0
                
            button = ttk.Button(row_frame, text=caption, command=(lambda button=caption: self.controller.button_click(button)))
            button.pack(side="left")
            
            buttons_in_row += 1
    def _center_window(self):
        self.update()
        
        width = self.winfo_width()
        height = self.winfo_height()
        
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
    
    def main(self):
        self.mainloop()
