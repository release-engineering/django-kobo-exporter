import os

from setuptools import find_packages, setup


def get_long_description():
    readme = os.path.join(os.path.dirname(__file__), "README.md")
    out = []

    with open(readme, "rt") as f:
        # Long description is the README but slightly tweaked:
        # - drop the first line (header) as it's redundant on pypi
        # - drop the unusable TOC (no anchors rendered on pypi)
        lines = f.__iter__()
        next(lines)
        for line in lines:
            if "<!--TOC-->" in line:
                for toc_line in lines:
                    if "<!--TOC-->" in toc_line:
                        break
            else:
                out.append(line)

    return "".join(out)


setup(
    name="django-kobo-exporter",
    version="1.1.1",
    description="Prometheus exporter for kobo hub",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/release-engineering/django-kobo-exporter",
    license="GPLv3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=["django", "prometheus-client", "kobo"],
    python_requires=">=3.6",
    project_urls={
        "Changelog": "https://github.com/release-engineering/django-kobo-exporter/blob/master/CHANGELOG.md",
    },
)
