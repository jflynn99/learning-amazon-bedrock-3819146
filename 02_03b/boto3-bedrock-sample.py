#Imports
import boto3
import json
#Create the bedrock client
bedrock = boto3.client('bedrock-runtime')
#Setting the prompt
propmt_data = """Command: Write me a blog about product managers building things themselves on AWS bedrock.
Blog:
"""
#Model specification
modelId = "amazon.titan-text-express-v1"
accept = "application/json"
contentType = "application/json"
#Configuring parameters to invoke the model
body = json.dumps({
  "inputText" : propmt_data,
  "testGenerationConfig" : {
  "maxTokenCount" : 1000
    }
  })
#Invoke the model
response = bedrock.invoke_model(
  body = body, modelId = modelId, accept = accept, contentType = contentType
)
#Parsing and displaying the output
response_body = json.loads(response.get('body').read())
output = response_body.get('resuts')[0].get("outputText")
print(output)