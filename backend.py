import os
from groq import Groq


class MultilingualChatbot:
    """Multilingual chatbot using Groq's LLaMA 3.3 model."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY environment variable is not set. "
                "Please add it to your .env file or set it in your environment."
            )
        self.client = Groq(api_key=api_key)

    def chat(self, message, language="English", history=None):
        """
        Send a message to the chatbot and get a response in the specified language.

        Args:
            message (str): User's input message
            language (str): Target language for response
            history (list): Previous conversation messages (default: [])

        Returns:
            str: Assistant's response in the specified language
        """
        if history is None:
            history = []

        messages = [
            {
                "role": "system",
                "content": f"You are a helpful multilingual assistant. Always respond in {language}. Be concise, friendly, and accurate.",
            }
        ]
        messages.extend(history)
        messages.append({"role": "user", "content": message})

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )
        return response.choices[0].message.content
