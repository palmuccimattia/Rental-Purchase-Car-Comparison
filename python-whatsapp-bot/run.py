import logging

from app import create_app


app = create_app()

if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=80)
   # TODO: insert the assistant ID in the environment and find a way to have a debit card to use CHATGPT
