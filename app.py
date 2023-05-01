from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.constants import APP_HOST, APP_PORT
from src.pipeline.training_pipeline import TrainingPipeline
from src.pipeline.prediction_pipeline import SinglePrediction

class InputData(BaseModel):
    data: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Welcome to the home page"}

@app.post("/train")
async def train():
    train_pipeline = TrainingPipeline()
    # train_pipeline.run_pipeline()    
    return {"message": "Training completed"}

@app.post("/predict")
async def getsummary(input_data: InputData):
    input_text = input_data.data
    single_prediction = SinglePrediction()
    # result = single_prediction.predict(input_text)
    result = 'working'
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
