import requests
import json

# The pushshift api only alows a size of < 500 responses per request
resp = requests.get('https://api.pushshift.io/reddit/search/comment/?q=dems&subreddit=The_Donald&metadata=true&size=499')
if resp.status_code != 200:
    # Just die if we don't get what we want. Dramatic I know.
    raise requests.HTTPError('GET /reddit/search/comment  {}'.format(resp.status_code))
    os._exit(1)

# Parse the body of each comment
jsonresponse = resp.json()["data"]
for val in jsonresponse:
    print(val["body"])