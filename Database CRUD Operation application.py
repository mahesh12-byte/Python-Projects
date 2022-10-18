import pymysql as p

def getconnect():
    return p.connect(host="localhost", user="root", password="", database="itv")
    
def insertdata(t):
    db=getconnect()
    cr=db.cursor()
    sql = "insert into itvtable values(%s, %s, %s, %s)"
    cr.execute(sql,t)
    print("Data Inserted Successfully")
    db.commit()
    db.close()


def updatedata(t):
    db=getconnect()
    cr=db.cursor()
    sql="update itvtable set name=%s, email=%s, adress=%s where id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()


def updateNameById(t):
    db=getconnect()
    cr=db.cursor()
    sql="update itvtable set name=%s where id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def updateEmailById(t):
    db=getconnect()
    cr=db.cursor()
    sql="update itvtable set email=%s where id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()

def updateAddById(t):
    db=getconnect()
    cr=db.cursor()
    sql="update itvtable set adress=%s where id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()
    
def read():
    db=getconnect()
    cr=db.cursor()
    sql ="select * from itvtable"
    cr.execute(sql)
    data=cr.fetchall()
    for d in data:
        print (f"{d[0]:^3} {d[1]:^10} {d[2]:^30} {d[3]:^20}")
    db.commit()
    db.close()


def selectEmpById(t):
    db=getconnect()
    cr=db.cursor()
    sql ="select * from itvtable where id=%s"
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0]
    

def login():
    db=getconnect()
    cr=db.cursor()
    sql="select email, adress from itvtable"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return(data)


def delete(t):
    db=getconnect()
    cr=db.cursor()
    sql="delete from itvtable where id=%s"
    cr.execute(sql,t)
    print("Data Updated Successfully")
    db.commit()
    db.close()


##print("To access the database, Enter email & password")
##log=login()
##
##u=input("Enter Email Id :")
##p=input("Enter password :")
##
##if (u,p) in log:
##    print("Access Granted")


abc=True
while(abc):
    print("""
         Database operations as follows :
         To Insert record, press '1'
         To Update record, press '2'
         To Delete record, press '3'
         To Update an entry, press '4'
         To view record of any id, press 'i'
         To view all records, press '*'
         To exit database, press 'e'
      """)

    a=input("Enter your choice :")

    if(a=="1"):
        b=int(input("Enter the data for Id :"))
        c=input("Enter the data for Name :")
        d=input("Enter the data for EmailId :")
        e=input("Enter the data for Address :")
        t=(b,c,d,e)
        insertdata(t)

    elif(a=="2"):
        b=int(input("Enter Id of which data is to be updated:"))
        c=input("Enter the data for Name :")
        d=input("Enter the data for EmailId :")
        e=input("Enter the data for Address :")
        t=(c,d,e,b)
        updatedata(t)

    elif(a=="3"):
        t=input("Enter the Id, to delete it's record :")
        delete(t)

    elif(a=="4"):
        print("""
                To update Name, select '1'
                To update EmailID, select '2'
                To update the Address, select '3'""")
        z=int(input("What do you want to update :"))
        b=int(input("Enter Id of which data is to be updated:"))
        if(z==1):
            c=input("Enter the data for Name :")
            t=(c,b)
            updateNameById(t)

        elif(z==2):
            d=input("Enter the data for EmailId :")
            t=(d,b)
            updateEmailById(t)

        elif(z==3):
            e=input("Enter the data for Address :")
            t=(e,b)
            updateAddById(t)
        else:
            print("Invalid Choice")

    elif(a=="*"):
        read()

    elif(a=="i"):
        t=int(input("Enter Id to fetch it's record:"))
        f=selectEmpById(t)
        print(f)

    elif(a=="e"):
        abc=False
        break
        
    else:
        print("Syntax Error : Invalid Option")               
##else:
##    print("Access Denied")
