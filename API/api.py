from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
import google.generativeai as genai
import os
import re
import json
import uvicorn
# === Import your project functions ===
from events.pdp import get_events
from places_to_visit.pl_req import places_to_visit
from movies.cinemas import extract_cinemas
from movies.shows import process_single_url
from restaurants.restaurant import main
app = FastAPI()

# === Gemini API Key ===
GEMINI_API_KEY = "AIzaSyBss-VliYiVEptERQgoEXYmSaiwn1OOD5A"
genai.configure(api_key=GEMINI_API_KEY)

# === Local API key for your app ===
VALID_API_KEY = "weekendplanner"

# === Pydantic model ===
class PromptRequest(BaseModel):
    query: str
    api_key: str
class CinemaShowRequest(BaseModel):
    cinema_name: str
    url: str
    city: str = None  # optional
    state: str = None
    country: str = None
    date: str = None
# === Gemini helper ===
def extract_intent_with_gemini(query: str) -> dict:
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are an API assistant.
Your task is to detect the user's intent.

Possible event_type values:
- "restaurants"
- "places"
- "events"
- "cinemas" (means movie theatres, multiplexes, where to watch a movie)

Extract:
1. event_type → exactly one of ["restaurants", "places", "events", "cinemas"]
2. location → the city or area the user says.

Respond with only valid JSON — no explanation, no markdown, no backticks.

Example:
{{
  "event_type": "cinemas",
  "location": "mumbai"
}}

Now process this:
\"{query}\"
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    # Clean any markdown block
    if text.startswith("```json") or text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    try:
        return json.loads(text)
    except Exception:
        raise HTTPException(status_code=400, detail=f"Gemini returned invalid JSON:\n{text}")

# === /ask endpoint ===
@app.post("/ask")
async def ask_ai(payload: PromptRequest):
    if payload.api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    intent = extract_intent_with_gemini(payload.query)
    event_type = intent.get("event_type")
    location = intent.get("location")

    result = {
        "status": "success",
        "event_type": event_type,
        "location": location
    }
    if not event_type or not location:
        raise HTTPException(status_code=400, detail="Could not extract event type or location.")

    if event_type == "places":
        data = places_to_visit(location)
        result.update({"data": data})
        
    elif event_type == "events":
        data = get_events(location)
        result.update({"data": data})
        
    elif event_type == "restaurants":
        data, address, lat, long = main(location)
        result.update({
            "data": data,
            "address": address,
            "latitude": lat,
            "longitude": long
        })
    elif event_type == "cinemas":
        # ✅ Don't call extract_cinemas() here — let the client call /cinemas!
        data = None
        result.update({"data": data})
    else:
        raise HTTPException(status_code=400, detail="Invalid event type from Gemini.")
    
    return result
# === /cinemas endpoint ===
@app.get("/cinemas")
async def get_cinemas_by_location(
    city: str = Query(..., description="City name to fetch cinemas")
):
    try:
        data = extract_cinemas(city)
        if not data:
            raise HTTPException(status_code=404, detail=f"No cinemas found for city: {city}")
        return {
            "status": "success",
            "city": city,
            "total": len(data),
            "cinemas": data,
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/cinema_shows")
async def get_cinema_shows(payload: CinemaShowRequest):
    # Build the same entry your scraper expects:
    entry = {
        "url": payload.url,
        "cinema_name": payload.cinema_name,
        "city": payload.city,
        "state": payload.state,
        "country": payload.country,
        "date": payload.date
    }

    results = process_single_url(entry)

    if not results:
        raise HTTPException(status_code=404, detail="No shows found for this cinema.")

    return {
        "status": "success",
        "total": len(results),
        "shows": results
    }
# if __name__ == "__main__":
#     uvicorn.run(
#         "API.api:app",       # module_name:variable_name
#         host="localhost",
#         port=8000,
#         reload=True
#     )