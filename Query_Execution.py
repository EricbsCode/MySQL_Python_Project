#This file contains the code for all the Queries 1-10 Requested
#commands.py contains all the code for setting up the mysql workbench
#all queries are commented out, to test just uncomment that Query till you arrive at the next Query
#screenshots of query results are in screenshot folder
#Results can also be found in text format in output.txt
#copy.txt is just copied code from the project document

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Eric102199!')
    if connection.is_connected():

        cursor = connection.cursor()

        #Query 1
        #print('\nContents of Publishers Table:\n')
        #cursor.execute("SELECT * FROM publishers")
        #for x in cursor:
        #    print(x)


        #Query 2
        #customersTable = """CREATE TABLE customers(
        #    custID INT(5) NOT NULL,
        #    custName VARCHAR(30) NULL,
        #    zip INT(5) NULL,
        #    city VARCHAR(30) NULL,
        #    state VARCHAR(15) NULL,
        #    PRIMARY KEY (custID)
        #)"""

        #cursor.execute(customersTable)
        #print('\nDescribing Customers Table:\n')
        #cursor.execute("DESCRIBE customers")
        #for x in cursor:
        #    print(x)


        #Query 3
        #customersValues =  [('1', 'ABRAHAM SILBERSCHATZ', 92395, 'Victorville', 'California'),
        #                    ('2', 'HENRY KORTH', 92395, 'Victorville', 'California'),
        #                    ('3', 'CALVIN HARRIS', 92395, 'Victorville', 'California'),
        #                    ('4', 'MARTIN GARRIX', 92395, 'Victorville', 'California'),
        #                    ('5', 'JAMES GOODWILL', 92395, 'Victorville', 'California')]
        
        #customersInsertion = "INSERT INTO customers (custID, custName, zip, city, state) VALUES (%s, %s, %s, %s, %s)"

        #for x, customer in enumerate(customersValues):
        #    cursor.execute(customersInsertion, customer)

        #print('\nContents of Customers Table:\n')
        #cursor.execute("SELECT * FROM customers")
        #for x in cursor:
        #    print(x)
        #print('\n')


        #Query 4
        #mostProlificAuthor ="""
        #                    SELECT
        #                        au.aName
        #                    FROM
        #                        authors au
        #                    JOIN
        #                        titleauthors ta ON au.auID = ta.auID
        #                    GROUP BY
        #                        ta.auID
        #                    ORDER BY COUNT(*) DESC
        #                    LIMIT 1;
        #                    """
        #
        #print('\nThe Author who has the most books in this database is:\n')        
        #cursor.execute(mostProlificAuthor)
        #for x in cursor:
        #    print(x)
        #print('\n')


        #Query 5
        #totalPublishedPrice = """
        #                        SELECT 
        #                            p.pname,
        #                            SUM(t.price) AS totalPrice
        #                        FROM 
        #                            publishers p
        #                        JOIN
        #                            titles t ON p.pubID = t.pubID
        #                        GROUP BY
        #                            p.pname
        #                      """
        #
        #print('\nPublishers and the total price of their titles:\n')
        #cursor.execute(totalPublishedPrice)
        #for x in cursor:
        #    print(x)
        #print('\n')


        #Query 6
        #javaAuthors = """
        #                SELECT 
        #                    au.aName
        #                FROM 
        #                    authors au
        #                JOIN
        #                    titleauthors ta ON au.auID = ta.auID
        #                JOIN
        #                    titles t  ON ta.titleID = t.titleID
        #                WHERE t.title LIKE '%Java%'
        #                GROUP BY 
        #                    au.aName
        #              """
        #
        #print('\nAuthors whose books have Java in the title:\n')
        #cursor.execute(javaAuthors)
        #for x in cursor:
        #    print(x)
        #print('\n')


        #Query 7
        #authorsRangePB = """
        #                    SELECT 
        #                        DISTINCT au.aName
        #                    FROM 
        #                        authors au
        #                    JOIN
        #                        titleauthors ta ON au.auID = ta.auID
        #                    JOIN
        #                        titles t  ON ta.titleID = t.titleID
        #                    WHERE 
        #                        t.cover LIKE '%PAPER BACK%'
        #                    AND
        #                        t.price > 475 
        #                    AND
        #                        t.price < 500 
        #                    GROUP BY 
        #                        au.aName
        #                 """
        #
        #print('\nAuthors who have at least one book between 475$ - 500$ and are Paper Back:\n')
        #cursor.execute(authorsRangePB)
        #for x in cursor:
        #    print(x)
        #print('\n')


        #Query 8
        #authorsVBnotORA = """
        #                    SELECT 
        #                        DISTINCT au.aName
        #                    FROM 
        #                        authors au
        #                    JOIN
        #                        titleauthors ta ON au.auID = ta.auID
        #                    JOIN
        #                        titles t  ON ta.titleID = t.titleID
        #                    JOIN
        #                        subjects s ON t.subID = s.subID
        #                    WHERE 
        #                        s.sName = 'VISUAL BASIC.NET'
        #                    AND
        #                        au.aName NOT IN (
        #                            SELECT au.aName
        #                            FROM authors au
        #                            JOIN titleauthors ta ON au.auID = ta.auID
        #                            JOIN titles t ON ta.titleID = t.titleID
        #                            JOIN subjects s ON t.subID = s.subID
        #                            WHERE s.sName = 'ORACLE DATABASE'
        #                        )
        #                 """
        #
        #print('\nAuthors who have at least one book for VisualBasic.Net, but none for Oracle:\n')
        #cursor.execute(authorsVBnotORA)
        #for x in cursor:
        #    print(x)
        #print('\n')


        #Query 9
        #namesWithGmail = """
        #                    SELECT 
        #                        au.aName
        #                    FROM 
        #                        authors au
        #                    WHERE 
        #                        au.email LIKE '%gmail.com%'
        #                    GROUP BY 
        #                        au.aName
        #                 """
        #
        #print('\nAll names whose email addresses contain gmail.com:\n')
        #cursor.execute(namesWithGmail)
        #for x in cursor:
        #    print(x)
        #print('\n')


        #Query 10
        updatePrice = """
                        UPDATE titles
                        SET price = 
                            CASE
                                WHEN pubDate < '2003-01-01' THEN price * 0.75
                                WHEN pubDate > '2004-12-31' THEN price * 0.90
                                ELSE price
                            END;
        
                      """
        print("\nOld titles table:\n")
        cursor.execute("SELECT * FROM titles")
        for x in cursor:
            print(x)
        print('\n')
        print('\nNew titles table:\n')
        cursor.execute(updatePrice)
        cursor.execute("SELECT * FROM titles")
        for x in cursor:
            print(x)
        print('\n')

        connection.commit()
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")