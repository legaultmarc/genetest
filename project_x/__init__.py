
# This file is part of project_x.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to Creative
# Commons, PO Box 1866, Mountain View, CA 94042, USA.


try:
    from .version import genipe_version as __version__
except ImportError:
    __version__ = None


__copyright__ = "Copyright 2016, Beaulieu-Saucier Pharmacogenomics Centre"
__credits__ = ["Louis-Philippe Lemieux Perreault", "Marc-Andre Legault"]
__license__ = "CC BY-NC 4.0"
__status__ = "Development"
