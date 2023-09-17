This task is an application of file formats and relational databases. A database name HyperionDev.db was created in the HyperionDev.py file and was populated by running SQlite in the command prompt and using .read create_database.sql. HyperionDev.db is a mock relational database based on HyperionDev, the organisation through which I completed my bootcamp in data science. In HyperionDev.py, a program allowing a user to make certain SQL queries in the database was written where certain fields are shown on the console when printed. After each query the user is given a choice to either save the query in JSON or XML format with chosen filename. The following queries are be able to be made by the user:
- Viewing all courses taken by specified student which is searched by the student 
  ID where only the subject name is shown on the console.
- Looking up an address using a first name and last name where only the street name 
  and city are displayed on the console.
- Itemising all of the course taught by a certain teacher searched using the 
  teacher ID where the course name is shown on the console.
- Listing all of the learners whose courses are incomplete by showing the student 
  number, first and last names, email addresses and course names are shown on the 
  console.
- Listing all of the students who finished their course and got a mark of 30 or 
  below where the student number, first names and surnames, email addresses and 
  marks are displayed on the console

The functionality of the code of saving the results of a query in XML/JSON form were tested and saved as results.xml and results.json.
