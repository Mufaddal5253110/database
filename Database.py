import tkinter.messagebox as msg
from tkinter import *
from tkinter import filedialog
import sys
import time
root = Tk()
root.title("Database")
root.wm_iconbitmap('database.ico')
# Label(root,text="Credit : Mufaddal Shakir",bg='sky blue').grid(columnspan=2,ipadx=150)


import sqlite3

# Database

"""""""""
#create table
c.execute(''' CREATE TABLE addresses(first_name text,last_name text,adress text,city text,state text,zipcode integer) ''')
"""""""""
Label(root,text="First Name",fg='red').grid(row=0,column=0,padx=10)
Label(root,text="Last Name",fg='red').grid(row=1,column=0)
Label(root,text="Address",fg='red').grid(row=2,column=0)
Label(root,text="City",fg='red').grid(row=3,column=0)
Label(root,text="State",fg='red').grid(row=4,column=0)
Label(root,text="Zipcode",fg='red').grid(row=5,column=0)



first = Entry(root,width=30,borderwidth=3)
last = Entry(root,width=30,borderwidth=3)
address = Entry(root,width=30,borderwidth=3)
city = Entry(root,width=30,borderwidth=3)
state= Entry(root,width=30,borderwidth=3)
zipcode= Entry(root,width=30,borderwidth=3)

first.grid(row=0,column=1,padx=5)
last.grid(row=1,column=1)
address.grid(row=2,column=1)
city.grid(row=3,column=1)
state.grid(row=4,column=1)
zipcode.grid(row=5,column=1)

def submit():
    # Create Database or connect
    connect = sqlite3.connect('AddressBook.db')

    # Create cursor
    c = connect.cursor()

    # Insert data
    c.execute("INSERT INTO addresses VALUES (:first,:last,:address,:city,:state,:zipcode)",
              {
                  'first':first.get(),
                  'last':last.get(),
                  'address':address.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
              }
              )

    # Commit changes
    connect.commit()

    # close connection
    connect.close()


    first.delete(0,END)
    last.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
b1=Button(root,text="Add Record",borderwidth=5,command=submit)
b1.grid(row=6,column=1,ipadx=50,pady=10)

def display():

    # Create Database or connect
    connect = sqlite3.connect('AddressBook.db')

    # Create cursor
    c = connect.cursor()

    # Frame for Records
    global frame
    frame = LabelFrame(root)
    frame.grid(row=9, column=0, columnspan=2)

    #Display Data
    global record
    global rcrd
    c.execute('SELECT *, oid FROM addresses')
    record = c.fetchall()

    # loop through record
    for rcrd in record:


        lable = Label(frame,text= rcrd[0]+' '+rcrd[1]+'  '+rcrd[3]+'\t\t\t\t'+str(rcrd[6])+'\n')
        lable.pack()

    b2['state']=DISABLED
    b1['state']=DISABLED

    # Commit changes
    connect.commit()

    # close connection
    connect.close()

b2=Button(root,text="Display Records",borderwidth=5,command=display)
b2.grid(row=6,column=0,ipadx=50,pady=10)

def clr_display():
    frame.destroy()
    b2['state']= NORMAL
    b1['state']= NORMAL

Button(root,text="Clear Display",borderwidth=5,command=clr_display).grid(row=7,column=0,columnspan=2,ipadx=50,pady=10)



# DElETE Record
def dlt_msg():
    msg_ans=msg.askquestion('Delete',"Are you want to delete Some record?")
    if msg_ans == 'yes':
        # New window for deletion
        global top
        top = Toplevel()
        top.title('Delete Record')
        top.wm_iconbitmap('database.ico')
        Label(top, text="Credit : Mufaddal Shakir", bg='sky blue').grid(row=10, column=0, columnspan=2, ipadx=150)
        Label(top,text="ID Number").grid(row=0,column=0,padx=10)

        global ans_label
        ans_label=Label(top,text="")
        ans_label.grid(row=2,column=0,columnspan=2,padx=10)

        # dlt as Id/oid number for reference
        global dlt
        dlt = Entry(top, width=30, borderwidth=3)
        dlt.grid(row=0,column=1,padx=5)


        b3=Button(top,text="Delete",borderwidth=5,command=dlt_rcrd)
        b3.grid(row=1,columnspan=2,ipadx=20,pady=10)
    else:
        pass

