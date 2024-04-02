import logging
from io import BytesIO

from flask import Blueprint, jsonify, request, send_file
from PIL import Image

from utils.segmentation_utils import instance_segmentation_api

segmentation_bp = Blueprint("segmentation_bp", __name__)


@segmentation_bp.route('/segmentation', methods=['POST'])
def index():
    logger = logging.getLogger(__name__)
    if 'file' not in request.files:
        return jsonify({'error': 'No file sent'})

    file = request.files['file']
    img = Image.open(file)

    logger.info(f"Received image with size {img.size}")
    segmented_img = instance_segmentation_api(img)

    img_buffer = BytesIO()

    segmented_img_pil = Image.fromarray(segmented_img)
    segmented_img_pil.save(img_buffer, format='JPEG')
    img_buffer.seek(0)

    logger.info("Successfully segmented image")
    return send_file(img_buffer, mimetype='image/jpeg', as_attachment=True, download_name='segmented_image.jpg')
