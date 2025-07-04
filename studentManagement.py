# Functions 
        

def addStudent(Students):
    addStudent=True
    while(addStudent == True):
        option=input("Do you want to add student (y/n): ")
        if(option == "y"):
            name=input("Enter name of student : ")
            rollNumber=int(input("Enter roll Number of Student : "))
            marks=int(input("Enter marks of student : "))
            Students.update({rollNumber : [name,marks]})
        elif option.strip() == " ":
            print("make a choice...")
        else :
            addStudent=False   
    return

def displayStudents(Students):
    print(Students)
    print(f"Number of Students : {len(Students)}")



def searchByRollNumber(Students):
    searchRollNumber=int(input("Enter a rollNumber : "))

    if searchRollNumber in Students:
            print(f"Student Found with roll Number# {searchRollNumber}")
            print(Students.get(searchRollNumber))
    else :
        print(f"Student Not Found With Roll Number # {searchRollNumber}")        

                


def updateMarks(Students):
    rollNumberToUpdate=int(input("Enter a rollNumber  to update marks : ")) 
        
    if rollNumberToUpdate in Students :
        print("Student Found")
        newMarks=int(input("Enter New Marks : "))
        Students[rollNumberToUpdate][1]=newMarks
        print("Marks Updated...")
    else :
        print("Student Not Found")    


def deleteStudent(Students):
    deleteStudentRollNumber=int(input("Enter rollNumber to delete : "))
    if deleteStudentRollNumber in Students :
        del Students[deleteStudentRollNumber]
        print("Student Deleted From Record...")
    else :
        print("Student Not Found")   

def displayUniqueMarks(Students):
   uniqueMarks={data[1] for data in Students.values()}
   print(f"Unique Marks in Class {uniqueMarks}")

def classStatistics(Students):
    marks=[data[1] for data in Students.values()]
    avg_marks=sum(marks)/len(marks)
    highestMarks=max(marks)
    lowestMarks=min(marks)
    print(f"average Marks : {avg_marks} \n Highest Marks : {highestMarks} \n Lowest Marks : {lowestMarks}")
       

# Beggining of Program
Students={}
print("Wellcome to Student Management System")
while True :
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll Number")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Display Unique Marks")
    print("7. Display Class Statistics")
    print("8. Exit")
    choice=int(input("Make a choice :"))
    if choice == 1 :
        addStudent(Students)
        print(f"Number of Students : {len(Students)}")
    elif choice == 2 : 
        if len(Students)>=0:
            displayStudents(Students)
        else :   
            print("No student details available...")
    elif choice == 3 :
        searchByRollNumber(Students)        
    elif choice == 4 :
        updateMarks(Students)   
    elif choice == 5 :
        deleteStudent(Students)
    elif choice == 6 :
        displayUniqueMarks(Students) 
    elif choice == 7 :
              classStatistics(Students) 
    elif choice == 8:
        while True:
            confirm=input("Are you sure YOU want to exit (y/n) : ").lower()
            if confirm == "y":
                print("Exiting Student Management System")
                break
    else :
        print("Invalid Choice..")