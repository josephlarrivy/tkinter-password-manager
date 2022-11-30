from tkinter import *
from models import connect_db, Set


#####################

fields = ('Website Nickname', 'Website URL',
          'email', 'username', 'password')

nickname = ''
url = ''
email = ''
username = ''
password = ''

def monthly_payment(entries):
    nickname = entries['Website Nickname'].get()
    print('nickname' - nickname)
   
    url = entries['Website URL'].get()
    print('url' - url)

    email = entries['email'].get()
    print('email' - email)

    username = entries['username'].get()
    print('username' - username)

    password = entries['password'].get()
    print('password' - password)


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        # ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def add_password():
    print(nickname)
    print('testing')



if __name__ == '__main__':
    root = Tk()
    
    connect_db(root)
    root.title('Password Manager')
    ents = makeform(root, fields)

    # root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    b1 = Button(root, text='Save',
               command=(lambda e=ents: add_password()))
    b1.pack(side=LEFT, padx=6, pady=6)

    # b2 = Button(root, text='username',
    #            command=(lambda e=ents: monthly_payment(e)))
    # b2.pack(side=LEFT, padx=5, pady=5)
    # b3 = Button(root, text='Quit', command=root.quit)
    # b3.pack(side=LEFT, padx=5, pady=5)


    root.mainloop()















# import tkinter as tk
# from tkinter import *
# from tkinter import ttk, filedialog, Text
# import os


# root = tk.Tk()
# root.title("Password Manager")
# root.geometry('400x300')


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

# fields = ('Test1', 'Test2')

# def add_password(entries):

#     x = entries['Test1'].get()
#     print(x)
    # print(entries)




#####################

# b = Label(root, text="website nickname").grid(row=1, column=0)
# b = Label(root, text="website_url").grid(row=2, column=0)
# c = Label(root, text="email").grid(row=3, column=0)
# d = Label(root, text="username").grid(row=4, column=0)
# e = Label(root, text="password").grid(row=5, column=0)

# a1 = Entry(root).grid(row=1, column=1)
# b1 = Entry(root).grid(row=2, column=1)
# c1 = Entry(root).grid(row=3, column=1)
# d1 = Entry(root).grid(row=4, column=1)
# e1 = Entry(root).grid(row=5, column=1)


# def add_password():
#     print()
#     print('testing')

# def clicked():
#    res = "Welcome to " + txt.get()
#    add_password()

#    lbl.configure(text=res)


# btn = ttk.Button(root, text="Submit").grid(row=6, column=0)




# commit_password = tk.Button(root, text="Add Password", padx=20,
#                     pady=15, fg='black', bg="white", command=add_password).grid(row=7, column=1)
# # commit_password.pack()










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


# root.mainloop()


# with open('save.txt', 'w') as f:
#     for app in apps:
#         f.write(app + ',')
