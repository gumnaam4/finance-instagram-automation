from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def summarize_news(text):

    prompt = f"""
    Convert this finance news into an Instagram post.

    Format:
    Headline
    3 bullet points
    Investor takeaway

    News: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content