from tkinter import *
root = Tk()
root.title('BRIEF-INFO-STORAGE')
root.iconbitmap('Screenshot (66).ico')
root.geometry('400x300')
root.resizable(False,False)
import sqlite3
import tkinter.messagebox as mb

#creating adatabase
conn = sqlite3.connect('personal_info.db')
#========creating a cursor
cur = conn.cursor()

#creating a table in a database

#cur.execute("""CREATE TABLE brief_personal_info( 
 #         initial_name text,
  #        middle_name text,
   #       last_name text,
    #      date_of_birth integer,
     #     place_of_birth text,
      #    residence text)""")
 

#labels for data to be entered
initial_name = Label(root, text="Initial Name")
middle_name=Label(root, text="Middle Name")
last_name = Label(root, text="Last Name")
date_of_birth = Label(root, text="Date of Birth")
place_of_birth = Label(root, text="Place of Birth")
residence = Label(root, text="Residence")
select = Label(root, text = "SELECT")

#Creating entry for fields
i_name = Entry(root, width=30)
m_name = Entry(root, width=30)
l_name = Entry(root, width=30)
d_birth = Entry(root, width=30)
p_birth = Entry(root, width=30)
reside = Entry(root, width=30)
sel = Entry(root, width=30)

#locating field labels
initial_name.grid(row=0, column=0,pady=(10,0))
middle_name.grid(row=1,column=0)
last_name.grid(row=2,column=0)
date_of_birth.grid(row=3,column=0)
place_of_birth.grid(row=4,column=0)
residence.grid(row=5, column=0)
select.grid(row=9,column=0)

#locating entry for fields
i_name.grid(row=0,column=1,pady=(10,0))
m_name.grid(row=1,column=1)
l_name.grid(row=2,column=1)
d_birth.grid(row=3,column=1)
p_birth.grid(row=4,column=1)
reside.grid(row=5,column=1)
sel.grid(row=9,column=1)

#creating a record selection label and positioning it
rec_sel = Label(root, text="RECORD SELECTION & OPTIONS")
rec_sel.grid(row=8, column=1)

#functions for buttons
def enter():
    #WRITE ENTERED CODE INTO DATABASE
    conn = sqlite3.connect('personal_info.db')
    #========creating a cursor
    cur = conn.cursor()

    #insert data into database
    cur.execute("INSERT INTO brief_personal_info VALUES(:i_name, :m_name, :l_name, :d_birth, :p_birth, :reside)",
             {
               'i_name': i_name.get(),
               'm_name': m_name.get(),
               'l_name': l_name.get(),
               'd_birth': d_birth.get(),
               'p_birth': p_birth.get(),
               'reside': reside.get()
            })

    

    #commiting changes
    conn.commit()

    #close connection
    conn.close()

    #clear text boxes
    i_name.delete(0,END)
    m_name.delete(0, END)
    l_name.delete(0,END)
    d_birth.delete(0,END)
    p_birth.delete(0, END)
    reside.delete(0,END)

def available():
    viewer = Tk()
    viewer.title("RECORD'S VIEWER")
    viewer.iconbitmap('Screenshot (66).ico')
    viewer.geometry('400x300')
    viewer.resizable(False,False)

    conn = sqlite3.connect('personal_info.db')
    #========creating a cursor
    cur = conn.cursor()
     
     #QUERY THE DATABASE
    cur.execute("SELECT *, oid FROM brief_personal_info")
    records=cur.fetchall()
    #print(records)
     
    print_records=''
    for record in records:
        print_records += str(record) + "\n" + "\n"

    query_label = Label(viewer, text=print_records)  
    query_label.grid(row=12, column=0, columnspan=2) 


    #commiting changes
    conn.commit()

    #close connection
    conn.close()

#function to update info
def update(): 
  conn = sqlite3.connect('personal_info.db')
  #create cursor
  cur = conn.cursor()

  record_id = sel.get()

  cur.execute("""UPDATE brief_personal_info SET
          initial_name = :iname,
          middle_name = :mname,
          last_name = :lname,
          date_of_birth = :dbirth,
          place_of_birth = :pbirth,
          residence = :reside

          WHERE oid = :oid""",
          {
          'iname': i_name.get(),
          'mname':m_name.get(),
          'lname':l_name.get(),
          'dbirth':d_birth.get(),
          'pbirth':p_birth.get(),
          'reside':reside.get(),
          'oid': record_id
          })
          
  #commit changes
  conn.commit()
  #close connection
  conn.close() 

  editor.destroy()


