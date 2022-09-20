import pathlib
#from distutils.core import setup

from setuptools import find_packages,setup

here = pathlib.Path(__file__).parent.resolve()

install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setup(
    name="pyspcli-ui",
    version='0.1.0',
    py_modules=['spui'],
    setup_requires=["setuptools"],
    install_requires=install_requires,
    packages=find_packages(where="spcli_ui"),
    package_dir={"": "spcli_ui"},
    include_package_data=True,
    package_data={"spcli_ui": ["*.py",]},

    #zip_safe=False,
    entry_points='''
        [console_scripts]
        spui=spui:main
    ''',
    python_requires=">=3.7, <4",
)