def dlt_rcrd():
    # Create Database or connect
    connect = sqlite3.connect('AddressBook.db')

    # Create cursor
    c = connect.cursor()

    if dlt.get().isdigit():

            # Removing record
            c.execute('DELETE FROM addresses WHERE oid=' + dlt.get())

            ans_label.config(text="Record deleted successfully")
    else:
        ans_label.config(text="Invalid Syntax")


    # CLearing Entry
    dlt.delete(0,END)

    # Commit changes
    connect.commit()

    # close connection
    connect.close()


# Update Record
def edit_func():

    global top1
    # Creating New window for updates
    top1 = Toplevel()
    top1.title('Update Record')
    top1.wm_iconbitmap('database.ico')
    Label(top1, text="Credit : Mufaddal Shakir", bg='sky blue').grid(row=10, column=0, columnspan=2, ipadx=150)
    Label(top1, text="ID Number").grid(row=0, column=0, padx=10)

    # Taking edit as Id/oid number
    global edit
    edit = Entry(top1, width=30, borderwidth=3)
    edit.grid(row=0, column=1, padx=5)

    # Button for selecting id/oid
    b4 = Button(top1, text="Select", borderwidth=5,command=edit_rcrd)
    b4.grid(row=1, columnspan=2, ipadx=20, pady=10)


def edit_rcrd():

    # Initialising the labels
    Label(top1, text="First Name", fg='red').grid(row=2, column=0, padx=10,pady=20)
    Label(top1, text="Last Name", fg='red').grid(row=3, column=0)
    Label(top1, text="Address", fg='red').grid(row=4, column=0)
    Label(top1, text="City", fg='red').grid(row=5, column=0)
    Label(top1, text="State", fg='red').grid(row=6, column=0)
    Label(top1, text="Zipcode", fg='red').grid(row=7, column=0)

    # Define Global variable For Update
    global first_edit
    global last_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit

    # Initailising Entries
    first_edit = Entry(top1, width=30, borderwidth=3)
    last_edit = Entry(top1, width=30, borderwidth=3)
    address_edit = Entry(top1, width=30, borderwidth=3)
    city_edit = Entry(top1, width=30, borderwidth=3)
    state_edit = Entry(top1, width=30, borderwidth=3)
    zipcode_edit = Entry(top1, width=30, borderwidth=3)

    # Packing/Griding Entries
    first_edit.grid(row=2, column=1, padx=5,pady=20)
    last_edit.grid(row=3, column=1)
    address_edit.grid(row=4, column=1)
    city_edit.grid(row=5, column=1)
    state_edit.grid(row=6, column=1)
    zipcode_edit.grid(row=7, column=1)

    # Create Database or connect
    connect = sqlite3.connect('AddressBook.db')

    # Create cursor
    c = connect.cursor()

    # Update  Data
    c.execute('SELECT * FROM addresses WHERE oid='+edit.get())
    record = c.fetchall()

    # Traverse through previous data for particular oid
    for rcrd in record:
        first_edit.insert(0,rcrd[0])
        last_edit.insert(0,rcrd[1])
        address_edit.insert(0,rcrd[2])
        city_edit.insert(0,rcrd[3])
        state_edit.insert(0,rcrd[4])
        zipcode_edit.insert(0,rcrd[5])

    # Commit changes
    connect.commit()

    # close connection
    connect.close()


    Button(top1, text="Save", borderwidth=5, command=update_rcrd).grid(row=8, column=1, ipadx=50, pady=10)

def update_rcrd():

    # Create Database or connect
    connect = sqlite3.connect('AddressBook.db')

    # Create cursor
    c = connect.cursor()

    # Update Table
    c.execute(
        ''' UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        adress = :address,
        city = :city, 
        state = :state,
        zipcode = :zipcode
         
        WHERE oid = :oid''',
        {
            'first': first_edit.get(),
            'last': last_edit.get(),
            'address': address_edit.get(),
            'city': city_edit.get(),
            'state': state_edit.get(),
            'zipcode': zipcode_edit.get(),

            'oid':edit.get()
        }
    )

    # Commit changes
    connect.commit()

    # close connection
    connect.close()

    # Closing after update
    top1.destroy()


# Menu

menu = Menu(root)
filemenu = Menu(menu,tearoff=0)

filemenu.add_command(label='Delete Record',command = dlt_msg)
filemenu.add_separator()
filemenu.add_command(label="Edit record",command= edit_func)

menu.add_cascade(label='File Menu',menu=filemenu)
root.config(menu=menu)

Label(root,text="Credit : Mufaddal Shakir",bg='sky blue').grid(columnspan=2,ipadx=150)
root.mainloop()