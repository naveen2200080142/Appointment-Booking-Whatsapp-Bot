import logging
from flask import Flask
from config import configure_app
from whatsapp import webhook_get,webhook_post

# Initialize Flask app
app = Flask(__name__)
configure_app(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Define routes
app.add_url_rule('/webhook', 'webhook_get', webhook_get, methods=['GET'])
app.add_url_rule('/webhook', 'webhook_post', webhook_post, methods=['POST'])

if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=8080)