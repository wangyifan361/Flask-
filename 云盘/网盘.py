#encoding:utf-8
#templates需要disk和diskfile
from flask import Flask ,render_template,request,url_for,redirect
import os,sqlite3
app = Flask(__name__)
app.config["SECRET_KEY"] = "hellokey"
@app.route('/disk',methods=['POST', 'GET'])
def disk():
    if request.method == 'POST':   
        name=request.form['user']
        formpassword=request.form['password']#提取表单数据
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        sql="select * from user where username = "+'"'+str(name)+'"'#拼接寻找用户名和密码的SQL语句
        find=c.execute(sql)#查询结果
        result=find.fetchall()
        if len(result) ==0:
            return "未注册"
        else:
            pass
        username=result[0][0]
        password=result[0][1]
        if  formpassword != password:
            return "密码错误"
        else:
            wz=os.getcwd()+str("\\")+"static"+"\\"+username
            filelist=os.listdir(wz)
            c.close()
            conn.close()
            return render_template("diskfile.html",filelist=filelist,username=username)
        return render_template("disk.html")
        
    else:
        return render_template("disk.html")
@app.route('/')
def mainpage():
    return render_template("mainpage.html")
@app.route('/register',methods=['POST', 'GET'])
def register():
    if request.method == 'POST':   
        name=request.form['user']
        formpassword=request.form['password']#提取表单数据
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        sql="select * from user where username = "+'"'+str(name)+'"'#拼接寻找用户名和密码的SQL语句
        find=c.execute(sql)#查询结果
        result=find.fetchall()
        if len(result) ==0:
            sql1='insert into user(username,password)values('
            sql2='"'
            sql3=sql2+name+sql2+","+sql2+formpassword+sql2+')'
            sql=sql1+sql3
            c.execute(sql)
            conn.commit()
            c.close()
            conn.close()
            try:
                cj1=os.getcwd()
                cj1=cj1+str("\\")+"static"
                cj2=name
                cj=cj1+"\\"+cj2
                os.mkdir(cj)
            except:
                return"数据库插入成功,但是没有创建文件夹"
            return "注册成功"
            
        else:
            return "用户名已注册,请更换用户名"
    else:
        return render_template("disk.html")
@app.route('/upload',methods=['POST', 'GET'])
def uploadfile():
    if request.method == 'POST':
        filename=request.form['filename']
        name=request.form['user']
        formpassword=request.form['password']#提取表单数据
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        sql="select * from user where username = "+'"'+str(name)+'"'
        find=c.execute(sql)
        result=find.fetchall()
        if len(result)!=0:
            username=result[0][0]
            password=result[0][1]
            if name==username and formpassword==password:
                f = request.files['file']
                path=os.getcwd()+str("\\")+"static"+"\\"+username+"\\"+filename
                f.save(path)
                return "存储成功"
            else:
                return "密码错误"
        else:
            return "您还未注册"
        c.close()
        conn.close()
    else:
        return render_template("uploads.html")
@app.route('/remove',methods=['POST', 'GET'])
def removefile():
    if request.method == 'POST':   
        name=request.form['user']
        formpassword=request.form['password']#提取表单数据
        removefile=request.form['removefile']
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        sql="select * from user where username = "+'"'+str(name)+'"'#拼接寻找用户名和密码的SQL语句
        find=c.execute(sql)#查询结果
        result=find.fetchall()
        if len(result) ==0:
            return "未注册"
        else:
            pass
        username=result[0][0]
        password=result[0][1]
        if  formpassword != password:
            return "密码错误"
        else:
            wz=os.getcwd()+str("\\")+"static"+"\\"+username
            try:  
                remove=os.path.join(wz,removefile)
                os.remove(remove)
            except:
                return "文件不存在,或已删除"
            c.close()
            conn.close()
            return "删除成功"
        return render_template("remove.html")
        
    else:
        return render_template("remove.html")
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
