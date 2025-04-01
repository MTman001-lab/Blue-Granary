import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management")
        self.root.geometry("1400x650+0+0")
        self.mainLabel = tk.Label(self.root, bd=5, relief="groove", text="Employee Management System", font=("Arial", 40, "bold"), bg="pink", fg="black")
        self.mainLabel.pack(side=tk.TOP, fill="x")

        # ----Variables----
        self.eid = tk.IntVar()
        self.ename = tk.StringVar()
        self.edesig = tk.StringVar()
        self.esal = tk.IntVar()
        self.egender = tk.StringVar()
        self.searchType= tk.StringVar()
        self.searchin= tk.StringVar()

        # ----Frame1----
        self.fram1 = tk.Frame(self.root, width=350, height=550, bg="grey")
        self.fram1.place(x=10, y=80, width=350, height=550)

        self.idLabel = tk.Label(self.fram1, padx=5, text="Employee's ID:", bg="grey", fg="white", font=("Arial", 14, "bold"), pady=10)
        self.idLabel.grid(row=0, column=0)
        self.idIn = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.eid)
        self.idIn.grid(row=0, column=1, pady=10)

        self.nameLabel = tk.Label(self.fram1, padx=5, text="Employee's Name:", bg="grey", fg="white", font=("Arial", 14, "bold"), pady=10)
        self.nameLabel.grid(row=1, column=0)
        self.nameIn = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.ename)
        self.nameIn.grid(row=1, column=1, pady=10)

        self.desigLabel = tk.Label(self.fram1, padx=5, text="Designation:", bg="grey", fg="white", font=("Arial", 14, "bold"), pady=10)
        self.desigLabel.grid(row=2, column=0)
        self.desigIn = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.edesig)
        self.desigIn.grid(row=2, column=1, pady=10)

        self.salLabel = tk.Label(self.fram1, padx=5, text="Employee's Salary:", bg="grey", fg="white", font=("Arial", 14, "bold"), pady=10)
        self.salLabel.grid(row=3, column=0)
        self.salIn = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.esal)
        self.salIn.grid(row=3, column=1, pady=10)

        self.genLabel = tk.Label(self.fram1, padx=5, text="Employee's Gender:", bg="grey", fg="white", font=("Arial", 14, "bold"), pady=10)
        self.genLabel.grid(row=4, column=0)
        self.genIn = ttk.Combobox(self.fram1, font=("Arial", 14), width=13, state="readonly", textvariable=self.egender)
        self.genIn['values'] = ("male", "female")
        self.genIn.grid(row=4, column=1, pady=10)

        self.addrLabel = tk.Label(self.fram1, padx=5, text="Employee's Address:", bg="grey", fg="white", font=("Arial", 14, "bold"), pady=10)
        self.addrLabel.grid(row=5, column=0)
        self.addrIn = tk.Text(self.fram1, width=15, height=3, font=("Arial", 14), pady=10)
        self.addrIn.grid(row=5, column=1, pady=10)

        # ----Button Frame---
        self.btnframe = tk.Frame(self.fram1, width=370, height=150, bg="indigo", bd=5, relief="raised")
        self.btnframe.place(x=10, y=380)

        self.addbtn = tk.Button(self.btnframe, text="Add", width=10, font=("Arial", 14, "bold"), command=self.add)
        self.addbtn.grid(row=0, column=0, padx=20, pady=20)

        self.updatebtn = tk.Button(self.btnframe, text="Update",command=self.Update, width=10, font=("Arial", 14, "bold"))
        self.updatebtn.grid(row=0, column=1, padx=20, pady=10)

        self.delbtn = tk.Button(self.btnframe, text="Delete",command=self.remove, width=10, font=("Arial", 14, "bold"))
        self.delbtn.grid(row=1, column=0, padx=20, pady=10)

        self.clearbtn = tk.Button(self.btnframe, text="Clear", width=10, font=("Arial", 14, "bold"), command=self.clear)
        self.clearbtn.grid(row=1, column=1, padx=20, pady=10)

        # ----Frame2----
        self.fram2 = tk.Frame(self.root, bg="grey", bd=5, relief="ridge")
        self.fram2.place(x=400, y=80, width=870, height=550)

        self.searchLabel = tk.Label(self.fram2, padx=5, text="Search By", bg="grey", fg="white", font=("Arial", 14, "bold"), pady=10)
        self.searchLabel.grid(row=0, column=0)
        self.searchType = ttk.Combobox(self.fram2,textvariable=self.searchType, font=("Arial", 14), width=13, state="readonly")
        self.searchType['values'] = ("ID", "Name")
        self.searchType.grid(row=0, column=1, pady=10)

        self.searchin = tk.Entry(self.fram2, font=("Arial", 14), width=15,textvariable=self.searchin)
        self.searchin.grid(row=0, column=2, pady=10, padx=10)

        self.searchbtn = tk.Button(self.fram2,command=self.search, text="Search", width=10, font=("Arial", 14))
        self.searchbtn.grid(row=0, column=3, padx=5, pady=10)

        self.showbtn = tk.Button(self.fram2,command=self.show_all, text="Display All", width=10, font=("Arial", 14))
        self.showbtn.grid(row=0, column=4, padx=5, pady=10)

        # ----Table Frame---
        self.tabframe = tk.Frame(self.fram2, bg="pink", bd=5, relief="ridge")
        self.tabframe.place(x=10, y=80, width=840, height=450)

        self.x_scrl = tk.Scrollbar(self.tabframe, orient="horizontal")
        self.x_scrl.pack(side=tk.BOTTOM, fill="x")

        self.y_scrl = tk.Scrollbar(self.tabframe, orient="vertical")
        self.y_scrl.pack(side=tk.RIGHT, fill="y")

        self.table = ttk.Treeview(self.tabframe, columns=("id", "name", "desig", "sal", "gender", "addr"),
                                  xscrollcommand=self.x_scrl.set, yscrollcommand=self.y_scrl.set)
        self.x_scrl.config(command=self.table.xview)
        self.y_scrl.config(command=self.table.yview)

        self.table.heading("id", text="Emp_ID")
        self.table.heading("name", text="Emp_Name")
        self.table.heading("desig", text="Designation")
        self.table.heading("sal", text="Emp_Salary")
        self.table.heading("gender", text="Emp_Gender")
        self.table.heading("addr", text="Emp_Address")
        self.table['show'] = "headings"

        self.table.column("id", width=100)
        self.table.column("name", width=100)
        self.table.column("desig", width=100)
        self.table.column("sal", width=100)
        self.table.column("gender", width=100)
        self.table.column("addr", width=100)

        self.table.pack(fill="both", expand=1)

    def add(self):
        con = pymysql.connect(host="localhost", user="root", passwd="mtman001", database="emp_db")
        cur = con.cursor()
        cur.execute("insert into emp values (%s,%s,%s,%s,%s,%s)",
                    (self.eid.get(), self.ename.get(), self.edesig.get(), self.esal.get(),
                     self.egender.get(), self.addrIn.get('1.0', tk.END)))

        con.commit()
        tk.messagebox.showinfo("Success", "Data Inserted Successfully!")
        self.get_data()
        con.close()


    def get_data(self): 
          con = pymysql.connect(host="localhost", user="root", passwd="mtman001", database="emp_db")
          cur = con.cursor()
          cur.execute("select * from emp")  
          data= cur.fetchall()
          if len(data) > 0:
               self.table.delete(*self.table.get_children())
               for i in data:
                    self.table.insert('',tk.END, values=i)
               con.commit() 
          con.close()

    def clear(self):
          self.eid.set(0)
          self.ename.set("")
          self.edesig.set("")
          self.esal.set(0)
          self.egender.set("")
          self.addrIn.delete('1.0',tk.END)
         
    def Update(self):      
         con = pymysql.connect(host="localhost", user="root", passwd="mtman001", database="emp_db")
         cur = con.cursor()
         cur.execute("update emp set name=%s, desig=%s, sal=%s, gender=%s, address=%s where id=%s", (self.ename.get(),
                                                                                                     self.edesig.get(), self.esal.get(),
                                                                                                     self.egender.get(), self.addrIn.get('1.0',tk.END),
                                                                                                     self.eid.get())) 
         
         con.commit()
         tk.messagebox.showinfo("Success", "Data Updated Successfully!")
         self.get_data()
         con.close()

    def remove(self):
         con = pymysql.connect(host="localhost", user="root", passwd="mtman001", database="emp_db")
         cur = con.cursor()
         cur.execute("delete from emp where id=%s", self.eid.get())
         con.commit()
         tk.messagebox.showinfo("Success", "Data Deleted Successfully!")
         self.get_data()
         con.close()


    def search(self):
         con = pymysql.connect(host="localhost", user="root", passwd="mtman001", database="emp_db")
         cur = con.cursor()
         cur.execute("select * from emp where " +self.searchType.get()+ " =%s", self.searchin.get())
         rows= cur.fetchall()
         if len(rows) >0:
              self.table.delete(*self.table.get_children())
              for j in rows:
                   self.table.insert('',tk.END, values=j)
              con.commit()
         else:
              tk.messagebox.showerror("Error", "Data Not Found!")
         con.close()

    def show_all(self): 
          con = pymysql.connect(host="localhost", user="root", passwd="mtman001", database="emp_db")
          cur = con.cursor()
          cur.execute("select * from emp")  
          data= cur.fetchall()
          if len(data) > 0:
               self.table.delete(*self.table.get_children())
               for i in data:
                    self.table.insert('',tk.END, values=i)
               con.commit() 
          else:
               tk.messagebox.showerror("Error", "Data Not Found!")
          con.close()  



root = tk.Tk()
obj = Employee(root)
root.mainloop()
