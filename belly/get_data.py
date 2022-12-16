"""Fetch data from API."""
import requests

def api_response():
    """Fetch the data from API."""
    url = "https://yummly2.p.rapidapi.com/feeds/list"

    querystring = {"limit":"24","start":"0"}

    headers = {
	"X-RapidAPI-Key": "0904899d48msh10f8b458c86e4d0p1989fbjsne56317b331a6",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # get json 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    # print(requests.request("GET", url, headers=headers, params=querystring).text)
    return response['feed']