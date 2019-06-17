from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))  # pylint: disable=invalid-name
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()  # pylint: disable=invalid-name

setup(name='quickcerts',
      version='0.2.0',
      description='Quick and easy X.509 certificate generator for SSL/TLS utilizing local PKI',
      url='https://github.com/Snawoot/quickcerts',
      author='Vladislav Yarmak',
      author_email='vladislav-ex-src@vm-0.com',
      license='MIT',
      packages=['quickcerts'],
      python_requires='>=3.4',
      setup_requires=[
          'wheel',
      ],
      install_requires=[
          'cryptography>=1.6',
      ],
      entry_points={
          'console_scripts': [
              'quickcerts=quickcerts.__main__:main',
          ],
      },
      classifiers=[
          "Programming Language :: Python :: 3.4",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: End Users/Desktop",
          "Intended Audience :: Telecommunications Industry",
          "Intended Audience :: System Administrators",
          "Intended Audience :: Other Audience",
          "Natural Language :: English",
          "Topic :: Communications :: Email :: Mail Transport Agents",
          "Topic :: Internet",
          "Topic :: Security",
          "Topic :: Internet :: Proxy Servers",
          "Topic :: Security :: Cryptography",
          "Topic :: Utilities",
      ],
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=True)
