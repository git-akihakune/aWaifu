import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.rst").read_text()

setup(
    name='aWaifu',
    version='0.1.1',
    description='Mass waifu profile generator',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/git-akihakune/aWaifu',
    author='Aki Hakune',
    author_email='akihakune@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=['aWaifu'],
    include_package_data=True,
    install_requires=[
        'Pillow',
        'psutil',
        'Waifulabs'
    ],
    entry_points={
        "console_scripts": [
            "awaifu=awaifu.__main__:main"
        ]
    }
)