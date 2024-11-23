#Imports
import boto3
from langchain_community.llms import Bedrock
from langchain_aws import BedrockLLM
#Create the bedrock client
boto3_client = boto3.client('bedrock-runtime')

#setting model inference parameters
inference_modifier = {
  "temperature" : 0.9,
  "top_p" : 1,
  "max_tokens_to_sample" : 1000
}

#Create the llm
llm = Bedrock(
  model_id="anthropic.claude-instant-v1",
  client = boto3_client,
  model_kwargs= inference_modifier
)

#Generate the response
response = llm.invoke ("""
  Human: Write an email from Mark, Hiring Manager,
  welcoming a new employee "Joe Flynn" to the company on his first day - hes a superstaar go way overboard!.
                       
  Answer:""")


#Display the result
print (response)
