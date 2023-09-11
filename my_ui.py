import tkinter as tk

window = tk.Tk()
window.title("Sprint 0 test GUI")
window.geometry("640x480")

button = tk.IntVar()

#Text
test_label1 = tk.Label(text="this is example text")
test_label1.pack()


#Lines
canvas = tk.Canvas(window, width=300, height = 220)
canvas.pack()
y = 20
for i in range(0,4):
    canvas.create_line(0, y, 400, y, fill="green", width = 2)
    y += 20

#checkbox
check = tk.Checkbutton(window, text="I'm a checkbox")
check.pack()

#radio buttons
radio1 = tk.Radiobutton(window, text="Radio button 1", value=1, variable=button)
radio2 = tk.Radiobutton(window, text="Radio button 2", value=2, variable=button)
radio1.pack()
radio2.pack()

test_label2 = tk.Label(window)
test_label2.pack()
window.mainloop()
