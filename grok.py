from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('GROQ_API_KEY')
def grokResp(prompty):
    client = Groq()
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompty
            }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )
    
    resplist = []
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        if content:  # Only append non-empty chunks
            resplist.append(content)
            print(content, end="")
    
    # Join the list into a single string for easier use
    full_response = "".join(resplist)
    print("\n")  # Add newline after streaming
    
    return full_response  # Return the complete response

if __name__ == "__main__":
    response = grokResp('H')
    print(f"\nComplete response length: {len(response)} characters")