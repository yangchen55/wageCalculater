from tkinter import *
import sqlite3 as sql
from tkinter import messagebox

parent = Tk()
parent.title("weekly wages calculater")
my_label = Label(parent, text="weekly wages calculater", font=("Arial Bold", 20))
my_label.grid(column=100, row=100)


#  TO CREATE DATABASE VIA SQL language

try:
    con = sql.connect('wages.db')
    cur = con.cursor()
    cur.execute(''' create table wages_table
    (day text, hour int, wage float)''')
except:
    print("connected to table of database")

# FUNCTION TO ADD  INPUT INTO THE DATABASE(WAGE.DB)
def calculate_wages():
    day = day_entry.get()
    hour = hour_entry.get()
    wage = wage_entry.get()
    if (len(day) <= 0) & (len(hour) <= 0) & (len(wage) <= 0):
        messagebox.showerror(message="enter required details")
    else:
        cur.execute("insert into wages_table values ('%s', '%s', '%s')" % (day, hour, wage))
        messagebox.showinfo(message = "wages added successfully")
        con.commit()


# fucntion to view wages from the database after adding add to the table
def view_wages():
    day = day_entry.get()
    hour = hour_entry.get()
    wage = wage_entry.get()
    if (len(day) <= 0) & (len(wage) <= 0):
        sql_statement = "select * from wages_table"
    else:
        sql_statement = "select * from wages_table where day = '%s'" % (day)

        cur.execute(sql_statement)
        row = cur.fetchall()

        if len(row) <= 0:
            messagebox.showerror(message="No note found")
        else:
            for i in row:

                messagebox.showinfo(message=i)


# day  input
day_label = Label(parent, text="day:").place(x=10, y=50)
day_entry = Entry(parent, width=20)
day_entry.place(x=60, y=50)

# hour input
hour_label = Label(parent, text="hours:").place(x=10, y=70)
hour_entry = Entry(parent, width=20)
hour_entry.place(x=60, y=70)

# hour input
wage_label = Label(parent, text="wages $:").place(x=10, y=90)
wage_entry = Entry(parent, width=20)
wage_entry.place(x=60, y=90)

# we have buttons to calculate wages, view wages and many more, the button only only if we add fuction assigned to command
button1 = Button(parent, text='calculate wage', bg='blue', fg='black', command=calculate_wages).place(x=10, y=200)
button2 = Button(parent, text='view  wages', bg='blue', fg='black', command=view_wages).place(x=100, y=200)

# geometry set default window size
parent.geometry('600x300')
# disable resizing the GUI
# parent.resizable(0,0)
parent.mainloop()
