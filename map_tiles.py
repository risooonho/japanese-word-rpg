#! /usr/bin/env python

from classes import LocationType
from collections import OrderedDict

location_types = OrderedDict([('grass', LocationType(name='grass',
                                                     block_mv=False,
                                                     block_fov=False,
                                                     level=0,
                                                     )),
                              ('city', LocationType(name='city',
                                                    block_mv=False,
                                                    block_fov=False,
                                                    level=-1)),
                              ('mountain', LocationType(name='mountain',
                                                        block_mv=True,
                                                        block_fov=False,
                                                        level=1))])