#function to edit info
def edit():
  global editor
  editor = Tk()
  editor.title('RECORD-UPDATE')
  editor.iconbitmap('Screenshot (66).ico')
  editor.geometry('400x200')
  editor.resizable(False,False)
  
  conn = sqlite3.connect('personal_info.db')
  #========creating a cursor
  cur = conn.cursor()
 

  record_id = sel.get()
  #QUERY THE DATABASE
  cur.execute("SELECT * FROM brief_personal_info WHERE oid = " + record_id)
  records=cur.fetchall()

  #create global variables
  global i_name
  global l_name
  global m_name
  global d_birth
  global p_birth
  global reside

  #labels for data to be entered
  initial_name = Label(editor, text="Initial Name")
  middle_name=Label(editor, text="Middle Name")
  last_name = Label(editor, text="Last Name")
  date_of_birth = Label(editor, text="Date of Birth")
  place_of_birth = Label(editor, text="Place of Birth")
  residence = Label(editor, text="Residence")
  
  #Creating entry for fields
  i_name = Entry(editor, width=30)
  m_name = Entry(editor, width=30)
  l_name = Entry(editor, width=30)
  d_birth = Entry(editor, width=30)
  p_birth = Entry(editor, width=30)
  reside = Entry(editor, width=30)
  
  #locating field labels
  initial_name.grid(row=0, column=0,pady=(10,0))
  middle_name.grid(row=1,column=0)
  last_name.grid(row=2,column=0)
  date_of_birth.grid(row=3,column=0)
  place_of_birth.grid(row=4,column=0)
  residence.grid(row=5, column=0)
  
  #locating entry for fields
  i_name.grid(row=0,column=1,pady=(10,0))
  m_name.grid(row=1,column=1)
  l_name.grid(row=2,column=1)
  d_birth.grid(row=3,column=1)
  p_birth.grid(row=4,column=1)
  reside.grid(row=5,column=1)

  #loop through
  for record in records:
    i_name.insert(0, record[0])
    l_name.insert(0, record[1])
    m_name.insert(0, record[2])
    d_birth.insert(0, record[3])
    p_birth.insert(0, record[4])
    reside.insert(0, record[5])

  save_btn = Button(editor, text="SAVE",command=update)
  save_btn.grid(row=6,column=1,columnspan=2, pady=10,ipadx=80)


def delete():
    conn = sqlite3.connect('personal_info.db')
    #========creating a cursor
    cur = conn.cursor()

    #delete record
    cur.execute("DELETE from brief_personal_info WHERE oid = " + sel.get())

    sel.delete(0,END)

    #erase content in select box
    #selectid = sel.get()
    #selectid.delete(0,END) 

    #commiting changes
    conn.commit()

    #close connection
    conn.close()

#function to enter password before viewing the contents in a database 
def password():
    passw = Tk()
    passw.title('Password')    
    passw.iconbitmap('Screenshot (66).ico')
    passw.geometry('250x50')
    passw.resizable(False,False)
    import tkinter.messagebox as mb

    #Global variable
    global passw_e

    passw_label = Label(passw, text="Password:")
    passw_label.grid(row=0, column=0,pady=(10,0))

    passw_e = Entry(passw, width=30, show="#")
    passw_e.grid(row=0,column=1,pady=(10,0))

    def click_enter():
        #global passw
        global passw_e
        word = "caren"
        if passw_e.get() == word:
            available()
            passw.destroy()
        else:
            mb.showinfo("Invalid", "Invalid password!!")


    enter_btn = Button(passw, text="enter", command= click_enter )
    enter_btn.grid(row=1, column=1)

#Buttons creation
enter_btn =  Button(root, text="Enter Record", command=enter)
available_btn =Button(root, text="Available Records",command=password)
delete_btn = Button(root,text="Delete",command=delete )
update_btn = Button(root, text="Update",command=edit)

#locating buttons
enter_btn.grid(row=6, column=3)
available_btn.grid(row=7, column=0)
delete_btn.grid(row=10,column=3)
update_btn.grid(row=9,column=3)

#commiting changes
conn.commit()

#close connection
conn.close()
mainloop()

 
 


