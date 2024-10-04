from odoo import models, fields, api
import base64
import face_recognition
import numpy as np
from PIL import Image
from io import BytesIO


class ResUsers(models.Model):
    _inherit = 'res.users'

    face_encoding = fields.Binary(compute="_compute_face_encoding", store=True)

    @api.depends('image_512')
    def _compute_face_encoding(self):
        for user in self.filtered('image_512'):
            image_data = base64.b64decode(user.image_512)
            image = Image.open(BytesIO(image_data))

            if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                image = image.convert('RGBA')
            else:
                image = image.convert('RGB')

            image_np = np.array(image)
            encodings = face_recognition.face_encodings(image_np)
            if encodings:
                user.face_encoding = base64.b64encode(encodings[0].tobytes())
