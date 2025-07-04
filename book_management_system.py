#Functions 
def addBooks(Books):
    while True :
        addBook=input("Do you want to add Books (y/n): ").lower()
        if addBook == "y" :
            title=input("Enter Title of Book : ").title()
            author=input("Enter author name : ").title()
            yearOfPublish=int(input("Enter year of publishment : "))
            ISBN=int(input("Enter ISBN number : "))
            availabilityStatus=input("Enter availability Status (borrowed/available): ").lower()
            Books[ISBN]=[title,author,yearOfPublish,availabilityStatus]
            print("Book added")
            
        elif addBook.strip()=="" :
            print("Make a Choice ...")
        else :
            break

def displayBooks(Books):
    print(Books)
    print(f"Number of Books : {len(Books)}")

def searchBookByIsbn(Books):
    searchIsbn=int(input("Enter ISBN number to search : "))
    print("Searching...")
    if searchIsbn in Books:
        print("Book Found")
        print(Books.get(searchIsbn))
    else :
        print("No Book found")    
    

def updateStatus(Books):
    updateIsbn=int(input("Enter a Book ISBN to update status : "))
    print("Searching...")
    if updateIsbn in Books :
        newStatus=input("Enter Current Status (borrowed/available) : ").lower()
        Books[updateIsbn][3]=newStatus
        print("Book Status updated...")
    else :
        print("No Book Found")    

def deleteBook(Books):
    deleteIsbn=int(input("Enter a ISBN to delete a book : "))
    print("Searching..")
    if deleteIsbn in Books :
        Books.pop(deleteIsbn)
        print("Book Deleted")
    else :
        print("No Book Found")
def DisplayUniqueAuthors(Books):
    uniqueAuthors=set()
    for author in Books.values() :
        uniqueAuthors.add(author[1])
    print(uniqueAuthors)


def libraryStats(Books):
    numberOfBooks=len(Books)
    yearsOfPublish=[]
    for year in Books.values():
        yearsOfPublish.append(year[2])
    authors=[]
    for author in Books.values():
        authors.append(author[1])
    books=[]
    for book in Books.values():
        books.append(book[0])
    print("*************************")
    print("*******Library Stats*****") 
    print("*************************") 
    print(f"Number Of Books : {numberOfBooks}")    
    print(f"years in which Books are published : {yearsOfPublish}")    
    print(f"Authors of Books : {authors}")    
    print(f"Books : {books}")    
 
#Program start
print("*************************************")
print("*************Wellcome To*************")
print("****Library Book Management System***")
print("**************************************")

Books= {}

while True :
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book By ISBN")
    print("4. Update Book Status")
    print("5. Delete Book")
    print("6. Display Unique Authors")
    print("7. Show Library Statistics")
    print("8. Exit")
    choice=int(input("Make a choice : "))

    if choice == 1 :
            addBooks(Books)
            print(f"Number of Books : {len(Books)}")

    elif choice == 2 :
        if len(Books)> 0:
            displayBooks(Books)
        else :
           print("No book Found")
            
    elif choice== 3:
        if len(Books) > 0 :
            searchBookByIsbn(Books)
        else :
            print("No Book Found...") 

    elif choice == 4:
        if len(Books) > 0:
            updateStatus(Books)
        else :
            print("No Book found") 

    elif choice ==5 :
        if len(Books) > 0:
            deleteBook(Books)
        else :
            print("No Book found")    
        
    elif choice == 6 :
        if len(Books) > 0:
            DisplayUniqueAuthors(Books)
        else :
            print("No Book found")    
        
    elif choice == 7 :
        if len(Books) > 0:
            libraryStats(Books)
        else :
            print("No Book found")    
        
    elif choice == 8:
        confirm=input("Are you sure YOU want to exit (y/n) : ")
        if confirm == "y" :
            print("Exiting Library Book Management System")
            break
    else :
        print("Invalid Choice")
