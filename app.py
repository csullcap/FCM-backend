from fastapi import FastAPI
import FirebaseCloudMessaging as FCM
app = FastAPI()

token=['fOXRcYgJQb2_ZewesBIpEb:APA91bFNM9RpdUngpKWzj8CWKI4osXxscq9sV4jjgOKoT2sMP4PxzQzemhpeK2vADI9MPDWwILFzoUhidGzyiRoKX_dYvaVZpoQuDVUFyyVAZxK5Ay-VjBcoc5WZ-FrKq25VS1XmsffI']

@app.get('/send')
async def sendNotification(title: str , msg: str):
    response= FCM.sendPushNotification(title, msg, token)
    return response

@app.get('/')
async def home():
    return {"APP": "DANP-FCM-API"}
