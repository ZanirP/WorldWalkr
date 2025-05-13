import os

import pandas as pd
import numpy as np

#input filepath for the text file
txt_filepath = "data/booksummaries.txt"
#output filepath for the csv file
csv_filepath = "data/books.csv"
# output filepath for the json file
json_filepath = "data/books.json"

# Read the text file
books = pd.read_csv(txt_filepath, sep="\t", header=None, names=["wikipedia_id", "Freebase_id", "Book title", "Book Author", "Publication Date", "Genres", "Summary"], index_col=False)
# print(df.head())
'''
   wikipedia_id Freebase_id                                 Book title      Book Author Publication Date                                             Genres                                            Summary
0           620     /m/0hhy                                Animal Farm    George Orwell       1945-08-17  {"/m/016lj8": "Roman \u00e0 clef", "/m/06nbt":...   Old Major, the old boar on the Manor Farm, ca...
1           843     /m/0k36                         A Clockwork Orange  Anthony Burgess             1962  {"/m/06n90": "Science Fiction", "/m/0l67h": "N...   Alex, a teenager living in near-future Englan...
2           986     /m/0ldx                                 The Plague     Albert Camus             1947  {"/m/02m4t": "Existentialism", "/m/02xlf": "Fi...   The text of The Plague is divided into five p...
3          1756     /m/0sww  An Enquiry Concerning Human Understanding       David Hume              NaN                                                NaN   The argument of the Enquiry proceeds by a ser...
4          2080     /m/0wkt                       A Fire Upon the Deep     Vernor Vinge              NaN  {"/m/03lrw": "Hard science fiction", "/m/06n90...   The novel posits that space around the Milky ...
'''

# Drop the Freebase_id column
books.drop(columns=["Freebase_id"], inplace=True)

# count the number of missing values in each column
missing_values = books.isnull().sum()
# print("Missing values in each column:")
# print(missing_values)
'''
Missing values in each column:
wikipedia_id           0
Book title             0
Book Author         2382
Publication Date    5610
Genres              3718
Summary                0
'''
# THOUGHTS:
'''
This missing values are not necessarily a problem for us. We have all summaries, and publication dates and authors is not important for us.
However, we need Genres to be able to create a theme when writing our version of the book.
We can drop the rows with missing values in the Genres column, but we need to check if there are any rows with missing values in the Summary column.
However, that would just be removing possible books that we would use in our database. And removing books does nothing for us.
We can just leave the missing values in the dataframe and just ignore them when we are creating our database. When encountering a book with missing genre
we can just assign it a genre of "unknown" and let the user choose, or we can use AI to guess the genre based on the summary. We can also do that in the Database 
so that we have all our values in the database and we can just use the database to create the values as needed.
Now we need to check for duplicates, and i kinda of want to understand how these genres are formatted and the significance of the keys and values in the dictionary.

Ok did some looking around the keys and values in the dictionaries. The keys are the Freebase ids of the genres, and the values are the names of the genres.
The Freebase ids are not important for us, we can just use the names of the genres. We can also use the Freebase ids to get the names of the genres if we want to.
So we are going to reformat the Genres column to be a list of genres instead of a dictionary.

For duplicates, we can just check duplicates of the wikipedia_id column, since that is the only column that is unique to each book.
There can be multiple books with the same title or author, but they will have different wikipedia_ids.
and checking everything is a waste of time, cause if there is a duplicate in the wikipedia_id column, then there is a duplicate in the whole dataframe, 
and if there is a duplicate in the Book title and Book Author, it can easily be missed if capitalization is different or if there are extra spaces.
We can just check the wikipedia_id column for duplicates and drop them if there are any.
'''

# Check for duplicates
duplicates = books.duplicated(subset=["wikipedia_id"])
#print("Duplicates:")
#print(duplicates.sum())
'''
Duplicates:
0
'''

# Changing the Genres column to be a list of genres instead of a dictionary
def convert_genres_to_list(genres):
    if isinstance(genres, str):
        # Convert the string representation of the dictionary to an actual dictionary
        genres_dict = eval(genres)
		# Extract the values (genre names) from the dictionary
        genres_list = list(genres_dict.values())
        return genres_list

books["Genres"] = books["Genres"].apply(convert_genres_to_list)
# print(books["Genres"].head())
'''
0    [Roman à clef, Satire, Children's literature, ...
1    [Science Fiction, Novella, Speculative fiction...
2    [Existentialism, Fiction, Absurdist fiction, N...
3                                                 None
4    [Hard science fiction, Science Fiction, Specul...
Name: Genres, dtype: object
'''


'''
I think that's everything for now so we will save the dataframe to a csv and json file.
'''

''' 
NOT A PRIORITY: 
publication date is not important for us, but the format is not consistent.
I think we should ignore it for now, and not use publication date for anything other than outputting it to the user.
'''

# Save the dataframe to a csv file
books.to_csv(csv_filepath, index=False)
# Save the dataframe to a json file
books.to_json(json_filepath, orient="records", lines=True)