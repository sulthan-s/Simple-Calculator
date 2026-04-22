import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x500")
        self.root.resizable(True, True)
        
        # Theme settings
        self.current_theme = "dark"  # dark, light, blue, purple, green
        self.themes = {
            "dark": {
                "bg": "#1e1e1e",
                "display_bg": "#2d2d2d",
                "display_fg": "#ffffff",
                "button_bg": "#3c3c3c",
                "button_fg": "#ffffff",
                "button_hover": "#4a4a4a",
                "operator_bg": "#ff9800",
                "operator_fg": "#ffffff",
                "operator_hover": "#f57c00",
                "equal_bg": "#4caf50",
                "equal_fg": "#ffffff",
                "equal_hover": "#45a049",
                "clear_bg": "#f44336",
                "clear_fg": "#ffffff",
                "clear_hover": "#da190b"
            },
            "light": {
                "bg": "#f5f5f5",
                "display_bg": "#ffffff",
                "display_fg": "#000000",
                "button_bg": "#e0e0e0",
                "button_fg": "#000000",
                "button_hover": "#d0d0d0",
                "operator_bg": "#ff9800",
                "operator_fg": "#ffffff",
                "operator_hover": "#f57c00",
                "equal_bg": "#4caf50",
                "equal_fg": "#ffffff",
                "equal_hover": "#45a049",
                "clear_bg": "#f44336",
                "clear_fg": "#ffffff",
                "clear_hover": "#da190b"
            },
            "blue": {
                "bg": "#1a237e",
                "display_bg": "#283593",
                "display_fg": "#ffffff",
                "button_bg": "#3949ab",
                "button_fg": "#ffffff",
                "button_hover": "#5c6bc0",
                "operator_bg": "#ffb74d",
                "operator_fg": "#000000",
                "operator_hover": "#ffa726",
                "equal_bg": "#66bb6a",
                "equal_fg": "#ffffff",
                "equal_hover": "#4caf50",
                "clear_bg": "#ef5350",
                "clear_fg": "#ffffff",
                "clear_hover": "#e53935"
            },
            "purple": {
                "bg": "#4a148c",
                "display_bg": "#6a1b9a",
                "display_fg": "#ffffff",
                "button_bg": "#8e24aa",
                "button_fg": "#ffffff",
                "button_hover": "#ab47bc",
                "operator_bg": "#ffb74d",
                "operator_fg": "#000000",
                "operator_hover": "#ffa726",
                "equal_bg": "#66bb6a",
                "equal_fg": "#ffffff",
                "equal_hover": "#4caf50",
                "clear_bg": "#ef5350",
                "clear_fg": "#ffffff",
                "clear_hover": "#e53935"
            },
            "green": {
                "bg": "#1b5e20",
                "display_bg": "#2e7d32",
                "display_fg": "#ffffff",
                "button_bg": "#388e3c",
                "button_fg": "#ffffff",
                "button_hover": "#4caf50",
                "operator_bg": "#ffb74d",
                "operator_fg": "#000000",
                "operator_hover": "#ffa726",
                "equal_bg": "#42a5f5",
                "equal_fg": "#ffffff",
                "equal_hover": "#2196f3",
                "clear_bg": "#ef5350",
                "clear_fg": "#ffffff",
                "clear_hover": "#e53935"
            }
        }

        self.expression = ""
        self.operators = set(['+', '-', '*', '/'])
        
        # Create a string variable to display the text
        self.display_text = tk.StringVar()
        self.display_text.set("0")
        
        # Apply theme
        self.apply_theme()
        
        # Create the display frame
        display_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]["bg"])
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create display with border and shadow effect
        self.display_label = tk.Label(
            display_frame,
            textvariable=self.display_text,
            font=('Segoe UI', 32, 'bold'),
            anchor="e",
            bg=self.themes[self.current_theme]["display_bg"],
            fg=self.themes[self.current_theme]["display_fg"],
            padx=15,
            pady=20,
            relief=tk.FLAT
        )
        self.display_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        
        # Create Button Frame
        button_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]["bg"])
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Theme selector frame
        theme_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]["bg"])
        theme_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        theme_label = tk.Label(
            theme_frame, 
            text="Theme:", 
            font=('Segoe UI', 10),
            bg=self.themes[self.current_theme]["bg"],
            fg=self.themes[self.current_theme]["display_fg"]
        )
        theme_label.pack(side=tk.LEFT, padx=5)
        
        # Theme selector buttons
        theme_buttons_frame = tk.Frame(theme_frame, bg=self.themes[self.current_theme]["bg"])
        theme_buttons_frame.pack(side=tk.LEFT, padx=5)
        
        themes_list = ["dark", "light", "blue", "purple", "green"]
        theme_colors = ["#1e1e1e", "#f5f5f5", "#1a237e", "#4a148c", "#1b5e20"]
        
        for theme, color in zip(themes_list, theme_colors):
            theme_btn = tk.Button(
                theme_buttons_frame,
                bg=color,
                width=2,
                height=1,
                relief=tk.RAISED,
                borderwidth=1,
                command=lambda t=theme: self.change_theme(t)
            )
            theme_btn.pack(side=tk.LEFT, padx=2)
        
        self.create_buttons(button_frame)
        
        # Bind keyboard keys
        self.bind_keyboard()
        
        # Bind hover effects
        self.bind_hover_effects()

    def apply_theme(self):
        """Apply the current theme to the root window"""
        self.root.configure(bg=self.themes[self.current_theme]["bg"])
        
        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('default')
        
        # Custom styles for different button types
        style.configure('TButton', 
                       font=('Segoe UI', 12, 'bold'),
                       padding=10)
        
    def change_theme(self, theme_name):
        """Change the current theme"""
        if theme_name in self.themes:
            self.current_theme = theme_name
            # Refresh the entire UI
            self.root.destroy()
            new_root = tk.Tk()
            app = CalculatorApp(new_root)
            new_root.mainloop()

    def create_buttons(self, frame):
        # Configure grid weights
        for i in range(7):
            frame.rowconfigure(i, weight=1)
        for i in range(4):
            frame.columnconfigure(i, weight=1)
        
        # Button definitions: (text, row, col, rowspan, colspan, button_type)
        buttons = [
            ('C', 0, 0, 1, 1, 'clear'), ('⌫', 0, 1, 1, 1, 'clear'), ('/', 0, 2, 1, 1, 'operator'), ('*', 0, 3, 1, 1, 'operator'),
            ('7', 1, 0, 1, 1, 'number'), ('8', 1, 1, 1, 1, 'number'), ('9', 1, 2, 1, 1, 'number'), ('-', 1, 3, 1, 1, 'operator'),
            ('4', 2, 0, 1, 1, 'number'), ('5', 2, 1, 1, 1, 'number'), ('6', 2, 2, 1, 1, 'number'), ('+', 2, 3, 1, 1, 'operator'),
            ('1', 3, 0, 1, 1, 'number'), ('2', 3, 1, 1, 1, 'number'), ('3', 3, 2, 1, 1, 'number'), ('=', 3, 3, 2, 1, 'equal'),
            ('0', 4, 0, 1, 2, 'number'), ('.', 4, 2, 1, 1, 'number')
        ]
        
        self.buttons = {}
        theme = self.themes[self.current_theme]
        
        for (text, row, col, rowspan, colspan, btn_type) in buttons:
            # Set colors based on button type
            if btn_type == 'clear':
                bg_color = theme["clear_bg"]
                fg_color = theme["clear_fg"]
                hover_color = theme["clear_hover"]
            elif btn_type == 'operator':
                bg_color = theme["operator_bg"]
                fg_color = theme["operator_fg"]
                hover_color = theme["operator_hover"]
            elif btn_type == 'equal':
                bg_color = theme["equal_bg"]
                fg_color = theme["equal_fg"]
                hover_color = theme["equal_hover"]
            else:  # number
                bg_color = theme["button_bg"]
                fg_color = theme["button_fg"]
                hover_color = theme["button_hover"]
            
            button = tk.Button(
                frame,
                text=text,
                font=('Segoe UI', 14, 'bold'),
                bg=bg_color,
                fg=fg_color,
                relief=tk.RAISED,
                borderwidth=2,
                cursor="hand2",
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, rowspan=rowspan, colspan=colspan, 
                       sticky='nsew', padx=3, pady=3)
            
            # Store button colors for hover effects
            self.buttons[text] = {
                'widget': button,
                'bg': bg_color,
                'hover': hover_color,
                'fg': fg_color
            }

    def bind_hover_effects(self):
        """Bind hover effects to all buttons"""
        for btn_info in self.buttons.values():
            button = btn_info['widget']
            original_bg = btn_info['bg']
            hover_bg = btn_info['hover']
            
            def on_enter(event, b=button, h=hover_bg):
                b.configure(bg=h)
            
            def on_leave(event, b=button, o=original_bg):
                b.configure(bg=o)
            
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)

    def bind_keyboard(self):
        """Bind keyboard keys to calculator functions"""
        # Number keys
        for i in range(10):
            self.root.bind(str(i), lambda event, num=i: self.on_button_click(str(num)))
        
        # Operator keys
        self.root.bind('+', lambda event: self.on_button_click('+'))
        self.root.bind('-', lambda event: self.on_button_click('-'))
        self.root.bind('*', lambda event: self.on_button_click('*'))
        self.root.bind('/', lambda event: self.on_button_click('/'))
        
        # Special keys
        self.root.bind('<Return>', lambda event: self.on_button_click('='))
        self.root.bind('<BackSpace>', lambda event: self.on_button_click('⌫'))
        self.root.bind('<Escape>', lambda event: self.on_button_click('C'))
        self.root.bind('.', lambda event: self.on_button_click('.'))
        
        # Keypad support
        self.root.bind('<KP_Add>', lambda event: self.on_button_click('+'))
        self.root.bind('<KP_Subtract>', lambda event: self.on_button_click('-'))
        self.root.bind('<KP_Multiply>', lambda event: self.on_button_click('*'))
        self.root.bind('<KP_Divide>', lambda event: self.on_button_click('/'))
        self.root.bind('<KP_Enter>', lambda event: self.on_button_click('='))
        
        for i in range(10):
            self.root.bind(f'<KP_{i}>', lambda event, num=i: self.on_button_click(str(num)))

    def is_valid_input(self, button_text):
        """Validate input to prevent multiple operators in a row"""
        if not self.expression:
            # First character cannot be an operator except minus for negative numbers
            if button_text in self.operators and button_text != '-':
                return False
            return True
        
        last_char = self.expression[-1]
        
        # Prevent multiple operators in a row
        if button_text in self.operators and last_char in self.operators:
            return False
        
        # Prevent decimal point if number already has one
        if button_text == '.':
            # Find the last number in the expression
            last_number = ''
            for char in reversed(self.expression):
                if char in self.operators:
                    break
                last_number = char + last_number
            
            # Check if last number already contains a decimal point
            if '.' in last_number:
                return False
        
        # Prevent starting with operator except minus
        if not self.expression and button_text in self.operators and button_text != '-':
            return False
        
        return True

    def handle_backspace(self):
        """Delete the last character"""
        if self.expression:
            self.expression = self.expression[:-1]

    def evaluate_expression(self):
        """Evaluate the mathematical expression safely"""
        try:
            # Replace ^ with ** for exponentiation if needed
            expression_to_eval = self.expression.replace('^', '**')
            result = eval(expression_to_eval)
            
            # Convert to string and handle integers vs floats
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    # Round to reasonable precision
                    result = round(result, 10)
            
            self.expression = str(result)
        except ZeroDivisionError:
            self.expression = "Cannot divide by zero"
        except SyntaxError:
            self.expression = "Syntax Error"
        except Exception:
            self.expression = "Error"

    def on_button_click(self, button_text):
        """Handle button clicks and keyboard input"""
        
        # Handle clear button
        if button_text == "C":
            self.expression = ""
        
        # Handle backspace button
        elif button_text == "⌫":
            self.handle_backspace()
        
        # Handle equals button
        elif button_text == "=":
            if self.expression:
                self.evaluate_expression()
        
        # Handle all other inputs with validation
        else:
            # Check if input is valid
            if self.is_valid_input(button_text):
                # If expression shows an error, clear it first
                if self.expression in ["Error", "Syntax Error", "Cannot divide by zero"]:
                    self.expression = ""
                self.expression += button_text
        
        # Update display
        self.display_text.set(self.expression if self.expression else "0")
        
        # Move cursor to the end of the entry (for better UX with keyboard)
        if hasattr(self, 'display_label'):
            self.display_label.update()

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
