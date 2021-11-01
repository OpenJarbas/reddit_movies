from setuptools import setup

setup(
    name='reddit_movies',
    version='0.0.4',
    packages=['reddit_movies'],
    url='https://github.com/OpenJarbas/reddit_movies',
    license='apache2',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    description='',
    install_requires=[
        "json_database", "feedparser", "beautifulsoup4"
    ]
)
