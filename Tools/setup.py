from setuptools import setup
import os

setup(name='giki',
    version='0.1pre',
    description='a Git-based wiki',
    author='Adam Brenecki',
    author_email='adam@brenecki.id.au',
    url='',
    packages=['.'.join(i[0].split(os.sep))
        for i in os.walk('giki')
        if '__init__.py' in i[2]],
    install_requires=[
    
            beautifulsoup4==4.4.1,
            boto==2.48.0,
            bz2file==0.98,
            certifi==2017.7.27.1,
            chardet==3.0.4,
            gensim==2.3.0,
            html5lib==0.999,
            idna==2.5,
            nltk==3.2.4,
            numpy==1.13.1,
            pexpect==4.0.1,
            pip==9.0.1,
            ptyprocess==0.5,
            pyxdg==0.25,
            reportlab==3.3.0,
            requests==2.18.3,
            scipy==0.19.1,
            setuptools==20.7.0,
            six==1.10.0,
            smart-open==1.5.3,
            textblob==0.12.0,
            twitter==1.17.1,
            urllib3==1.22,

    ],
    extras_require = {
        'test':  [
            'nose==1.1.2',
            'WebTest==1.4.0',
        ],
        'faster_markdown':  [
            'misaka==1.0.2',
        ],
    },
    entry_points = {
    'console_scripts':
        ['giki = giki.cli:main'],
    },
)
