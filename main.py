from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(title="LightningMCP")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
