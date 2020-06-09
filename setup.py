from setuptools import find_packages, setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(
    name="privyfilter",
    version="0.1.15",
    description="Privacy Photo filter for GDPR compliant photo sharing and machine learning without bias.",
    url="https://github.com/deamoner/privyfilter",
    author="Mattthew Davis AKa Deamoner",
    author_email="mdavis@virtustructure.com",
    license="MIT",
    packages=["privyfilter"],
    package_directory={"privyfilter":"privyfilter/"},
    package_data={'privyfilter': ['Configs/*.xml']},
    include_package_data=True,
    keywords="photo privacy de-identification anonymization",
    install_requires=["numpy>=1.18.4",
    "opencv-python>=4.2.0.34", "PIL>=1.1.6"]
)
classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development",
          "Topic :: Photo Privacy :: Indexing",
          "Topic :: Utilities"
      ]
