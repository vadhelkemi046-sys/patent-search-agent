from dotenv import load_dotenv
from google import genai
from search import search_patents

load_dotenv()
client = genai.Client()  # GEMINI_API_KEY apne aap .env se le leta hai


def check_novelty(idea):
    similar = search_patents(idea, n=3)
    context = "\n\n".join(f"[{r['id']}] {r['text']}" for r in similar)

    prompt = f"""You are a patent analyst.

User's idea:
{idea}

Existing patents found:
{context}

Tell the user:
1. Which patents are most similar and why
2. A novelty verdict: High / Medium / Low
3. What the user could change to make the idea more unique

Keep it short and simple."""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )
    return response.text


if __name__ == "__main__":
    idea = input("Your idea: ")
    print(check_novelty(idea))