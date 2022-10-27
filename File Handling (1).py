import os

while(True):
    try:
        print("File Operations are as follow : ")
        z=int(input(
                """
                    1. Create a file
                    2. Update a file
                    3. Read a file
                    4. Delete a file

                    What do you want to do : """))
    except Exception as e:
        print("Error Occured :",e)

    else:
        if(z==1):
            a=input("\nEnter file name with its extension : ")
            x=input("""
                       Where do you want to create it :
                       1. Current Folder
                       2. Other folder""")
            if(x=="1"):
                with open(a,"w"):
                    print("\nFile Created Successfully")
                            
            elif(x=="2"):
                y=input("\nEnter folder path : ")
                b=y.split("\\")
                c=("/").join(b)
                with open(f"{c}/{a}","w"):
                    print("File Created Successfully")

        elif(z==2):
            a=input("\nEnter file path with file name & its extension : ")
            f1 = open(a,"a")
            b=int(input("""
                            1. Add a file
                            2. Add data manually"""))
            if(b==1):
                a=input("Enter file path with file name & its extension : ")
                b=a.split("\\")
                c=("/").join(b)        
                f2 = open(str(c),"r")
                cont = f2.read()
                f3=f1.write(cont)
                print("File Added Successfully")
                print(f3)
                f1.close()
                f2.close()

            elif(b==2):
                a=input("Input your data : ")
                f1.write(a)
                f1.close()
                print("Data Added Successfully")
                        
        elif(z==3):
            a=input("\nEnter file path with file name & its extension : ")
            b=a.split("\\")
            c=("/").join(b)        
            f1 = open(f"{c}","r")
            cont = f1.readlines()
            print(cont)
            f1.close()

        elif(z==4):
            a=input("\nEnter file path with file name & its extension : ")
            os.remove(a)
            print("File Deleted Successfully")

        else:
            print("\nInvalid Choice")
        
    finally:
        print("Task Completed, Thank You")
