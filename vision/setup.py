from setuptools import setup

setup(
    name = 'lightning_vision',
    version = '0.1.0',
    packages = ['vision', 'vision/camera', 'vision/inference', 'vision/network', 'vision/pipelines'],
    entry_points = {
        'console_scripts': [
            'lightning_vision = app.__main__:main'
        ]
    }
)
