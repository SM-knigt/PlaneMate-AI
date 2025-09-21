import os
from openai import OpenAI
from dotenv import load_dotenv

# تحميل المتغيرات من .env
load_dotenv()

# تهيئة العميل باستخدام مفتاح Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# تجربة طلب من الموديل الصحيح
resp = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # ✅ الموديل الجديد
    messages=[{"role": "user", "content": "Hello Groq, say hi in JSON"}],
    response_format={"type": "json_object"}
)

print(resp.choices[0].message.content)