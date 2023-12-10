Overview: COMP3005 Project relating to the implementation of a Health and Fitness Club Management System. This system will allow for users to register accounts and register for training sessions with trainers. This system will also allow for the staff members to attend sessions and monitor the usage of certain resources.

Build Status: As of 2023-12-10, a majority of the functionality is in place for the manipulation of the database through the use of a console-based user interface.

Code Style: Primarily coded in Python with the use of MySQL WorkBench 8.0 CE for database manipulation. 

How to Use:
To connect to the server, the need for the "SQL Tools" extension specifically for "MySQL" will be needed. You will then need to connect to the MySQL server using the following credentials: server: localhost, port: 3306, username: "root", password: "1234", database: "healt_fitness_club_management". The same information can be found in the "settings.json" file found in the ".vscode" folder. Upon establishing a connetion, the user will be able begin by running the "MySQL LocalSession.sql" file which will initialize the tables in the database. After initialization is complete, running "main.py" will begin the program and by typing in the console in accordance with what is printed to the user, the user will be able to navigate through the features of the system. 