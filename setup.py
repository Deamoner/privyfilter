from setuptools import find_packages, setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(
    name="privyfilter",
    version="0.2.5",
    description="Photo filter for decreasing bias in photo datasets by generating synthetic matching photos",
    url="https://github.com/deamoner/privyfilter",
    author="Matthew Davis",
    author_email="mdavis@virtustructure.com",
    license="MIT",
    packages=["privyfilter"],
    package_directory={"privyfilter":"privyfilter/"},
    package_data={'privyfilter': ['Configs/*.xml', 'peoplemod/*']},
    include_package_data=True,
    keywords="photo sythetic bias privacy de-identification anonymization",
    install_requires=["numpy>=1.18.4",
    "opencv-python>=4.2.0.34", "Pillow>=7.1.2","thisapidoesnotexist>=0.2", "gdown>=3.10.1", "deepface>=0.0.29", "dlib>=19.20.0"]
)
classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development",
          "Topic :: Photo Privacy :: Indexing",
          "Topic :: Utilities"
      ]
