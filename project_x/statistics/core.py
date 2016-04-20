"""
"""


# This file is part of project_x.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to Creative
# Commons, PO Box 1866, Mountain View, CA 94042, USA.


import numpy as np


__copyright__ = "Copyright 2016, Beaulieu-Saucier Pharmacogenomics Centre"
__license__ = "Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)"


__all__ = ["StatsModels", "StatsResults", "StatsError"]


class StatsModels(object):
    def fit(self, y, X, result_col):
        """Fit the model.

        Args:
            y (pandas.DataFrame): The vector of endogenous variable.
            X (pandas.DataFrame): The matrix of exogenous variables.
            result_col (str): The variable for which the results are required.

        """
        raise NotImplementedError()


class StatsResults(object):
    def __init__(self, **kwargs):
        # '_index_of' has all the possible statistics
        self.__dict__["_index_of"] = {
            name: i for i, name in enumerate(kwargs.keys())
        }

        # Saving the description of each column
        self._description = kwargs

        # Creating the array that will contain the values
        self._results = np.full(len(self._index_of), np.nan, dtype=float)

    def __getattr__(self, name):
        if name in self._index_of:
            return self._results[self._index_of[name]]
        raise ValueError("{}: unknown statistic".format(name))

    def __setattr__(self, name, value):
        if name in self._index_of:
            self._results[self._index_of[name]] = value
        else:
            super().__setattr__(name, value)

    def reset(self):
        """Resets the statistics (sets all the values to NaN)."""
        self._results[:] = np.nan


class StatsError(Exception):
    """An Exception raised if there is any statistical problem."""
    def __init__(self, msg):
        self.message = str(msg)

    def __str__(self):
        return self.message
