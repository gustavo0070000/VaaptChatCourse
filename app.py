import streamlit as st
import boto3
from botocore.exceptions import ClientError



import uuid

def generate_session_id():
    return str(uuid.uuid4())

# Exemplo de uso
session_id = generate_session_id()
print("Session ID:", session_id)

# Set up AWS credentials
aws_access_key_id = st.sidebar.text_input("AWS Access Key ID", type="password")
aws_secret_access_key = st.sidebar.text_input("AWS Secret Access Key", type="password")
aws_region = st.sidebar.text_input("AWS Region", value="sa-east-1")

# Initialize Bedrock client
bedrock_runtime = boto3.client(
    'bedrock-agent-runtime',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Streamlit app
st.title("Amazon Bedrock Agent Chat")

# Chat interface
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    try:
        response = bedrock_runtime.invoke_agent(
            agentId='T35LYKJNFF',
            agentAliasId='HPGASZOM4B',
            sessionId=session_id,
            inputText=user_input
        )
        
        st.text("Agent:")
        for event in response['completion']:
            chunk = event['chunk']
            st.write(chunk['bytes'].decode())
    
    except ClientError as e:
        st.error(f"An error occurred: {e}")

