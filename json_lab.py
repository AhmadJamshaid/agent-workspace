import json
llm_string='{"agent": "MemoryAgent", "memory_capacity_gb": 16, "status": "optimized"}'

#converting into dictionary
agent_dict=json.loads(llm_string)
print("Step 1 completed : json.loads()        ")
print(f"Parsed type : {type(agent_dict)}      ")
print(f"The status of agent is {agent_dict['status']}\n")

#modifying dictionary and converting back it into string
agent_dict["status"]="upgraded"
raw_json_string=json.dumps(agent_dict)
print("Step 2 completed : json.dumps()        ")
print(f"Raw type : {type(raw_json_string)}      ")
print(f"The content of raw document is {raw_json_string}\n")

# saving config file "agent_dict" into physical file 
with open('agent_config.json','w') as file_pointer:
    json.dump(agent_dict,file_pointer,indent=4)
print("Step 3 completed : json.dump() , converted into file        ")


# reading the file
with open('agent_config.json','r')as file_pointer:
    file=json.load(file_pointer)
print("Step 4 completed : json.load() , reading from file      ")
print(f"Type : {type(file)}      ")
print(f"The status of agent is {file['status']}\n")
