from huggingface_hub import InferenceClient


class RewriteService:
    def __init__(self, api_token: str):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=api_token
        )
        self.model = "HuggingFaceH4/zephyr-7b-beta"

    def rewrite(self, input_text: str) -> str:
        prompt = (
            "You are a professional editor who specializes in making AI-generated text sound natural, conversational, and written by a human. "
            "Rewrite the following text so that it:\n"
            "- Sounds authentic and natural\n"
            "- Avoids robotic or overly formal phrasing\n"
            "- Uses common, everyday expressions\n"
            "- Maintains the original meaning\n\n"
            f"Here is the original text:\n\"{input_text}\"\n\n"
            "Now rewrite it to sound more human:"
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
