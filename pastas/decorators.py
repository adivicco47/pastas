import functools
import logging

logger = logging.getLogger(__name__)


def set_parameter(function):
    @functools.wraps(function)
    def _set_parameter(self, name, value, **kwargs):
        if name not in self.parameters.index:
            logger.error('Parameter name %s does not exist, please choose '
                         'from %s' % (name, self.parameters.index))
        else:
            return function(self, name, value, **kwargs)

    return _set_parameter


def get_stressmodel(function):
    @functools.wraps(function)
    def _get_stressmodel(self, name, **kwargs):
        if name not in self.stressmodels.keys():
            logger.error('The stressmodel name you provided is not in the '
                         'stressmodels dict. Please select from the '
                         'following list: %s' % self.stressmodels.keys())
        else:
            return function(self, name, **kwargs)

    return _get_stressmodel


def stats_tmin_tmax(function):
    @functools.wraps(function)
    def _stats_tmin_tmax(self, tmin=None, tmax=None, *args, **kwargs):
        if tmin is None:
            tmin = self.ml.settings["tmin"]
        if tmax is None:
            tmax = self.ml.settings["tmax"]

        return function(self, tmin, tmax, *args, **kwargs)

    return _stats_tmin_tmax
