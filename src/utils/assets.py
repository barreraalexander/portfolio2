from flask_assets import Bundle

bundles = {
    'main_scss':Bundle(
        'scss/main.scss',
        filters='libsass',
        depends=[
            'scss/*.scss',
            'scss/base/*.scss',
            'scss/components/sections/*.scss',
            'scss/components/navbars/*.scss',
        ],
        output='gen/css/main.%(version)s.css'
    ),
}