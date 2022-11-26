from googleapiclient.discovery import build

api_key='AIzaSyCnPb68yffLHdI_E24ycQ_xp42f-LuklvQ'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics', 
    forUsername='schafer5'
    )

response = request.execute()

print(response)