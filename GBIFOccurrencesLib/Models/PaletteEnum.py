"""
GBIFOccurrencesLib

This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""

class PaletteEnum(object):

    """Implementation of the 'Palette' enum.

    Colour palette used in the Mapping API

    Attributes:
        YELLOWS_REDS: yellows_reds
        BLUES: blues
        GREENS: greens
        GREYS: greys
        ORANGES: oranges
        PURPLES: purples
        REDS: reds

    """

    YELLOWS_REDS = "yellows_reds"

    BLUES = "blues"

    GREENS = "greens"

    GREYS = "greys"

    ORANGES = "oranges"

    PURPLES = "purples"

    REDS = "reds"


    @classmethod
    def to_string(cls, val):
        """Returns the string equivalent for the Enum.

        """
        for k,v in vars(cls).iteritems():
            if v==val:
                return k

    @classmethod
    def from_string(cls, str):
        """Creates an instance of the Enum from a given string.

        """
        return getattr(cls, str.upper(), None)