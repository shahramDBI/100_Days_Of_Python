import smtplib
# SMTP Protocol = Simple Mail Transfer Protocol
my_email = "myemail@gmail.com"   # My Email
my_password = "123456789"
# Gmail = "smtp.gmail.com"
# Yahoo = "smtp.mail.yahoo.com"
# Hotmail = "smtp.live.com"
# TLS = Transport Layer Security
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="youremail@yahoo.com",
                        msg="Subject:Hi\n\nHello!")

