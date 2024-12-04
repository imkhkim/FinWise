# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import datetime
import pytz

from nlp_processor import NLPProcessor
from src.relation_extractor import cleanup
from recommend import ArticleRecommender

app = FastAPI()

class InputText(BaseModel):
    text: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp_processor = NLPProcessor()
recommender = ArticleRecommender()

@app.post("/service")
async def main(input: InputText):
    local_tz = pytz.timezone("Asia/Seoul")

    print("request_time:", datetime.datetime.now(local_tz))
    print("received_text:\n", input.text)

    try:
        result = nlp_processor.process_text(input.text)
        print("\nresult:", result)

        cur_unique_keywords = [node["id"] for node in result["nodes"]]
        cur_unique_keywords = list(set(cur_unique_keywords))
        recommendations = recommender.recommend(cur_unique_keywords)
        print("\nrecommendations:", recommendations)

        return JSONResponse({
            "hypergraph_data": result,
            "recommendations": recommendations,
            "response_time": datetime.datetime.now(local_tz).isoformat()
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("shutdown")
async def shutdown_event():
    cleanup()