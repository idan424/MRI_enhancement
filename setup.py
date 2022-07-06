from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Apply CLAHE algorithem to improve image contrast '
LONG_DESCRIPTION = 'A package that allows the user to choose different paramaters for CLAHE algorithem and compare differences'

# Setting up
setup(
    name="CLAHEckethon",
    version=VERSION,
    author="The best team in the world ever",
    author_email="<adigincher@mail.tau.ac.il>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'MRI', 'Contrast', 'CLHAE', 'ENHANCMENT'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)