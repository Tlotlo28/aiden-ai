from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
import os, json, re
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Aiden - AI Idea Validator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are Aiden, a sharp, experienced startup advisor and business strategist. 
You ONLY help with business ideas, startups, entrepreneurship, and related business topics.

If the user's input is NOT related to a business idea, startup, product, service, or entrepreneurship, 
respond with EXACTLY this JSON and nothing else:
{"off_topic": true, "message": "I can only help with business ideas and startups."}

If it IS a business idea, respond ONLY with valid JSON (no markdown, no explanation, just raw JSON) in this exact structure:
{
  "off_topic": false,
  "idea_summary": "Brief 1-sentence summary of the idea",
  "market_demand": {
    "score": <integer 0-100>,
    "verdict": "<Low|Moderate|High|Very High>",
    "analysis": "<2-3 sentence market analysis>"
  },
  "competitors": [
    {"name": "<company name>", "description": "<what they do and their weakness>", "threat_level": "<Low|Medium|High>"}
  ],
  "monetization_ideas": [
    {"model": "<name>", "description": "<how it works for this idea>", "potential": "<Low|Medium|High>"}
  ],
  "risks": [
    {"risk": "<risk name>", "description": "<explanation>", "severity": "<Low|Medium|High>"}
  ],
  "advertising_channels": [
    {"channel": "<channel name>", "strategy": "<specific tactic for this idea>", "cost": "<Free|Low|Medium|High>"}
  ],
  "learn_more_links": [
    {"title": "<resource title>", "url": "<real URL>", "type": "<Article|Course|Community|Tool>"}
  ],
  "overall_score": <integer 0-100>,
  "aiden_verdict": "<2-3 sentence personal advisor take from Aiden — be direct, honest, motivating>",
  "startup_checklist": [
    "<checklist item 1>",
    "<checklist item 2>",
    "<checklist item 3>",
    "<checklist item 4>",
    "<checklist item 5>",
    "<checklist item 6>",
    "<checklist item 7>",
    "<checklist item 8>"
  ]
}

Be specific to the idea. Give real competitor names. Give real, working URLs for resources. Be honest but encouraging."""


class IdeaRequest(BaseModel):
    idea: str
    want_plan: bool = False


@app.post("/api/validate")
async def validate_idea(request: IdeaRequest):
    if len(request.idea.strip()) < 10:
        raise HTTPException(status_code=400, detail="Please describe your idea in more detail.")

    user_message = f"Evaluate this business idea: {request.idea}"
    if request.want_plan:
        user_message += "\n\nThe entrepreneur wants a step-by-step startup plan included."

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=3000,
        )

        raw = completion.choices[0].message.content.strip()
        # Strip markdown code fences if present
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

        data = json.loads(raw)
        return data

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Aiden had trouble parsing the response. Please try again.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    return {"status": "Aiden is online"}


# Serve frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
