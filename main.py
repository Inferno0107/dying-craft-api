from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import uuid

app = FastAPI()

# IMPORTANT: Change this to your Vercel URL after deploying the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

artisans_db = [
    {
        "id": "1", "name": "Master Hiroshi", "craft_type": "Kintsugi", "region": "Kyoto, Japan",
        "age": 78, "experience": 55, "bio": "Last practitioner of the Edo-style lacquer technique.",
        "practitioners_count": 3, "has_apprentice": False, "is_documented": False,
        "lat": 35.0116, "lng": 135.7681, "image_url": "https://images.unsplash.com/photo-1615111784767-4d7c0279bc6a"
    },
    {
        "id": "2", "name": "Elena Rodriguez", "craft_type": "Backstrap Weaving", "region": "Cusco, Peru",
        "age": 62, "experience": 40, "bio": "Preserving Inca-pattern weaving using natural insect dyes.",
        "practitioners_count": 12, "has_apprentice": True, "is_documented": True,
        "lat": -13.5319, "lng": -71.9675, "image_url": "https://images.unsplash.com/photo-1590076214667-c0f33b98c442"
    }
]

@app.get("/")
def home():
    return {"status": "Dying Craft API Online"}

@app.get("/artisans")
def get_artisans():
    for a in artisans_db:
        # Simple risk calculation logic
        score = 0
        if a['age'] > 70: score += 40
        if a['practitioners_count'] < 5: score += 40
        if not a['has_apprentice']: score += 20
        a['risk_score'] = score
    return artisans_db

@app.post("/compare-technique")
async def compare_technique():
    import random
    return {"score": random.randint(70, 95), "feedback": "Excellent lineage alignment!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)