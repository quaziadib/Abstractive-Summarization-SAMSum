import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Abstractive-Summarization-SAMSum"
AUTHOR_USER_NAME = "quazi_adib"
SRC_REPO = "abstractSummarizer"
AUTHOR_EMAIL = "quazi_adib@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Basic Model for Summarization App",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)