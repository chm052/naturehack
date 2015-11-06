"""
GBIFOccurrencesLib

This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""

class LayersSpecimensEnum(object):

    """Implementation of the 'Layers_Specimens' enum.

    Specimen layers can take no year (&layer=SP_NO_YEAR), before the 1900s
    (&layer=SP_PRE_1900) or any decade after 1900.

    Attributes:
        SP_NO_YEAR: SP_NO_YEAR
        SP_PRE_1900: SP_PRE_1900
        SP_1900_1910: SP_1900_1910
        SP_1910_1920: SP_1910_1920
        SP_1920_1930: SP_1920_1930
        SP_1930_1940: SP_1930_1940
        SP_1940_1950: SP_1940_1950
        SP_1950_1960: SP_1950_1960
        SP_1960_1970: SP_1960_1970
        SP_1970_1980: SP_1970_1980
        SP_1980_1990: SP_1980_1990
        SP_1990_2000: SP_1990_2000
        SP_2000_2010: SP_2000_2010
        SP_2010_2020: SP_2010_2020

    """

    SP_NO_YEAR = "SP_NO_YEAR"

    SP_PRE_1900 = "SP_PRE_1900"

    SP_1900_1910 = "SP_1900_1910"

    SP_1910_1920 = "SP_1910_1920"

    SP_1920_1930 = "SP_1920_1930"

    SP_1930_1940 = "SP_1930_1940"

    SP_1940_1950 = "SP_1940_1950"

    SP_1950_1960 = "SP_1950_1960"

    SP_1960_1970 = "SP_1960_1970"

    SP_1970_1980 = "SP_1970_1980"

    SP_1980_1990 = "SP_1980_1990"

    SP_1990_2000 = "SP_1990_2000"

    SP_2000_2010 = "SP_2000_2010"

    SP_2010_2020 = "SP_2010_2020"


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