from email import message
from email.mime import text
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now=datetime.datetime.now
content=''

#HackerNews Extract

def extract_news(url):
    print ("Extracting the content from the provided website")
    cnt=''
    cnt+=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*100+'<br>\n')
    response=requests.get(url)
    content=response.content
    soup=BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title', 'valign':''})):
        cnt+=((str(i+1)+':'+tag.text+'\n'+'<br>') if tag.text!='More' else '')
    return(cnt)
    
    
#cnt = extract_news('https://economictimes.com/')
cnt = extract_news('https://news.ycombinator.com/jobs')
content+=cnt
content+=('<br>--------<br>')
content+=('<br><br> End of Message')

print('Reterived Content'+ content)
print('Composing Email')

SERVER='smtp.gmail.com'
PORT = 587
FROM ='OTsureshbabu@gmail.com'
TO ='sureshbabuv@gmail.com'
PASS ='Suchi04Jai10'
msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' 
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
#server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
  
server.quit()

