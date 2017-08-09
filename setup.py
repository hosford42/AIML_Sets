from distutils.core import setup

setup(
    name='AIML_Sets',
    version='1.0',
    packages=['aiml_sets'],
    url='https://github.com/hosford42/AIML_Sets',
    license='GNU GPL',
    author='ALICE A.I. Foundation, Inc.',
    author_email='info@alicebot.org',
    maintainer='Aaron Hosford',
    maintainer_email='hosford42@gmail.com',
    description='AIML sets (ALICE & Mitsuku)',
    package_data={
        'aiml_sets': ['*/*.aiml']
    },
)
