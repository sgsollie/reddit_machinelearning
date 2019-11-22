import requests
import json

f = open("api_responses.txt", "a")

def pull_comments(requestUrl):
    # The pushshift api only alows a size of < 500 responses per request
    resp = requests.get(requestUrl)
    if resp.status_code != 200:
        # Just die if we don't get what we want. Dramatic I know.
        raise requests.HTTPError('GET /reddit/search/comment  {}'.format(resp.status_code))
        f.close()
        os._exit(1)

    # Obtain unix time of last entry from intial request
    jsonresponse = resp.json()["data"]
    time = None
    for time in jsonresponse:
        pass
    time = time["created_utc"]
    print(time)

    # Parse the body of each comment
    for val in jsonresponse:
        #print(val["body"])
        f.write(val["body"])
    return time

# Run initial query
time = pull_comments('https://api.pushshift.io/reddit/search/comment/?q=dems&subreddit=The_Donald&metadata=true&size=499')

# Grab the 499 queries before the last - do this 50 times
for i in range(50):
    time = pull_comments('https://api.pushshift.io/reddit/search/comment/?q=dems&subreddit=The_Donald&metadata=true&size=499' + '&before=' + str(time))

f.close()