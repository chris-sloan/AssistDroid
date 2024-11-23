from setuptools import setup

setup(
    name="android-helper",
    version="0.1",
    py_modules=["menu", "android_helper", "adb_devices", "create_branch", "utilities"],
    entry_points={
        'console_scripts': [
            'android-helper=android_helper:main',
        ],
    },
)