import tkinter

window=tkinter.Tk()
window.title("Miles to kilometer Converter")
window.minsize(200,100)

#1miles=1.6km

def calc():
    Label_km.config(text=int(int(enter.get())*1.6))

enter=tkinter.Entry()
enter.grid(column=2,row=1)

Label_miles_text=tkinter.Label(text="Miles")
Label_miles_text.grid(column=3,row=1)

Label_km=tkinter.Label(text="0")
Label_km.grid(column=2,row=2)

Label_km_text=tkinter.Label(text="Km")
Label_km_text.grid(column=3,row=2)

Label_equal=tkinter.Label(text="is equal to")
Label_equal.grid(column=1,row=2)

button=tkinter.Button(text="Calculate",command=calc)
button.grid(column=2,row=3)

window.mainloop()