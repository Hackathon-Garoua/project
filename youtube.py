import os
from googleapiclient.discovery import build

def rechercher_videos_youtube(keyword):
    api_key = "AIzaSyCCgVqbjyh37H-SIMdD1Lm7x553DpnOKhM"
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=10
    )

    response = request.execute()

    videos = []
    for item in response['items']:
        titre = item['snippet']['title']
        video_id = item['id']['videoId']
        lien = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"titre": titre, "lien": lien})

    return videos

# Exemple d'utilisation :
keyword = "python programming"
resultats_videos = rechercher_videos_youtube(keyword)
for resultat in resultats_videos:
    print(resultat["titre"], ": ", resultat["lien"])
