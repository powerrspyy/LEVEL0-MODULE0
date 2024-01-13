from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    code = simpledialog.askstring(title = "Can you code?", prompt="Do you know how to write code?(Y/N)")
    if code.lower() == "yes" or code.lower() == "y":
        messagebox.showinfo("Great", "There is success in your future")
    elif code.lower() == "no" or code.lower() == "n":
        messagebox.showerror("Sad", "Sign up for lessons")
    else:
        messagebox.showerror("Invalid", "Error: Invalid input")
    # Make a new window variable, window = Tk()
    
    # Hide the window using the window's .withdraw() method
    
    # 1. Ask the user if they know how to write code.
    
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.

    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
