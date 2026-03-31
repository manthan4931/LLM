import requests


def web_search(query:str):
    url= f"https://api.duckduckgo.com/?q={query}&format=json"

    try:
        data=requests.get(url).json()
        result= data.get("AbstractText")


        if not result:
            result=data.get("RelatedTopics",[])
            if result and isinstance(result, list):
                result = result[0].get("Text", "No results found." )
    except:
        return "Search failed"
    
