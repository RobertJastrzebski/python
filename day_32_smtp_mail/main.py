# import smtplib
# import ship
#
#
# my_email =ship.my_email
# reciver_email=ship.reciver_email
# password=ship.password
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=reciver_email,
#         msg="Subject:Witam serdecznie \n\n Nowa wiadowmosc tekstowa 1 ")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()+1
print(day_of_the_week)

date_of_birth = dt.datetime(year=1983,month=12,day=25,hour=12)
print(date_of_birth)


