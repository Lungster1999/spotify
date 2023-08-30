from dotenv import load_dotenv
import os
import base64
import requests
import json

load_dotenv()

c_id = os.getenv('CLIENT_ID')
c_secret = os.getenv('CLIENT_SECRET')


def get_token():
    auth_string = c_id + ":" + c_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")


    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = requests.post(url,headers=headers,data=data)

    json_result = json.loads(result.content)

    token = json_result["access_token"]
    #return token




def get_auth_header(token):
    return {"Authorization":f"Bearer {token}",
            "scope": "playlist-read-private"}



def return_playlist(token):
    url = "https://api.spotify.com/v1/me/playlists"
    headers = get_auth_header(token)
    print(headers)
    result = requests.get(url,headers=headers)
    
    print(result)


token = get_token()
return_playlist(token)