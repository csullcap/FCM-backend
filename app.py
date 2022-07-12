from fastapi import FastAPI
import FirebaseCloudMessaging as FCM
app = FastAPI()

token=['cUjA60KWRseP3zPI3DjxID:APA91bGBDrihSC6hVxxUaGbAikbn6dluZF8CYqf8eeBn69IHVh5YYHMQ4HMMXeHcPjhXXz5KgNpldo0HtbfZzAdbrFrDz9aktofLVj8uG67lOO58hTu9r-50BlFB0D6PiEHWPqOVU-F7']

@app.get('/send')
async def sendNotification(title: str , msg: str):
    response= FCM.sendPushNotification(title, msg, token)
    return response

@app.get('/')
async def home():
    return {"APP": "DANP-FCM-API"}
