from fastapi import FastAPI, Depends
from pydantic import BaseModel
from .api.model import get_model, QAModel

app = FastAPI()


class QARequest(BaseModel):
    text: str
    query: str


class QAResponse(BaseModel):
    answer: str
    confidence: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Path for QA service
@app.post("/predict", response_model=QAResponse)
async def predict(text_query: QARequest, qa_model: QAModel = Depends(get_model)):
    output_dict = {}
    text = text_query.text
    query = text_query.query
    answer, confidence = qa_model.predict(text, query)
    output_dict["answer"] = answer
    output_dict["confidence"] = confidence
    return output_dict
