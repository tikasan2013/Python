import pyodbc

cn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.100.1.183;DATABASE=pes;UID=sa;PWD=inn0d@t@')
cur = cn.cursor();
cur.execute("select top 10 userid, firstname from employees")
row = cur.fetchone()
print 'userid: ', row[0]
print 'firstname: ', row.firstname
