from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Db connection string

# connection = mysql.connector.connect(host="localhost", user="root", password="", database="test_db")


class PharmacyManagmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1330x800+0+0")
        
        #=================== addMed Variable==================
        self.refMed_var=StringVar()
        self.addMed_var=StringVar()
        
        self.ref_var=StringVar()
        self.compName_var=StringVar()
        self.typeMed_vsr=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.iss_var=StringVar()
        self.exp_var=StringVar()
        self.use_var=StringVar()
        self.sidee_var=StringVar()
        self.war_var=StringVar()
        self.dos_var=StringVar()
        self.price_var=StringVar()
        self.prod_var=StringVar()
      
        
        
        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
                         bg='white', fg='darkgreen', font=("times new roman", 30, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)
        
        img1 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/logos.jpg')
        img1 = img1.resize((80, 48), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=70, y=18)
        
        #====================DataFrame=====================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1330,height=300)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20
                                 ,text="Medicine Infomation",fg="darkgreen",font=("arial", 12, "bold"))
        
        DataFrameLeft.place(x=0,y=5,width=860,height=260)
        
               
        #======================ButtonsFrame====================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=400,width=1330,height=65)
        
        #======================Main Button======================
        btnAddData=Button(ButtonFrame,command=self.Add_Data,width=10,text="Medicine Add",font=("arial", 12, "bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnUpdateData=Button(ButtonFrame,command=self.Update,width=10,text="UPDATE",font=("arial", 13, "bold"),bg="darkgreen",fg="white")
        btnUpdateData.grid(row=0,column=1)
        
        btnDeleteData=Button(ButtonFrame,command=self.Delete,width=10,text="DELETE",font=("arial", 13, "bold"),bg="red",fg="white")
        btnDeleteData.grid(row=0,column=2)
        
        btnRestData=Button(ButtonFrame,command=self.Reset,width=10,text="RESET",font=("arial", 13, "bold"),bg="darkgreen",fg="white")
        btnRestData.grid(row=0,column=3)
        
        btnExitData=Button(ButtonFrame,width=10,text="EXIT",font=("arial", 13, "bold"),bg="darkgreen",fg="white")
        btnExitData.grid(row=0,column=4)
        
        # =====================Search By================
        lblSearch=Label(ButtonFrame,font=("arial", 17, "bold"),text="Search By",padx=2, bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        # variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=13,font=("arial", 17, "bold"),state="readonly",background="blue")
        search_combo["values"]=("Refno","MedName","Lotno")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        self.search_txt=StringVar()
        textSearch=Entry(ButtonFrame,textvariable=self.search_txt,bd=3,relief=RIDGE,width=12,font=("arial", 17, "bold"))
        textSearch.grid(row=0,column=7)
        
        searchBtn=Button(ButtonFrame,command=self.Search,width=10,text="SEARCH",font=("arial", 13, "bold"),bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)
        
        showAll=Button(ButtonFrame,command=self.fetch_Data,width=10,text="SHOW ALL",font=("arial", 13, "bold"),bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)
        
        #===========================LAbEL AND ENTERY=================================
        lblRefno=Label(DataFrameLeft,font=("arial", 10, "bold"),text="Reference No:",padx=2,pady=6)
        lblRefno.grid(row=0,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from medn")
        row=my_cursor.fetchall()
        
        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=24,font=("arial", 11, "bold"),state="readonly",background="blue")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        
        lblComN=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Company Name:", padx=2, pady=6)
        lblComN.grid(row=1, column=0,sticky=W)
        textComN=Entry(DataFrameLeft,textvariable=self.compName_var, font=("arial", 11, "bold"),bg="white", bd=2, relief=RIDGE, width=26)
        textComN.grid(row=1, column=1)
        
        lblTOM=Label(DataFrameLeft,font=("arial", 10, "bold"),text="Type Of Medicine:",padx=2,pady=6)
        lblTOM.grid(row=2, column=0, sticky=W)
        
        tom_combo=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_vsr,width=24,font=("arial", 11, "bold"),state="readonly",background="blue")
        tom_combo["values"]=("Tablet","Liquid","Capsule","Topical Medicines", "Inhales", "Drops","Injection")
        tom_combo.grid(row=2,column=1)
        tom_combo.current(0)
        
        #=========================AddMedicine==============================
        
        lblMname=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Medicine Name:", padx=2,pady=6)
        lblMname.grid(row=3, column=0, sticky=W)
        
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from medn")
        row=my_cursor.fetchall()
        
        
        comMN=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var ,state="readonly",
                           font=("arial", 11, "bold"), width=24)
        comMN['value']=row
        comMN.current(0)
        comMN.grid(row=3, column=1)
        
        lblLotno=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotno.grid(row=4, column=0,sticky=W)
        textLotno=Entry(DataFrameLeft,textvariable=self.lot_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textLotno.grid(row=4, column=1)
        
        lblIssueDate=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0,sticky=W)
        textIssueDate=Entry(DataFrameLeft, textvariable=self.iss_var,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textIssueDate.grid(row=5, column=1)
        
        
        lblExD=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExD.grid(row=6, column=0,sticky=W)
        textExD=Entry(DataFrameLeft,textvariable=self.exp_var ,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textExD.grid(row=6, column=1)
        
        lblUses=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Uses:", padx=20, pady=6)
        lblUses.grid(row=0, column=2,sticky=W)
        textUses=Entry(DataFrameLeft,textvariable=self.use_var ,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textUses.grid(row=0, column=3)
        
        lblSideE=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Side Effect:", padx=20, pady=6)
        lblSideE.grid(row=1, column=2,sticky=W)
        textSE=Entry(DataFrameLeft,textvariable=self.sidee_var ,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textSE.grid(row=1, column=3)
        
        lblPreWar=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Prec&Warning:", padx=20)
        lblPreWar.grid(row=2, column=2,sticky=W)
        textPW=Entry(DataFrameLeft,textvariable=self.war_var ,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textPW.grid(row=2, column=3)
        
        lblDos=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Dosage:", padx=20)
        lblDos.grid(row=3, column=2,sticky=W)
        textDos=Entry(DataFrameLeft,textvariable=self.dos_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textDos.grid(row=3, column=3)
        
        lblPrice=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Tablets Price:", padx=20, pady=6)
        lblPrice.grid(row=4, column=2,sticky=W)
        textP=Entry(DataFrameLeft,textvariable=self.price_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textP.grid(row=4, column=3)
        
        lblPQT=Label(DataFrameLeft,font=("arial", 10, "bold"), text="Product QT:", padx=20, pady=6)
        lblPQT.grid(row=5, column=2,sticky=W)
        textPQT=Entry(DataFrameLeft,textvariable=self.prod_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=26)
        textPQT.grid(row=5, column=3)
        
        # ==================================Images=========================
        
        lblhome=Label(DataFrameLeft, font=("arial", 8,"bold" ),text="Stay home Stay Safe:", padx=2, pady=2, bg="white", fg="red")
        lblhome.place(x=698,y=0)
        
        
        img2 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/tab.jpg')
        img2 = img2.resize((120, 100), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(self.root, image=self.photoimg2, borderwidth=0)
        b2.place(x=762, y=155)
        
        img3 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/tab4.jpg')
        img3 = img3.resize((120, 114), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(self.root, image=self.photoimg3, borderwidth=0)
        b3.place(x=762, y=245)
        
        img4 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/eng.jpg')
        img4 = img4.resize((220, 35), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(self.root, image=self.photoimg4, borderwidth=0)
        b4.place(x=535, y=325)
        
        img5 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/eng1.jpeg')
        img5 = img5.resize((120, 35), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b4 = Button(self.root, image=self.photoimg5, borderwidth=0)
        b4.place(x=420, y=325)
        
        #===================DataFrameRight======================
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20
                                 ,text="Medicine Add Department",fg="darkgreen",font=("arial", 12, "bold"))
        
        DataFrameRight.place(x=870,y=5,width=400,height=260)
        
        img6 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/tablets2.jpeg')
        img6 = img6.resize((130, 55), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b4 = Button(self.root, image=self.photoimg6, borderwidth=0)
        b4.place(x=920, y=130)
        
        img7 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/tablets2.jpeg')
        img7 = img7.resize((130, 55), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(self.root, image=self.photoimg7, borderwidth=0)
        b4.place(x=1050, y=130)
        
        img8 = Image.open('C:/Users/PMLS/Desktop/Python 100-Days Of Code/tkinter/tab4.jpg')
        img8 = img8.resize((115, 95), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing replace of Image.ANTIALIAS
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b4 = Button(self.root, image=self.photoimg8, borderwidth=0)
        b4.place(x=1180, y=130)
        
        lblrefno=Label(DataFrameRight,font=("arial", 10, "bold"), text="Reference No:")
        lblrefno.place(x=0,y=60)
        textrefno=Entry(DataFrameRight,textvariable=self.refMed_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=16)
        textrefno.place(x=110, y=60)
        
        lblmedn=Label(DataFrameRight,font=("arial", 10, "bold"), text="Medicine Name:")
        lblmedn.place(x=0,y=85)
        textmedn=Entry(DataFrameRight,textvariable=self.addMed_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=16)
        textmedn.place(x=110, y=85)
        
       # ======================side Frame===================
        side_frame=Frame(DataFrameRight,bd=4, relief=RIDGE,bg="white")
        side_frame.place(x=0, y=115, width=245, height=110)
        
        sc_x=ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y=ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,columns=("ref", "medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)   #to config scrollbar
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("ref",text="Ref")   # to take headen
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings" #to show headings
        self.medicine_table.pack(fill=BOTH,expand=1)
        
        self.medicine_table.column("ref",width=100)  # to set width
        self.medicine_table.column("medname",width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>", self.MedGet_cursor)
        
      #  ========================Medicine Button========================
        down_frame=Frame(DataFrameRight,bd=4, relief=RIDGE,bg="darkgreen")
        down_frame.place(x=250,y=100,width=105,height=128)
        
        btnAddmed=Button(down_frame,width=11,text="ADD",font=("arial", 10, "bold"),bg="lime",fg="white",pady=2,command=self.addMed)
        btnAddmed.grid(row=0,column=0)
        
        btnUpDatemed=Button(down_frame,width=11,text="UPDATE",font=("arial", 10, "bold"),bg="purple",fg="white",pady=2,command=self.UpdateMed)
        btnUpDatemed.grid(row=1,column=0)
        
        btnDeletemed=Button(down_frame,width=11,text="DELETE",font=("arial", 10, "bold"),bg="red",fg="white",pady=2,command=self.DeleteMed)
        btnDeletemed.grid(row=2,column=0)
        
        btnClearmed=Button(down_frame,width=11,command=self.ClearMed,text="CLEAR",font=("arial", 10, "bold"),bg="orange",fg="white",pady=2)
        btnClearmed.grid(row=3,column=0)
       
       #=========================Frame Details======================
        Frame_details=Frame(self.root,bd=15, relief=RIDGE)
        Frame_details.place(x=0, y=470, width=1330,height=210)
        
        Table_frame=Frame(Frame_details,bd=15, relief=RIDGE)
        Table_frame.place(x=0, y=1, width=1300,height=180)
       
        scr_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scr_x.pack(side=BOTTOM, fill=X)
        scr_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scr_y.pack(side=RIGHT,fill=Y)
        
        self.pharmacy_table=ttk.Treeview(Table_frame,columns=("ref","companyname","type","tabletname","lotno","issued",
                                                              "expdate","uses","sideeffect","warning","dosage","price","productqt")
                                         ,xscrollcommand=scr_x.set,yscrollcommand=scr_y.set)
        
        scr_x.pack(side=BOTTOM,fill=X)
        scr_y.pack(side=RIGHT,fill=Y)
        
        scr_x.config(command=self.pharmacy_table.xview)
        scr_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table["show"]="headings"
        
        self.pharmacy_table.heading("ref",text="Rrefernce No:")
        self.pharmacy_table.heading("companyname",text="Company Name:")
        self.pharmacy_table.heading("type",text="Type Of Medicine:")
        self.pharmacy_table.heading("tabletname",text="Tablet Name:")
        self.pharmacy_table.heading("lotno",text="Lot No:")
        self.pharmacy_table.heading("issued",text="Issue Date:")
        self.pharmacy_table.heading("expdate",text="Exp Date:")
        self.pharmacy_table.heading("uses",text="Uses:")
        self.pharmacy_table.heading("sideeffect",text="Side Effect:")
        self.pharmacy_table.heading("warning",text="Prec&Warning:")
        self.pharmacy_table.heading("dosage",text="Dosage:")
        self.pharmacy_table.heading("price",text="Price:")
        self.pharmacy_table.heading("productqt",text="Product Qts:")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("ref",width=100) 
        self.pharmacy_table.column("companyname",width=100) 
        self.pharmacy_table.column("type",width=100) 
        self.pharmacy_table.column("tabletname",width=100) 
        self.pharmacy_table.column("lotno",width=100) 
        self.pharmacy_table.column("issued",width=100) 
        self.pharmacy_table.column("expdate",width=100) 
        self.pharmacy_table.column("uses",width=100) 
        self.pharmacy_table.column("sideeffect",width=100) 
        self.pharmacy_table.column("warning",width=100) 
        self.pharmacy_table.column("dosage",width=100) 
        self.pharmacy_table.column("price",width=100) 
        self.pharmacy_table.column("productqt",width=100) 
        self.fetch_datamed()
        self.fetch_Data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        # ======================Add Medicine functionality declaration======================
    def addMed(self):
      conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
      my_cursor=conn.cursor()
      query= ("INSERT INTO medn (Ref,MedName) VALUES (%s,%s)")
      val=(self.refMed_var.get(), self.addMed_var.get())
      my_cursor.execute(query, val)
      
      messagebox.showinfo("Success","Medicine Added")
      conn.commit()
      self.fetch_datamed()
      self.MedGet_cursor()
      conn.close()
      
      
    def fetch_datamed(self):    # fetch the data from table
      conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from medn")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
        self.medicine_table.delete(*self.medicine_table.get_children())
        for i in rows:
          self.medicine_table.insert("", END,values=i)
        conn.commit()
      conn.close()  
        
          
        
        
        # ==================MedGet Function===================
    def MedGet_cursor(self, event=""):
      cursor_row=self.medicine_table.focus()
      content=self.medicine_table.item(cursor_row)
      row=content["values"]
      self.refMed_var.set(row[0])
      self.addMed_var.set(row[1])
      
    
    def UpdateMed(self):
      if self.refMed_var.get() == "" or self.addMed_var.get() == "":
          messagebox.showerror("Error", "All fields are required")
      else:
          try:
              # Debugging print statements
              print(f"Ref Value: {self.refMed_var.get()}")
              print(f"MedName Value: {self.addMed_var.get()}")

              # Make sure to convert Ref to the correct type if it's an integer in the database
              ref_value = int(self.refMed_var.get())  # Convert Ref to int if necessary
              med_name_value = self.addMed_var.get()

              conn = mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
              my_cursor = conn.cursor()

              # SQL query to update the medicine name using the reference ID
              sql = "UPDATE medn SET MedName = %s WHERE Ref = %s"
              val = (med_name_value, ref_value)

              print(f"Executing SQL: {sql} with values {val}")  # Debugging SQL execution

              my_cursor.execute(sql, val)
              conn.commit()  # Commit the changes

              self.fetch_datamed()  # Fetch the updated data

              # If the update is successful, show a success message
              messagebox.showinfo("Success", "Medicine Updated Successfully")
          except Exception as e:
              messagebox.showerror("Error", f"Error due to: {str(e)}")
              print(f"Error: {str(e)}")  # Print the error for debugging
          finally:
              conn.close()  # Ensure the connection is closed


    
    # def UpdateMed(self):
    #   if self.refMed_var.get() == "" or self.addMed_var.get() == "":
    #       messagebox.showerror("Error", "All fields are Required")
    #   else:
    #       try:
    #           conn = mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
    #           my_cursor = conn.cursor()

    #           # SQL query to update the medicine name using the reference ID
    #           sql = "UPDATE medn SET MedName=%s WHERE Ref=%s"
    #           val = (self.addMed_var.get(), self.refMed_var.get())

    #           my_cursor.execute(sql, val)
    #           conn.commit()  # Commit the changes

    #           self.fetch_datamed()  # Fetch the updated data

    #           # If update is successful, show success message
    #           messagebox.showinfo("Success", "Medicine Updated Successfully")
    #       except Exception as e:
    #           messagebox.showerror("Error", f"Error due to: {str(e)}")
    #       finally:
    #           conn.close()  # Ensure connection is closed in the 'finally' block

          
        
    def DeleteMed(self):
      conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
      my_cursor=conn.cursor()
      
      sql="DELETE FROM medn WHERE Ref=%s"
      val=(self.refMed_var.get(),)
      my_cursor.execute(sql,val)
      
      conn.commit()
      self.fetch_datamed()
      conn.close()
      messagebox.showinfo("Success","Medicine Deleted")
        
    def ClearMed(self):
      self.refMed_var.set("")
      self.addMed_var.set("")
      
      
      
     # ===================================Main Table=================================
     
    def Add_Data(self):
      if self.ref_var.get()=="" or self.lot_var.get()=="":
        messagebox.showerror("Error","All fields are Required")
      else:  
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO phs VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
          self.ref_var.get(),
          self.compName_var.get(),
          self.typeMed_vsr.get(),
          self.medName_var.get(),
          self.lot_var.get(),
          self.iss_var.get(),
          self.exp_var.get(),
          self.use_var.get(),
          self.sidee_var.get(),
          self.war_var.get(),
          self.dos_var.get(),
          self.price_var.get(),
          self.prod_var.get(),
        ))
        conn.commit()
        self.fetch_Data()
        conn.close()
        messagebox.showinfo("Success","Data has been inserted")
                             
    def fetch_Data(self):
      conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
      my_cursor=conn.cursor()
      my_cursor.execute("SELECT * FROM phs")
      row=my_cursor.fetchall()
      if len(row)!=0:
        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
        for i in row:
          self.pharmacy_table.insert("",END,values=i)
          conn.commit()
        conn.close()
        
    def get_cursor(self, ev=""):
      cursor_row=self.pharmacy_table.focus()
      content=self.pharmacy_table.item(cursor_row)
      row=content["values"]
      self.ref_var.set(row[0])
      self.compName_var.set(row[1])
      self.typeMed_vsr.set(row[2])
      self.medName_var.set(row[3])
      self.lot_var.set(row[4])
      self.iss_var.set(row[5])
      self.exp_var.set(row[6])
      self.use_var.set(row[7])
      self.sidee_var.set(row[8])
      self.war_var.set(row[9])
      self.dos_var.set(row[10])
      self.price_var.set(row[11])
      self.prod_var.set(row[12])
      
    def Update(self, ev=""):
      if self.ref_var.get()=="" or self.lot_var.get()=="":
        messagebox.showerror("Error","All fields are Required")
      else:
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
        my_cursor=conn.cursor()
        sql="UPDATE phs SET compname=%s, typemed=%s, medname=%s,lotno=%s, issuedate=%s, expdate=%s, user=%s, sideeff=%s, precwarning=%s, dos=%s, tabprice=%s, pqt=%s WHERE refno=%s"
        val=(self.ref_var.get(),
             self.compName_var.get(),
             self.typeMed_vsr.get(),
             self.medName_var.get(),
             self.lot_var.get(),
             self.iss_var.get(),
             self.exp_var.get(),
             self.use_var.get(),
             self.sidee_var.get(),
             self.war_var.get(),
             self.dos_var.get(),
             self.price_var.get(),
             self.prod_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_Data()
        conn.close()
        messagebox.showinfo("UPDATE","Record has been Updated successfully")
        
    def Delete(self):
      conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
      my_cursor=conn.cursor()
      
      sql="DELETE FROM phs WHERE refno=%s"
      val=(self.ref_var.get(),)
      my_cursor.execute(sql,val)
      
      conn.commit()
      self.fetch_Data()
      conn.close()
      messagebox.showinfo("DELETED","Info Deleted Successfully")
      
    def Reset(self):
      # self.ref_var.set(""),
      self.compName_var.set(""),
      # self.typeMed_vsr.set(""),
      # self.medName_var.set(""),
      self.lot_var.set(""),
      self.iss_var.set(""),
      self.exp_var.set(""),
      self.use_var.set(""),
      self.sidee_var.set(""),
      self.war_var.set(""),
      self.dos_var.set(r""),
      self.price_var.set(r""),
      self.prod_var.set(r"")
      
    def Search(self):
      conn=mysql.connector.connect(host="localhost", username="root", password="", database="pharm_db")
      my_cursor=conn.cursor()
  
      sql =f"select * from phs where {self.search_var.get()} = '{self.search_txt.get()}'"
      
      my_cursor.execute(sql)

      rows=my_cursor.fetchall()
      if len(rows)!=0:
        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
        for i in rows:
          self.pharmacy_table.insert("",END,values=i)
        conn.commit()
      conn.close()
      
    
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagmentSystem(root)
    root.mainloop()