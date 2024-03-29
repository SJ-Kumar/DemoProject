import imaplib
import email
import yaml

<<<<<<< HEAD:Gmail_dataanalysis/data.py
with open(r'C:\DemoProject\DemoProject\Gmail_dataanalysis\credentials.yaml') as f:
=======
with open(r'C:\10-Practice\DemoProject\python_practice\Gmail_dataanalysis\credentials.yaml') as f:
>>>>>>> ff5f67142432e7f0428d59a868f23d26b3159a95:python_practice/Gmail_dataanalysis/data.py
    content = f.read()
my_credentials = yaml.load(content, Loader = yaml.FullLoader)
user, password = my_credentials['user'], my_credentials['password']

imap_url = 'imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
try:
  my_mail.login(user, password)
except Exception as e:
  print('Exception is')
  print(e)

  my_mail.select('Inbox')

data = my_mail.search(None, 'ALL')
mail_ids = data[1]
id_list = mail_ids[0].split()
len(id_list)

first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

import pandas as pd
email_df = pd.DataFrame(columns=['Date','From', 'Subject','Status'], index=range(100000,first_email_id,-1))
for i in range(100000,first_email_id, -1):
    data = my_mail.fetch(str(i), '(RFC822)' )
    for response_part in data:
      arr = response_part[0]
      if isinstance(arr, tuple):
        msg = email.message_from_string(str(arr[1],'ISO-8859–1'))
        print(i) #This will let you know what row is being appended
        new_row = pd.Series({"Date":msg['Date'] , "From":msg['from'],"Subject":msg['subject'], "Status":msg['X-Antivirus-Status'] })
email_df = email_df.append(new_row, ignore_index=True)

from wordcloud import WordCloud, STOPWORDS
text = email_df['Subject'].values

stopwords = set(STOPWORDS)
stopwords.update([" "]) #You can add stopwords if you have any 
wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(str(text))
import matplotlib.pyplot as plt

plt.figure(figsize = (20, 20), facecolor = None) 
plt.imshow(wordcloud)
plt.axis("off")
plt.show()