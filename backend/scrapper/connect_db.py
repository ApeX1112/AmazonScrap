import psycopg2

conn=psycopg2.connect(host="localhost",dbname="data",user="postgres",password="Mohamedmos111",port="5432")
cur=conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS person(
            id INT PRIMARY KEY ,
            name VARCHAR(255),
            age INT
)
            """)

cur.execute("""INSERT INTO person (id,name,age) VALUES (5,'lol',45),(5,'ko',5)
            """)

cur.execute(""" SELECT * FROM person WHERE age<50;
            """)
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()