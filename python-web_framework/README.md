# PYTHON-WEB_FRAMEWORK

This repo contains a flaskweb app. The web app demonstrates the various routes for displaying messages and rendering HTML templates.

This applivcation uses templates for rendering HTML content.

### TABLE OF CONTENTS

- Routes
- Challenges
- Credits

## ROUTES

**/ :** This route display “Hello HBNB!”

**/hbnb:** This route displays the message "HBNB".

**/c/<text>:** This route displays the message "C ", followed by the value of the text variable from the URL. The underscores \_ are replaced with spaces.

**/python/<text>:** This route displays the message "Python ", followed by the value of the text variable from the URL. The underscores \_ are replaced with spaces. If no text is provided, "is cool" is used as the default.

**/number/<n>:** This route displays the message " is a number" if n is an integer.

**/number_template/<n>:** This route renders an HTML page with an H1 tag containing the text "Number: n". The n value is taken from the URL.

**/number_odd_or_even/<n>:** This route renders an HTML page with an H1 tag containing the text "Number: n is even|odd" depending on whether n is even or odd. The n value is taken from the URL.

### CHALLENGES

I had challenge configuring the routes for the web application.

### CREDITS

Giving credit to @alx_africa, for giving us the project and giving us more projects to improve our software enginerring skills.
