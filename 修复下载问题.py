#encoding:utf-8
#恢复下载问题
import os,sqlite3
conn=sqlite3.connect('user.db')
c=conn.cursor()
try:
    sql="select * from user"
    c.execute(sql)
    all=c.fetchall()
except:
    try:
        

print(all)
c.close()
conn.close()
where=os.getcwd()
print("当前位置为",where)
pjstatic=os.getcwd()+"//"+"static"
os.chdir(pjstatic)
for i in range(len(all)):
    username=all[i][0]
    print(username)
    try:  
        os.mkdir(username)
    except:
        pass
