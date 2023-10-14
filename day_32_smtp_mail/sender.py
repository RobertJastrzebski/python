import datetime as dt
import smtplib
import random
import ship

now = dt.datetime.now()
weekday= now.weekday()

my_email =ship.my_email
receiver_email=ship.receiver_email
password=ship.password

if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=(f"Subject: Hello cytacik  \n\n {random_quote}"))