import requests

# create an endpoint to jsonplaceholder
url = 'https://jsonplaceholder.typicode.com/posts'

# create a request to get the post from url
response = requests.get(url)
# print the response
print(response.text)
