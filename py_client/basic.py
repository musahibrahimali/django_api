import requests

# create an endpoint to jsonplaceholder
url = 'http://localhost:8000/api/home/'  # http://127.0.0.1:8000/

# create a request to get the post from url
response = requests.get(url)
# print the response
print(response.text)
