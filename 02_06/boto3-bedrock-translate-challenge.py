#Imports
import boto3
import json

#Create the client
client = boto3.client(service_name='bedrock-runtime')

#Construct the body
#specify your prompt
body = json.dumps({
     "prompt": "Human: Please translate the following text into French, German, Spanish, and Russian:\n'Joe Flynn is the hottest man in the world.'\nAssistant:",
    "max_tokens_to_sample": 200,
    "temperature": 0.5
})

#Specify model id and content types
modelId = 'anthropic.claude-instant-v1'
accept = 'application/json'
contentType = 'application/json'

#Invoke the model
response = client.invoke_model(
    body=body, 
    modelId=modelId, 
    accept=accept, 
    contentType=contentType
)

#Extract the response
response_body = json.loads(response.get('body').read())
print(response_body)
#Display the output
completions = response_body.get('completions')
if completions and isinstance(completions, list) and len(completions) > 0:
    # Ensure 'data' exists in the first completion and handle it gracefully
    data = completions[0].get('data')
    if data and 'text' in data:
        print(data['text'])
    else:
        print("No 'text' field found in the completion's 'data'.")
else:
    print("No completions returned by the model or invalid response format.")