import requests

API_KEY = "u0jZrSr76XvRFD9DkYgdu4d6NxvoVHCAqlD7T7BT"

def get_apod(date=None):
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': API_KEY}
    if date:
        params['date'] = date
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None