from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    rollno TEXT,
    name TEXT,
    email TEXT,
    gender TEXT,
    contact TEXT,
    dob TEXT,
    address TEXT
)
""")

conn.commit()


# ================= FUNCTIONS =================
def add_student():
    if roll_var.get() == "" or name_var.get() == "":
        messagebox.showerror("Error", "Roll No and Name are required")
        return

    cursor.execute(
        "INSERT INTO students VALUES(?,?,?,?,?,?,?)",
        (
            roll_var.get(),
            name_var.get(),
            email_var.get(),
            gender_var.get(),
            contact_var.get(),
            dob_var.get(),
            address_var.get()
        )
    )

    conn.commit()
    show_students()
    clear_fields()

    messagebox.showinfo("Success", "Student Added Successfully")


def show_students():
    table.delete(*table.get_children())

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        table.insert('', END, values=row)


def clear_fields():
    roll_var.set("")
    name_var.set("")
    email_var.set("")
    gender_var.set("")
    contact_var.set("")
    dob_var.set("")
    address_var.set("")


def delete_student():
    selected = table.focus()

    if not selected:
        messagebox.showerror("Error", "Select a student first")
        return

    data = table.item(selected)
    rollno = data['values'][0]

    cursor.execute("DELETE FROM students WHERE rollno=?", (rollno,))
    conn.commit()

    show_students()
    clear_fields()

    messagebox.showinfo("Deleted", "Student Deleted Successfully")


def get_data(event):
    selected = table.focus()
    data = table.item(selected)
    row = data['values']

    roll_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    gender_var.set(row[3])
    contact_var.set(row[4])
    dob_var.set(row[5])
    address_var.set(row[6])


def update_student():
    cursor.execute("""
    UPDATE students SET
    name=?,
    email=?,
    gender=?,
    contact=?,
    dob=?,
    address=?
    WHERE rollno=?
    """,
    (
        name_var.get(),
        email_var.get(),
        gender_var.get(),
        contact_var.get(),
        dob_var.get(),
        address_var.get(),
        roll_var.get()
    ))

    conn.commit()

    show_students()
    clear_fields()

    messagebox.showinfo("Updated", "Student Updated Successfully")


def search_student():
    table.delete(*table.get_children())

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + search_var.get() + '%',)
    )

    rows = cursor.fetchall()

    for row in rows:
        table.insert('', END, values=row)


# ================= WINDOW =================
root = Tk()
root.title("Student Management System")
root.geometry("1100x600")
root.config(bg="white")

title = Label(
    root,
    text="Student Management System",
    font=("Arial", 25, "bold"),
    bg="white",
    fg="darkblue"
)
title.pack(side=TOP, fill=X)

# ================= VARIABLES =================
roll_var = StringVar()
name_var = StringVar()
email_var = StringVar()
gender_var = StringVar()
contact_var = StringVar()
dob_var = StringVar()
address_var = StringVar()
search_var = StringVar()

# ================= LEFT FRAME =================
left_frame = Frame(root, bd=3, relief=RIDGE, bg="white")
left_frame.place(x=10, y=60, width=350, height=520)

Label(left_frame, text="Manage Students",
      font=("Arial", 18, "bold"),
      bg="white").pack(pady=10)

# Labels and Entries
labels = [
    ("Roll No.", roll_var),
    ("Name", name_var),
    ("Email", email_var),
    ("Gender", gender_var),
    ("Contact", contact_var),
    ("D.O.B", dob_var),
    ("Address", address_var)
]

y = 60

for text, var in labels:
    Label(left_frame,
          text=text,
          font=("Arial", 12, "bold"),
          bg="white").place(x=20, y=y)

    Entry(left_frame,
          textvariable=var,
          font=("Arial", 12),
          bd=2,
          relief=GROOVE).place(x=120, y=y, width=200)

    y += 50

# Buttons
Button(left_frame,
       text="Add",
       width=8,
       command=add_student,
       bg="green",
       fg="white").place(x=20, y=430)

Button(left_frame,
       text="Update",
       width=8,
       command=update_student,
       bg="blue",
       fg="white").place(x=100, y=430)

Button(left_frame,
       text="Delete",
       width=8,
       command=delete_student,
       bg="red",
       fg="white").place(x=180, y=430)

Button(left_frame,
       text="Clear",
       width=8,
       command=clear_fields,
       bg="gray",
       fg="white").place(x=260, y=430)

# ================= RIGHT FRAME =================
right_frame = Frame(root, bd=3, relief=RIDGE, bg="white")
right_frame.place(x=370, y=60, width=720, height=520)

# Search Area
Label(right_frame,
      text="Search By Name",
      font=("Arial", 12, "bold"),
      bg="white").place(x=20, y=20)

Entry(right_frame,
      textvariable=search_var,
      font=("Arial", 12),
      bd=2,
      relief=GROOVE).place(x=170, y=20, width=200)

Button(right_frame,
       text="Search",
       command=search_student,
       bg="darkblue",
       fg="white").place(x=400, y=20)

Button(right_frame,
       text="Show All",
       command=show_students,
       bg="green",
       fg="white").place(x=480, y=20)

# ================= TABLE =================
table_frame = Frame(right_frame, bd=2, relief=RIDGE)
table_frame.place(x=10, y=70, width=690, height=430)

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)

table = ttk.Treeview(
    table_frame,
    columns=("roll", "name", "email", "gender",
             "contact", "dob", "address"),
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set
)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)

table.heading("roll", text="Roll No")
table.heading("name", text="Name")
table.heading("email", text="Email")
table.heading("gender", text="Gender")
table.heading("contact", text="Contact")
table.heading("dob", text="D.O.B")
table.heading("address", text="Address")

table['show'] = 'headings'

table.column("roll", width=80)
table.column("name", width=120)
table.column("email", width=150)
table.column("gender", width=80)
table.column("contact", width=100)
table.column("dob", width=100)
table.column("address", width=150)

table.pack(fill=BOTH, expand=1)

table.bind("<ButtonRelease-1>", get_data)

show_students()

root.mainloop()