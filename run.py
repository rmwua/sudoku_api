from app import create_app
import logging

app = create_app()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)


@app.route('/', methods=['GET'])
def health_check():
    return "OK", 200

if __name__ == '__main__':
    import os
    debug = os.getenv('FLASK_ENV', 'production') != 'production'
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=debug)

