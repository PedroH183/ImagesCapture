from main import app

@app.route("/ping")
def ping():
    return "pong", 200

@app.route("/all-images", methods=["GET"])
def get_all_images(request):
    """ This controller is to take all data of images downloaded """

    request_body = request.body
    return request_body, 200

@app.route("/get-image", methods=["GET"])
def get_image_download():
    """ This controller take a base64 image """
    pass
