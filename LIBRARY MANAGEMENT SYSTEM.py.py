# ============================================================
#              LIBRARY MANAGEMENT SYSTEM
# Basic Python Project: Functions, Lists, Tuples,
# Dictionaries and Strings
# ============================================================
books = [
    {"id": 101, "title": "Python Programming", "author": "John Smith",
     "category": "Programming", "status": "Available", "issued_to": ""},
    {"id": 102, "title": "Data Structures", "author": "Mark Allen",
     "category": "Computer Science", "status": "Available", "issued_to": ""},
    {"id": 103, "title": "Computer Networks", "author": "A. Tanenbaum",
     "category": "Computer Science", "status": "Available", "issued_to": ""},
    {"id": 104, "title": "Introduction to AI", "author": "David Poole",
     "category": "Artificial Intelligence", "status": "Available", "issued_to": ""},
    {"id": 105, "title": "The Alchemist", "author": "Paulo Coelho",
     "category": "Fiction", "status": "Available", "issued_to": ""}
]
members = [
    {"id": 1, "name": "Rahul Sharma", "phone": "9876543210", "books": []},
    {"id": 2, "name": "Priya Verma", "phone": "9123456780", "books": []},
    {"id": 3, "name": "Aman Singh", "phone": "9988776655", "books": []}
]
transactions = []
# Tuple - fixed library information
library_info = ("Central City Library", "Main Road, India", "9 AM - 6 PM")
def line():
    print("-" * 65)
def heading(text):
    line()
    print(text.center(65))
    line()
def pause():
    input("\nPress Enter to continue...")
def integer(message):
    while True:
        n = input(message)
        if n.isdigit():
            return int(n)
        print("Enter a valid number.")
def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None
def find_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None
def library_information():
    heading("LIBRARY INFORMATION")
    print("Name    :", library_info[0])
    print("Address :", library_info[1])
    print("Time    :", library_info[2])
    pause()
def add_book():
    heading("ADD BOOK")
    book_id = integer("Enter book ID: ")
    if find_book(book_id):
        print("Book ID already exists.")
        pause()
        return
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    category = input("Enter category: ").strip()
    if not title or not author or not category:
        print("All fields are required.")
    else:
        books.append({
            "id": book_id, "title": title, "author": author,
            "category": category, "status": "Available", "issued_to": ""
        })
        print("Book added successfully.")
    pause()
def display_books():
    heading("ALL BOOKS")
    if not books:
        print("No books available.")
    else:
        for b in books:
            print("ID:", b["id"], "|", b["title"], "|", b["author"])
            print("Category:", b["category"], "| Status:", b["status"])
            if b["status"] == "Issued":
                print("Issued to:", b["issued_to"])
            line()
    pause()
def search_book():
    heading("SEARCH BOOK")
    key = input("Enter title, author or category: ").strip().lower()
    if not key:
        print("Search field cannot be empty.")
        pause()
        return
    found = False
    for b in books:
        if (key in b["title"].lower() or
            key in b["author"].lower() or
            key in b["category"].lower()):
            print("ID:", b["id"])
            print("Title:", b["title"])
            print("Author:", b["author"])
            print("Category:", b["category"])
            print("Status:", b["status"])
            line()
            found = True
    if not found:
        print("No matching book found.")
    pause()
def remove_book():
    heading("REMOVE BOOK")
    book = find_book(integer("Enter book ID: "))
    if book is None:
        print("Book not found.")
    elif book["status"] == "Issued":
        print("Issued book cannot be removed.")
    else:
        books.remove(book)
        print("Book removed successfully.")
    pause()
def update_category():
    heading("UPDATE BOOK CATEGORY")
    book = find_book(integer("Enter book ID: "))
    if book is None:
        print("Book not found.")
    else:
        category = input("Enter new category: ").strip()
        if category:
            book["category"] = category
            print("Category updated.")
        else:
            print("Category cannot be empty.")
    pause()
def add_member():
    heading("ADD MEMBER")
    member_id = integer("Enter member ID: ")
    if find_member(member_id):
        print("Member ID already exists.")
        pause()
        return
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    if not name or not phone:
        print("All fields are required.")
    else:
        members.append({
            "id": member_id, "name": name,
            "phone": phone, "books": []
        })
        print("Member added successfully.")
    pause()
def display_members():
    heading("ALL MEMBERS")
    if not members:
        print("No members registered.")
    else:
        for m in members:
            print("ID:", m["id"], "| Name:", m["name"])
            print("Phone:", m["phone"], "| Books:", m["books"] or "None")
            line()
    pause()
def search_member():
    heading("SEARCH MEMBER")
    key = input("Enter name or phone: ").strip().lower()
    if not key:
        print("Search field cannot be empty.")
        pause()
        return
    found = False
    for m in members:
        if key in m["name"].lower() or key in m["phone"].lower():
            print("ID:", m["id"])
            print("Name:", m["name"])
            print("Phone:", m["phone"])
            print("Books:", m["books"] or "None")
            line()
            found = True
    if not found:
        print("No matching member found.")
    pause()
