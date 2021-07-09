from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as mysql


class ConnectorDB:

    def __init__(self, root):
        self.root = root
        self.root.title("Life Choices Database")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='green')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE, bg='black')
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE, bg='black')
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, relief=RIDGE, bg='green')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=100, padx=2, relief=RIDGE, bg='black')
        LeftFrame1.pack(side=TOP, padx=0, pady=0)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg='green')
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE, bg='black')
        RightFrame1a.pack(side=TOP)

        ##

        ID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()

        ## Functions

        def iExit():
            iExit = tkinter.messagebox.askyesno("Alert", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entID.delete(0, END)
            self.entFirstname.delete(0, END)
            self.entSurname.delete(0, END)
            self.entAddress.delete(0, END)
            self.cboGender.set("")
            self.entMobile.delete(0, END)

        def addData():
            if ID.get() == "" or Firstname.get() == "" or Surname.get() == "":
                tkinter.messagebox.showerror("Enter your details")
            else:
                sqlCon = mysql.connect(
                    host="sql4.freesqldatabase.com",
                    user="sql4423917",
                    password="akpfe8zmEA",
                    database="sql4423917"
                )
                cur = sqlCon.cursor()
                cur.execute("insert into sql4423917 values(%s,%s,%s,%s,%s,%s)", (
                    ID.get(),
                    Firstname.get(),
                    Surname.get(),
                    Address.get(),
                    Gender.get(),
                    Mobile.get(),
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        def DisplayData():
            sqlCon = mysql.connect(host="sql4.freesqldatabase.com", user="sql4423917", password="akpfe8zmEA",
                                   database="sql4423917")
            cur = sqlCon.cursor()
            cur.execute("select * from sql4423917")
            result = cur.fetchall()
            if len(result) != 0:
                self.records.delete(*self.records.get_children())
                for row in result:
                    self.records.insert('', END, values=row)
                sqlCon.commit()
                sqlCon.close()

        ## Labels

        self.lbltitle = Label(TitleFrame, font=('arial', 40, 'bold'), text="Life Choices", bd=7, bg='black', fg='white')
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.lblMember = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Member", bd=7, bg='black', fg='white')
        self.lblMember.grid(row=0, column=0, sticky=W, padx=5)
        self.cboMember = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=43, state='readonly')
        self.cboMember['values'] = (' ', 'Student', 'Staff', 'Visitor')
        self.cboMember.current(0)
        self.cboMember.grid(row=0, column=1)

        self.lblID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Identity(ID)", bd=7, bg='black', fg='white')
        self.lblID.grid(row=1, column=0, sticky=W, padx=5)
        self.entID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=ID)
        self.entID.grid(row=1, column=1, sticky=W, padx=5)

        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="First Name", bd=7, bg='black',
                                  fg='white')
        self.lblFirstname.grid(row=2, column=0, sticky=W, padx=5)
        self.entFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=Firstname)
        self.entFirstname.grid(row=2, column=1, sticky=W, padx=5)

        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Surname", bd=7, bg='black', fg='white')
        self.lblSurname.grid(row=3, column=0, sticky=W, padx=5)
        self.entSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                textvariable=Surname)
        self.entSurname.grid(row=3, column=1, sticky=W, padx=5)

        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Address", bd=7, bg='black', fg='white')
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5)
        self.entAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                textvariable=Address)
        self.entAddress.grid(row=4, column=1, sticky=W, padx=5)

        self.lblGender = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Gender", bd=7, bg='black', fg='white')
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=43, state='readonly',
                                      textvariable=Gender)
        self.cboGender['values'] = (' ', 'Male', 'Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Mobile", bd=7, bg='black', fg='white')
        self.lblMobile.grid(row=6, column=0, sticky=W, padx=5)
        self.entMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                               textvariable=Mobile)
        self.entMobile.grid(row=6, column=1, sticky=W, padx=5)

        ## Table with list of names

        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)

        self.records = ttk.Treeview(LeftFrame, height=12,
                                            column=("id", "firstname", "surname", "address", "gender", "mobile"),
                                            yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        self.records.heading("id", text="ID")
        self.records.heading("firstname", text="Firstname")
        self.records.heading("surname", text="Surname")
        self.records.heading("address", text="Address")
        self.records.heading("gender", text="Gender")
        self.records.heading("mobile", text="Mobile")

        self.records['show'] = 'headings'

        self.records.column("id", width=70)
        self.records.column("firstname", width=100)
        self.records.column("surname", width=100)
        self.records.column("address", width=100)
        self.records.column("gender", width=70)
        self.records.column("mobile", width=70)

        self.records.pack(fill=BOTH, expand=1)

        ## Buttons

        self.btnAddNew = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24,
                                width=8, height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=8, height=2, command=DisplayData)
        self.btnDisplay.grid(row=1, column=0, padx=1)
        # self.btnUpdate = Button(RightFrame1a, font=('arial',16,'bold'),text="Update",bd=4,pady=1,padx=24,width=8, height=2)
        # self.btnUpdate.grid(row=2, column=0, padx=1)
        self.btnDelete = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24, width=8,
                                height=2)
        self.btnDelete.grid(row=3, column=0, padx=1)
        # self.btnSearch = Button(RightFrame1a, font=('arial',16,'bold'),text="Search",bd=4,pady=1,padx=24,width=8, height=2)
        # self.btnSearch.grid(row=4, column=0, padx=1)
        self.btnReset = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24, width=8,
                               height=2, command=Reset)
        self.btnReset.grid(row=5, column=0, padx=1)
        self.btnExit = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8,
                              height=2, command=iExit)
        self.btnExit.grid(row=6, column=0, padx=1)


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()