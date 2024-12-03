import sys
import logging
from flask import Blueprint, request
from app.Database import repository


bp = Blueprint('controllers', __name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('INFO')


@bp.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

@bp.route("/all-images", methods=["GET"])
def get_all_images():
    """ This controller is to take all data of images downloaded """

    data = request.get_json()

    all_file_list = repository.get_all_files()
    logger.info(f"All files >> {all_file_list}")

    return data, 200

@bp.route("/get-image", methods=["GET"])
def get_image_download():
    """ This controller take a base64 image """
    pass
