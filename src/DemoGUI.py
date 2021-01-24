# Mindula Dilthushan
from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("My First Crud App Python-MySQL")
root.configure(background="#54a0ff")
root.geometry("1000x650")
root.resizable(width=False,height=False)

id_label = ttk.Label(root, text="ID", background="#54a0ff", font=("VALORANT", 16))
id_label.grid(row=0, column=0, sticky=W)
id_text = StringVar()
id_entry = ttk.Entry(root, width=25, textvariable=id_text)
id_entry.grid(row=0, column=1, sticky=W)

name_label = ttk.Label(root, text="Name", background="#54a0ff", font=("VALORANT", 16))
name_label.grid(row=0, column=2, sticky=W)
name_text = StringVar()
name_entry = ttk.Entry(root, width=25, textvariable=name_text)
name_entry.grid(row=0, column=3, sticky=W)

address_label = ttk.Label(root, text="Address", background="#54a0ff", font=("VALORANT", 14))
address_label.grid(row=0, column=4, sticky=W)
address_text = StringVar()
address_entry = ttk.Entry(root, width=25, textvariable=address_text)
address_entry.grid(row=0, column=5, sticky=W)

email_label = ttk.Label(root, text="Email", background="#54a0ff", font=("VALORANT", 14))
email_label.grid(row=0, column=6, sticky=W)
email_text = StringVar()
email_entry = ttk.Entry(root, width=25, textvariable=email_text)
email_entry.grid(row=0, column=7, sticky=W)

add_btn = Button(root, text="Save", bg="#1dd1a1", fg="white", font="VALORANT 10", command="")
add_btn.grid(row=0, column=8, sticky=W)

list_bx = Listbox(root, height=16, width=40, font="VALORANT 13", bg="#95afc0")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=9, rowspan=14, sticky=W)

list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

delete_btn = Button(root, text="Delete", bg="#1dd1a1", fg="white", font="VALORANT", command="")
delete_btn.grid(row=15, column=2)

update_btn = Button(root, text="Update", bg="#1dd1a1", fg="white", font="VALORANT" , command="")
update_btn.grid(row=15, column=3)

view_all_btn = Button(root, text="View All", bg="#1dd1a1", fg="white", font="VALORANT" , command="")
view_all_btn.grid(row=15, column=4)

clear_btn = Button(root, text="Clear", bg="#1dd1a1", fg="white", font="VALORANT" , command="")
clear_btn.grid(row=15, column=5)

exit_btn = Button(root,text="Exit", bg="#1dd1a1", fg="white", font="VALORANT" , command="")
exit_btn.grid(row=15, column=6)

root.mainloop()