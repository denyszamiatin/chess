__author__ = 'BohdanPidopryhora'

"""
Initiation of chess desk 8x8
with 0's in every checkerboard
"""

def desk_initiation():
    desk = [x * 0 for x in xrange(8) for y in range(8)]
