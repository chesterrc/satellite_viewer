from flask import Flask
from sscws.sscws import SscWs

# Instantiate app
app = Flask(__name__, template_folder="../pages/templates")
ssc = SscWs()
