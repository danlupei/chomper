import setuptools

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#") and not line.startswith("-e")]

with open('readme.org', 'r') as f:
    long_description = f.read()

reqs = parse_requirements('requirements.txt')

setuptools.setup(
    name="chomper",
    version="0.0.1",
    url="https://github.com/aniketpanjwani/chomper",
    author="Aniket Panjwani",
    description="Block distracting websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="productivity internet distractions self-control",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3",
        "Operating System :: GNU/Linux",
        "Development Status :: 3 - Alpha"
    ),
    install_requires=reqs,
    dependency_links=['https://github.com/mitmproxy/mitmproxy/tarball/master#egg=mitmproxy'],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'chomper=chomper:main',
        ],
    },
    package_data={
        'data': ['data/rules.yaml'],
    },
)