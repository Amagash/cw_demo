import boto3

def print_foundation_models():
  bedrock = boto3.client('bedrock')
  
  response = bedrock.list_foundation_models()
  
  models = response['modelSummaries']
  
  print(f"Found {len(models)} foundation models:")
  
  for model in models:
    print(f"- {model['modelId']}")

print_foundation_models()