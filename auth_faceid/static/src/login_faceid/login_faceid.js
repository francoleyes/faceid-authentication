/** @odoo-module **/
import { Component, useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class FaceIDLogin extends Component {
    static template = "auth_faceid.FaceIDLogin";
    videoRef = useRef("videoElement");
    stream = null;

    setup() {
        this.rpc = useService("rpc");
        this.notification = useService("notification");
    }

    async openModal() {
        const modal = document.getElementById('faceidModal');
        modal.style.display = "block";

        try {
            this.stream = await navigator.mediaDevices.getUserMedia({ video: true });
            this.videoRef.el.srcObject = this.stream;
            this.videoRef.el.play();
        } catch (error) {
            this.notification.add('Failed to access the camera.', { type: 'danger' });
            console.error('Camera access error:', error);
        }
    }

    closeModal() {
        const modal = document.getElementById('faceidModal');
        modal.style.display = "none";

        if (this.stream) {
            const tracks = this.stream.getTracks();
            tracks.forEach(track => track.stop());
            this.stream = null;
        }
    }

    async captureImage() {
        const canvas = document.createElement('canvas');
        canvas.width = this.videoRef.el.videoWidth;
        canvas.height = this.videoRef.el.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(this.videoRef.el, 0, 0, canvas.width, canvas.height);

        const image = canvas.toDataURL('image/png');
        this.closeModal();
        this.verifyFace(image);
    }

    async verifyFace(image) {
        try {
            const result = await this.rpc("/web/login/verify_face", { image: image });
            if (result.success) {
                this.notification.add('FaceID verified successfully!', { type: 'success' });
                window.location.href = '/web';
            } else {
                this.notification.add('Face verification failed. Please try again.', { type: 'danger' });
            }
        } catch (error) {
            this.notification.add('An error occurred during face verification.', { type: 'danger' });
            console.error('Face verification error:', error);
        }
    }
}

registry.category("public_components").add("auth_faceid.FaceIDLogin", FaceIDLogin);
