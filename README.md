# Advanced Calculator Application

A feature-rich calculator built with Python's Tkinter library, supporting both mouse and keyboard input with advanced input validation.

## Features

### Core Functionality
- Basic arithmetic operations (+, -, *, /)
- Decimal point support for floating-point calculations
- Clear screen (C) and backspace (⌫) functionality
- Real-time expression display

### Input Validation
- Prevents multiple operators in a row (e.g., `+++`, `+-*/`)
- Prevents multiple decimal points in the same number
- Handles negative numbers correctly
- Auto-clears error messages when new input starts

### Keyboard Support
Full keyboard and numpad integration:
- **Number keys**: 0-9 (both top row and numpad)
- **Operators**: +, -, *, / (main keyboard and numpad)
- **Enter/Return**: Calculate result
- **Backspace**: Delete last character
- **Escape (Esc)**: Clear all input
- **Period (.)**: Add decimal point

### Error Handling
- Division by zero protection
- Syntax error detection
- Clear, user-friendly error messages
- Automatic error recovery

## How to Run

```bash
python calculator.py

