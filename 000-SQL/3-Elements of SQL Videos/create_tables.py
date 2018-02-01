##  After all the success promoting your music tour last section, 
##  a new friend has asked to partner up and build your own music website!
##  You'll need to rebuild your own database and import the data to your new system.

##  Let's first take a closer look at how to build and populate your local database.
##  The box below shows the Album table schema including Primary and Foreign Keys.
##  Have a look at this table and the CREATE TABLE statement below to see how they 
##  relate.

'''
First, disconnect from your Chinook database.
> .exit

Create a new database named whatever you'd like your store to be called.
$ sqlite3 UdaciousMusic.db

Now we can populate this database with our first table.

Here's a graphic showing some information about the Album table.
We can use this to build a table in our new database.

######################################################################
#                         Table: Album                               #
######################################################################
+--------------------+---------------+-----------------+--------------+
|      Columns       |   Data Type   |    Primary Key  |  Foreign Key |
+====================+===============+=================+==============+ 
|      AlbumId           INTEGER            YES              NO       |
|      Title             TEXT               NO               NO       |
|      ArtistId          INTEGER            NO               YES      |
|      UnitPrice         REAL               NO               NO       |
|      Quantity          INTEGER            NO               NO       |
+====================+===============+=================+==============+ 

We can use this information to decide how our schema should look.
Do you see how the schema below reflects the table above?

CREATE TABLE Album
(
    AlbumId INTEGER PRIMARY KEY,
    Title TEXT,
    ArtistId INTEGER,
    FOREIGN KEY (ArtistId) REFERENCES Artist (ArtistId) 
);

Try pasting the schema into your local database.  
Let's check to see if anything happened.

sqlite> .tables
Album <--- Do you see the Album table?  I hope so!

Now, do we have any data in our new table?

sqlite> SELECT * FROM Album;

Do you see data?  I hope not, we haven't added any yet!

Open the Album.sql tab.  You can copy and paste these lines directly into 
your sqlite terminal. (Use Ctrl+A or Command+A to select all lines when the
code editor is selected to select all the lines at once.)

Now try to run your query again.  You've got data... NICE!

'''
##  Use the previous example to help you construct the InvoiceLine table.
##  When you're ready, run you query to CREATE and populate the InvoiceLine table 
##  using data from the InvoiceLine.sql file. 

QUERY='''
CREATE TABLE InvoiceLine
(
    InvoiceLineID INTEGER PRIMARY KEY,
    InvoiceId INTEGER,
    TrackId INTEGER,
    UnitPrice REAL,
    Quantity INTEGER,
    FOREIGN KEY (InvoiceId) REFERENCES Invoice (InvoiceId),
    FOREIGN KEY (TrackId) REFERENCES Track (TrackId)
);
'''

'''
######################################################################
#                         Table: InvoiceLine                         #
######################################################################
+--------------------+---------------+-----------------+--------------+
|      Columns       |   Data Type   |    Primary Key  |  Foreign Key |
+====================+===============+=================+==============+ 
|      InvoiceLineId     INTEGER            YES              NO       |
|      InvoiceId         INTEGER            NO               YES      |
|      TrackId           INTEGER            NO               YES      |
|      UnitPrice         REAL               NO               NO       |
|      Quantity          INTEGER            NO               NO       |
+====================+===============+=================+==============+ 
'''

##  These examples should help you build any remaining tables from the Chinook database.

##  Use .schema when connected to the Chinook database to see the tables and columns 
##  in your Chinook database, and try recreating them in your new database.
##  You can populate these tables using the sql files from the Downloadables section, or 
##  with CSV files, which you'll learn to do next!



'''
WORKING WITH CSV’s in SQLite
Working with CSV's in SQLite is simple :)

You're able to both import CSV files and export data as CSV files from SQLite.

EXPORT DATA TO CSV FROM DATABASE
sqlite> .mode csv
sqlite> .output newFile.csv
sqlite> SELECT * FROM myTable;
sqlite> .exit
IMPORT YOUR CSV INTO A TABLE
$ sqlite3 new.db   <--- If you'd like your csv's in a new database remember to make it first.

sqlite> CREATE TABLE myTable() <--- Build your schema!
sqlite> .mode csv
sqlite> .import newFile.csv myTable
There are a few limitations you'll come up against working this way. SQLite can't handle EVERYTHING but it's a great start!

You'll learn a ton about how to handle more complex data if you take our Data Wrangling course.

If you are doing our OpenStreetMaps project, you'll be able to import CSV's just like we do here.


'''



