import sys
sys.path.append('fw\lib\site-packages')


from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime


app = Flask(__name__)
app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'studentdb'
mysql = MySQL(app)


@app.route('/register',methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'new_username' in request.form and 'new_password' in request.form :
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM list_user WHERE username = %s', (new_username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', new_username):
            msg = 'Username must contain only characters and numbers!'
        elif not new_username or not new_password:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO list_user (username , password) VALUES (%s, %s)', (new_username, new_password,))
            mysql.connection.commit()
            Time_Create = Set_Text_Time()
            cursor.execute('INSERT INTO ticket (Ticket_User,Ticket_Time_Create) VALUES (%s,%s)', (new_username,Time_Create,))
            mysql.connection.commit()
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)


@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('login'))


@app.route('/',methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM list_user WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['ID']
            session['username'] = account['username']
            if session['id'] == 1:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('profile'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)


@app.route('/home_admin') 
def home(): 
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM ticket')
        rows=cursor.fetchall()
        if session['id'] == 1:
            return render_template('home.html',data=rows, username=session['username'])
        else:
            return redirect(url_for('profile')) 
    return redirect(url_for('login'))

@app.route('/home_admin/refresh',methods=['GET','POST']) 
def home_refresh(): 
    if request.method == 'POST':
        value=request.form['submit_2']
        if value == "Accept":
            id_update=request.form['id_2']
            User_Status = "Accepted"
            cursor = mysql.connection.cursor()
            sql = "UPDATE ticket SET Ticket_Status=%s  WHERE Ticket_ID=%s"
            cursor.execute(sql,(User_Status,id_update,))
            mysql.connection.commit()
            return redirect(url_for('home'))
    return redirect(url_for('login'))



@app.route('/Profile') 
def profile(): 
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM ticket WHERE Ticket_ID = %s', (session['id'],))
        account = cursor.fetchone()
        if session['id'] == 1:
            return redirect(url_for('profile_admin'))
        else:
            return render_template('profile.html',account=account)
    return redirect(url_for('login'))


@app.route('/Profile_admin') 
def profile_admin(): 
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM ticket WHERE Ticket_ID = %s', (session['id'],))
        account = cursor.fetchone()
        if session['id'] == 1:
            return render_template('profile_admin.html',account=account)
        else:
            return redirect(url_for('profile'))
    return redirect(url_for('login'))


@app.route('/update',methods=['GET','POST']) 
def update(): 
    if request.method=="POST":
        value=request.form['submit']
        if value == "Resolved":
            id_update=request.form['id']
            edit_title = request.form['edit_title']
            edit_description = request.form['edit_description']
            edit_contact = request.form['edit_contact']
            edit_information = request.form['edit_information']
            User_Status = "Resolved"
            Time_Update = Set_Text_Time()
            cursor = mysql.connection.cursor()
            sql = "UPDATE ticket SET Ticket_Title=%s , Ticket_Description=%s , Ticket_Contact=%s , Ticket_Information=%s ,Ticket_Status=%s,Ticket_Time_Update=%s  WHERE Ticket_ID=%s"
            cursor.execute(sql,(edit_title,edit_description,edit_contact,edit_information,User_Status,Time_Update,id_update,))
            mysql.connection.commit()
            if session['id'] == 1:
                return redirect(url_for('home'))
            else :
                return redirect(url_for('profile'))
        elif value == "Rejected":
            id_update=request.form['id']
            User_Status = "Rejected"
            Time_Update = Set_Text_Time()
            cursor = mysql.connection.cursor()
            sql = "UPDATE ticket SET Ticket_Status=%s,Ticket_Time_Update=%s  WHERE Ticket_ID=%s"
            cursor.execute(sql,(User_Status,Time_Update,id_update,))
            mysql.connection.commit()
            if session['id'] == 1:
                return redirect(url_for('home'))
            else :
                return redirect(url_for('profile'))
    else :
        return redirect(url_for('profile'))
        

@app.route('/Send',methods=['POST']) 
def User_Send(): 
    if request.method=="POST":
        id_update=request.form['id']
        edit_title = request.form['edit_title']
        edit_description = request.form['edit_description']
        edit_contact = request.form['edit_contact']
        edit_information = request.form['edit_information']
        User_Status = "Sending"
        cursor = mysql.connection.cursor()
        sql = "UPDATE ticket SET Ticket_Status=%s , Temp_Title=%s , Temp_Description=%s , Temp_Contact=%s , Temp_Information=%s WHERE Ticket_ID=%s"
        cursor.execute(sql,(User_Status,edit_title,edit_description,edit_contact,edit_information,id_update,))
        mysql.connection.commit()
        if session['id'] == 1:
            return redirect(url_for('profile_admin'))
        else :
            return redirect(url_for('profile'))
    else :
        return redirect(url_for('profile'))


def Set_Text_Time():
    Time_Now = datetime.datetime.now()
    Day_Now = str(Time_Now.day)
    Mouth_Now = str(Time_Now.month)
    Year_Now = str(Time_Now.year)
    Hour_Now = str(Time_Now.hour)
    Minute_Now = str(Time_Now.minute)
    Second_Now = str(Time_Now.second)
    All_Date_Now = str(Hour_Now+":"+Minute_Now+":"+Second_Now+" "+Day_Now+"/"+Mouth_Now+"/"+Year_Now)
    return All_Date_Now


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8000)