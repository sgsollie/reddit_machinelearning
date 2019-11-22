import requests
import json

resp = requests.get('https://api.pushshift.io/reddit/search/comment/?q=dems&subreddit=The_Donald&metadata=true&size=2')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /reddit/search/comment  {}'.format(resp.status_code))

jsonresponse = resp.json()["data"]
for val in jsonresponse:
    print(val["body"])