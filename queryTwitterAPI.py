#This version of code modified by: dpe22

#Original Code from https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Search/recent_search.py\
#Original Code Copyright 2020 @TwitterDev

  # Licensed under the Apache License, Version 2.0 (the "License");
  # you may not use this file except in compliance with the License.
   #You may obtain a copy of the License at

    #   http://www.apache.org/licenses/LICENSE-2.0

  # Unless required by applicable law or agreed to in writing, software
   #distributed under the License is distributed on an "AS IS" BASIS,
   #WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  # See the License for the specific language governing permissions and
   #limitations under the License.

import requests
import os
import json
import sys

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

bearer_token = os.environ.get("BEARER_TOKEN")
search_url = "https://api.twitter.com/2/tweets/search/recent"

print()
print('Please enter the name of the company you want to evaluate: ')
COMPANY = input()
print()
print('How do you want to evaluate %s?' %(COMPANY))
print('    [1] Brand Sentiment')
print('    [2] Employee Sentiment')

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
while True:
    CHOICE = input()
    if CHOICE == "2":
        query_params = {'query' : 'lang: en -is:reply -is:retweet "Working at %s" OR "Working for %s" -"$"' %(COMPANY, COMPANY), 'max_results': 10}
        break
    elif CHOICE == "1":
        query_params = {'query' : 'lang: en -is:reply -is:retweet %s -"$"' %(COMPANY), 'max_results': 100}
        break
    else:
        print()
        print("ERROR: Invalid Choice. Please choose option 1 or option 2.") 
        print('    [1] Brand Sentiment')
        print('    [2] Employee Sentiment')

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

##uprint function defined by Jelle Fresen on May 1 2015 on stockoverflow.com, used to resolve a character mapping issue
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def main():
    json_response = connect_to_endpoint(search_url, query_params)
    encoded_tweets = json.dumps(json_response, indent=4, ensure_ascii = False, sort_keys=True)
    decoded_tweets = json.loads(encoded_tweets)
    d1 = [item['text'] for item in decoded_tweets['data']]
    with open('tweets_to_analyze.txt','w') as f:
        uprint(*d1, sep = ". \n", file=f)

if __name__ == "__main__":
    main()
