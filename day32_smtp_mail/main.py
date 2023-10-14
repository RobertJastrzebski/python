import smtplib
import ship


my_email =ship.my_email
reciver_email=ship.reciver_email
password=ship.password
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=reciver_email,
        msg="Subject:Witam serdecznie \n\n Nowa wiadowmosc tekstowa ")
