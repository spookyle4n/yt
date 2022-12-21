import requests

# Set up the API endpoint and your API access token
ENDPOINT = "https://api.soundcloud.com/tracks"
TOKEN = "YOUR_API_TOKEN"

# Set up the parameters for your API request
params = {
    "client_id": TOKEN,
    "limit": 10,  # Set the number of tracks to retrieve
    "offset": 0  # Set the offset to start retrieving tracks from
}

# Make the API request
response = requests.get(ENDPOINT, params=params)

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # Get the list of tracks from the response
    tracks = response.json()
    # Iterate over the tracks and print the title and permalink URL
    for track in tracks:
        print(track["title"])
        print(track["permalink_url"])
else:
    # Print an error message if the request was not successful
    print("An error occurred:", response.status_code)
