import smtplib
import datetime as dt
import random


my_email = "tobepatrick236@gmail.com"
password= "upgoczkakevoxykd"

now =dt.datetime.now()
weekDay = now.weekday()

if weekDay == 4:
    with open("qoutes.txt", encoding="utf-8") as qoutes_file:
        all_qoutes = qoutes_file.readlines()  # Read all lines
        qoute = random.choice(all_qoutes)     # Choose a random quote

    subject = "Daily Motivational Quotes"
    message = f"Subject: {subject}\n\n{qoute}"
    message = message.encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                            from_addr=my_email,
                            to_addrs="tochukwupatrick2003@gmail.com",
                            msg=message
                            )


