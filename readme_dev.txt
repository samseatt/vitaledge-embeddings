


# conda create -n vitaledge-embeddings python=3.11 -y
conda activate vitaledge-embeddings


uvicorn app.main:app --host 0.0.0.0 --port 8007 --reload


curl -X POST "http://localhost:8007/embeddings/generate" -H "Content-Type: application/json" -d '{
    "texts": ["What are the symptoms of diabetes?", "How do you treat a cold?"]
}'

