import smtplib
from email.message import EmailMessage

#email details
senderemail="rishithajanjirala@gmail.com"
apppassword='yddu kcal nxon pfeg'
reciveremail=["srikarjanjirala92@gmail.com","rishithajanjirala03@gmail.com"]

#email content

subject='Remainder Meeting-Email Automation with python'

body="""

Hey Guys,
This is to remaind you that,
we have have python  class on how send email with python.

Regards,
Rishitha

"""

msg=EmailMessage()
msg['Subject']=subject
msg['From']=senderemail
msg['To']=reciveremail
msg.set_content(body)

#sending email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(senderemail,apppassword)
        smtp.send_message(msg)
        print("Email Sent Successfully")
except Exception as e:
    print("Something Went Wrong",e)


