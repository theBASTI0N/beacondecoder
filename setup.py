from distutils.core import setup
setup(
  name = 'beacon-decoder',
  packages = ['beacon-decoder'],
  version = '1.0',  
  license='MIT',
  description = 'A Python library for decoding certain types of Bluetooth LE Beacons',
  author = 'theBASTI0N',
  author_email = 'theBASTI0Ncode@gmail.com',
  url = 'https://github.com/theBASTI0N/beacon-decoder',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['BLE', 'decode', 'iot'],
  install_requires=[            # I get to this in a second
          'math',
          'binascii',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7'
  ],
)