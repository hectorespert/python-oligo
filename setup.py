from distutils.core import setup

setup(
    name='oligo',
    version='0.0.4',
    packages=['oligo'],
    install_requires=[
          'requests',
      ],
    url='https://github.com/blackleg/python-oligo',
    license='MIT',
    author='blackleg',
    author_email='hectorespertpardo@gmail.com',
    description='Obtiene datos del contador inteligente en la red de iberdrola distribucion'
)
