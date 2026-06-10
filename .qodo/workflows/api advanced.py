import json
import requests
API_ENDPOINT = "http://universities.hipolabs.com/search"

# Structuring Query Parameters
search_arguments={
    "country":"Pakistan",
}

# Structuring Custom Headers
costum_headers = {
    "User-Agent": "AgenticAILearningWorkspace/1.0",
    "Accept": "application/json"
}

response=requests.get(API_ENDPOINT,params=search_arguments,headers=costum_headers)
print(f"Status of response is {response.status_code}")

if (response.status_code==200):
    print("Connection Succesful\n")
    universities=response.json()
    print(f"Number of uni founds are{len(universities)}\n")

    for index,school in enumerate(universities,start=1):
        name=school['name']
        website=school['web_pages'][0]
        country=school['country']

        print(f"{index} School Name: {name}  website: {website}  country: {country}")

else:
    print(f"Error is {response.status_code}")
