from numpy.distutils.core import setup
from pathlib import Path

scripts = [str(x) for x in Path('Scripts').iterdir() if x.is_file()]

setup(
    name='LabelSAC2NPZ',
    version='0.0.1',
    description='Produce stardard Earthquake waveform samplings',
    author='Hao Mai',
    author_email='hmai090@uottawa.ca',
    install_requires=['obspy'],
    python_requires='>=3.6',
    packages=['LabelSAC2NPZ'],
    scripts=scripts)
