# coding=utf-8
"""

Inka Algorithmic Music
Creates fully arranged algorithmic instrumental music.
Copyright (C) 2019  Udo Wollschläger

This file contains all (possible) basic_scale related functions and definitions
A basic_scale defines the steps of a scale but not the first note or its interpretation as c, d, ...

example: the same basic_scale (7, 65) is used for c major, c minor, d major, ...)
         the actual first tone and its interpretation (c, d, ...)
         are defined in the SCALES_LIST structure of module menu_entries
         The SCALES_LIST is accessible through the web interface

"""


class BasicScale():
    """ BasicScale related functions and definitions
    """

    def __init__(self):
        """ Defines all possible basic_scales
            (cyclic permutations don't change the basic_scale)
        """

        self.all_basic_scales = [	 # starts with scales of length 3 and ends with length 12
            [
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # 0
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 1
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 2
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 3
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],  # 4
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # 5
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # 6
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],  # 7 major
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],  # 8 minor
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # 9
            ],  # end 3

            [
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],  # 0
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],  # 1
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],  # 2
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],  # 3
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],  # 4
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # 5
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],  # 6
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # 7
                [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],  # 8
                [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],  # 9
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # 10
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],  # 11
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],  # 12
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],  # 13
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],  # 14
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],  # 15
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],  # 16
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],  # 17
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],  # 18
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],  # 19
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],  # 20
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],  # 21
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],  # 22
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],  # 23
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],  # 24
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],  # 25
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],  # 26
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],  # 27
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],  # 28
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],  # 29
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],  # 30
            ],  # end 4

            [
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],  # 0
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],  # 1
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],  # 2
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],  # 3
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],  # 4
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],  # 5
                [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],  # 6
                [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],  # 7
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],  # 8
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],  # 9
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],  # 10
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],  # 11
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],  # 12
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],  # 13
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],  # 14
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],  # 15
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],  # 16
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],  # 17
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],  # 18
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],  # 19
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],  # 20
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],  # 21
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1],  # 22
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],  # 23
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],  # 24
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],  # 25
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],  # 26
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],  # 27
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],  # 28
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],  # 29
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],  # 30
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],  # 31
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],  # 32
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],  # 33
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1],  # 34
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],  # 35
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],  # 36
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],  # 37
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],  # 38 japanese pentatonic
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0],  # 39
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],  # 40
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # 41
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],  # 42
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],  # 43 chinese pentatonic from 0
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],  # 44
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],  # 45
                [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],  # 46
                [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],  # 47
                [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],  # 48
                [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],  # 49
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],  # 50
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],  # 51
                [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],  # 52
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],  # 53
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],  # 54
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],  # 55
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],  # 56
                [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],  # 57
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],  # 58 major pentatonic from 8, minor pentatonic from 5

            ],  # end 5

            [
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # 0
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],  # 1
                [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],  # 2
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],  # 3
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],  # 4
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],  # 5
                [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],  # 6
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],  # 7
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],  # 8
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],  # 9
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],  # 10
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],  # 11
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],  # 12
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],  # 13
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],  # 14
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],  # 15
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],  # 16
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],  # 17
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],  # 18
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],  # 19
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],  # 20
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],  # 21
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],  # 22
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],  # 23
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],  # 24
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],  # 25
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],  # 26
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],  # 27
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],  # 28
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],  # 29
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1],  # 30
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],  # 31
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],  # 32
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1],  # 33
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],  # 34
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],  # 35
                [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],  # 36
                [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1],  # 37
                [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],  # 38
                [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],  # 39
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],  # 40
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],  # 41
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],  # 42
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],  # 43
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0],  # 44
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],  # 45
                [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],  # 46
                [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],  # 47
                [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],  # 48
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],  # 49
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],  # 50
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],  # 51
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],  # 52
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],  # 53
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],  # 54
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],  # 55
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],  # 56
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],  # 57
                [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],  # 58
                [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],  # 59
                [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0],  # 60
                [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],  # 61
                [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],  # 62
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],  # 63 minor blues scale from 5
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],  # 64
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],  # 65
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],  # 66
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # 67
                [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],  # 68
                [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],  # 69
                [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],  # 70
                [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],  # 71
                [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],  # 72
                [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],  # 73
                [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],  # 74
                [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],  # 75
                [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0],  # 76
                [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],  # 77
                [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],  # 78
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # 79 whole tone scale

            ],  # end 6

            [
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],  # 0
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],  # 1
                [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],  # 2
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],  # 3
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],  # 4
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],  # 5
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],  # 6
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],  # 7
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],  # 8
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],  # 9
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1],  # 10
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],  # 11
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],  # 12
                [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],  # 13
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],  # 14
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],  # 15
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],  # 16
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0],  # 17
                [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],  # 18
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],  # 19
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],  # 20
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],  # 21
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],  # 22
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],  # 23
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],  # 24
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],  # 25
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],  # 26
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # 27
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],  # 28
                [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1],  # 29
                [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1],  # 30
                [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1],  # 31
                [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],  # 32
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],  # 33
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 34
                [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],  # 35
                [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],  # 36
                [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],  # 37
                [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1],  # 38
                [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],  # 39
                [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],  # 40
                [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],  # 41
                [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],  # 42
                [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],  # 43
                [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],  # 44
                [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],  # 45
                [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],  # 46
                [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1],  # 47
                [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],  # 48
                [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],  # 49
                [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],  # 50
                [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],  # 51
                [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],  # 52
                [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],  # 53
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],  # 54 byzantine from pos 11
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],  # 55 (harmonic minor from pos 4)
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],  # 56
                [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],  # 57
                [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],  # 58
                [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 59
                [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0],  # 60
                [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],  # 61
                [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],  # 62
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],  # 63 arabic scale from 6
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],  # 64 (melodic minor from 9)
                [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],  # 65 (major from 0, minor from 9, mixolydic)
            ],  # end 7

            [
                [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 0
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],  # 1
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],  # 2
                [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],  # 3
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],  # 4
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],  # 5
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],  # 6
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],  # 7
                [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],  # 8
                [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],  # 9
                [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],  # 10
                [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],  # 11
                [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],  # 12
                [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],  # 13
                [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],  # 14
                [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],  # 15
                [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],  # 16
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],  # 17
                [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],  # 18
                [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],  # 19
                [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],  # 20
                [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],  # 21
                [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],  # 22
                [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1],  # 23
                [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],  # 24
                [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],  # 25
                [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],  # 26
                [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],  # 27
                [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],  # 28
                [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],  # 29
                [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],  # 30
                [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0],  # 31
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],  # 32
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],  # 33
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],  # 34
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],  # 35
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],  # 36
                [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],  # 37
                [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],  # 38
                [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],  # 39
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],  # 40
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],  # 41
                [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],  # 42

            ],  # end 8

            [
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 0
                [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],  # 1
                [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],  # 2
                [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # 3
                [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 4
                [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],  # 5
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],  # 6
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],  # 7
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # 8
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],  # 9
                [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],  # 10
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],  # 11
                [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],  # 12
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],  # 13
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],  # 14
                [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],  # 15
                [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],  # 16
                [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],  # 17
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],  # 18
            ],  # end 9

            [
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
                [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],  # 2
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],  # 3
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # 4
                [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 5
            ],  # end 10

            [
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0
            ],  # end 11

            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0 (chromatic)
            ],  # end 12
        ]
#         for i in range(len(self.all_basic_scales)):
#             print(' ')
#             for j in range(len(self.all_basic_scales[i])):
#                 x = '['
#                 x += repr(self.all_basic_scales[i][j][11])+', '
#                 for t in range(10):
#                     x+= repr(self.all_basic_scales[i][j][t])+', '
#
#                 x +=  repr(self.all_basic_scales[i][j][10])+'],  # '+repr(j)
#                 print(x)

    def get_scale_by_index(self, len_indx, count_indx, pattern_starts_at, based_on_note):
        """returns basic_scale given by length and index
           all scales start at tone C unless shifted by based_on_note
           pattern_starts_at is the index where the scale pattern starts
           example: a C-major scale uses 7 65 with pattern_starts_at=0 and based_on_note Note_C
                    a A-minor scale uses 7 65 with pattern_starts_at=9 and based_on_note Note_A"""
        return [self.all_basic_scales[len_indx - 3]
                [count_indx][(i - based_on_note + pattern_starts_at) % 12] for i in range(12)]

    def get_all_basic_scales(self):
        """returns list of all basic_scales"""
        return self.all_basic_scales
