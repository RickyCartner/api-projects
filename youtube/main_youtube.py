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
    DEVELOPER_KEY = "AIzaSyAz7d152hEdtGHtupiEZxSux5TfHkKzhLI"
    # API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    # 'request' variable is the only thing you must change
    # depending on the resource and method you need to use
    # in your query

    # request = youtube.search().list(
    # )

    # # To perform list method on playlists resource
    # request = youtube.playlists().list(
    # )

    # # To perform list method on videos resource
    # request = youtube.videos().list(
    # )

    # to perform list method on channels resource
    request = youtube.search().list(
        part="id,snippet",
        channelId="UC2wDu7KMJGNxLQsHYDLwGTg"
    )

    # Query execution
    response = request.execute()
    # Print the results
    print(response)

# def api_call_youtube():
#     url = 'https://www.googleapis.com/youtube/v3'
#     response = requests.get(url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_call_youtube()
    # api_call_bible('https://bible-api.com/BOOK+CHAPTER:VERSE')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
