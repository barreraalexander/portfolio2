from flask_assets import Bundle

bundles = {
    'main_scss':Bundle(
        'scss/main.scss',
        filters='libsass',
        depends=[
            'scss/*.scss',
            # 'scss/base/*.scss',
            # 'scss/pages/*.scss',
            # 'scss/components/navbars/*.scss',
            # 'scss/components/pieces/*.scss',
            # 'scss/components/sections/*.scss',
        ],
        output='gen/css/main.%(version)s.css'
    ),
}