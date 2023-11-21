try:
    import database #Database list of employee records
except: # If database does not exist or has been deleted, a new empty file will be created
    print("database.py not found")
    db = open("database.py", "w") 
    db.write("#This is a list of tuples containing the records\n" + "records = []\n" +
                     "\n#This is a number that increases with every entry but does not decrease with deletions, it is used to assign a unique number to employees\n" +
                     "unique = 1")
    db.close()
    print("database.py created")
    import database
    

def write_database(): # Writes the databases current state to the database file
            db = open("database.py", "w") 
            db.write("#This is a list of tuples containing the records\n" + "records = {}\n".format(database.records) +
                     "\n#This is a number that increases with every entry but does not decrease with deletions, it is used to assign a unique number to employees\n" +
                     "unique = {}".format(database.unique))
            db.close()

def full_name(record): # Prints the first and second names in a two column table
    print(("|{:" "^20}"*2 + "|").format(record[1], record[2]))
def full_record(record):# Prints whole record
    print(("|{:" "^20}"*7 + "|").format(str(record[0]).zfill(4), record[1], record[2], record[3], record[4], "£"+str(record[5]), str(record[6])))

# This function displayes the table in a suitable format, either two columns for first and surname, or seven for a whole record
def top_table(size):
    S = size
    if S == 2:
        print("\n" + ("|{:" "^20}"*S + "|").format("Surname", "First Name"))
    elif S == 7:
        print("\n" + ("|{:" "^20}"*S + "|").format("ID Number", "Surname", "First Name", "Job Title", "Full time", "Hourly Rate", "Hours Per Week"))
    print(("|" + ("-"*20))*S + "|")

while True:
    #A menu of options
    print("\nHuman Resources department\nPersonnel Database")      
    print("Employee Records: {}".format(len(database.records))) # Counts number of records in database by checking how many tuples are in the "records" list.
    print("""
a. Add a new employee record
b. Display all employees
c. Search for employee record (view details)
d. Delete an employee record
e. Show all full-time employees
f. Show all part-time employees
g. View all records (A-Z)
h. View employees above a specified weekly cost
x. Exit
""")
    options = "abcdefghx" # Possible menu selections for input handling

    while True:
        sel = input("Choose an option (a to h) or x to Exit: ").lower() # Takes user menu selection, stores as a lower case string for easy checking
        if options.count(sel) == 1 and len(sel) == 1: # the .count() checks that the selection is a valid character, and the len() checks that there is only one character
            break

    if sel == "a": # a sequence of inputs for employee record data
        while True: 
            sname = input("Please enter the surname of the employee (Max 20 char): ").capitalize()
            if len(sname) > 0:
                break
        while True:
            fname = input("Please enter the first name of the employee (Max 20 char): ").capitalize()
            if len(fname) > 0:
                break
        while True:
            jtitle = input("Please enter the job title of the employee: ").capitalize()
            if len(jtitle) > 0:
                break
        while True:
            ft = input("Is the employee full-time? Please enter 'Y' or 'N': ").lower()
            if ft == "y":
                ft = "Yes"
                break
            elif ft == "n":
                ft = "No"
                break
        while True:
            try:
                rate = int(input("What is the employee's Hourly rate (in £)?: "))
            except:
                print("Must be a number.")
            if rate >= 0:
                break
            else:
                print("No negative numbers, please.")
        while True:
            try:
                hpw = int(input("How many hours per week does the employee work?: "))
            except:
                print("Must be a number.")
            if hpw >= 0:
                break
            else:
                print("Please only use numbers for this entry")
        database.records.append((database.unique, sname, fname, jtitle, ft, rate, hpw))
        database.unique += 1
        write_database()

    elif sel == "b": # Display all employees
        if len(database.records) > 0: # Checks that there are records to print
            top_table(2)
            for record in database.records:
                full_name(record)
        else:
            print("There are no records to print")
            
    elif sel == "c": # Search for records by name
        match = input("Please enter the first name or surname of the employee you wish to search for: ").capitalize()
        top_table(7)
        found = False
        for record in database.records:
            if record[1] == match or record[2] == match: # prints record if input is equal to first name or surname
                full_record(record)
                found = True
        if found == False: # Prints a message if there are no matches found
            print(("\n{:" "^140}").format('N0 MATCHES FOR "' + match + '" FOUND!'))
        
    elif sel == "d": # Delete an employee record
        rm = int(input("Please enter the unique ID number of the employee you wish to delete from database: "))    
        top_table(2)
        match = False
        for record in database.records:
            if record[0] == rm:
                print(("|{:" "^20}"*2 + "|").format(record[1], record[2]))
                delete = input("Are you sure you wish to delete? (Y/N): ")
                match = True
                if delete == "y":
                    database.records.remove(record)
                    write_database()
        if match == False:
            print(("\n{:" "^60}").format('N0 MATCHES FOR "' + str(rm) + '" FOUND!'))

           
    elif sel == "e": # Show all full-time employees
        if len(database.records) > 0: # Checks that there are records to print
            print("Full-time employees: \n")
            top_table(2)
            for record in database.records:
                if record[4] == "Yes":
                    full_name(record)
        else:
            print("There are no records to print")
            
    elif sel == "f": # Show all part-time employees
        if len(database.records) > 0: # Checks that there are records to print
            print("Part-time employees: \n")
            top_table(2)
            for record in database.records:
                if record[4] == "No":
                    full_name(record)
        else:
            print("There are no records to print")
            
    elif sel == "g": # Show all records in alphabetical order of surname or job title
        if len(database.records) > 0: # Checks that there are records to print
            while True:
                srt = input("Records sorted Alphabetically by [S]urname or [J]ob title?: ").lower() 
                if srt == "s":
                    top_table(7)
                    for record in sorted(database.records, key = lambda record: record[1]):
                         full_record(record)
                    break
                elif srt == "j":
                    top_table(7)
                    for record in sorted(database.records, key = lambda record: record[3]):
                         full_record(record)
                    break
                else:
                    print("Invalid entry!")
        else:
            print("There are no records to print")

    elif sel == "h": # Show everyone who costs above a certain amount per week
        if len(database.records) > 0: # Checks that there are records to print
            while True:
                try:
                    twc = int(input("Please enter the total weekly cost you want to check against employees: "))
                except:
                    print("Must be a number.")
                if twc >= 0:
                    break
                else:
                    print("No negative numbers, please.")
                    
            highest = 0 # These two variables will hold the highest and lowest weekly cost employees
            lowest = 0
            print("\nEmployees who earn more than £{} per week:\n".format(twc))
            top_table(7)
            for record in database.records:
                total = record[6] * record[5] #Hours per week multiplied by hourly rate
                if lowest == 0:
                    lowest = total
                if total > highest:
                    highest = total
                if total > twc:
                    full_record(record)
                if total < lowest:
                    lowest = total
            if twc > highest:
                print("\nNo employees Found, the highest cost per week is £{}".format(str(highest)))
            elif twc < lowest:
                print("\nAll employees earn more than £{} per week".format(str(twc)))
        else:
            print("There are no records to print")
                    
    elif sel == "x": # Exit
        break 
print("Goodbye")
