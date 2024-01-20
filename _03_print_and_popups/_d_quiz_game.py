from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    answer = simpledialog.askstring("Question 1", "How many sides does a decagon have?")
    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct
    if answer == "10" or answer.lower() == "ten":
    #      // 4.  if the user's answer was correct, add one to their score 
        score += 1
    answer2 = simpledialog.askstring("Question 2", "How many sides does a octagon have?")
    #      // 2.  Ask the user a question

    #      // 3.  Use an if statement to check if their answer is correct
    if answer2 == "8" or answer.lower() == "eight":
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo("Quiz Completed", f"Final Score: {score}/2")
    # Run the window's .mainloop() method
    window.mainloop()
