import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="health_fitness_club_management"
)

# Create a cursor
mycursor = db.cursor()

sqlFormula_member = "INSERT INTO member (Name, Email, ContactNumber, DateOfBirth, FitnessGoals, LoyaltyPoints) VALUES (%s, %s, %s, %s, %s, %s)"

sqlFormula_trainer = "INSERT INTO trainer (Name, Email, ContactNumber, DateOfBirth, Certification) VALUES (%s, %s, %s, %s, %s)"

sqlFormula_admin = "INSERT INTO admin (Name, Email, ContactNumber, DateOfBirth) VALUES (%s, %s, %s, %s)"

sqlFormula_session = "INSERT INTO session (Date, ProgressNotes) VALUES (%s, %s)"

sqlFormula_clubResources = "INSERT INTO clubresources (Name, Status) VALUES (%s, %s)"

#By default, lets insert a trainer since a member needs a trainer on creation
#Checks if there is no existing table
if mycursor.fetchall is None: 
    default_trainer = ("John Smith", "johnsmith@gmail.com", "613-111-1111", "2023-12-10", 7)
    mycursor.execute(sqlFormula_trainer, default_trainer)
    db.commit()

    default_admin = ("Jimothy Tom", "jimtom@gmail.com", "613-555-1523", "2023-12-10")
    mycursor.execute(sqlFormula_admin, default_admin)
    db.commit()

    default_resource = ("Dumbells, Available")
    mycursor.execute(sqlFormula_clubResources, default_resource)
    db.commit()
else:
    pass

#Basic UI

run = True

