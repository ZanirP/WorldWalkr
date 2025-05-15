from mongo_connect import atlas_client
import os
from dotenv import load_dotenv

load_dotenv()
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

books = atlas_client.find(collection_name=COLLECTION_NAME)

print("======== Going to try to tokenize the summaries ========================")
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

token_counts_file = "database/token_counts.txt"
with open(token_counts_file, "w") as f:
    for idx, book in enumerate(books):
        summary = book["Summary"]
        token_count = len(tokenizer.encode(summary))
        f.write(f"{token_count}\n")
        print(f"Book {idx+1} has {token_count} tokens")
print("================================")


atlas_client.close()
print("Closed the connection to the database")