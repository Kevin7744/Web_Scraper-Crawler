"""
Trying to send email
"""
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')

msg['Subject'] = 'An email Alert'
msg['From'] = 'arapbiisubmissions@gmail.com'
msg['To'] = 'kevinkirui1340@gmail.com'

s = smtplib.SMTP('127.0.0.1')
s.send_message(msg)
s.quit()
