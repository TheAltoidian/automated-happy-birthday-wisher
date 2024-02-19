##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import pandas as pd
import datetime as dt
from random import randint

# dictionary of people with their birthdays and emails
data = pd.read_csv("birthdays.csv")
birthday_dict = {row['name']: {"email": row['email'], "month":row['month'], "day":row['day']} for (index, row) in data.iterrows()}

# get today's month and date
now = dt.datetime.now()
day = now.day
month = now.month

# get the name and email address of whose birthday is today
for name in birthday_dict:
    if birthday_dict[name]["month"] == month:
        if birthday_dict[name]["day"] == day:
            celebrant = name
            email = birthday_dict[name]["email"]

# create a birthday email for the person whose birthday is today
try:
    letter_number = randint(1,3)
    with open(f"./letter_templates/letter_{letter_number}.txt") as file:
        template = file.read()
        filled_letter = template.replace("[NAME]", celebrant)
        with open("birthday_email", "w") as birthday_email:
            birthday_email.write(filled_letter)
except NameError:
    pass
