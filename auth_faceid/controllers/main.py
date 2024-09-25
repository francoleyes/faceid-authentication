from odoo import http
from odoo.http import request
import base64
import face_recognition
from io import BytesIO
from PIL import Image
import numpy as np
from odoo.exceptions import AccessDenied


class FaceIDLoginController(http.Controller):

    @http.route('/web/login/verify_face', type='json', auth='public', methods=['POST'])
    def verify_face(self, image):
        try:
            image_data = base64.b64decode(image.split(',')[1])
            image_pil = Image.open(BytesIO(image_data)).convert('RGB')
            captured_image = np.array(image_pil)

            captured_face_encodings = face_recognition.face_encodings(captured_image)

            if not captured_face_encodings:
                return {'success': False, 'message': 'No face detected in the captured image.'}

            captured_face_encoding = captured_face_encodings[0]

            users = request.env['res.users'].sudo().search([('image_1920', '!=', False)])

            if not users:
                return {'success': False, 'message': 'No users with registered images found.'}

            for user in users:
                user_image_data = base64.b64decode(user.image_1920)
                user_image_pil = Image.open(BytesIO(user_image_data)).convert('RGB')
                user_image = np.array(user_image_pil)

                user_face_encodings = face_recognition.face_encodings(user_image)

                if not user_face_encodings:
                    continue

                user_face_encoding = user_face_encodings[0]

                match = face_recognition.compare_faces([user_face_encoding], captured_face_encoding)

                if match[0]:
                    return self._login_user(user)

            return {'success': False, 'message': 'No match found for the captured face.'}

        except AccessDenied:
            return {'success': False, 'message': 'Access denied.'}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    def _login_user(self, user):
        try:
            request.session.uid = user.id
            session_token = user._compute_session_token(request.session.sid)
            request.session.session_token = session_token

            return {'success': True, 'message': f'User {user.login} authenticated successfully.'}

        except Exception as e:
            return {'success': False, 'message': f'Session creation error: {str(e)}'}
