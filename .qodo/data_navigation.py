import json

raw_api_payload = """
{
    "query": "Agentic AI frameworks 2026",
    "total_results": 1042,
    "search_metadata": {
        "engine": "Google Scholar Custom API",
        "execution_time_ms": 142
    },
    "results_list": [
        {
            "title": "Hierarchical Multi-Agent Orchestration via LangGraph",
            "author": "Dr. Aris",
            "metrics": {"citations": 42, "relevance_score": 0.98},
            "url": "https://arxiv.org/abs/2601.12345"
        },
        {
            "title": "Production Deployment Patterns for CrewAI Frameworks",
            "author": "Sarah Chen",
            "metrics": {"citations": 12, "relevance_score": 0.91},
            "url": "https://arxiv.org/abs/2602.54321"
        },
        {
            "title": "Memory Systems and State Persistence in Autonomous Agents",
            "author": "Alex Mercer",
            "metrics": {"citations": 89, "relevance_score": 0.99},
            "url": "https://arxiv.org/abs/2512.98765"
        }
    ]
}
"""
# Step 1: Converting into dictionary
search_data=json.loads(raw_api_payload)
print("--- 1. ACCESSING DEEPLY NESTED METADATA ---")
# Accessing a nested object key-by-key
search_engine = search_data["search_metadata"]["engine"]
time_taken = search_data["search_metadata"]["execution_time_ms"]
print(f"Results fetched using {search_engine} in {time_taken}ms.\n")

#Step 2 : Extracting relevant information
print("--- 2. ITERATING AND EXTRACTING FROM ARRAYS ---")
cleaned_agent_context=[]
for index,paper in enumerate(search_data["results_list"],start=1):
    title=paper['title']
    url=paper['url']
    score=paper['metrics']['relevance_score']
    cleaned={'index':index,'title':title,'url':url,'score':score}
    cleaned_agent_context.append(cleaned)

#Step 3 : Showing Restructured data that will be feed to LLM Context window 
print(type(cleaned_agent_context))
print(cleaned_agent_context)