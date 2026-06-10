import json

# Response 1: A flawless API text string payload
good_response = '{"agent": "CriticAgent", "verdict": "approved"}'

# Response 2: A broken, corrupted response  missing closing '}' at the end!
bad_response = '{"agent": "ExecutorAgent", "action": "deploy_code"'

def safe_parser(raw_text):
    try:
        parsed_data=json.loads(raw_text)
        print(f"{type(raw_text)}\n")
        pretty=json.dumps(parsed_data)
        print(f"{type(parsed_data)}\n")
        return parsed_data
    except json.JSONDecodeError as err:
        print(f"Error in json file : {err}")
        return None
    
safe_parser(bad_response)
