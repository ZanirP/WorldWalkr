import streamlit as st
from app import atlas_search
import model.story_generator as sg
import os

# Load environment variables
hf_token = os.getenv("HUGGING_FACE_TOKEN")

st.set_page_config(
    page_title="WorldWalkr",
    page_icon="🌍",
    layout="centered"
)

st.title("WorldWalkr")
st.subheader("Turn any book into a immersive travel experience!")
with st.expander("What is WorldWalkr?"):
    st.write(
        "WorldWalkr is a story generator that allows you to explore the world of your favorite book. "
        "Simply upload a book, and we'll generate a immersive, character-driven side story that feels true to the world you love."
    )
    
st.header("Input")

book_title = st.text_input("Book Title", placeholder="Enter the title of the book")
character = st.text_input("Character", placeholder="Enter the name of the character whose story you want to create")
situation = st.text_area("Situation", placeholder="Describe the situation your character is in!")



submit_button = st.button("Confirm Book")


if submit_button:
    possible_books = atlas_search(book_title)
    if possible_books:
        st.session_state["possible_books"] = possible_books
        st.session_state.book_index = 0
    else:
        st.error("No books found. Please input a different title.")
    
if "possible_books" in st.session_state and st.session_state.book_index < len(st.session_state.possible_books):
    book = st.session_state.possible_books[st.session_state.book_index]
    st.write(f"**Book Title:** {book['Book title']}")
    st.write(f"**Author:** {book['Book Author']}")
    st.write(f"**Genres:** {', '.join(book['Genres'])}")
    st.write(f"**Summary:** {book['Summary']}")
    
    if st.button("Next Book"):
        st.session_state.book_index += 1
        st.rerun()
    if st.button("Generate Story"):
        st.write("Generating story...")
        story_teller = sg.StoryTeller(
            hf_token=hf_token,
            summary=book['Summary'],
            genres=", ".join(book['Genres']),
            character=character,
            situation=situation
        )
        print(dir(story_teller))
        story_teller.summary = book['Summary']
        story_teller.genres = ", ".join(book['Genres'])
        story_teller.character = character
        story_teller.situation = situation
        
        response = story_teller.generate_story()
        st.write("**Generated Story:**")
        for chunk in response:
            st.write(chunk['generated_text'])
    else:
        st.write("Please select a book to generate a story.")
else:
    st.write("No books available. Please input a book title to search.")
        
