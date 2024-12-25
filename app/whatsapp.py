
## handlers.py
import logging
import requests
from flask import jsonify, request
from config import ACCESS_TOKEN, PHONE_NUMBER_ID, VERSION, VERIFY_TOKEN
from webhook import signature_required


def send_message(to, text):
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    response = requests.post(url, headers=headers, json=payload)
    logging.info(f"Response: {response.json()}")
    return response.json()

def send_interactive_message(to, body, buttons):
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": body},
            "action": {"buttons": buttons}
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    logging.info(f"Response: {response.json()}")
    return response.json()


def webhook_get():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            logging.info("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            logging.info("VERIFICATION_FAILED")
            return jsonify({"status": "error", "message": "Verification failed"}), 403
    else:
        logging.info("MISSING_PARAMETER")
        return jsonify({"status": "error", "message": "Missing parameters"}), 400

@signature_required
def webhook_post():
    body = request.get_json()
    logging.info(f"Incoming message: {body}")

    if "messages" in body.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}):
        for message in body["entry"][0]["changes"][0]["value"]["messages"]:
            sender = message["from"]
            message_type = message["type"]
            if message_type == "text":
                text = message["text"]["body"].lower()
                if text in ["hi", "hello", "hey"]:
                    buttons = [
                        {"type": "reply", "reply": {"id": "1", "title": "Book Appointment"}},
                        {"type": "reply", "reply": {"id": "3", "title": "Last Bookings"}},
                        {"type": "reply", "reply": {"id": "4", "title": "Others"}}
                    ]
                    send_interactive_message(sender, "Welcome! Please select an option:", buttons)
                else:
                    send_message(sender, "Invalid option. Please select a valid option.")
    return jsonify({"status": "ok"}), 200

