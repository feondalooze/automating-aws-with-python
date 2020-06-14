from setuptools import setup_cdn

setup(
    name='webotron-80',
    version='0.1',
    author='',
    author_email='',
    description="Webotron is a tool that deploy static website to AWS.",
    license='GPLv3+',
    packages=['webotron'],
    url='',
    installs_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
