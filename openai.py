from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
