FaceID Login Module for Odoo
=============================

This module integrates FaceID authentication for Odoo users, allowing them to log in by recognizing their facial features using a camera. The authentication process is based on the **face_recognition** Python library, providing a simple and secure face detection and verification system.

Features
--------

- Face recognition-based login for Odoo.
- Secure facial authentication using the `face_recognition` Python library.
- Allows the use of a camera to capture and verify user faces.

Installation
------------

### Dependencies

To run this module, you need to install the following packages and libraries:

#### System-level Dependencies

Make sure you have the necessary system libraries installed. You will need a C++ compiler and some essential build tools for compiling the `dlib` library, which is a dependency of `face_recognition`.

```
    sudo apt-get update && sudo apt-get install -y g++ build-essential cmake
```

#### Python Dependencies

This module uses the `face_recognition` Python library to perform face detection and recognition. Install it with `pip`:

```
    python3 -m pip install face-recognition
```

If you'd like to use a `requirements.txt` file to manage Python dependencies, create one with the following content:

```
    face-recognition
```

You can install the dependencies from `requirements.txt` by running:

```
    pip install -r requirements.txt
```

### Odoo Integration

1. **Download or clone the module**: Place the module in your Odoo `addons` directory.

   Example:

```
    git clone https://github.com/francoleyes/faceid-authentication.git /path/to/odoo/addons/
```

2. **Restart Odoo**: Restart your Odoo instance to load the new module.

   Example:

```
    ./odoo-bin -c /path/to/odoo.conf
```

3. **Activate the module**: Go to the Odoo interface, and in the Apps section, search for the module "FaceID Login". Install it.

Usage
-----

### Setting up FaceID for a User

1. Go to the user form in Odoo.
2. Upload a profile picture for the user. The system will automatically generate a face encoding from the uploaded image.
3. Save the user form. The face encoding will be stored for future FaceID authentications.

### Logging in with FaceID

1. On the login page, click on the **Log in FaceID** button.
2. The system will capture the user's face through the camera.
3. The captured face will be compared with the stored face encoding.
4. If a match is found, the user will be logged in automatically.

Contributing
------------

If you'd like to contribute to this module, feel free to open issues or submit pull requests on GitHub.

License
-------

This module is licensed under the LGPLv3 (Lesser General Public License), which allows you to freely use, modify, and distribute the module under the same license.

Authors
-------

- Franco Leyes
- Augusto Cáceres
- Santiago Agüero
