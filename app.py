from fastapi import FastAPI
import FirebaseCloudMessaging as FCM
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class requets(BaseModel):
    title: str
    msg: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post('/send')
async def sendNotification(request: requets):
    tokens_registrations=[]
    await gettokens(tokens_registrations)
    response= FCM.sendPushNotification(request.title,request.msg, tokens_registrations)
    return response

app.mount("/", StaticFiles(directory="static",html = True), name="static")

async def gettokens(arr):
    tokens = FCM.db.collection('tokens').stream()
    for token in tokens:
        arr.append(token.to_dict()['token'])