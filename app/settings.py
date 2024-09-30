from pathlib import Path
import os

# Define the base directory (project root)
BASE_DIR = Path(__file__).resolve().parent

class paths:
    # Define the paths for the project
    BASE_DIR = BASE_DIR
    
    azure_path =  os.path.join(BASE_DIR, 'azure')

    dotenv_path = os.path.join(azure_path,'.env')

