import logging
import flask

from flask import request
from flask_cors import CORS
from routes.src import tmoflask, form99

logger = logging.getLogger()

app = flask.Blueprint("controllers", __name__)
APP = tmoflask.TMOFlask(__name__, instance_relative_config=True)
CORS(app)


@app.route('/print', methods=['POST'])
def print_pdf():
    """
    This function is being invoked from FECFile and Vendors
    HTTP request needs to have form_type, file, and attachment_file
    form_type : F99
    file: please refer to below sample JSON
    :return: return JSON response
    sample:
    {
    "message": "",
    "results": {
        "file_name": "bd78435a70a70d656145dae89e0e22bb.pdf",
        "file_url": "https://fecfile-dev-components.s3.amazonaws.com/output/bd78435a70a70d656145dae89e0e22bb.pdf"
    },
    "success": "true"
    }
    """
    form_type = request.form['form_type']
    if form_type == 'F99':
        return form99.print_f99()