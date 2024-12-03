import smtplib, ssl


def sent_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ashutoshswain465@gmail.com"
    password = "hwvr hddd qnhe nmah"
    receiver = "ashutoshswain465@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

