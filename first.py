from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def hii():
    return {"message":"hello"}