__author__ = 'CSU-OSS-RLTea'

from tqdm import tqdm
import random
from pytz import timezone
from datetime import datetime
from ProgressBar import *


def process(iterable, prefix=None, ncols=None, unit="it", metric=None, colour=None):
    now = datetime.utcnow().astimezone(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')

    _tq = None

    """colour"""
    if colour is None:
        colour = ColourMaker().get_random_colour_hex()

    """ncols and generate tqdm object"""
    if ncols is not None:
        _tq = tqdm(iterable, colour=colour, unit=unit, ncols=ncols)
    else:
        _tq = tqdm(iterable, colour=colour, unit=unit, dynamic_ncols=True)

    """set prefix"""
    if prefix is not None:
        _tq.set_description(prefix)

    """set metric"""
    if isinstance(metric, dict):
        metric["start"] = now
        _tq.set_postfix(metric)
    else:
        _tq.set_postfix_str("{}".format(now))
    return _tq


if __name__ == '__main__':
    """sample"""
    print("This is the first sample:")
    for e in range(3):
        _t = ProgressBar(range(5000), prefix="epoch {}".format(e + 1), colour='random')
        for i in _t:
            for j in range(100):
                for k in range(100):
                    pass

    print("This is the second sample:")
    for e in range(3):
        m = {
            "acc": random.random(),
            "loss": random.random()
        }
        _t = ProgressBar(range(5000), ncols=160, prefix="epoch {} / {}".format(e + 1, 3), metric=m)
        for i in _t:
            for j in range(100):
                for k in range(100):
                    pass

    print("This is the third sample:")
    # colour_maker = ColourMaker(15, [180, 220, 250], [30, 120, 150])
    colour_maker = ColourMaker(10)
    for e in range(30):
        m = {
            "loss": random.random()
        }
        _t = ProgressBar(iterable=range(500), ncols=160, prefix="epoch {} / {}".format(e + 1, 30), metric=m,
                         colour=colour_maker.get_colour())
        for i in _t:
            for j in range(100):
                for k in range(50):
                    pass
