import requests
import json

# URL of the API endpoint
url = "https://www.sofascore.com/api/v1/sport/basketball/events/live"

payload = ""
headers = {"User-Agent": "insomnia/8.4.5"}

# Make the GET request to the API
response = requests.request("GET", url, headers=headers, data=payload)
json_data = json.loads(response.text)

def get_live_matches():
    final_string = ""
    for event in json_data['events']:
        league = event['tournament']['name']
        home_team = event['homeTeam']['name']
        away_team = event['awayTeam']['name']
        home_score = event['homeScore']['current']
        away_score = event['awayScore']['current']
        status = event['status']['description']

        final_string += f"{league}: {home_team} {home_score} - {away_team} {away_score} ({status})\n"
    
    return final_string

live_scores = get_live_matches()
print(live_scores)


# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()

#     # Pretty print the response (optional)
#     import json
#     print(json.dumps(data, indent=4))

#     # Example of how to access specific data
#     events = data.get('events', [])
#     for event in events:
#         tournament_name = event.get('tournament', {}).get('name', 'N/A')
#         home_team = event.get('homeTeam', {}).get('name', 'N/A')
#         away_team = event.get('awayTeam', {}).get('name', 'N/A')
#         home_score = event.get('homeScore', {}).get('current', 'N/A')
#         away_score = event.get('awayScore', {}).get('current', 'N/A')
#         status_description = event.get('status', {}).get('description', 'N/A')

#         print(f"Tournament: {tournament_name}")
#         print(f"Match: {home_team} vs {away_team}")
#         print(f"Score: {home_team} {home_score} - {away_team} {away_score}")
#         print(f"Status: {status_description}")
#         print("-" * 40)
# else:
#     print(f"Failed to retrieve data: {response.status_code}")
