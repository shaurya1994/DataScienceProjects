from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import datetime

# import pymysql
import mysql.connector as sql_connector


class LibraryManagementSystem:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1550x800+0+0') # x, y=0

        # =================== Data Variables ===================
        self.prnno_var = StringVar()
        self.memberid_var = StringVar()
        self.membertype_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.phone_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrow_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latefine_var = StringVar()
        self.finalprice_var = StringVar()
        self.selected_book = StringVar()

        # =================== Main Title =================== 
        labelTitle = Label(
            self.root, 
            text='Library Management System', 
            bg='powder blue', 
            fg='green',
            bd=20,
            relief=RIDGE,
            font=('times new roman', 50, 'bold'),
            padx=2,
            pady=6,
        ) 
        labelTitle.pack(side=TOP, fill=X)

        # Ṃain Frame
        input_frame = Frame(
            self.root, 
            bd=12, 
            relief=RIDGE, 
            padx=20, 
            bg='powder blue'
        )
        input_frame.place(x=0, y=130, width=1535, height=335)


        # =================== DataFrame Left ===================
        dataFrameLeft = LabelFrame(
            input_frame, 
            bg='powder blue', 
            text='Library Membership Information', 
            font=('times new roman', 20, 'bold'),
            fg='green',
            bd=12,
            relief=RIDGE
        )
        dataFrameLeft.place(x=0, y=5, width=900, height=290)

        # PRN Number
        labelPRN_No = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='PRN No:', 
            font=('times new roman', 16, 'bold'),
            padx=2,
            pady=6
        )
        labelPRN_No.grid(row=1, column=0, sticky=W)
            
        textPRN_No = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.prnno_var,
        width=26)
        textPRN_No.grid(row=1, column=1)

        # Member ID
        label_ID_No = Label(
            dataFrameLeft, 
            bg='powder blue', 
            # text='ID No:', 
            text='Member ID:', 
            font=('times new roman', 16, 'bold'),
            padx=2,
            pady=6
        )
        label_ID_No.grid(row=2, column=0, sticky=W)

        text_ID_No = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.memberid_var,
        width=26)
        text_ID_No.grid(row=2, column=1)

        # Member type
        labelMember = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Member Type:', 
            font=('times new roman', 16, 'bold'),
            padx=2,
            pady=6
        )
        labelMember.grid(row=0, column=0, sticky=W)

        comboMember = ttk.Combobox(
            dataFrameLeft,
            width=24,
            textvariable=self.membertype_var,
            font=('times new roman', 14, 'bold'),
            state='readonly'
        )
        comboMember['value'] = ('Admin Staff', 'Student', 'Lecturer')
        comboMember.current(0)
        comboMember.grid(row=0, column=1)

        # Member First Name
        label_frst_nme = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='First Name:',
            font=('times new roman', 16, 'bold'),
            padx=2,
            pady=6
        )
        label_frst_nme.grid(row=3, column=0, sticky=W)

        text_frst_nme = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.firstname_var, 
        width=26)
        text_frst_nme.grid(row=3, column=1)

        # Member Last Name
        label_lst_nme = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Last Name:',
            font=('times new roman', 16, 'bold'),
            padx=2,
            pady=6
        )
        label_lst_nme.grid(row=4, column=0, sticky=W)

        text_lst_nme = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.lastname_var,
        width=26)
        text_lst_nme.grid(row=4, column=1)

        # Phone 
        label_phone = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Phone:',
            font=('times new roman', 16, 'bold'),
            padx=2,
            pady=6
        )
        label_phone.grid(row=5, column=0, sticky=W)

        text_phone = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.phone_var,
        width=26)
        text_phone.grid(row=5, column=1)  

        # Book ID 
        label_book_id = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Book ID:', 
            font=('times new roman', 16, 'bold'),
            padx=20,
            pady=6
        )
        label_book_id.grid(row=0, column=3, sticky=W)

        text_book_id = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.bookid_var,
        width=26)
        text_book_id.grid(row=0, column=4)

        # Book Title 
        label_book_title = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Book Title:', 
            font=('times new roman', 16, 'bold'),
            padx=20,
            pady=6
        )
        label_book_title.grid(row=1, column=3, sticky=W)

        text_book_title = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.booktitle_var,
        width=26)
        text_book_title.grid(row=1, column=4)     

        # Author Name 
        label_author = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Author:', 
            font=('times new roman', 16, 'bold'),
            padx=20,
            pady=6
        )
        label_author.grid(row=2, column=3, sticky=W)

        text_author = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.author_var,
        width=26)
        text_author.grid(row=2, column=4)       

        # Date Borrowed 
        label_borrow_dte = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Date Borrowed:',
            font=('times new roman', 16, 'bold'),
            padx=20,
            pady=6
        )
        label_borrow_dte.grid(row=3, column=3, sticky=W)

        text_borrow_dte = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.dateborrow_var,
        width=26)
        text_borrow_dte.grid(row=3, column=4)      

        # Date Due 
        label_due_dte = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Date Due:', 
            font=('times new roman', 16, 'bold'),
            padx=20,
            pady=6
        )
        label_due_dte.grid(row=4, column=3, sticky=W)

        text_due_dte = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.datedue_var,
        width=26)
        text_due_dte.grid(row=4, column=4)   

        # Late fine 
        label_late_fine = Label(
            dataFrameLeft, 
            bg='powder blue', 
            text='Late Return fine:', 
            font=('times new roman', 16, 'bold'),
            padx=20,
            pady=6
        )
        label_late_fine.grid(row=5, column=3, sticky=W)

        text_late_fine = Entry(dataFrameLeft, font=('times new roman', 15, 'bold'), 
        textvariable=self.latefine_var,
        width=26)
        text_late_fine.grid(row=5, column=4)        


        # =================== DataFrame Right ===================
        dataFrameRight = LabelFrame(
            input_frame, 
            text='Book Details', 
            bg='powder blue', 
            fg='green',
            bd=12,
            relief=RIDGE,
            font=('times new roman', 20, 'bold')
        )
        dataFrameRight.place(x=910, y=5, width=564, height=290)

        # Text box for book information
        self.txtBox = Text(dataFrameRight, font=('arial', 12, 'bold'), width=35, height=12, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        # List Scroll
        listScrollBar = Scrollbar(dataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky='ns')

        # List of books
        books_list = ['Head First Python', 'Learn Python the Hard Way', 'Python Programming', 'Python Secrets', 'Python Cookbook', 'Intro to ML'
        , 'Machine Techno', 'My Python', 'Wudang Python', 'The Algorithm', 'Shaolin Python', 'Joss Ellif Guru', 'Elite Jungle Python', 'Machine Python', 'Advance Python',
        'RedChilli Python', 'Python Dojo', 'Head First Python', 'Learn Python the Hard Way', 'Python Programming', 'Python Secrets', 'Python Cookbook', 'Intro to ML'
        , 'Machine Techno', 'My Python', 'Wudang Python', 'The Algorithm', 'Shaolin Python', 'Joss Ellif Guru', 'Elite Jungle Python', 'Machine Python', 'Advance Python',
        'RedChilli Python', 'Python Dojo', 'Head First Python', 'Learn Python the Hard Way', 'Python Programming', 'Python Secrets', 'Python Cookbook', 'Intro to ML'
        , 'Machine Techno', 'My Python', 'Wudang Python', 'The Algorithm', 'Shaolin Python', 'Joss Ellif Guru', 'Elite Jungle Python', 'Machine Python', 'Advance Python',
        'RedChilli Python', 'Python Dojo']


        # Function to select book from list (passing default parameter as '')
        def getBookInfo(event=''):

            # Selection cursor *Important
            if books_listBox.curselection() != ():
                self.selected_book = str(books_listBox.get(books_listBox.curselection()))
            else:
                return self.selected_book

            # Get data from API here (Hard coded for now)
            if (self.selected_book == 'Head First Python'):
                # Datetime variables
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15) 
                d3 = d1 + d2

                self.bookid_var.set('BKID0123')
                # self.booktitle_var.set('Head First Python')
                self.author_var.set('Paul Berry')
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.latefine_var.set('Rs 420')

            elif (self.selected_book == 'Wudang Python'):
                # Datetime variables
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20) 
                d3 = d1 + d2

                self.bookid_var.set('BKID0042')
                # self.booktitle_var.set(self.selected_book)
                self.author_var.set('100 Eyes')
                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.latefine_var.set('Rs 0')
            
            # Temp assignment
            self.booktitle_var.set(self.selected_book)


        # Listbox to display list of books
        books_listBox = Listbox(dataFrameRight, font=('arial', 12, 'bold'), width=21, height=12)
        books_listBox.bind('<<ListboxSelect>>', getBookInfo)
        books_listBox.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=books_listBox.yview)    

        # To generate the books list
        for book in books_list:
            books_listBox.insert(END, book)


        # =================== Buttons Frame ===================
        frameButton = Frame(self.root, bd=12, relief='ridge', padx=21, pady=1, bg='powder blue')
        frameButton.place(x=0, y=465, width=1535, height=70)

        # Add Data
        btnAddData = Button(
            frameButton, 
            text='Add Data', 
            command=self.insert_data,
            font=('arial', 12, 'bold'), 
            width=23, pady=4, 
            border=3, bg='blue', 
            fg='white'
        )
        btnAddData.grid(row=0, column=0)

        # Show Data
        btnShowData = Button(
            frameButton, 
            text='Show Data', 
            # command=self.fetch_data,
            command=self.show_data,
            font=('arial', 12, 'bold'), 
            width=24, pady=4, 
            border=3, bg='blue', 
            fg='white'
        )
        btnShowData.grid(row=0, column=1)

        # Update Data
        btnUpdateData = Button(
            frameButton, 
            text='Update Data', 
            command=self.update_data,
            font=('arial', 12, 'bold'), 
            width=23, pady=4, 
            border=3, bg='blue', 
            fg='white'
        )
        btnUpdateData.grid(row=0, column=2)

        # Delete Data
        btnDeleteData = Button(
            frameButton, 
            text='Delete',
            # command=self.var_check, 
            command=self.delete_data, 
            font=('arial', 12, 'bold'), 
            width=23, pady=4, 
            border=3, bg='blue', 
            fg='white'
        )
        btnDeleteData.grid(row=0, column=3)

        # Reset Data
        btnReset = Button(
            frameButton, 
            text='Reset', 
            command=self.reset_data,
            font=('arial', 12, 'bold'), 
            width=23, pady=4, 
            border=3, bg='blue', 
            fg='white'
        )
        btnReset.grid(row=0, column=4)

        # Exit Button
        btnExit = Button(
            frameButton, 
            text='Exit', 
            command=self.exit_program,
            font=('arial', 12, 'bold'), 
            width=23, pady=4, 
            border=3, bg='blue', 
            fg='white'
        )
        btnExit.grid(row=0, column=5)


        # ================= Information Frame =================
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        frameDetails.place(x=0, y=535, width=1535, height=255)

        # Scroll bar
        xscroll = ttk.Scrollbar(frameDetails, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(frameDetails, orient=VERTICAL)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        # Main Table
        self.library_table = ttk.Treeview(frameDetails, column=(
            'prnno', 'memberid', 'membertype', 'firstname', 'lastname',
            'phone', 'bookid', 'booktitle', 'author', 'dateborrow', 'datedue', 'latefine'),
            xscrollcommand=xscroll.set, yscrollcommand=yscroll.set    
        )
        # Assigning scroll bar
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        # Column headers
        self.library_table.heading('prnno', text='PRN No.')
        self.library_table.heading('memberid', text='Member ID') 
        self.library_table.heading('membertype', text='Member Type')
        self.library_table.heading('firstname', text='First Name')
        self.library_table.heading('lastname', text='Last Name')
        self.library_table.heading('phone', text='Member Phone')
        self.library_table.heading('bookid', text='Book ID')
        self.library_table.heading('booktitle', text='Book Title')
        self.library_table.heading('author', text='Book Author')
        self.library_table.heading('dateborrow', text='Borrowing Date')
        self.library_table.heading('datedue', text='Due Date')
        self.library_table.heading('latefine', text='Late Fee')

        # To show table
        self.library_table['show'] = 'headings'
        self.library_table.pack(fill=BOTH, expand=1)
        
        self.library_table.column('membertype', width=100)
        self.library_table.column('prnno', width=100)
        self.library_table.column('memberid', width=100)
        self.library_table.column('firstname', width=100)
        self.library_table.column('lastname', width=100)
        self.library_table.column('phone', width=100)
        self.library_table.column('bookid', width=100)
        self.library_table.column('booktitle', width=100)
        self.library_table.column('author', width=100)
        self.library_table.column('dateborrow', width=100)
        self.library_table.column('datedue', width=100)
        self.library_table.column('latefine', width=100)

        # To fetch data if inserted
        self.fetch_data()

        # Filling data in table
        self.library_table.bind('<ButtonRelease-1>', self.get_table_row) # Check different types of binds


    # For selecting data on-click *Important
    def get_cursor(self):
        cursor_row = self.library_table.focus() 
        content = self.library_table.item(cursor_row)
        row = content['values']
        if row:
            return row


    # Important function (Used to fill input fields upon click on library_table row) 
    def get_table_row(self, event=''):

        table_row = self.get_cursor()

        if table_row: 
            self.prnno_var.set(table_row[0])
            self.memberid_var.set(table_row[1])
            self.membertype_var.set(table_row[2])
            self.firstname_var.set(table_row[3])
            self.lastname_var.set(table_row[4])
            self.phone_var.set(table_row[5])
            self.bookid_var.set(table_row[6])
            self.booktitle_var.set(table_row[7])
            self.author_var.set(table_row[8])
            self.dateborrow_var.set(table_row[9])
            self.datedue_var.set(table_row[10])
            self.latefine_var.set(table_row[11])
        else:
            messagebox.showerror('Error', 'Please click on a row to select member')


    # Check for values in variables (Not in video)
    def var_check(self):
        if self.prnno_var.get()=='' or self.memberid_var.get()=='' or self.membertype_var.get()=='' or self.firstname_var.get()=='' or \
            self.lastname_var.get()=='' or self.phone_var.get()=='' or self.bookid_var.get()=='' or self.booktitle_var.get()=='' or \
            self.author_var.get()=='' or self.dateborrow_var.get()=='' or self.datedue_var.get()=='' or self.latefine_var.get()=='':
            return False
        else: 
            return True


    # Creating MySQL connection object 
    def connection_obj(self):
        conn_obj = sql_connector.connect(
            host='127.0.0.1', 
            port='3306', 
            user='root', 
            password='123456', 
            database='python_test',
            auth_plugin='mysql_native_password') 
        return conn_obj


    # ================= Query Operations =================

    # Fetch existing data
    def fetch_data(self):

        # Had to use pymysql because fetchall() in mysql.connector was not working
        # connection = pymysql.connect(
        #     host='127.0.0.1', 
        #     user='root', 
        #     password='123456', 
        #     db='python_test')

        connection = self.connection_obj()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM library')
        rows = cursor.fetchall()

        # Filling the table with the rows returned from query
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children()) # Understand *self.library_table.get_children()
            for i in rows:
                self.library_table.insert('', END, values=i)
            # connection.commit()
            connection.close()

    # Insert new data
    def insert_data(self):

        if self.var_check():
            connection = self.connection_obj()
            cursor = connection.cursor()
            
            # Order of variables is very important 
            cursor.execute('INSERT INTO library VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
            (self.prnno_var.get(), self.memberid_var.get(), self.membertype_var.get(), self.firstname_var.get(),
            self.lastname_var.get(), self.phone_var.get(), self.bookid_var.get(), self.booktitle_var.get(),
            self.author_var.get(), self.dateborrow_var.get(), self.datedue_var.get(), self.latefine_var.get()))

            connection.commit()
            connection.close()
            self.fetch_data()

            messagebox.showinfo('Success', 'Data inserted successfully')
        else:
            messagebox.showerror('Error', 'Please enter all the fields')

    # Update existing data  (Solve .get() removing leading 0's issue)
    def update_data(self):
    
        if self.var_check():
            connection = self.connection_obj()
            cursor = connection.cursor()

            cursor.execute("""UPDATE library SET memberid='{}', membertype='{}', firstname='{}', lastname='{}', 
                            phone='{}', bookid='{}', booktitle='{}', author='{}', dateborrow='{}', datedue='{}', 
                            latefine='{}' WHERE prnno='{}'""".format(self.memberid_var.get(), self.membertype_var.get(), 
                            self.firstname_var.get(),self.lastname_var.get(), self.phone_var.get(), self.bookid_var.get(), 
                            self.booktitle_var.get(), self.author_var.get(), self.dateborrow_var.get(), self.datedue_var.get(), 
                            self.latefine_var.get(), self.prnno_var.get()))
            
            connection.commit()
            connection.close()
            self.fetch_data()
            self.reset_data()

            messagebox.showinfo('Success', 'Data updated successfully')
        else:
            messagebox.showerror('Error', 'Please select a member to update')  


    # To delete a row
    def delete_data(self):
            
        if self.var_check():
            connection = self.connection_obj()
            cursor = connection.cursor()        
        
            query = 'DELETE FROM library WHERE prnno = %s'
            value = self.prnno_var.get()
            cursor.execute(query % value)

            connection.commit()
            connection.close()

            self.reset_data()
            self.fetch_data()

            messagebox.showinfo('Success', 'Data deleted successfully')
        else:
            messagebox.showerror('Error', 'Please select a member')

    # ================= Non-Query Button Operations =================

    # To show all the details 
    def show_data(self):
        table_row = self.get_cursor()

        if table_row:
            # Initially used this to fill data but it takes data from the text fields and not from DB 
            # self.txtBox.insert(END, 'Member Type:\t\t' + self.membertype_var.get() + '\n')
            # self.txtBox.insert(END, 'PRN No:\t\t' + self.prnno_var.get() + '\n')
            
            self.txtBox.delete('1.0', 'end')
            self.txtBox.insert(END, 'Member Type:\t\t' + table_row[2] + '\n')
            self.txtBox.insert(END, 'PRN No:\t\t' + str(table_row[0]) + '\n')
            self.txtBox.insert(END, 'Member ID:\t\t' + str(table_row[1]) + '\n')
            self.txtBox.insert(END, 'First Name: \t\t' + table_row[3] + '\n')
            self.txtBox.insert(END, 'Last Name:\t\t' + table_row[4] + '\n')
            self.txtBox.insert(END, 'Phone:\t\t' + str(table_row[5]) + '\n')
            self.txtBox.insert(END, 'Book ID:\t\t' + table_row[6] + '\n')
            self.txtBox.insert(END, 'Book Title:\t\t' + table_row[7] + '\n')
            self.txtBox.insert(END, 'Author:\t\t' + table_row[8] + '\n')
            self.txtBox.insert(END, 'Date Issued\t\t' + table_row[9] + '\n')
            self.txtBox.insert(END, 'Date Due\t\t' + table_row[10] + '\n')
            self.txtBox.insert(END, 'Late Fine\t\t' + str(table_row[11]) + '\n')
        else:
            messagebox.showerror('Error', 'Please select a member')


    # To reset variable entries
    def reset_data(self):
        
        self.prnno_var.set('')
        self.memberid_var.set('')
        self.membertype_var.set('')
        self.firstname_var.set('')
        self.lastname_var.set('')
        self.phone_var.set('')
        self.bookid_var.set('')
        self.booktitle_var.set('')
        self.author_var.set('')
        self.dateborrow_var.set('')
        self.datedue_var.set('')
        self.latefine_var.set('')
        self.txtBox.delete('1.0', END)  


    # To exit application
    def exit_program(self):

        exit_pr = messagebox.askyesno('Library Management System', 'Exit Application ?')
        if exit_pr == 1:
            self.root.destroy()
            return   


if __name__ == '__main__':
    root = Tk()
    winObj = LibraryManagementSystem(root)
    root.mainloop() # To keep the window running