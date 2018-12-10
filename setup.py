from setuptools import setup
import nltk

nltk.download('popular', download_dir='./env/nltk_data')

setup(name='pendulum',
      version='1.0',
      description='Intelligent chronoparsing',
      url='https://github.com/TomLavenziano/Pendulum/',
      license='LGPLv3',
      packages=['pendulum'],
      zip_safe=False)
