import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate('fcm-exam-b7848-firebase-adminsdk-3i48v-de2e15e070.json')
firebase_admin.initialize_app(cred)

def sendPushNotification(title, msg, registration_token, dataObject=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )
    response = messaging.send_multicast(message)
    return {'Successfully sent message:', response}