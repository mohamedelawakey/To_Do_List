import tkinter as tk
from tkinter import messagebox

task_count = 1

# Function to add a task to the list
def add_task():
    global task_count
    task = entry.get()
    if task != "":  
        task_with_number = f"{task_count}. {task}"
        listbox.insert(tk.END, task_with_number)  
        entry.delete(0, tk.END) 
        task_count += 1 
    else:
        messagebox.showwarning("Invalid Input", "Please enter a task.")  

# Function to delete selected tasks
def delete_tasks():
    selected_tasks = listbox.curselection()
    if selected_tasks:
        for task in selected_tasks:
            listbox.delete(task)  
    else:
        messagebox.showwarning("Invalid Removal", "Please select a task or tasks to remove.") 

# Set up the application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x480")
root.configure(bg="#2e2e2e")

# Add a label at the top of the window
label = tk.Label(root, text="To-Do List", font=("Arial", 30), fg="black", bg="#2e2e2e")
label.pack(pady=10)

# Add an entry field for entering tasks
entry = tk.Entry(root, font=("Arial", 14), width=51)
entry.pack(pady=10)

# Add a listbox to display the tasks
listbox = tk.Listbox(root, font=("Arial", 14), width=51, height=10, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

# Create a frame to hold the buttons next to each other
button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=10)

# Define the size of the buttons
button_width = 24
button_height = 2

# Add an "Add Task" button, Change the cursor to a hand when hovering over the button
add_button = tk.Button(button_frame, text="Add Task", font=("Arial", 14), fg="black", bg="white", width=button_width, height=button_height, command=add_task)
add_button.pack(side=tk.LEFT, padx=10)
add_button.config(cursor="hand2")  

# Add a "Delete Selected Tasks" button, Change the cursor to a hand when hovering over the button
delete_button = tk.Button(button_frame, text="Delete Selected Tasks", font=("Arial", 14), fg="black", bg="white", width=button_width, height=button_height, command=delete_tasks)
delete_button.pack(side=tk.LEFT, padx=10)
delete_button.config(cursor="hand2") 

# Run the application
root.mainloop()
