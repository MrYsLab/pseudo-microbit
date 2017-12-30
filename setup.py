from setuptools import setup

setup(
    name='pseudo-microbit',
    version='0.1.0',
    py_modules=['microbit', 'music', 'neopixel',
                'os','speech', 'radio'],
    url='https://github.com/MrYsLab/pseudo-microbit',
    download_url='https://github.com/MrYsLab/pseudo-microbit',
    license='MIT',
    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    description='API to be used with PyCharm for micro:bit python development',
    keywords=['micro:bit', 'microbit', 'micropython'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
)
