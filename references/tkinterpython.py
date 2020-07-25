import tkinter as tk

root = tk.Tk()

root.title('Get Information Program')

HEIGHT = 900
WIDTH = 900

root.resizable(False, False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='pic.png', master=root)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40, bg = 'white')
entry.place(relwidth=0.65, relheight=1)

button_1 = tk.Button(frame, text="Get Info", command=lambda: getinfo(entry.get()))
button_1.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame2 = tk.Frame(root, bg='white', bd=5)
lower_frame2.place(relx=0.5, rely=0.22, relwidth=0.9, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='white', bd=5)
lower_frame.place(relx=0.5, rely=0.34, relwidth=0.9, relheight=0.6, anchor='n')

# =============================================================================
# I have an extra text field positioned perfectly in case I want to add an extra
# feature in the future.
# =============================================================================

#lower_frame3 = tk.Frame(root, bg='white', bd=5)
#lower_frame3.place(relx=0.5, rely=0.76, relwidth=0.9, relheight=0.1, anchor='n')

label = tk.Label(lower_frame, bg='white')
label.place(relwidth=1, relheight=1)

label2 = tk.Label(lower_frame2, bg='white')
label2.place(relwidth=1, relheight=1)


root.mainloop()
