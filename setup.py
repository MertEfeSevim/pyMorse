from distutils.core import setup

setup(
    name='pyMorse',
    version='1.0',
    packages=[''],
    url='https://github.com/MertEfeSevim/pyMorse',
    author='Mert Efe Sevim',
    author_email='mertefesevim@gmail.com',
    description='pyMorse is a Python library project that translates the Morse Code into an Latin alphabet or vice versa.',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ], requires=['pygame']
)
