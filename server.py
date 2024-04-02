__author__ = 'Jeremy MOREL'
__version__ = '1.0.0'
__status__ = 'Dev'

from flask import Flask, render_template, request
from PIL import Image
from utils.segmentation_utils import instance_segmentation_api
from io import BytesIO
from base64 import b64encode


def create_app():
    app = Flask(__name__)

    import secrets 

    app.secret_key = secrets.token_hex(128)
    
    @app.route('/', methods=['GET'])
    def home():
        
        return render_template('image.html')
    
    @app.route('/segment', methods=['POST'])
    def segment():
        if request.method == 'POST':
            file = request.files['img']

            img_buffer = BytesIO()
            original_img = Image.open(file)
            original_img.save(img_buffer, format='JPEG')
            original_img = 'data:image/png;base64,' + b64encode(img_buffer.getvalue()).decode('ascii')

            img = Image.open(file)
            segmented_img = instance_segmentation_api(img)
            img_buffer = BytesIO()
            segmented_img_pil = Image.fromarray(segmented_img)
            segmented_img_pil.save(img_buffer, format='JPEG')
            img_buffer.seek(0)

            segmented_img = 'data:image/png;base64,' + b64encode(img_buffer.getvalue()).decode('ascii')

            return render_template('image.html', original_image=original_img, segmented_image=segmented_img)
    
    return app

flask_app = create_app()
 
if __name__ == '__main__':
    flask_app.run(port=80, host="0.0.0.0", debug=True)