
from pandas import DataFrame as df
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from kafka import SimpleProducer, KafkaClient
import json

DEVELOPER_KEY = 'past here you YouYube developer key' #new api key
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)


topic = 'youtube'
kafka= KafkaClient('localhost:9092')
producer= SimpleProducer(kafka)

class sendTokafka():
 
    def on_data(self, data):
        try:
            #print(data)
            producer.send_messages('youtube' , data.encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def kafkaSend(data):
    try:
        #print(data)
        producer.send_messages('youtube' , data.encode('utf-8'))
        return True
    except BaseException as e:
            print("Error on_data: %s" % str(e))
    return True

def getvideos(categary, categarycode, country):
    
    stream_videos = []
       
    try:
        search_response = youtube.videos().list(part='id,snippet,statistics',chart='mostPopular',
                                            regionCode= country, videoCategoryId= categarycode ,maxResults=50).execute()
    
        for i in search_response['items']:
            temp_res = dict(v_id = i['id'], v_title = i['snippet']['title'], ch_id= i['snippet']['channelId'], ch_title= i['snippet']['channelTitle'], country= country, categary_name = categary, publised_date = i['snippet']['publishedAt'])                     
            temp_res.update(i['statistics'])
            stream_videos.append(temp_res)
        
    except HttpError:
        pass
    
    return stream_videos
    
def getcategary(c):
    videos_categary_india = youtube.videoCategories().list(part= 'id,snippet', regionCode=c).execute()
    
    categary ={}
    
    for i in videos_categary_india['items']:
        categary[i['snippet']['title']]= i['id'] 
        
    return categary # returning a dictionary of categaries in country
    
if __name__ == '__main__':
    
    country= 'IN'
    categary = getcategary(country)
    for k,v in categary.items():
        print("getting data for counrty: %s and categary: %s" %(country,k ))
        print('\n')
        youtube_data = getvideos(k,v,country)

        youtube_data = json.dumps(youtube_data)
        u = sendTokafka()
        u.on_data(youtube_data)        
        #youtube_df = df.from_dict(youtube_data)
        #youtube_df = youtube_df[['v_id', 'v_title', 'ch_id', 'ch_title', 'categary_name', 'publised_date', 'country', 'likeCount', 'viewCount', 'commentCount', 'dislikeCount', 'favoriteCount']]
        #kafkaSend(youtube_df)
        print(youtube_data)
        print('\n'*2)
    