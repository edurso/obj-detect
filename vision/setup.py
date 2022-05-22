from setuptools import setup

setup(
    name = 'lightning_vision',
    version = '0.1.0',
    packages = ['app', 'app/camera', 'app/inference', 'app/network', 'app/pipelines'],
    entry_points = {
        'console_scripts': [
            'lightning_vision = app.__main__:main'
        ]
    }
)
