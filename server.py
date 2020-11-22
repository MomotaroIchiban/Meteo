from flask import render_template
#import connexion
import config
from settings import (
    DEBUG,
    REST_API_IP,
    REST_API_PORT
)

# Create the application instance
#app = connexion.App(__name__, specification_dir='./')
app = config.connex_app

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


# stand alone mode
if __name__ == '__main__':
    app.run(host=REST_API_IP, port=REST_API_PORT, debug=DEBUG)
