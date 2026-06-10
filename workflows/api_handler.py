import json 
import requests

TARGET_URL = "https://jsonplaceholder.typicode.com/posts/1"
response=requests.get(TARGET_URL)
print(f"State of response is {response.status_code}")
if(response.status_code==200):
    print("Connection is Succesful")
    print(response)
    raw_string=response.text
    print(type(raw_string))
    print(raw_string)

    # Converting into dictionary
    api_data=response.json()
    print(type(api_data))
    print(f"Title: {api_data['title']}     Body: {api_data['body']}\n")

else:
    print(f"Error dure to {response.status_code}")