def update_phone():
    heading("UPDATE MEMBER PHONE")
    member = find_member(integer("Enter member ID: "))
    if member is None:
        print("Member not found.")
    else:
        phone = input("Enter new phone: ").strip()
        if phone:
            member["phone"] = phone
            print("Phone updated successfully.")
        else:
            print("Phone cannot be empty.")
    pause()
def issue_book():
    heading("ISSUE BOOK")
    book = find_book(integer("Enter book ID: "))
    member = find_member(integer("Enter member ID: "))
    if book is None:
        print("Book not found.")
    elif member is None:
        print("Member not found.")
    elif book["status"] == "Issued":
        print("Book is already issued.")
    elif len(member["books"]) >= 3:
        print("A member can issue maximum 3 books.")
    else:
        book["status"] = "Issued"
        book["issued_to"] = member["name"]
        member["books"].append(book["id"])
        transactions.append({
            "book_id": book["id"], "title": book["title"],
            "member": member["name"], "action": "Issued"
        })
        print("Book issued successfully.")
    pause()
def return_book():
    heading("RETURN BOOK")
    book = find_book(integer("Enter book ID: "))
    if book is None:
        print("Book not found.")
    elif book["status"] == "Available":
        print("Book is already available.")
    else:
        name = book["issued_to"]
        member = None
        for m in members:
            if m["name"] == name:
                member = m
                break
        if member and book["id"] in member["books"]:
            member["books"].remove(book["id"])
        transactions.append({
            "book_id": book["id"], "title": book["title"],
            "member": name, "action": "Returned"
        })
        book["status"] = "Available"
        book["issued_to"] = ""
        print("Book returned successfully.")
    pause()
def issued_books():
    heading("ISSUED BOOKS")
    found = False
    for b in books:
        if b["status"] == "Issued":
            print("ID:", b["id"], "|", b["title"],
                  "| Issued to:", b["issued_to"])
            line()
            found = True
    if not found:
        print("No books are currently issued.")
    pause()
def available_books():
    heading("AVAILABLE BOOKS")
    found = False
    for b in books:
        if b["status"] == "Available":
            print("ID:", b["id"], "|", b["title"],
                  "|", b["author"])
            found = True
    if not found:
        print("No books are currently available.")
    pause()
def transactions_report():
    heading("TRANSACTION HISTORY")
    if not transactions:
        print("No transactions recorded.")
    else:
        for i, t in enumerate(transactions, 1):
            print("Transaction:", i)
            print("Book:", t["book_id"], "-", t["title"])
            print("Member:", t["member"])
            print("Action:", t["action"])
            line()
    pause()
def category_report():
    heading("CATEGORY REPORT")
    count = {}
    for b in books:
        category = b["category"]
        count[category] = count.get(category, 0) + 1
    for category in count:
        print(category, ":", count[category], "book(s)")
    pause()
def statistics():
    heading("LIBRARY STATISTICS")
    total = len(books)
    issued = 0
    for b in books:
        if b["status"] == "Issued":
            issued += 1
    available = total - issued
    print("Total Books     :", total)
    print("Available Books :", available)
    print("Issued Books    :", issued)
    print("Total Members   :", len(members))
    print("Transactions    :", len(transactions))
    if total:
        print("Available %     :", round(available / total * 100, 2))
        print("Issued %        :", round(issued / total * 100, 2))
    pause()
def menu():
    while True:
        heading("LIBRARY MANAGEMENT SYSTEM")
        print("1.  Library Information")
        print("2.  Add Book")
        print("3.  Display Books")
        print("4.  Search Book")
        print("5.  Remove Book")
        print("6.  Add Member")
        print("7.  Display Members")
        print("8.  Search Member")
        print("9.  Issue Book")
        print("10. Return Book")
        print("11. Issued Books")
        print("12. Available Books")
        print("13. Transaction History")
        print("14. Category Report")
        print("15. Library Statistics")
        print("16. Update Member Phone")
        print("17. Update Book Category")
        print("18. Exit")
        line()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            library_information()
        elif choice == "2":
            add_book()
        elif choice == "3":
            display_books()
        elif choice == "4":
            search_book()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            add_member()
        elif choice == "7":
            display_members()
        elif choice == "8":
            search_member()
        elif choice == "9":
            issue_book()
        elif choice == "10":
            return_book()
        elif choice == "11":
            issued_books()
        elif choice == "12":
            available_books()
        elif choice == "13":
            transactions_report()
        elif choice == "14":
            category_report()
        elif choice == "15":
            statistics()
        elif choice == "16":
            update_phone()
        elif choice == "17":
            update_category()
        elif choice == "18":
            heading("THANK YOU")
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Select 1 to 18.")
print("\nWelcome to the Library Management System")
menu()
