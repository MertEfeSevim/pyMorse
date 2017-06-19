from distutils.core import setup

try :
    import pip
except ImportError:
    raise ImportError("Pip should be imported")
else:
    pip.main(["install", "--upgrade", "pygame"])

    try:
        import pygame, time
    except ImportError:
        raise ImportError("You need to import PyGame to use sound feature.")

setup(
    name='pyMorse',
    version='1.1',
    url='https://github.com/MertEfeSevim/pyMorse',
    author='Mert Efe Sevim',
    author_email='mertefesevim@gmail.com',
    description='pyMorse is a Python library project that translates the Morse Code into an Latin alphabet or vice versa.',
    classifiers = [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        ], requires=['pygame', 'pip']
)
