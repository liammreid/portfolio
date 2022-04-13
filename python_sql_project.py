#Import
import mysql.connector
from mysql.connector import Error
import pandas as pd

#Connecting to MySQL Server
def create_server_connection(localhost:3306, root, sqlproject2022):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = localhost:3306,
            user = root,
            passwd = sqlproject2022
            )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
    
connection = create_server_connection("localhost3306", "root", "sqlproject2022")


# #How to Run a Query
def ExecuteQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query successful!")
    except Error as err:
        print(f"Error:'{err}'")
        
def ReadQuery(connection,query):# Reading the Query
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err: #returning error if theres an error message
        print(f"Error: '{err}'")

# #Running a simple query to test the connection
q1 = """
SELECT *
FROM STUDENT;
"""

connection = create_db_connection("localhost", "root",pw,db)
results = read_query(connection, q1)

for result in results:
  print(result)
  
 
# Returns a list of lists and then creates a pandas DataFrame
db = []

for result in results:
  result = list(result)
  db.append(result)


columns = ["student_id", "first_name", "last_name", "grade", "major"]
df = pd.DataFrame(db, columns=columns)

print(db)
