import base64


SYSTEM_PROMPT = """You are a careful multimodal AI assistant.

Answer only what the user asks.
Analyze only information visible in the image.
Do not guess or invent information.

If the requested information is not visible:
- Clearly say it is not visible.
- Do not explain unrelated parts of the image.

For document images, extract information faithfully when requested.
For diagrams, explain the visible relationships and labels only when the user asks for an explanation.

Keep responses concise and relevant."""


def image_to_data_url(image_bytes: bytes, mime_type: str) -> str:
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def analyze_image(client, model, image_bytes: bytes, mime_type: str, question: str) -> str:
    image_data_url = image_to_data_url(image_bytes, mime_type)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_data_url
                        }
                    }
                ]
            }
        ],
        max_completion_tokens=700
    )

    return response.choices[0].message.content
