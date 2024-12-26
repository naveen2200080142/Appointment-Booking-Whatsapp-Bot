# Appointment Booking WhatsApp Bot

This project is a WhatsApp bot for booking appointments, providing information about the business, and managing user interactions. The bot is built using Flask and integrates with the WhatsApp Cloud API. It uses PostgreSQL for storing user data and chat history.

## Features

- Book appointments
- Provide information about the business
- Retrieve booking history
- Handle user queries with interactive buttons

## Technologies Used

- Python
- Flask
- PostgreSQL
- WhatsApp Cloud API
- psycopg2
- dotenv

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- WhatsApp Business Account
- Ngrok (for local development)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/naveen2200080142/Appointment-Booking-Whatsapp-Bot.git
    cd Appointment-Booking-Whatsapp-Bot
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL:**

    - Create a new PostgreSQL database and user:

        ```sql
        CREATE DATABASE whatsapp_bot;
        CREATE USER bot_user WITH PASSWORD 'your_password';
        GRANT ALL PRIVILEGES ON DATABASE whatsapp_bot TO bot_user;
        ```

5. **Configure environment variables:**

    - Create a `.env` file in the project root and add the following:

        ```plaintext
        ACCESS_TOKEN=your_access_token
        PHONE_NUMBER_ID=your_phone_number_id
        VERIFY_TOKEN=your_verify_token
        VERSION=v21.0
        APP_SECRET=your_app_secret
        DATABASE_URL=postgresql://bot_user:your_password@localhost/whatsapp_bot
        ```

6. **Initialize the database:**

    ```sh
    python db.py
    ```

7. **Run the Flask app:**

    ```sh
    python app.py
    ```

8. **Expose your local server using Ngrok:**

    ```sh
    ngrok http 8080
    ```

    - Update your WhatsApp Cloud API settings with the Ngrok URL for the webhook.

## Usage

- Start the bot by sending a greeting message like "hi", "hello", or "hey".
- The bot will respond with interactive buttons for different options.
- Select an option to proceed with booking an appointment, getting information, or querying your booking history.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or support, please contact [your-email@example.com].
