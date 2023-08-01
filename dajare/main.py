from fastapi import FastAPI
import dajare
app = FastAPI()
@app.get("/")
async def root():
    return {"summary":"https://github.com/yuzu-machan/Dajare-checker/tree/main"}
@app.get("/judge")
async def judge(text:str="",length:int=0):
    return dajare.judgment(text,length)