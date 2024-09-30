from dotenv import load_dotenv
import os

load_dotenv()

print(type(os.getenv('AZURE_CLIENT_ID')))
#print("Tenant ID:", os.environ.get('AZURE_TENANT_ID'))
#
# print("Client Secret:", os.environ.get('AZURE_CLIENT_SECRET'))
#print("Vault URL:", os.environ.get('AZURE_VAULT_URL'))

# Your existing code to retrieve the secret goes here
