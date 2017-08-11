"""
# Free AIML Rule Sets

This is a collection of open-sourced AIML (Artificial Intelligence Markup
Language) rule sets, for use with any compatible AIML conversational engine.
The files have been repackaged into a single repo for easy download and
installation. I plan to eventually distribute this on the Python Package
Index to make it installable with Python's package installer, pip, making
it easily available for use with [AIML
Bot](https://github.com/hosford42/aiml_bot).

## GNU General Public License

All files are released under the GNU General Public License. The included
AIML files are (c) ALICE A.I. Foundation, Inc. I have taken care to
exclude any files that did not specifically contain a copyright & license
header provided by the original author. Any additional files that are not
marked with a copyright header of their own are (c) Aaron Hosford.

## Included AIML Sets

* [Free A.L.I.C.E. AIML Set](
  https://code.google.com/archive/p/aiml-en-us-foundation-alice/downloads)
  (ALICE)
* [Square Bear's AIML files](http://www.square-bear.co.uk/aiml/)
  (Mitsuku)
* [Standard AIML Set](https://github.com/cdwfs/pyaiml/tree/master/standard)
  (PyAIML)

"""


from setuptools import setup
import os
import warnings


def get_long_description():
    """Load the long description from the README file. In the process,
    convert the README from .md to .rst using Pandoc, if possible."""
    rst_path = os.path.join(os.path.dirname(__file__), 'README.rst')
    md_path = os.path.join(os.path.dirname(__file__), 'README.md')

    try:
        # Imported here to avoid creating a dependency in the setup.py
        # if the .rst file already exists.

        # noinspection PyUnresolvedReferences,PyPackageRequirements
        from pypandoc import convert_file
    except ImportError:
        warnings.warn("Module pypandoc not installed. Unable to generate README.rst.")
    else:
        # First, try to use convert_file, assuming Pandoc is already installed.
        # If that fails, try to download & install it, and then try to convert
        # again.
        # noinspection PyBroadException
        try:
            # pandoc, you rock...
            rst_content = convert_file(md_path, 'rst')
            with open(rst_path, 'w') as rst_file:
                rst_file.write(rst_content)
        except Exception:
            try:
                # noinspection PyUnresolvedReferences,PyPackageRequirements
                from pypandoc.pandoc_download import download_pandoc

                download_pandoc()
            except FileNotFoundError:
                warnings.warn("Unable to download & install pandoc. Unable to generate README.rst.")
            else:
                # pandoc, you rock...
                rst_content = convert_file(md_path, 'rst')
                with open(rst_path, 'w') as rst_file:
                    rst_file.write(rst_content)

    if os.path.isfile(rst_path):
        with open(rst_path) as rst_file:
            return rst_file.read()
    else:
        # It will be messy, but it's better than nothing...
        with open(md_path) as md_file:
            return md_file.read()


setup(
    name='AIML Sets',
    version='1.0',
    author='ALICE A.I. Foundation, Inc.',
    author_email='info@alicebot.org',
    maintainer='Aaron Hosford',
    maintainer_email='hosford42@gmail.com',
    license='GNU GPL',
    description='AIML sets (ALICE & Mitsuku)',
    long_description=get_long_description(),
    url='https://github.com/hosford42/AIML_Sets',

    packages=['aiml_sets'],
    package_data={
        'aiml_sets': ['*/*.aiml']
    },
    zip_safe=False
)
