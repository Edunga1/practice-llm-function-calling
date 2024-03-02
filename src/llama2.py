import json
from typing import Callable, Dict, List

# Define the roles and markers
B_FUNC, E_FUNC = "<FUNCTIONS>", "</FUNCTIONS>\n\n"
B_INST, E_INST = "[INST] ", " [/INST]"  # Llama style

# Function metadata
# function_metadata = {
#     "function": "search_bing",
#     "description": "Search the web for content on Bing. This allows users to search online/the internet/the web for content.",
#     "arguments": [
#         {
#             "name": "query",
#             "type": "string",
#             "description": "The search query string"
#         }
#     ]
# }
# Format the function list and prompt
# function_list = json.dumps(function_metadata, indent=4)

def parse_function_list(func: Callable, description: str, args: List[Dict[str, str]]):
    function_metadata = {
        "function": func.__name__,
        "description": description,
        "arguments": [
            {
                "name": arg["name"],
                "type": arg["type"],
                "description": arg["description"]
            } for arg in args
        ]
    }
    return json.dumps(function_metadata, indent=4)


# Example response from the API
# {"model":"example","created_at":"2024-03-02T08:43:14.431308084Z","response":"{","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:14.587414677Z","response":"\n","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:14.734397646Z","response":"   ","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:14.877616776Z","response":" \"","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:15.029126347Z","response":"function","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:15.184017038Z","response":"\":","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:15.329783087Z","response":" \"","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:15.478581331Z","response":"search","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:15.627355861Z","response":"_","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:15.779146108Z","response":"bing","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:15.924549915Z","response":"\",","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:16.086198774Z","response":"\n","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:16.255244363Z","response":"   ","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:16.40091363Z","response":" \"","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:16.547181911Z","response":"arguments","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:16.702371615Z","response":"\":","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:16.856878228Z","response":" {","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:17.006191701Z","response":"\n","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:17.151720766Z","response":"       ","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:17.298545833Z","response":" \"","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:17.443699004Z","response":"query","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:17.592071613Z","response":"\":","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:17.737501021Z","response":" \"","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:17.88242396Z","response":"latest","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:18.028581123Z","response":" news","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:18.175666417Z","response":" on","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:18.322490391Z","response":" A","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:18.475887233Z","response":"I","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:18.62906871Z","response":"\"","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:18.775566172Z","response":"\n","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:18.925534643Z","response":"   ","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:19.078187891Z","response":" }","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:19.222279079Z","response":"\n","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:19.372116145Z","response":"}","done":false}
# {"model":"example","created_at":"2024-03-02T08:43:19.525196542Z","response":"","done":true,"context":[529,29943,28700,29903,26208,13,1678,376,2220,1115,376,4478,29918,10549,613,13,1678,376,8216,1115,376,7974,278,1856,363,2793,373,350,292,29889,910,6511,4160,304,2740,7395,29914,1552,8986,29914,1552,1856,363,2793,19602,13,1678,376,25699,1115,518,13,4706,426,13,9651,376,978,1115,376,1972,613,13,9651,376,1853,1115,376,1807,613,13,9651,376,8216,1115,376,1576,2740,2346,1347,29908,13,4706,500,13,1678,4514,13,16040,29943,28700,29903,29958,13,13,29961,25580,29962,11856,363,278,9281,9763,373,319,29902,29889,518,29914,25580,29962,13,13,29912,13,1678,376,2220,1115,376,4478,29918,10549,613,13,1678,376,25699,1115,426,13,4706,376,1972,1115,376,12333,9763,373,319,29902,29908,13,1678,500,13,29913],"total_duration":15587672658,"load_duration":741576900,"prompt_eval_count":114,"prompt_eval_duration":9746009000,"eval_count":35,"eval_duration":5098274000}
#
def parse_function_calling(response_raw: str):
    """Parse the response from the API.
    Args:
        response_raw (str): The raw response from the API
    Returns:
        Tuple[str, Dict]: The function and arguments(key-value pairs)
    """
    # Split the response into lines
    lines = response_raw.split("\n")

    # Collect `response` field
    response_raw = ''
    for line in lines:
        if line == '':
            break
        obj = json.loads(line)
        response_raw += obj.get('response', '')

    response = json.loads(response_raw)
    return response.get('function'), response.get('arguments')


def parse_response(response_raw: str):
    # Split the response into lines
    lines = response_raw.split("\n")

    # Collect `response` field
    result = ''
    for line in lines:
        if line == '':
            break
        obj = json.loads(line)
        result += obj.get('response', '')

    return result


class Llama2Toolkit:
    def __init__(self, func: Callable, description: str, args: List[Dict[str, str]]):
        self.func = func
        self.function_list = parse_function_list(func, description, args)

    def get_prompt(self, user_prompt: str):
        prompt = f"{B_FUNC}{self.function_list.strip()}{E_FUNC}{B_INST}{user_prompt.strip()}{E_INST}\n\n"
        return prompt
