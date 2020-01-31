"""
@author: Rodrigo Rangel

@description: - This script focuses on implementing the
                pyodbc library to connect to an existing
              - DB2 database
              - Below the following are covered:
                  1. SQL Connection
                  2. SQL Examples: Select Data
                  3. SQL Examples: Insert Data
                  4. SQL Examples: Update Data

"""

#-----------------------------------------------------------------------------#
#                              SQL Conenction                                 #
#-----------------------------------------------------------------------------#

# Dependencies
import pyodbc 
import pandas as pd # Optional

# Login Credentials
username = 'USERNAME_HERE'
password = 'PASSWORD_HERE'

# Creating DB2 Connection/cursor
database = 'DATABASE_NAME_HERE'
connection_string = 'DSN='+str(database)+';UDI='+str(username)+';PWD'+str(password)
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

#-----------------------------------------------------------------------------#
#                       SQL Examples: Select Data                             #
#-----------------------------------------------------------------------------#

query = """ 
		SELECT COLUMN1, COLUMN2
		FROM SHEMA.TABLE
		"""
		
		
# Executing Query
cursor.execute(query)
rows = cursor.fetchall()   # This will return all rows

# Pulling Column Names
column_names = [var[0] for var in cursor.description]
      
# Drop Into Pandas If Perfered (Optional)
data = pd.DataFrame([list(row) for row in rows])
data.columns = column_names


#-----------------------------------------------------------------------------#
#                       SQL Examples: Insert Data                             #
#-----------------------------------------------------------------------------#

value1 = 'SOME VALUE X'
value2 = 'SOME VALUE Y'
query = """
        INSERT INTO SCHEMA.TABLE (COLUMN1, COLUMN2)
        VALUES ('{}','{}')
        """.format(value1,value2)
cursor.execute(query)
connection.commit() 
    
#-----------------------------------------------------------------------------#
#                       SQL Examples: Update Data                             #
#-----------------------------------------------------------------------------#   

value1 = 'SOME VALUE X'
value2 = 'SOME VALUE Y'
query = """
        UPDATE SCHEMA.TABLE
        SET VARIABLE_HERE = '{}'
        WHERE VARIABLE_CONDITION = '{}'
        """.format(value1,value2)
        
cursor.execute(query)
connection.commit() 
