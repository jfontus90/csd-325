import tkinter as tk

root = tk.Tk()
root.title("Fontus-ToDo")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task(event):
    try:
        index = listbox.nearest(event.y)
        listbox.delete(index)
    except:
        pass

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

label = tk.Label(root, text="Right click a task to delete it.")
label.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

listbox.bind("<Button-3>", delete_task)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0, bg="lightblue", fg="black")
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()