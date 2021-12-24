import psycopg2

# connect to the db
con = psycopg2.connect(
     host="localhost",
     database="sampleDatabase",
     user="postgres",
     password="clp"
)

## will be replaced
# cursor
cur = con.cursor()

table = '''create table products_initial(
   id serial primary key,
   name varchar(200) not null,
   itemType varchar(200) not null, 
   sellPrice numeric not null)'''

cur.execute(table)

# close the cursor
cur.close()

con.commit()

# close the db
con.close()