while run:
    print("Health and Fitness Club Management System:\n")

    userInput = input("Please Select Your Role: (Member | Staff)\n")

    if userInput == "Member": 
        userInput = input("What would you like to do: \n(Register | Sign In)\n")
        if userInput == "Register":
            #No userInput check
            userInput = input("Please enter your Name: ")
            name = userInput
            userInput = input("Please enter your Email: ")
            email = userInput
            userInput = input("Please enter your Contact Number: ")
            contactNumber = userInput
            userInput = input("Please enter your Date of Birth: ")
            dateOfBirth = userInput
            userInput = input("Please enter your Fitness Goal: ")
            fitnessGoal = userInput

            member = (name, email, contactNumber, dateOfBirth, fitnessGoal, 0)

            mycursor.execute(sqlFormula_member, member)

            db.commit()

            #Hard Coded 
            assign_trainer = "UPDATE member SET trainerID = (SELECT trainerID FROM trainer WHERE Certification = '7') WHERE Email = '" + email + "'"

            mycursor.execute(assign_trainer)

            db.commit()

            print("You are now registered " + name + ". Welcome to the Health and Fitness Club!\n")
        elif "Sign In":
            userInput = input("Please provide your email address: \n")
            user_address = userInput

            userInput = input("What would you like to do: \n(Schedule Session | Reschedule Session | View Profile | Exit) \n")

            if userInput == "Schedule Session":

                userInput = input("What time would you like to book: \n")
                date = userInput

                session = (date, "")

                mycursor.execute(sqlFormula_session, session)
                
                db.commit()

                assign_session = "UPDATE member SET sessionID = (SELECT sessionID FROM session WHERE Date = '" + date + "') WHERE Email = '" + user_address + "'"

                print("You are now registered for a session at " + date + ". Enjoy ur training!")

            elif userInput == "Reschedule Session":

                userInput = input("Please enter the date for the session you would like to reschedule: \n")
                date = userInput

                userInput = input("Would you like to cancel or change the date?\n(Cancel | Change | Exit): \n")
                action = userInput

                if action == "Cancel":
                    cancel = "DELETE FROM session WHERE Date = '" + date + "'"

                    mycursor.execute(cancel)
                    db.commit()

                    update_user = "UPDATE member SET sessionID = null WHERE Email = '" + user_address + "'"

                    mycursor.execute(update_user)
                    db.commit()

                    print("Session Cancelled")

                elif action == "Change":
                    userInput = input("Please type the date you would like to reschedule to: \n")
                    date = userInput

                    change = "UPDATE session SET Date = '" + date +"' WHERE sessionID = (SELECT sessionID FROM member WHERE Email = '" + user_address + "')"

                    mycursor.execute(change)
                    db.commit()

                    print("Session Date Changed")

                else:
                    pass

            elif userInput == "View Profile":
                mycursor.execute("SELECT * FROM member WHERE Email = '" + user_address + "'")
                result = mycursor.fetchall()

                for row in result:
                    print("Name: " + row[1])
                    print("Email: " + row[2])
                    print("Contact Number: " + row[3])
                    print("Date of Birth: " + str(row[4]))
                    print("Fitness Goal: " + row[5])
                    print("Loyalty Points: " + str(row[6]) + "\n")
                
            else:
                pass

    elif userInput == "Staff":
        userInput = input("Select the kind of staff member: \n(Trainer | Admin)")
        staff = userInput

        userInput = input("Please provide your email address: \n")
        user_address = userInput

        if staff == "Trainer":
            userInput = input("What would you like to do: \n(Attend Session | View Member Profile | View Profile | Progress Notes | Exit) \n")

            if userInput == "Attend Session":
                mycursor.execute("SELECT sessionID FROM member WHERE trainerID = (SELECT trainerID FROM trainer WHERE Email = '" + user_address + "')")
                result = mycursor.fetchall

                if result != "null":
                    mycursor.execute("SELECT Date FROM session WHERE sessionID = '" + result + "'")
                    result = mycursor.fetchall()
                    userInput = input("You have a session at " + result + ". Would you like to attend it? (Yes | No | Exit)")

                    if userInput == "Yes":
                        update_user = "UPDATE trainer SET sessionID = '" + result + "' WHERE Email = '" + user_address + "'"

                        mycursor.execute(update_user)
                        db.commit()

                        print("You are now attending that session")

                    elif userInput == "No":
                        print("No problem")

                    else:
                        pass
            elif userInput == "View Member Profile":
                userInput = input("Enter the address of the member you would like to view:\n")
                member = userInput

                mycursor.execute("SELECT * FROM member WHERE Email = '" + member + "'")
                result = mycursor.fetchall()

                for row in result:
                    print("Name: " + row[1])
                    print("Email: " + row[2])
                    print("Contact Number: " + row[3])
                    print("Date of Birth: " + str(row[4]))
                    print("Fitness Goal: " + row[5])
                    print("Loyalty Points: " + str(row[6]) + "\n")

            elif userInput == "View Profile":
                mycursor.execute("SELECT * FROM trainer WHERE Email = '" + user_address + "'")
                result = mycursor.fetchall()

                for row in result:
                    print("Name: " + row[1])
                    print("Email: " + row[2])
                    print("Contact Number: " + row[3])
                    print("Date of Birth: " + str(row[4]))
                    print("Certification: " + str(row[5]) + "\n")

            elif userInput == "Progress Notes":
                userInput = input("Would you like to write notes or read notes? (Write | Read | Exit): \n")

                action = userInput

                if action == "Write":
                    userInput = input("Please provide the date for session you want to write notes for:\n")
                    date = userInput

                    userInput = input("What would you like to say about the session?\n")
                    notes = userInput

                    update_notes = "UPDATE session SET ProgressNotes = '" + notes + "' WHERE trainerID = (SELECT trainerID FROM trainer WHERE Email = '" + user_address + "')"

                    mycursor.execute(update_notes)
                    db.commit()

                    print("Notes Updated\n")
                elif action == "Read":
                    userInput = input("Please provide the date for session you want to read notes for:\n")
                    date = userInput

                    mycursor.execute("SELECT ProgressNotes FROM session WHERE Date = '" + date + "'")
                    result = mycursor.fetchall()

                    print(result)

                else:
                    pass

        if staff == "Admin":
            userInput = input("What would you like to do: \n(Oversee Session | Manage Resource | Exit)\n")

            if userInput == "Oversee Session":
                userInput = input("Please enter the date for the session you would like to oversee:\n")

                date = userInput

                update_user = "UPDATE admin SET sessionID = (SELECT sessionID FROM session WHERE Date = '" + date + "')"

                mycursor.execute(update_user)
                db.commit()

                print("You are now overseeing that session")


            elif userInput == "Manage Resource":
                #Only resource that exists is Dumbells
                userInput = input("What resource would you like to manage? (Please enter the Name)\n")

                resource = userInput

                userInput = input("Set to Available or Unavailable?\n")
                status = userInput

                update_user = "UPDATE admin SET resourceID = (SELECT resourceID FROM clubresources WHERE Name = '" + resource + "') WHERE Email = '" + user_address + "'"

                mycursor.execute(update_user)
                db.commit()

                update_resource = "UPDATE clubresources SET adminID = (SELECT adminID FROM admin WHERE Email = '" + user_address + "') WHERE Name = '" + resource + "'"

                mycursor.execute(update_resource)
                db.commit()

                set_status = "UPDATE clubresources SET status = '" + status + "'"

                mycursor.execute(set_status)
                db.commit()
                
                print("You are now managing that resource")

            else: 
                pass
        else:
            pass
    else:
        run = False
        pass

            
            
            

