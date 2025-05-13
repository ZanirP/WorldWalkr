from mongo_connect import atlas_client
import os
from dotenv import load_dotenv

load_dotenv()
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

print("======== Finding some sample books ========================")
books = atlas_client.find(collection_name=COLLECTION_NAME, limit=5)

print(f"Found {len (books)} books")
for idx, book in enumerate(books):
    print(
        f'{idx+1}\ntitle: {book["Book title"]}\tAuthor {book["Book Author"]},\tyear: {book["Publication Date"]}\n'
    )
print("================================")
print("======== Finding some books written in 1990 ========================")

books_1990 = atlas_client.find(
	collection_name=COLLECTION_NAME,
	filter={"Publication Date": "1962"},
)

for idx, book in enumerate(books_1990):
    print(
        f'{idx+1}\ntitle: {book["Book title"]}\tAuthor {book["Book Author"]},\tyear: {book["Publication Date"]}\n'
    )
    
print("================================")