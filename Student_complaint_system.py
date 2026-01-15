complaints = []

def add_complaint():
    name = input("Enter student name: ")
    issue = input("Enter complaint: ")
    complaints.append({"name": name, "issue": issue})
    print("Complaint submitted successfully")

def view_complaints():
    if not complaints:
        print("No complaints submitted")
    else:
        for complaint in complaints:
            print(complaint["name"], "-", complaint["issue"])

def main():
    while True:
        print("1. Submit Complaint")
        print("2. View Complaints")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()

