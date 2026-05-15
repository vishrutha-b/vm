from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def home():
    return "<h1>Welcome to My Python Web App!</h1><p>Hosted with Docker on GCP VM</p>"

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
