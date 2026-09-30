import base64


SYSTEM_PROMPT = """You are a careful multimodal AI assistant.

Analyze only information that is actually visible in the provided image.
Answer the user's question clearly and accurately.
Do not invent names, dates, prices, phone numbers, labels, or other details.
If the requested information is not visible or cannot be determined from the image,
clearly say that it is not visible or cannot be determined.
For document images, extract information faithfully.
For diagrams, explain the visible relationships and labels.
Keep answers concise but useful."""


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
