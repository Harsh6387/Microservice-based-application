from fastapi import FastAPI
from transformers import pipeline

# Initialize FastAPI
app = FastAPI()

# Load the Hugging Face model
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/generate")
def generate_answer(question: str):
    response = qa_pipeline(question, max_length=100)
    return {"answer": response[0]['generated_text']}

# Run the API server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

