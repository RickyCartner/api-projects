# This is a sample Python script.
# import requests
# import google_auth_oauthlib.flow
import googleapiclient.discovery
# import googleapiclient.errors

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# API client library
def api_call_youtube():
    # API information
    api_service_name = "youtube"
    api_version = "v3"
    # API key
    DEVELOPER_KEY = {dev_key}
    CHANNEL_ID = {channel_id}  # Ricky
    #CHANNEL_ID = {channel_id} # Oakwood
    # API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=DEVELOPER_KEY)
    # 'request' variable is the only thing you must change
    # depending on the resource and method you need to use
    # in your query

    # to create a new livestream video
    request = youtube.liveStreams().insert(
        part="snippet,cdn,contentDetails,status",
        body={
            "cdn": {
                "frameRate": "60fps",
                "ingestionType": "rtmp",
                "resolution": "1080p"
            },
            "contentDetails": {
                "isReusable": True
            },
            "snippet": {
                "title": "Your new video stream's name",
                "description": "A description of your video stream. This field is optional."
            }
        }
    )

    # Query execution
    response = request.execute()
    # Print the results
    print(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_call_youtube()
    # api_call_bible('https://bible-api.com/BOOK+CHAPTER:VERSE')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
