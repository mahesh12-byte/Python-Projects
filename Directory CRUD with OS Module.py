import os

abc=True
while (abc):
    print("""
            To view all files in the folder, press '1'
            To Make a new Folder, press '2'
            To create a file, press '3'
            To create a file at desired location, press '4'
            To remove a file from the folder, Press '5'
            To delete a folder, press '6'
            To view current working folder/directory, press '9'
            To Exit the application, press '0'""")

    z=int(input("Enter your choice :"))

    if (z==1):
        a=os.listdir()
        for i in a:
            print(i)

    elif(z==2):
        b=input("Enter directory name :")
        os.mkdir(b)
        print("New Directory created")

    elif(z==3):
        c=input("Enter a name for New file with it's extension:")
        file=open(c,"w")
        file.close()
        print("New File created")

    elif(z==4):
        file=input("Enter a name for New file with it's extension:")
        path=input("Enter a path of directory where you want to save the file :")
        destinationfile=os.path.join(path,file)
        newfile=open(destinationfile,"w")
        newfile.close()
        print("New File created at given location")

    elif(z==5):
        b=input("To remove, enter file name with extension :")
        os.remove(b)
        print("File removed Successfully")

    elif(z==6):
        b=input("To remove, enter directory name  :")
        os.rmdir(b)
        print("Directory removed Successfully")
    
    elif(z==9):
       print(os.getcwd())
       
    elif(z==0):
        abc=False
        break

    else:
        print("Invalid Choice")
