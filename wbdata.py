import sqlite3

# conn=sqlite3.connect('d:\lifetrac\main.db')
conn = sqlite3.connect(":memory:")
cu=conn.cursor()

cu.execute("create table wb (id integer primary key,content varchar(288))")
cu.execute("insert into wb values(0,'test1dsf obama recall')")
cu.execute("insert into wb values(1,'lil xii recall')")
# conn.commit()

cu.execute("select * from wb")
# cu.fetchall()
# print cu.fetchone()

i=1
for item in cu.fetchall():
	for element in item:
		print element
		print i
		i=i+1
	print

t='0'
cu.execute('SELECT * FROM wb WHERE id=?', t)

'''
# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

c.execute("UPDATE catalog SET trans='SELL' WHERE symbol = 'IBM'")
'''

cu.execute("delete from wb")
cu.execute("drop table wb")

conn.close;

