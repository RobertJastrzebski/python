from tkinter import *

window = Tk()

window.title("Miles to kilometers converter")
window.config(pady=30,padx=30)

miles_input= Entry(width=10)
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is__equal_label=Label(text="Is equal to")
is__equal_label.grid(column=0,row=1)

result_label=Label(text="0")
result_label.grid(column=1,row=1)

km_label=Label(text="Km",)
km_label.grid(column=2,row=1)

def miles_to_Km():
    print("I got clicked")
    miles = miles_input.get()
    km = float(miles) * 1.60934
    result_label.config(text=km)


convert_button= Button(text="Convert",command=miles_to_Km)
# convert_button.config(text="converttttooo")
# convert_button["text"]="convert"

convert_button.grid(column=1,row=2)


window.mainloop()