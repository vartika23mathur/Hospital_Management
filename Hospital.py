import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn=mysql.connector.connect(host='localhost',user='root',password='student',db='Hospital')
cursor=conn.cursor()

def New_Patient():
    Pid=int(input("Enter Patient id "))
    Patient_Name=input("Enter Patient Name ")
    Gender=input("Enter Patient Gender ")
    Father_name=input("Enter Patient Father Name ")
    Age=int(input("Enter your age "))
    Doctor_Name=input("Enter Doctor Name ")
    Address=input("Enter Address ")
    Mobile=input("Enter Mobile  number ")
    Adm_date=input("Enter Admission date")
    query="insert into Patient values({},'{}','{}','{}',{},'{}','{}',{},'{}')".format(Pid,Patient_Name,Gender,Father_name,Age,Doctor_Name,Address,Mobile,Adm_date)
    cursor.execute(query)
    conn.commit()
    print("Patient Admited Successfully ")

def discharge():
    Pid=int(input("Enter Patient id "))
    query="Delete from Patient where pid={}".format(Pid)
    cursor.execute(query)
    conn.commit()
    print("Patient Discharge Successfully")


def Patient_update():
    Pid=int(input("Enter Patient id "))
    Patient_Name=input("Enter Patient Name ")
    Gender=input("Enter Patient Gender ")
    Father_name=input("Enter Patient Father Name ")
    Age=int(input("Enter your age "))
    Doctor_Name=input("Enter Doctor Name ")
    Address=input("Enter Address ")
    Mobile=input("Enter Mobile  number ")
    query="update Patient set Pname='{}',Gender='{}',fname='{}',age={},Dname='{}',Address='{}',mobile='{}' where pid={}".format(Patient_Name,Gender,Father_name,Age,Doctor_Name,Address,Mobile,Pid)
    print(query)
    cursor.execute(query)
    conn.commit()
    print("Patient update Successfully ")

    
def show_deatil():
    Pid=int(input("Enter Patient Id"))
    
    query="select * from Patient where pid={}".format(Pid)
    
    cursor.execute(query)
    
    t=cursor.fetchall()

    
    for row in t:
        print("Name of Patient ", row[1])
        print("Father Name of Patient ",row[3])
        print("Age ",row[4])
        print("Doctor Name ",row[5])
        print("Address ",row[6])

    input("Press any key to continue ")

    
def show_plot():
    query="Select * from Patient"
    cursor.execute(query)
    data=cursor.fetchall()
    name=[]
    age=[]

    for row in data:
        name.append(row[1])
        age.append(row[4])

    plt.bar(name,age,width=0.25)
    plt.xlabel("\n Patient Name")
    plt.ylabel("\n Patient Age")
    plt.show()

def Save_in_CSV():
    query="Select * from Patient"
    cursor.execute(query)
    data=cursor.fetchall()
    name=[]
    age=[]
    pid=[]
    Address=[]
    for row in data:
        pid.append(row[0])
        name.append(row[1])
        age.append(row[4])
        Address.append(row[6])

    Patient={
        'Pid':pid,
        'Name':name,
        'Age':age,
        'Address':Address
        }

    dtf=pd.DataFrame(Patient)
    dtf.to_csv("Dav.csv")
    input("Data Exported to CSV\n Press any key to continue ")

    
def New_Doctor():
    Did=int(input("Enter Doctor  id "))
    Dname=input("Enter Doctor Name ")
    Degree=input("Enter Degree of the Doctor  ")
    Specialist=input("Doctor Specialist in ")
    Mobile=input("Enter Mobile  number ")
    
    query="insert into doctor values({},'{}','{}','{}',{})".format(Did,Dname,Degree,Specialist,Mobile)
    
    cursor.execute(query)
    conn.commit()
    input("New Doctor Details Add Successfully ")    


def Regin():
    Did=int(input("Enter Doctor  id "))
    query="Delete from doctor where DID={}".format(Did)
    
    cursor.execute(query)
    conn.commit()
    print("Doctor regin Successfully ")    

def Show_Dcotor_Detail():
    Did=int(input("Enter Doctor Id"))
    
    query="select * from Doctor where did={}".format(Did)
    
    cursor.execute(query)
    
    t=cursor.fetchall()

    
    for row in t:
        print("Name of Dcotr ", row[1])
        print("Degree ",row[2])
        print("Doctor Specialist ",row[3])
        print("Mobile ",row[4])
        
    input("Press any key to continue ")
    
def Update_doctor():
    Did=int(input("Enter Doctor  id "))
    Dname=input("Enter Doctor Name ")
    Degree=input("Enter Degree of the Doctor  ")
    Specialist=input("Doctor Specialist in ")
    Mobile=input("Enter Mobile  number ")
    
    query="update doctor  set Dname='{}',Degree='{}',Specialist='{}',Mobile={} where did={}".format(Dname,Degree,Specialist,Mobile,Did)
    
    cursor.execute(query)
    conn.commit()
    input("Update  Doctor Details  Successfully ")    

    
    
print("==========================WELCOME TO SMS HOSPITAL MANAGEMENT=================")
print("==========================MAIN MENU==========================================")


while True:
    print("1 For  Patient \n2 For Doctor \n3 exit")
    choice=int(input("Enter your choice "))
    print("=========================================================================")
    
               
    if choice==1:
        while True:
            print("\n1 For New Patient Admission\n2 For Discharge \n3 For Update Detail\n4 For show Detail \n5 Show Plot \n6 Save Data in CSV \n7 Main Menu ")
            choice=int(input("Enter your choice "))
            if choice==1:
                New_Patient()
            elif choice==2:
                discharge()
            elif choice==3:
                Patient_update()
            elif choice==4:
                show_deatil()            
            elif choice==5:
                show_plot()
            elif choice==6:
                Save_in_CSV()                
            elif choice==7:
                break

            
    elif choice==2:
        while True:
            print("\n1 For New Doctor \n2 For Regin \n3 For Update Detail\n4 For show Detail \n5 Main Menu ")
            choice3=int(input("Enter your choice "))
            if choice3==1:
                New_Doctor()
            elif choice3==2:
                Regin()
            elif choice3==3:
                Update_doctor()
            elif choice3==4:
                Show_Dcotor_Detail()
            elif choice3==5:
                break
    elif choice==3:
        break

                
        
    
        
    
    

