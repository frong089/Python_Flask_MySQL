# Python_Flask_MySQL
Flask connect MySQL
Projet
    งานนี้ทำให้ผู้ใช้งานโปรแกรมเมอร์ สามารถเปิด Server Local ได้โดยใช้ Flask เชื่อมต่อกับ Mysql แบบง่าย

Tools
    1.Python 
    2.MySQL (XAMPP)
    3.HTML
    4.CSS (Bootstrap)
    5.Visual studio code

Prepare
    1.XAMPP
        1.1 ดาวโหลดและติดตั้ง Xampp เพื่อเปิดการเชื่อต่อกับ Mysql ลิ้งดาวโหลด https://www.apachefriends.org/download.html
        1.2 หลังติดตั้งเปิด XAMPP Control Panel กดปุ่ม Start ช่อง MySQL และ Apche
        1.3 กดปุ่ม Admin ช่อง MySQL เพื่อเข้าหน้าเว็บ phpMyAdmin
        1.4 หน้า phpMyAdmin กด New เพื่อเพิ่มในแท็ปซ้ายมือจากนั้นตั้งชื่อ Database ว่า "studentdb" แล้วกด Create
        1.5 กดที่ชื่อ Database ที่ตั้งแล้วกด Go ในมุมซ้ายล่างแท็ปขวา Create table 
        1.6 table 1 ตั้งชื่อว่า "list_user" เก็บรายชื่อสมาชิก ID, username, password
        1.7 ทำซ้ำในข้อ 1.5 table 2 ตั้งชื่อว่า "ticket" เก็บข้อมูลของแต่ละสมาชิก Ticket_ID, Ticket_Title, Ticket_Description, Ticket_Contact, Ticket_Information, Ticket_Status, Ticket_Time_Create ,Ticket_Time_Update ,Ticket_User,Temp_Title,Temp_Description,Temp_Contact,Temp_Information
        1.8 สร้างรายชื่อ ID ที่ 1 เพื่อตั้งให้เป็น Admin ทั้ง 2 Table
    2.Python
        2.1 ดาวโหลดและติดตั้ง Python ลิ้งดาวโหลด https://www.python.org/downloads/
    
Run
    1.กด Start พิมหา Command Prompt 
    2.พิมคำสั่ง cd {ชื่อโฟรเดอร์} ไปยังโฟลเดอร์ flaskweb อย่างเช่น C:\Users\{PC_Name}\Desktop\flaskweb>
    3.หลังจากนั้นพิมคำสั่ง python app.py หรือ python3 app.py
    4.ในหน้าจอ Command Prompt จะมีข้อความขึ้นว่า 
        * Running on http://192.168.X.XXX:8000/ (Press CTRL+C to quit)
      นำข้อความ http://192.168.X.XXX:8000/ ใส่ในหน้า Browser เพื่อเปิดหน้าเว็บได้
    5.สามารถปิด Server โดยการกด CTRL+C ใน Command Prompt
     
