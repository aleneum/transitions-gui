import codecs
from setuptools import setup, find_packages

with open('transitions_gui/version.py') as f:
    exec(f.read())

with codecs.open('README.md', 'r', 'utf-8') as f:
    # cut the badges from the description and also the TOC which is currently not working on PyPi
    long_description = ''.join(f.readlines()[0:])

setup(
    name="transitions-gui",
    version=__version__,
    description="A lightweight, object-oriented Python state machine implementation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alexander Neumann',
    author_email='aleneum@gmail.com',
    maintainer='Alexander Neumann',
    maintainer_email='aleneum@gmail.com',
    url='http://github.com/pytransitions/transitions-gui',
    packages=find_packages(exclude=['tests', 'test_*']),
    include_package_data=True,
    package_data={'transitions_gui': ['templates/*', 'static/css/*', 'static/js/*', 'static/img/*']},
    install_require=['tornado>=5.0', 'transitions>=0.7'],
    extras_require={},
    tests_require=['nose'],
    license='MIT',
    download_url='https://github.com/pytransitions/transitions-gui/archive/%s.tar.gz' % __version__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
