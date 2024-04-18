__author__ = 'CSU-OSS-RLTea'
from tqdm import tqdm
from datetime import datetime
from pytz import timezone

from ProgressBar.colour_maker import ColourMaker


class ProgressBar(tqdm):
    def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None,
                 ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
                 ascii=None, disable=False, unit='it', unit_scale=False,
                 dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                 position=None, postfix=None, unit_divisor=1000, write_bytes=False,
                 lock_args=None, nrows=None, colour=None, delay=0, gui=False, prefix=None, metric=None,
                 **kwargs):
        """Get time"""
        now = datetime.utcnow().astimezone(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')

        _tq = None

        """Generate random colour if required"""
        if colour == 'random':
            colour = ColourMaker().get_random_colour_hex()

        """Set the dynamic ncols if ncols is not specified"""
        if ncols is None:
            dynamic_ncols = True

        """Construct the tqdm object"""
        super().__init__(iterable=iterable, desc=desc, total=total, leave=leave, file=file,
                         ncols=ncols, mininterval=mininterval, maxinterval=maxinterval, miniters=miniters,
                         ascii=ascii, disable=disable, unit=unit, unit_scale=unit_scale,
                         dynamic_ncols=dynamic_ncols, smoothing=smoothing, bar_format=bar_format, initial=initial,
                         position=position, postfix=postfix, unit_divisor=unit_divisor, write_bytes=write_bytes,
                         lock_args=lock_args, nrows=nrows, colour=colour, delay=delay, gui=gui,
                         **kwargs)

        """Set prefix"""
        if prefix is not None:
            super().set_description_str(prefix)

        """Set metric"""
        if isinstance(metric, dict):
            metric["start"] = now
            super().set_postfix(metric)
        else:
            super().set_postfix_str("{}".format(now))
