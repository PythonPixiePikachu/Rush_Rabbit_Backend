from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
from app.settings import paths
import os


def load():
    load_dotenv(paths.dotenv_path)


def  get_customer_sql_secret():
    load()
    client_id = os.getenv('AZURE_CLIENT_ID')
    tenant_id = os.getenv('AZURE_TENANT_ID')
    client_secret = os.getenv('AZURE_CLIENT_SECRET')
    vault_url = os.getenv('AZURE_VAULT_URL')
    secret_name = "customersqlconnstring"

      # Check if environment variables are loaded correctly
    if not client_id or not tenant_id or not client_secret or not vault_url:
        raise ValueError(f"One or more environment variables are missing {client_id}")
    # create a credential 
    credentials = ClientSecretCredential(
    client_id = client_id, 
    client_secret= client_secret,
    tenant_id= tenant_id
    )
    # create a secret client object
    secret_client = SecretClient(vault_url= vault_url, credential= credentials)
    # retrieve the secret value from key vault
    secret = secret_client.get_secret(secret_name)

    return secret.value
