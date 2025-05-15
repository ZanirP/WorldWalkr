from huggingface_hub import InferenceClient


class StoryTeller:
    def __init__(self, 
                 hf_token,
                 summary,
                 genres,
                 character,
                 situation,
                 model_name="mistralai/Mistral-Nemo-Instruct-2407"
                 ):
        self.client = InferenceClient(model=model_name, token=hf_token)
        self.summary = summary
        self.genres = genres
        self.character = character
        self.situation = situation

        
        def build_prompt(summary, genres, character, situation):
            return f"""
        You are a creative writer crafting immersive stories based on fictional worlds.
        
        Summary of the world:
        {summary}
        
        Genres: {genres}
        Main character: {character}
        Current situation: {situation}
        
        Write a vivid short story of 700–1000 words that takes place in this world. The story should be grounded in the genre, centered on the character's experience, and emotionally engaging.
        """
        
        def generate_story(self):
            prompt = build_prompt(self.summary, self.genres, self.character, self.situation)
            response = self.client.text_generation(
                prompt, 
                max_new_tokens=2048,
                temperature=0.8,
                top_p=0.9,
                stream=True
                )
            return response


