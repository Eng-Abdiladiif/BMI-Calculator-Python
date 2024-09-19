from tkinter import *




root = Tk()



# Creating  BMI Function

def BMI():


    w =  int(weight.get())
    h = float(height.get())


    bmi  = (w/h ** 2)

    my_label = Label(root, text=f' MY BMI: {bmi}')
    my_label.pack()



    if  bmi  < 18.5:

        my_label = Label(root, text="Miisan isku dar",  )
        my_label.pack()
    elif bmi > 25:
        my_label = Label(root, text ="Misanka Dhin")
        my_label.pack()

    else:
        my_label= Label(root, text=" Normal ayaa tahay")
        my_label.pack()
        





root.geometry("400x250")

# change Color

root.config(background="#384B70")

# Change title name

root.title("Mini Project BMI")


# Creating Form



#   weight

weight = Entry(root, width=30)
weight.pack(padx=5, pady=20)

# height

height = Entry(root, width=30)
height.pack(padx=5, pady=10)

# Button


my_buton = Button(root, text='Calculate BMI', width=15, command=BMI)
my_buton.config(background="#A04747", font=("Arial", 10, "bold"), fg="white")
my_buton.pack(padx=5, pady=20)



root.mainloop()