import smtplib

user_email = "anis2thousand@gmail.com"
password = "2Thousand"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('anis2thousand@gmail.com', '2Thousand')


# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=user_email, password=password)
# connection.sendmail(from_addr=email, to_addrs="anis2hasan@gmail.com", msg="Hello")
# connection.close()
