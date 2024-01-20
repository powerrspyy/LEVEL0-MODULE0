from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    def ask(prompt):
        ans = simpledialog.askinteger("Guess My Number", prompt)
        return ans
    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 10)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        ans = ask("I have a number between 1 and 10 try to guess it!")
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if ans == random_num:
            messagebox.showinfo("You won!", "Good Job")
            sys.exit()
        # 7. if the guess is high
        elif ans > random_num:
            messagebox.showinfo("Your guess is too high!", "Try again")
            # 8. Tell them it's too high
        # 9. Else if the guess is low
        else:
            messagebox.showinfo("Your guess is too low!", "Try again")
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo("You Lost!", "Womp Womp")
    window.mainloop()
