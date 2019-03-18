

# Setting up YouTube Data API

Step1: Goto Below linke and Create a Project 
        
    https://console.cloud.google.com/projectcreate?previousPage=%2Fapis%2Fcredentials%3Fproject%3Dyoutubedataproject-229606&organizationId=0

Note: You must have google account for that, and i think definatly would have it.

Step2: Select the project that you have created and enable youtube Data api for that project.

        https://console.cloud.google.com/projectselector2/home/dashboard?organizationId=0&supportedpurview=project&project&folder

Enable YouTube Data API v3:
        
        https://console.cloud.google.com/marketplace/details/google/youtube.googleapis.com?q=youtube%20data%20api%20v3&id=125bab65-cfb6-4f25-9826-4dcc309bc508&project=youtubedataproject-229606&folder&organizationId&supportedpurview=project

Step3: After  enabling API you need to create a credential to use that API.
go to below link and create a creadential to use.

        https://console.cloud.google.com/apis/api/youtube.googleapis.com/credentials


Step 4: Copy your api key in below cod and python script to check key is working or not.
Example DEveloper key will look like below:
        
        key: AIzaSyB8-REIEV-************FSfnpdGGKbWE


Step 5: Install Google YouTube Data API v3 module for python.
        
        pip install --upgrade google-api-python-client

## Youtube Data API v3 test code;

    import time
    import socket
    import json
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError


    DEVELOPER_KEY = 'paste here your developer key'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    # word for which you want to search
    word =['python', 'local', 'funny', 'football']

    if __name__ == '__main__':
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
    
        for w in word:
            search_response = youtube.search().list(q='w',part='id,snippet',maxResults=50).execute()
            videos = {}
        
            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
        
            s= ','.join(videos.keys())
        
            videos_search = youtube.videos().list(id=s,part='id,statistics').execute()
            
            stream_videos = []
            
            for i in videos_search['items']:
                temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
                temp_res.update(i['statistics'])
                stream_videos.append(temp_res)
                
            data = str(stream_videos)
            print(data)
            time.sleep(10)
    

### API docs:

    https://developers.google.com/apis-explorer/?hl=en_US#p/youtube/v3/

### Manage_API:

    https://console.developers.google.com/apis/credentials?project=excellent-ship-193208&folder=&organizationId=

