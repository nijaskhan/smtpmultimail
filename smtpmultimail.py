import smtplib
from email.message import EmailMessage
import os

os.system('cls')

green = '\x1b[32m'
red = '\x1b[31m'
blue = '\x1b[34m'
yellow = '\x1b[33m'
backgroundyellow = '\x1b[43m'
backgroundwhite = '\x1b[47m'
stop = '\x1b[0m'

print(r"""

   ▄████████    ▄████████    ▄████████ ▄██   ▄          ▄▄▄▄███▄▄▄▄      ▄████████  ▄█   ▄█       
  ███    ███   ███    ███   ███    ███ ███   ██▄      ▄██▀▀▀███▀▀▀██▄   ███    ███ ███  ███       
  ███    █▀    ███    ███   ███    █▀  ███▄▄▄███      ███   ███   ███   ███    ███ ███▌ ███       
 ▄███▄▄▄       ███    ███   ███        ▀▀▀▀▀▀███      ███   ███   ███   ███    ███ ███▌ ███       
▀▀███▀▀▀     ▀███████████ ▀███████████ ▄██   ███      ███   ███   ███ ▀███████████ ███▌ ███       
  ███    █▄    ███    ███          ███ ███   ███      ███   ███   ███   ███    ███ ███  ███       
  ███    ███   ███    ███    ▄█    ███ ███   ███      ███   ███   ███   ███    ███ ███  ███▌    ▄ 
  ██████████   ███    █▀   ▄████████▀   ▀█████▀        ▀█   ███   █▀    ███    █▀  █▀   █████▄▄██ 
                                                                                        ▀          """)

print(f"""{blue}This is an app used to send multiple Emails by using GMAIL (THIS APP ONLY SUPPORTS GMAIL mail-ids).
We can use this app for social engineering trick in Mass Mailing Attack.
By using this App we can send unlimited emails to anyone with a just a click.

For security you have to do 2-step verification in your gmail & also enable app permissions.
we are providing the Video link in here : 'https://www.youtube.com/watch?v=pBtQ4IHkuQE' {stop}""")

print('\n')

msg = EmailMessage()

From = input("sender's EMAIL address : ")           
Pass = input("PASSWORD (sender's password) : ")

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp1:
        smtp1.login(From, Pass)
        print(f'{green} LOGIN SUCCESSFULL {stop}')
except Exception:
    print(f'{red} LOGIN FAILED ..check if you enable app permission in gmail & retry ! {stop}')
else:
    print('\n')
    numbe = input("To how many contacts {in number} : ")

    contacts = [ ]

    for i in range(int(numbe)):
        mail_id = input("reciever's mail-id : ")
        i = mail_id
        contacts.append(mail_id)
    
    print('\n')
    print(f"contacts : {contacts}")

    print('\n')
    Subject = input("subject :  ")
    print('\n')
    Body = input("your message : \n         ")

    msg['Subject'] = Subject
    msg['From'] = From
    msg['To'] = contacts

    msg.set_content(Body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(From, Pass)
        smtp.send_message(msg)
    
    print('\n')
    print(f"{green} ----------> your message sent to {contacts} {stop}")
    print('\n')

    smtp.close()

    ans = input(f"{yellow}If you want to send another Mail, please type 'yes'{stop} : ")
    print('\n')

    while ans == 'yes' : 
            msg = EmailMessage()

            From = input("sender's EMAIL address : ")
            Pass = input("PASSWORD (sender's password) : ")

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp1:
                    smtp1.login(From, Pass)
                    print(f'{green} LOGIN SUCCESSFULL {stop}')
            except Exception:
                print(f'{red} LOGIN FAILED  {stop}')
            else:
                print('\n')
                numbe = input("To how many contacts {in number} : ")

                contacts = [ ]

                for i in range(int(numbe)):
                    mail_id = input("reciever's mail-id : ")
                    i = mail_id
                    contacts.append(mail_id)
    
                print('\n')
                print(f"contacts : {contacts}")

                print('\n')
                Subject = input("subject :  ")
                print('\n')
                Body = input("your message : \n         ")

                msg['Subject'] = Subject
                msg['From'] = From
                msg['To'] = contacts

                msg.set_content(Body)

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(From, Pass)
                    smtp.send_message(msg)
    
                print('\n')
                print(f"{green} ----------> your message sent to {contacts} {stop}!")
                print('\n')

                smtp.close()

                ans = input(f"{yellow}If you want to send another Mail, please type 'yes'{stop} : ")
                print('\n')
