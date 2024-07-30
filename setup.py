from setuptools import setup,find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A module to access data from the Mauro Borges Statistic and Socioeconomic Institute (IMB), Goias - Brazil'
KEYWORDS = ['statistics','data','IMB','Mauro Borges','Brazil']

setup(
      name='pybdedata',
      version=VERSION,
      description=DESCRIPTION,
      url='https://www.imb.go.gov.br/bde/',
      author='Bernard Silva de Oliveira',
      author_email="bernard.oliveira@goias.gov.br",
      keywords=KEYWORDS,
      license='MIT License',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['requests'],
)