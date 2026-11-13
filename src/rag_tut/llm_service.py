import os
from urllib import response
from dotenv import load_dotenv
from typer import prompt
class LLMService:
    def initialize_model(self):

        load_dotenv()

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env")


        from langchain_google_genai import ChatGoogleGenerativeAI

        self.model = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash-lite",
            temperature=1.0,
            thinking_level="low",
            max_tokens=512,
            timeout=60,
            max_retries=1
        )
        return self.model   

    def generate_response(self, prompt):
        
        response = self.model.invoke(prompt)
        return response.content[0]["text"]
    