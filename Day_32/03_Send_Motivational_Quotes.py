import smtplib
import datetime as dt
import random

my_email = "myemail@gmail.com"   # My Email
my_password = "123456789"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as qoute_file:
        all_quotes = qoute_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smpt.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}")