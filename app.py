from database.mongo_connect import atlas_client
from dotenv import load_dotenv

load_dotenv()
import os

# Load environment variables
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Get book information
books = atlas_client.find(collection_name=COLLECTION_NAME)
def atlas_search(book_title, limit=10):
    pipeline= [
		{
			"$search": {
				"index": "book_search",
				"text": {
					"query": book_title,
					"path": ["Book Title", "Summary"]
     			}
			}
		},
		{
			"$project": {
				"_id": 0,
				"Book title": 1,
				"Summary": 1,
				"Book Author": 1,
				"Genres": 1	
			}
		},
		{
			"$limit": limit
		}
	]
    results = atlas_client.database[COLLECTION_NAME].aggregate(pipeline)
    return list(results)
    

