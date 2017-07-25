import urllib3
import time
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText


parser = argparse.ArgumentParser(description='Site checker with time scheduling')
parser.add_argument('--website', required=True,
                    help='website, that is needed to be checked')
parser.add_argument('--email',
                    help='the notification of falling the website will be sent to this email')
parser.add_argument('--time', type=int,
                    help='how often should this script check your website (in minutes)')

args = parser.parse_args()


def internet_on():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://216.58.192.142')
        return True
    except:
        return False


def check_website():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', args.website)
        if r.status == 200:
            return True
        else:
            return False
    except:
        return False


def send_an_email():
    my_email = "helloworldimmax@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = args.email
    msg['Subject'] = "Your website checker!"
    body = "Your website (" + str(args.website) + ") is down, check it ASAP! \n P.S. Your favorite checker"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, "willzoumarrzme_")
    text = msg.as_string()

    server.sendmail(my_email, args.email, text)
    server.quit()


def check_and_notify():
    if internet_on():
        if check_website():
            print("OK")
            return True
        else:
            print("It's down..fuck")
            print(args.website)
            if args.email:
                send_an_email()
            return False
    else:
        print("Oops, internet is not working")
        return False


def main():
    if args.time:
        print("First check...")
        if check_and_notify():
            print("I will check the website every " + str(args.time) + " minutes...")
            while True:
                mins = 0
                while mins != args.time:
                    time.sleep(60)
                    mins += 1
                    check_and_notify()
    else:
        check_and_notify()

if __name__ == "__main__":
    main()