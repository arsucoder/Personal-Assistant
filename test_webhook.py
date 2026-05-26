import requests

user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message" : user_message}

url = "http://localhost:5678/webhook-test/effeef99-a431-43d3-be9e-1a51c9113c74"

response = requests.post(url , json=request_message)

print(response.status_code)
print(response.json()[0]["output"])


