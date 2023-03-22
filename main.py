import datetime as dt
import os
import smtplib
import random as r
import pandas as pd

now = dt.datetime.now()
month = now.month
day = now.day

bdays_data = pd.read_csv("birthdays.csv")
# set the orientation to records so that we can access the keys and values easier
bdays_dict = bdays_data.to_dict(orient="records")
# iterate through the whole dictionary and check if it's someone's bday today
for key in bdays_dict:
    # if it's someone's bday today, we open the bday letters and randomly choose from them
    if key["month"] == month and key["day"] == day:
        dir = "letter_templates"
        f_list = os.listdir(dir)
        rand_file = r.choice(f_list)
        path = os.path.join(dir, rand_file)
    # reads the content of the letters
        with open(path, "r") as f:
            lines = f.readlines()
    # replaces the "[NAME]" in the file with the name of your friend
    # and stores the content of the file into a list
        mail_body = [line.replace("[NAME]", key["name"]) if "[NAME]" in line else line for line in lines]
    # turns the mail_body list into a text
        text = ""
        for line in mail_body:
            text += line
    # opens a connection to send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            my_email = "sintercvnt@gmail.com"
            password = os.environ.get("MY_APP_KEY")
            # secures the connection
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="sintercvnt606@yahoo.com",
                                msg=f"Subject: Happy Birthday!\n\n{text}")
