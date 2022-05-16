import os
# this import makes sure you are able to access environment variables

# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

# this class basically fetches environment variables
class Config():
    DEBUG=os.getenv('DEBUG')

