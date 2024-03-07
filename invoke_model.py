import boto3
import json
def list_foundation_models():
  
  bedrock_client = boto3.client('bedrock')

  try:
    response = bedrock_client.list_foundation_models()
    models = response["modelSummaries"]
    print(f"Found {len(models)} foundation models:")
    for model in models:
      print(f"- {model['modelName']}")

  except Exception as e:
    print("Unable to list models:", e)


def ask_claude(question):

    bedrock = boto3.client(service_name="bedrock-runtime")
    body = {
        "prompt": "What is the capital of France?",
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens_to_sample": 100
    }

    try:
        response = bedrock.invoke_model(
        modelId='anthropic.claude-v2:1',
        body=json.dumps(body),
        )
        
        print(response['generatedText'])

    except Exception as e:
        print("Error generating response:", e)

ask_claude("Hi")


def list_model_ids():

  bedrock = boto3.client('bedrock')

  try:
    response = bedrock.list_foundation_models()
    models = response["modelSummaries"]

    print(f"Found {len(models)} models:")
    for model in models:
      print(f"- {model['modelId']}")

  except Exception as e:
    print("Unable to list models:", e)

