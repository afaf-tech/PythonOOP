import tkinter

# dlam python setiap kelas diawali huruf besar
main_window = tkinter.Tk()

print(main_window.__dict__)

label1 = tkinter.Label(main_window, text="label1")
label2 = tkinter.Label(main_window, text="label2")

tombol1 = tkinter.Button(main_window, text="tombol1")
tombol2 = tkinter.Button(main_window, text="tombol2")
# positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan gui
main_window.mainloop()
