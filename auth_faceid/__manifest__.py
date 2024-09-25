{
    'name': 'Auth FaceID',
    'version': "17.0.1.0.0",
    'category': 'Hidden',
    'author': 'Franco Leyes - Augusto cáceres - Santiago Agüero',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/login_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'assets': {
        'web.assets_frontend': [
            'auth_faceid/static/src/login_faceid/**/*',
        ],
    }
}
