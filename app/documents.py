from dotenv import load_dotenv
import os

from couchdb import Database
load_dotenv()

SERVER_URL = os.getenv('COUCH_DB_URL')
database = Database(SERVER_URL +'/test_database')