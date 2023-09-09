"""
A script that starts a Flask Web application
"""

from flask import Flask

app = Flask(__name__)

class WebApp:
    """
    A simple Flask web application that displays a greeting message.
    
    Attributes:
        app (Flask): The Flask app instance.
    """

    def __init__(self, app):
        """
        Initialize the WebApp with a Flask app instance.

        Args:
            app (Flask): The Flask app instance.
        """
        self.app = app

    def configure_routes(self):
        """
        Configure the routes for the web application.
        """
        @self.app.route('/', strict_slashes=False)
        def hello_hbnb():
            """
            Route handler for the root URL '/'. Displays "Hello HBNB!".
            """
            return "Hello HBNB!"

if __name__ == '__main__':
    web_app = WebApp(app)
    web_app.configure_routes()
    app.run(host='0.0.0.0', port=5000)