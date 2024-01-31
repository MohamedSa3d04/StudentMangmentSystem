from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
root = Tk()


class Student :
    def __init__(self, root):
        #-------------Windows Mangment------------
        self.root = root
        self.root.geometry('1350x690+35+5')
        self.root.title('نظـام ادارة الطلاب')
        self.root.resizable(False,False)
        self.root.config(background='#A3E4D7')
        Head = Label(self.root,
        text='[نظـام ادارة الطلاب]',
        bg='green',
        font=('monospace',14),
        fg='white'
        )
        Head.pack(fill=X)

        #-------------variables--------------------
        self.Id_Var = StringVar()
        self.Name_Var = StringVar()
        self.Email_Var = StringVar()
        self.Phone_Var = StringVar()
        self.Ceritify_Var = StringVar()
        self.Address_Var = StringVar()
        self.Gender_Var = StringVar()
        self.Delete_Var = StringVar()
        self.Search_Var = StringVar()
        self.Search_About = StringVar()

        #-------------tools mangment---------------
        Mang_Frame =Frame(self.root, bg="white")
        Mang_Frame.place(x=1100,y=30,width=240,height=430)

        lbl_id = Label(Mang_Frame, text='Student ID', bg='white', font=(1))
        lbl_id.pack()
        txt_id = Entry(Mang_Frame, textvariable=self.Id_Var, bd=2, width=25, justify="center")
        txt_id.pack()

        lbl_name = Label(Mang_Frame, text='Student Name', bg='white', font=(1))
        lbl_name.pack()
        txt_name = Entry(Mang_Frame, textvariable=self.Name_Var, bd=2, width=25, justify="center")
        txt_name.pack()

        lbl_Email = Label(Mang_Frame, text='Student Email', bg='white', font=(1))
        lbl_Email.pack()
        txt_Email = Entry(Mang_Frame, textvariable=self.Email_Var, bd=2, width=25, justify="center")
        txt_Email.pack()

        lbl_Phone = Label(Mang_Frame, text='Student Phone', bg='white', font=(1))
        lbl_Phone.pack()
        txt_Phone = Entry(Mang_Frame, textvariable=self.Phone_Var, bd=2, width=25, justify="center")
        txt_Phone.pack()

        lbl_Certi = Label(Mang_Frame, text='Student Ceritfies', bg='white', font=(1))
        lbl_Certi.pack()
        txt_Certi = Entry(Mang_Frame, textvariable=self.Ceritify_Var, bd=2, width=25, justify="center")
        txt_Certi.pack()

        lbl_Address = Label(Mang_Frame, text='Student Address', bg='white', font=(1))
        lbl_Address.pack()
        txt_Address = Entry(Mang_Frame, textvariable=self.Address_Var, bd=2, width=25, justify="center")
        txt_Address.pack()
        
        lbl_Gender = Label(Mang_Frame, text='Gender', bg='white', font=(1))
        lbl_Gender.pack()
        gender = ttk.Combobox(Mang_Frame, textvariable=self.Gender_Var, state='readonly')
        gender['values'] = ('Male','Female')
        gender.pack()

        lbl_Delete = Label(Mang_Frame, text='Delete By Id', bg='white', fg="red", font=(1))
        lbl_Delete.pack()
        txt_Delete = Entry(Mang_Frame, textvariable=self.Delete_Var,  bd=2, width=25, justify="center")
        txt_Delete.pack()

        #---------Frame for button mangment------
        btnFrame = Frame(self.root, bg='white')
        btnFrame.place(x=1100,y=470,width=240,height=215)

        btn_Add = Button(btnFrame, text='Add Student', bg='#85929E', fg='white', font=1, command=self.Add_Student)
        btn_Add.place(x=43,y=25, width=150, height=30)

        btn_Del = Button(btnFrame, text='Delete Student', bg='#85929E', fg='white', font=1, command=self.Delete_STD)
        btn_Del.place(x=43,y=60, width=150, height=30)

        btn_Update = Button(btnFrame, text='Update Student', bg='#85929E', fg='white', font=1, command=self.Update_Data)
        btn_Update.place(x=43,y=95, width=150, height=30)

        btn_Clear = Button(btnFrame, text='Clear Fields', bg='#85929E', fg='white', font=1, command=self.Clear_Fields)
        btn_Clear.place(x=43,y=130, width=150, height=30)

        btn_Exit = Button(btnFrame, text='Exit Student', bg='red', fg='white', font=1, command=self.Exit_Program)
        btn_Exit.place(x=43,y=165, width=150, height=30)

        #---------Searching mangement---------
        search_Frame = Frame(self.root , bg="white")
        search_Frame.place(x=1, y=30, width=1134, height=50)

        lbl_search = Label(search_Frame, text='Search about student', bg='white', font=1)
        lbl_search.place(x=5,y=12)

        combo_search = ttk.Combobox(search_Frame, textvariable=self.Search_About)
        combo_search['values'] = ('Name', 'Id')
        combo_search.place(x=200, y=18)
        
        txt_Search = Entry(search_Frame, textvariable=self.Search_Var, bd=2, width=25, justify="center")
        txt_Search.place(x=350,y=18)

        btn_search = Button(search_Frame, text='search', bg='#A3E4D7', width=15, command=self.Searching)
        btn_search.place(x=530,y=15)
        
        #---------------Data_View table----------------------
        Data_Frame = Frame(root, bg='green')
        Data_Frame.place(x=5, y=85, width=1090, height=600)

        scroll_x = Scrollbar(Data_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Data_Frame, orient=VERTICAL)

        self.data_table = ttk.Treeview(Data_Frame,
                               columns=('Id', 'Name', 'Email', 'Phone', 'Ceritifies', 'Address', 'Gender'),
                               xscrollcommand=scroll_x.set,
                               yscrollcommand=scroll_y.set
                               )
        self.data_table.place(x=19, y=1, width=1070, height=580)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.data_table.xview)
        scroll_y.config(command=self.data_table.yview)

        self.data_table['show'] = 'headings'
        self.data_table.heading('Id', text='Student Id')
        self.data_table.heading('Name', text='Student Name')
        self.data_table.heading('Email', text='Student Email')
        self.data_table.heading('Phone', text='Student Phone')
        self.data_table.heading('Ceritifies', text='Student Ceritifies')
        self.data_table.heading('Address', text='Student Address')
        self.data_table.heading('Gender', text='Student Gender')
        
        self.data_table.column('Id', width=130, anchor="center")
        self.data_table.column('Name', width=60, anchor = "center")
        self.data_table.column('Email', width=130, anchor = "center")
        self.data_table.column('Phone', width=75, anchor = "center")
        self.data_table.column('Ceritifies', width=75, anchor = "center")
        self.data_table.column('Address', width=130, anchor = "center")
        self.data_table.column('Gender', width=40, anchor = "center")

        self.Fetch_All()
        self.data_table.bind('<ButtonRelease>',self.Fill_Fields)

    
    #--------Adding process----------
    def Add_Student(self): 
        try :
            if type(int(self.Id_Var.get())) != int or len(self.Id_Var.get()) == 0 or len(self.Name_Var.get()) == 0:
                raise Exception()
        

            con = pymysql.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'student'
            )
            cur = con.cursor()
            cur.execute('insert into student values (%s,%s,%s,%s,%s,%s,%s)',(self.Id_Var.get(), 
                                                                            self.Name_Var.get(),
                                                                            self.Email_Var.get(), 
                                                                        self.Phone_Var.get(),
                                                                        self.Ceritify_Var.get(),
                                                                            self.Address_Var.get(),
                                                                        self.Gender_Var.get()
            ))
            
            con.commit()
            self.Fetch_All()
            self.Clear_Fields()
            con.close()
        except:
            for item in self.data_table.get_children():
                if self.data_table.item(item, 'values')[0] == self.Id_Var.get() :
                    messagebox.showinfo("Message","The id is actually exist")  
                    
            raise Exception("Please enter correct values")
    #-------Fetching data to the table---------
    def Fetch_All(self):
        con = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'student'
        )
        cur = con.cursor()
        cur.execute('select * from student') #Select 
        rows = cur.fetchall() #Fetch
        if len(rows) != 0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows :
                self.data_table.insert('',END,value=row)
            con.commit()
        con.close()  

    #---------Delete specific student with name------
    def Delete_STD(self):
        con = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'student'
        )
        cur = con.cursor()
        cur.execute('delete from student where Id=%s',self.Delete_Var.get())
        con.commit()
        self.Fetch_All()
        con.close()   
    
    #---------Clear All Fields-------
    def Clear_Fields(self):
        self.Address_Var.set('')
        self.Name_Var.set('')
        self.Phone_Var.set('')
        self.Email_Var.set('')
        self.Id_Var.set('')
        self.Delete_Var.set('')
        self.Ceritify_Var.set('')
        self.Gender_Var.set('')

    #---------Fill the text fields with a specific data-------
    def Fill_Fields(self, ev):
        Row_Items = self.data_table.focus()
        Content_Row = self.data_table.item(Row_Items)
        Values = Content_Row['values']
        self.Address_Var.set(Values[5])
        self.Name_Var.set(Values[1])
        self.Phone_Var.set(Values[3])
        self.Email_Var.set(Values[2])
        self.Id_Var.set(Values[0])
        self.Ceritify_Var.set(Values[4])
        self.Gender_Var.set(Values[6])
        self.Delete_Var.set(Values[0])

    #---------Update student detail-----
    def Update_Data(self):
        con = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'student'
        )
        cur = con.cursor()
        cur.execute('Update student set  Name = %s,  Email = %s,  Phone = %s,  Critifies = %s,  Address = %s,  Gender = %s where Id = %s',
                                                                        (
                                                                        self.Name_Var.get(),
                                                                        self.Email_Var.get(), 
                                                                       self.Phone_Var.get(),
                                                                     self.Ceritify_Var.get(),
                                                                        self.Address_Var.get(),
                                                                       self.Gender_Var.get(),
                                                                       self.Id_Var.get()
        ))
        con.commit()
        self.Fetch_All()
        self.Clear_Fields()
        con.close()   

       #---------Search on value --------
    def Searching(self):#0id 1name 3phone
        value = self.Search_Var.get()
        counter = 0
        # Iterate through items in the Treeview
        for item in self.data_table.get_children(): #return me a tuble of tuble
            # Check if the value is in the first column of the item
            if self.Search_About.get() == "Id" :
                if self.data_table.item(item, "values")[0] == value:
                    #Hide other rows data
                    self.data_table.detach(*self.data_table.get_children())
                    self.data_table.insert('', END, value=self.data_table.item(item, "values"))  
                    # Set the focus to the item
                    self.data_table.focus(item)
                    #Fill the fiel with the data
                    self.Fill_Fields(None)
                    # Select the item to visually highlight it
                    self.data_table.selection_set(item)
                    counter += 1
                    break    
                
            elif self.Search_About.get() == 'Name':
                if self.data_table.item(item ,'values')[1] == value:
                    #Hide other rows data
                    self.data_table.detach(*self.data_table.get_children())
                    self.data_table.insert('', END, value=self.data_table.item(item, "values"))
                    # Set the focus to the item
                    self.data_table.focus(item)
                    # Select the item to visually highlight it
                    self.data_table.selection_set(item)
                    #Fill the fiel with the data
                    self.Fill_Fields(None)
                    counter += 1
                    
                
            else:
                messagebox.showerror("Error","Write an correct value")           
                break 
        if counter == 0 :
             messagebox.showinfo("Message","Isn't Exist")  
      

    #---------Exit the program-------     
    def Exit_Program(self):
        print("Maded By Eng/MohamedSaad \nWish helps you!")
        self.root.quit()
        self.root.destroy()

 
           
ob = Student(root)

root.mainloop()