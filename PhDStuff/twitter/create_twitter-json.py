import json


# Enter your keys/secrets as strings in the following fields
credentials = {}

creds = []
with open('/Users/jarvis/twitter.cred', 'r') as f:
    for line in f:
        creds.append(line.replace('\n',''))

credentials['CONSUMER_KEY'] = creds[0]
credentials['CONSUMER_SECRET'] = creds[1]
credentials['ACCESS_TOKEN'] = creds[2]
credentials['ACCESS_SECRET'] = creds[3]

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
