import sys
from ._version import get_versions
__version__ = get_versions()['version']
sys.stderr.write(f"MATER({__version__})\n")
del get_versions
