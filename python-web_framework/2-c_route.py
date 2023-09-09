"""
A script that starts a Flask Web application and also has
an additional route/path.
"""

from flask import Flask
from html import escape as html_escape


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
        
        @self.app.route('/hbnb', strict_slashes=False)
        def hbnb():
            """
            Route handler for '/hbnb'. Displays "HBNB".
            """
            return "HBNB"
        
        @self.app.route('/c/<text>', strict_slashes=False)
        def custom_text(text):
            """
            Route handler for '/c/<text>'. Displays "C " followed by the value of the text variable.
            Replace underscore _ symbols with spaces.

            Args:
                text (str): The text variable captured from the URL.
            """
            modified_text = html_escape(text.replace('_', ' '))
            return "C {}".format(modified_text)

if __name__ == '__main__':
    web_app = WebApp(app)
    web_app.configure_routes()
    app.run(host='0.0.0.0', port=5000)