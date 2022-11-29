import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, Text
import os


root = tk.Tk()
root.title("Password Manager")


# canvas = tk.Canvas(root, height=700, width=700, bg="black")
# canvas.pack()

# frame = tk.Frame(root, bg="white")
# frame.place(relx=0.1, rely=0.1, relwidth=1, relheight=1)

# if os.path.isfile('save.txt'):
#     with open('save.txt', 'r') as f:
#         tempApps = f.read()
#         tempApps = tempApps.split(',')
#         apps = [x for x in tempApps if x.strip()]
#         print(apps)


# a = Label(root, text="First Name", bg='white')
# a.pack()

b = Label(root, text="website nickname").grid(row=1, column=0)
b = Label(root, text="website_url").grid(row=2, column=0)
c = Label(root, text="email").grid(row=3, column=0)
d = Label(root, text="username").grid(row=4, column=0)
e = Label(root, text="password").grid(row=5, column=0)

a1 = Entry(root).grid(row=1, column=1)
b1 = Entry(root).grid(row=2, column=1)
c1 = Entry(root).grid(row=3, column=1)
d1 = Entry(root).grid(row=4, column=1)
e1 = Entry(root).grid(row=5, column=1)

def add_password():

    print('testing')







commit_password = tk.Button(root, text="Add Password", padx=20,
                    pady=15, fg='black', bg="white", command=add_password).grid(row=7, column=1)
# commit_password.pack()





# def addApp():

#     for widget in frame.winfo_children():
#         widget.destroy()

#     filename = filedialog.askopenfilename(
#         initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
#     apps.append(filename)
#     print(apps)
#     for app in apps:
#         label = tk.Label( text=app, bg="gray")
#         label.pack()


# def runApps():
#     for app in apps:
#         os.startfile(app)




# openFile = tk.Button(root, text="Open File", padx=25,
#                      pady=10, fg='white', bg="#263D42", command=addApp)
# openFile.pack()

# runApps = tk.Button(root, text="Run Apps", padx=25,
#                     pady=10, fg='white', bg="#263D42", command=runApps)
# runApps.pack()

# for app in apps:
#     label = tk.Label(frame, text=app)
#     label.pack()


root.mainloop()


# with open('save.txt', 'w') as f:
#     for app in apps:
#         f.write(app + ',')
