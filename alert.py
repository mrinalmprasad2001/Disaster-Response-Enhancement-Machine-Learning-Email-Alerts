import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = 'smtp.gmail.com'
smtp_port = 587  


sender_email = 'disasterauthority247@gmail.com'  
password = 'Mrinal@8928'  

recipient_email = 'imrinalmprasad2001@gmail.com' 
subject = 'Disaster alert Message'

def mail(msg):

    
    body = msg
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  
    server.login(sender_email, password)

    server.sendmail(sender_email, recipient_email, msg.as_string())

    server.quit()
