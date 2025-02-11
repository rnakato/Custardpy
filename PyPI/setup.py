import setuptools
from setuptools import setup
package_name = 'custardpy'

def get_version(rel_path):
    for line in open(rel_path).read().splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="custardpy",
    version=get_version(f"{package_name}/__init__.py"),
    license="GPL3.0",
    install_requires=[
        "numpy>=1.18",
        "pandas>=1.3.0",
        "scipy>=1.3",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.2.2",
        "seaborn>=0.11.1",
        "h1d>=0.2.0",
        "hic-straw>=1.3.0",
    ],
    author="Ryuichiro Nakato",
    author_email="rnakato@iqb.u-tokyo.ac.jp",
    description="Hi-C analysis tools by Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rnakato/custardpy",
    keywords="Hi-C analysis, 3D genome, NGS",
    scripts=['custardpy/checkHiCfile.py',
             'custardpy/convert_JuicerDump_to_dense.py',
             'custardpy/custardpy_clustering_boundary',
             'custardpy/custardpy_differential_DRF',
             'custardpy/DEG_boundary_analysis',
             'custardpy/drawSquareMulti',
             'custardpy/drawSquarePair',
             'custardpy/drawSquareRatioMulti',
             'custardpy/drawSquareRatioPair',
             'custardpy/drawTriangleMulti',
             'custardpy/drawTrianglePair',
             'custardpy/getBoundaryfromInsulationScore',
             'custardpy/InsulationScore.py',
             'custardpy/plotCompartmentGenome',
             'custardpy/plotInsulationScore',
             'custardpy/plotMultiScaleInsulationScore',
             'custardpy/plotHiCMatrix',
             'custardpy/plotHiCfeature'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
