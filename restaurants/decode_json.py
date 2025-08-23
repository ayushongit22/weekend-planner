import json
import urllib.parse
json_str='%7B%22lat%22%3A22.9798586%2C%22lng%22%3A72.502735%2C%22address%22%3A%22Sarkhej-Okaf%2C%20Gujarat%2C%20India%22%2C%22area%22%3A%22sarkhej-okaf%22%7D'
raw_json=urllib.parse.unquote(json_str)
json_data=json.loads(raw_json)
print(json_data)
