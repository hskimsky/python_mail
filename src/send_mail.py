from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import argparse
import os
import configparser


def get_body(payload):
    mail = MIMEMultipart('alternative')
    mail['Subject'] = payload['filenames']
    mail['From'] = payload['sender']
    mail['To'] = payload['receivers']
    mail.attach(MIMEText(get_contents(payload), 'html'))
    for file in payload['files']:
        with open(file, 'rb') as f:
            fname, ext = os.path.splitext(file)
            attach_file = MIMEImage(f.read(), ext)
            filename = file[file.rindex('/') + 1:]
            attach_file.add_header('Content-Disposition', 'attachment; filename= ' + filename)
            mail.attach(attach_file)
    return mail.as_string()


def get_contents(payload):
    contents = ''
    # with open('template.html', 'rb') as template_file:
    with open('template.html', 'r') as template_file:
        contents = template_file.read()

    return contents.format(sender=payload['sender'], receivers=payload['receivers'], filenames=payload['filenames'])


def send(payload):
    # print('send.payload', payload)
    mail_server = payload['sender'][payload['sender'].find('@') + 1:]
    # if 'gmail.com' == mail_server:
    #     server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # TLS: 587
    # elif 'naver.com' == mail_server:
    #     server = smtplib.SMTP_SSL('smtp.naver.com', 465)
    server = smtplib.SMTP_SSL('smtp.' + mail_server, 465)
    server.login(payload['sender'], payload['senderpassword'])

    body = get_body(payload)
    print(body)
    server.sendmail(payload['sender'], payload['receivers'].split(','), body)
    server.quit()

    return True


if __name__ == '__main__':
    # ArgumentParser
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sender', default='hskimsky@gmail.com', help='sender')
    parser.add_argument('-p', '--senderpassword', default='', help='sender password')
    parser.add_argument('-r', '--receivers', default='hskimsky@naver.com', help='receivers. comma delimited')
    # parser.add_argument('-f', '--filepattern', type=str, nargs='+', help='send absolute paths of file pattern.')
    parser.add_argument('-f', '--filepattern', nargs='+', help='send absolute paths of file pattern.')
    args = parser.parse_args()
    # print('args', args)
    filenames = ','.join(map(lambda f: f[f.rindex('/') + 1:], args.filepattern))
    payload = {'sender': args.sender, 'senderpassword': args.senderpassword, 'receivers': args.receivers, 'filenames': filenames, 'files': args.filepattern}

    # ConfigParser
    config = configparser.ConfigParser()
    config.read_file(open('config.ini'))
    if args.sender == config['DEFAULT']['SENDER_EMAIL']:
        payload['senderpassword'] = config['DEFAULT']['SENDER_PASSWORD']
    
    print('payload', payload)
    send(payload)
