from distutils.core import setup
import sys
import time


long_description = open('README.md').read()
sys.stderr.write('\n' + long_description)
time.sleep(5)


setup(
    name='requestes',
    version='0.0.1',
    description='Python Module Security Admonition',
    long_description=long_description,
    author='David Fischer',
    author_email='djfische@gmail.com',
    url='https://github.com/davidfischer/requestes',
    license='BSD',
    platforms=['OS Independent'],
    packages=[
        'requestes',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security',
    ],
)
