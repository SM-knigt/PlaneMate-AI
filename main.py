from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# تحميل المتغيرات من .env
load_dotenv()

app = FastAPI()

# إعداد CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تهيئة عميل Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# تعريف الـ Request والـ Response
class PlanRequest(BaseModel):
    goal: str

class PlanStep(BaseModel):
    order: int
    task: str
    duration: str
    resources: list[str]

class PlanResponse(BaseModel):
    title: str
    steps: list[PlanStep]

# Endpoint الأساسي
@app.get("/")
def read_root():
    return {"message": "Welcome to the Groq FastAPI app! Go to /docs to test."}

# Endpoint خطة التعلم
@app.post("/plan")
def generate_plan(request: PlanRequest):
    prompt = f"""
You are an assistant that outputs ONLY strict JSON. No prose, no markdown, no code fences.
Given the user's learning goal, generate a plan in EXACTLY this JSON structure and field names:
{{
  "title": "string",
  "steps": [
    {{
      "order": 1,
      "task": "string",
      "duration": "string",
      "resources": ["url1", "url2"]
    }}
  ]
}}

Rules:
- Output valid JSON only (UTF-8), no trailing text.
- Use integers for "order".
- For "resources", provide REAL working URLs to actual learning resources.
- Use these popular platforms with real URLs:
  * YouTube: https://www.youtube.com/results?search_query=[topic]
  * GitHub: https://github.com/topics/[topic]
  * MDN Docs: https://developer.mozilla.org/en-US/docs/Web/[topic]
  * W3Schools: https://www.w3schools.com/[topic]/
  * Coursera: https://www.coursera.org/search?query=[topic]
  * edX: https://www.edx.org/search?q=[topic]
  * Khan Academy: https://www.khanacademy.org/search?referer=%2F&page_search_query=[topic]
  * FreeCodeCamp: https://www.freecodecamp.org/news/tag/[topic]/
  * Stack Overflow: https://stackoverflow.com/questions/tagged/[topic]
  * Python.org: https://docs.python.org/3/tutorial/
  * React Docs: https://react.dev/learn
  * Node.js: https://nodejs.org/en/docs/
- Replace [topic] with relevant keywords from the user's goal.
- Do not include any additional fields.

User goal: {request.goal}
"""

    model_output = None
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        model_output = response.choices[0].message.content

        # Debug (يطبع الـ response في الـ terminal)
        print("Groq raw response:", model_output)

        parsed = json.loads(model_output)
        validated = PlanResponse(**parsed)
        return validated.model_dump()

    except ValidationError as ve:
        return {"error": "Validation failed", "raw": model_output, "details": json.loads(ve.json())}
    except json.JSONDecodeError as je:
        return {"error": f"JSON decode error: {str(je)}", "raw": model_output}
    except Exception as e:
        return {"error": str(e), "raw": model_output}