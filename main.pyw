import customtkinter
import random

nums_temp = []
nums = []

#creating a list of random numbers from 1 to 25
def random_nmb():
    for i in range(1, 26):
        nums_temp.append(i)

random_nmb()
nums = nums_temp

#picks random number from list
def pick_random():
    global picked
    picked = random.choice(nums)
    print(picked)

pick_random()
#taking user typed input from entry box, and checking if guessed number was to low , to high or equal
def get_guess():
    global guess_var
    guess_var = entry.get()
    if int(guess_var) == int(picked):
        pop_up_winner()
    if int(guess_var) > int(picked):
        pop_up_high()
    if int(guess_var) < int(picked):
        pop_up_low()
#pop up when user guessed the right number
def pop_up_winner():
    global yesnofrm
    global yes
    global no
    global plagainlabel
    yesnofrm = customtkinter.CTkFrame(master=root)
    yesnofrm.pack(pady=10)
    winner = customtkinter.CTkLabel(master=root, text="You Win congratulations!",font=('Helvetica',15))
    winner.pack(pady=10, padx=25)
    winner.after(1650, winner.destroy)
    plagainlabel = customtkinter.CTkLabel(master=yesnofrm, text="Do you want to play again?", font=('Helvetica', 15))
    plagainlabel.pack(pady=10)
    yes = customtkinter.CTkButton(master=yesnofrm, text="Yes", width=35, height=25,command=destr)
    yes.pack(side="left", padx=10)
    no = customtkinter.CTkButton(master=yesnofrm, text="No", width=35, height=25,command=dest_no)
    no.pack(side="right")
#pop up when user input was to high
def pop_up_high():
    too_high = customtkinter.CTkLabel(master=root,text="Your guess was to high")
    too_high.pack()
    too_high.after(1600,too_high.destroy)
    entry.delete(0,"end")
#pop up when user input was to low
def pop_up_low():
    too_low = customtkinter.CTkLabel(master=root,text="Your guess was to low")
    too_low.pack()
    too_low.after(1600,too_low.destroy)
    entry.delete(0,"end")
#destroy frame that contains buttons yes or no for playing again and calling pick_random function
def destr():
    yes.destroy()
    no.destroy()
    yesnofrm.destroy()
    plagainlabel.destroy()
    entry.delete(0,"end")
    pick_random()
# function that close program when user picked no on play again screen
def dest_no():
    root.destroy()
#main window and GUI settings
root = customtkinter.CTk()
root.geometry("450x386")
root.title("Guessing Game")
root.resizable(False, False)
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

label = customtkinter.CTkLabel(master=root, text="Number Guessing Game !", font=('Helvetica', 25))
label.pack(pady=10, padx=25)

inscturcion = customtkinter.CTkLabel(master=root, text="Guess an number from 1 to 25", font=('Helvetica', 17))
inscturcion.pack()

global entry
entry = customtkinter.CTkEntry(master=root, placeholder_text="Type Your guess : ", width=250, height=50, font=('Helvetica', 15))
entry.pack(pady=25, padx=25)

check_button = customtkinter.CTkButton(master=root, text="Check Guess", width=130, height=30, command=get_guess)
check_button.pack(pady=10, padx=25)
root.mainloop()
