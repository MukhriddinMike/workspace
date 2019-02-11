import smtplib

host= "smtp.gmail.com"
port = 587
username = "pythondev40@gmail.com"
password = 'python4.0'
from_email = username
to_list = ["pythondev40@gmail.com"]


email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(from_email,to_list,'hello my name is mike here is my email app')
email_conn.quit()