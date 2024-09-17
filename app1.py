import os

# Import necessary modules from Flask
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

# Initialize the Flask application. The __name__ argument helps Flask determine the root path of the application.
app = Flask(__name__)

# Define the route for the root URL. This function will be called when the root URL is accessed. 
@app.route('/')

def index():
   # Log a message to the console
   print('Request for index page received')
   # Render the index.html template
   return render_template('index.html')

# Define the route for the favicon
@app.route('/favicon.ico')
def favicon():
    # Send the favicon.ico file from the static directory
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Define the route for the /hello URL, only allowing POST requests
@app.route('/hello', methods=['POST'])
def hello():
   # Get the name from the form data
   name = request.form.get('name')

   if name:
       # Log a message to the console with the provided name
       print('Request for hello page received with name=%s' % name)
       # Render the hello.html template with the provided name
       return render_template('hello.html', name = name)
   else:
       # Log a message to the console indicating no name was provided
       print('Request for hello page received with no name or blank name -- redirecting')
       # Redirect to the root URL. This will trigger the index() function to get the URL. 
       return redirect(url_for('index'))

# Run the application if this script is executed directly (i.e. not being imported as a module in another script). 
# this ensures the flask development server is started only when this script is executed directly.
if __name__ == '__main__':
# app.run() starts the Flask development server. 
   app.run()