"""
GBIFOccurrencesLib

This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""

class ContinentEnum(object):

    """Implementation of the 'Continent' enum.

    Enumeration for all continents based on the 7 number model found on
    Wikipedia. In particular this splits the Americas into North and South
    America with North America including the Caribbean and reaching down and
    including Panama. See the Wikipedia continent map for the exact
    divisions.

    Attributes:
        AFRICA: AFRICA
        ANTARCTICA: ANTARCTICA
        ASIA: ASIA
        OCEANIA: OCEANIA
        EUROPE: EUROPE
        NORTH_AMERICA: North America includes the Caribbean and reaches down
            and includes Panama.
        SOUTH_AMERICA: SOUTH_AMERICA

    """

    AFRICA = "AFRICA"

    ANTARCTICA = "ANTARCTICA"

    ASIA = "ASIA"

    OCEANIA = "OCEANIA"

    EUROPE = "EUROPE"

    NORTH_AMERICA = "NORTH_AMERICA"

    SOUTH_AMERICA = "SOUTH_AMERICA"


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