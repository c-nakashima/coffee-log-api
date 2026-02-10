from fastapi import FastAPI

from app.api.routes.roasters import router as roasters_router

app = FastAPI()
app.include_router(roasters_router)

@app.get("/")
def root():
    return {"ok": True}
