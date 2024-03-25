from tkinter import *
import time
from tkinter import ttk,messagebox
import pymysql



#functionallity part

def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)




def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or email =%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)




    search_window=Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False,False)
    idLabel=Label(search_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15,sticky=W)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button=ttk.Button(search_window,text='Search',command=search_data)
    search_student_button.grid(row=7,columnspan=2,pady=15)

def add_student():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All Feilds are required',parent=add_window)


        else:
            currentdate = time.strftime('%d/%m/%Y')
            currenttime = time.strftime('%H:%M:%S')
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                                        genderEntry.get(),dobEntry.get(),currentdate,currenttime))
                con.commit()
                result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=add_window)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
                return



            query= 'select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('',END,values=data)


    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)
    idLabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15,sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)


#connect to database dialog box/page
def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host=hostentry.get(), user=usernameentry.get(), password=passwordentry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key, name varchar(30),mobile  varchar(10),email varchar(30),' \
                  'address varchar(50),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is sucessful', parent=connectWindow)
        connectWindow.destroy()

        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+770+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnamelabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnamelabel.grid(row=0,column=0,padx=20)

    hostentry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=40,pady=20)

    usernamelabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernamelabel.grid(row=1, column=0, padx=20)

    usernameentry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameentry.grid(row=1, column=1, padx=40, pady=20)

    passwordlabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordlabel.grid(row=2, column=0, padx=20)

    passwordentry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordentry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(300,slider)



def clock():
    date= time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)

#gui part
root= Tk()

root.wm_geometry('1174x680+0+0')
root.wm_resizable(0,0)
root.title('Student Management System')

datetimeLabel=Label(root,text='hello',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s='Student Management System'
sliderlabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderlabel.place(x=200,y=0)
slider()

#here i added connect database command
connectButton=Button(root,text='Connect Database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student (1).png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton=Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=Button(leftFrame,text='Update Student',width=25,state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=Button(leftFrame,text='Export Student',width=25,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=Button(leftFrame,text='Exit',width=25)
exitButton.grid(row=7,column=0,pady=20)

#Right side frame

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX= Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY= Scrollbar(rightFrame,orient=VERTICAL )

#created tree view... :)
studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile No','Email','Address','Gender',
                                 'D.O.B','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')





studentTable.config(show='headings')


root.mainloop()
