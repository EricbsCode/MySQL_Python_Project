import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Eric102199!')
    if connection.is_connected():

        subjectsValues = [('ORA','ORACLE DATABASE'),
                          ('JAVA','JAVA LANGUAGE'),
                          ('JEE','JAVA ENTEPRISE EDITION'),
                          ('VB','VISUAL BASIC.NET'),
                          ('ASP','ASP.NET')]
        
        publishersValues = [(1,'WILLEY','WDT@VSNL.NET','9112326087'),
                            (2,'WROX','INFO@WROX.COM',None),
                            (3,'TATA MCGRAWHILL','FEEDBACK@TATAMCGRAWHILL.COM','9133333322'),
                            (4,'TECHMEDIA','BOOKS@TECHMEDIA.COM','9133257660')]

        authorsValues =[(101, 'HERBERT SCHILD','HERBERT@YAHOO.COM','2137823450'),
                        (102, 'JAMES GOODWILL','GOODWILL@HOTMAIL.COM','9095871243'),
                        (103, 'DAVAID HUNTER','HUNTER@HOTMAIL.COM','9094235581'),
                        (104, 'STEPHEN WALTHER','WALTHER@GMAIL.COM','2138773902'),
                        (105, 'KEVIN LONEY','LONEY@ORACLE.COM','9493423410'),
                        (106, 'ED. ROMANS', 'ROMANS@THESERVERSIDE.COM','9495012201')]
        
        titlesValues = [(1001,'ASP.NET UNLEASHED',4,'ASP','2002-04-02','HARD COVER',540),
                        (1002,'ORACLE10G COMP. REF.',3,'ORA','2005-05-01','PAPER BACK',575),
                        (1003,'MASTERING EJB',1,'JEE','2005-02-03','PAPER BACK',475),
                        (1004,'JAVA COMP. REF',3,'JAVA','2005-04-03','PAPER BACK',499),
                        (1005,'PRO. VB.NET',2,'VB','2005-06-15','HARD COVER',450),
                        (1006,'INTRO. VB.NET',2,'VB','2002-12-02','PAPER BACK',425)]

        titleAuthorsValues =   [(1001,104,1),
                                (1002,105,1),
                                (1003,106,1),
                                (1004,103,1),
                                (1005,103,1),
                                (1005,102,2)]



        publishersTable = "CREATE TABLE publishers(pubID INT(3) NOT NULL PRIMARY KEY, pname VARCHAR(30) NULL, email VARCHAR(50) NULL, phone VARCHAR(30) NULL, UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE)"
        
        subjectsTable = "CREATE TABLE subjects(subID VARCHAR(5) NOT NULL PRIMARY KEY, sName VARCHAR(30) NULL)"

        authorsTable = "CREATE TABLE authors(auID INT(5) NOT NULL PRIMARY KEY, aName VARCHAR(30) NULL, email VARCHAR(50) NULL, phone VARCHAR(30) NULL, UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE)"
        
        titlesTable = """CREATE TABLE titles(
            titleID INT(5) NOT NULL,
            title VARCHAR(30) NULL,
            pubID INT(3) NULL,
            subID VARCHAR(5) NULL,
            pubDate DATE NULL,
            cover VARCHAR(10) NULL,
            price INT(4) NULL,
            PRIMARY KEY (titleID),
            INDEX pubid_idx (pubID ASC) VISIBLE,
            INDEX subid_idx (subID ASC) VISIBLE,
            CONSTRAINT pubid
                FOREIGN KEY (pubID)
                REFERENCES publishers (pubID)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT subid
                FOREIGN KEY (subID)
                REFERENCES subjects (subID)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        )"""
        
        titleAuthorsTable = """CREATE TABLE titleauthors(
            titleID INT(5) NOT NULL,
            auID INT(5) NOT NULL,
            importance INT(2) NULL,
            PRIMARY KEY (titleID, auID),
            INDEX auID_idx (auID ASC) VISIBLE,
            CONSTRAINT titleid
                FOREIGN KEY (titleID)
                REFERENCES titles (titleID)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT auID
                FOREIGN KEY (auID)
                REFERENCES authors (auID)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        )"""

        publishersInsertion = "INSERT INTO publishers (pubID, pname, email, phone) VALUES (%s, %s, %s, %s)"

        subjectsInsertion = "INSERT INTO subjects (subID, sName) VALUES (%s, %s)"

        authorsInsertion = "INSERT INTO authors (auID, aName, email, phone) VALUES (%s, %s, %s, %s)"

        titlesInsertion = "INSERT INTO titles (titleID, title, pubID, subID, pubDate, cover, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        titleAuthorsInsertion = "INSERT INTO titleAuthors (titleID, auID, importance) VALUES (%s, %s, %s)"

        cursor = connection.cursor()

        #cursor.execute(publishersTable)
        #cursor.execute(subjectsTable)
        #cursor.execute(authorsTable)
        #cursor.execute(titlesTable)
        #cursor.execute(titleAuthorsTable)
        #cursor.execute("SELECT * FROM titles")

        #for x in cursor:
        #    print(x)

        #for x, publisher in enumerate(publishersValues):
        #    cursor.execute(publishersInsertion, publisher)

        #for x, subject in enumerate(subjectsValues):
        #    cursor.execute(subjectsInsertion, subject)

        #for x, author in enumerate(authorsValues):
        #    cursor.execute(authorsInsertion, author)

        #for x, title in enumerate(titlesValues):
        #    cursor.execute(titlesInsertion, title)

        for x, titleAuthor in enumerate(titleAuthorsValues):
            cursor.execute(titleAuthorsInsertion, titleAuthor)

        connection.commit()


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")