import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x450")
        self.root.resizable(True, True)

        self.expression = ""
        self.operators = set(['+', '-', '*', '/'])
        
        # Create a string variable to display the text
        self.display_text = tk.StringVar()

        # Create the display frame
        display_frame = ttk.Frame(self.root)
        display_frame.pack(fill=tk.BOTH, expand=True)

        # Create the display label
        display_label = ttk.Label(
            display_frame,
            textvariable=self.display_text,
            font=('Arial', 26),
            anchor="e",
            background="white",
            foreground="black",
            padding=6
        )
        display_label.pack(fill=tk.BOTH, expand=True)

        # Create Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True)

        self.create_buttons(button_frame)
        
        # Bind keyboard keys
        self.bind_keyboard()

    def create_buttons(self, frame):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('.', 5, 0), ('⌫', 5, 1)  # Added decimal point and backspace buttons
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

        # Configure rows and columns weight for resizing
        for i in range(6):  # 6 rows (0-5)
            frame.rowconfigure(i, weight=1)
        for i in range(4):  # 4 columns (0-3)
            frame.columnconfigure(i, weight=1)

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