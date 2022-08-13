import modcam
from setuptools import setup

setup(
    name="ModCam",
    version=modcam.__version__,
    description="Camera FOV Modeller",
    url="https://github.com/alsimoneau/modcam",
    author="Alexandre Simoneau",
    author_email="alsimoneau@gmail.com",
    liscence="MIT",
    packages=["modcam"],
    zip_safe=False,
    install_requires=[
        "Click",
        "matplotlib",
        "numpy",
    ],
    entry_points="""
        [console_scripts]
        modcam=modcam.main:modcam
    """,
)
