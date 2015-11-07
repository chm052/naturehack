"""
GBIFOccurrencesLib

This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""

class LayersFossilEnum(object):

    """Implementation of the 'Layers_Fossil' enum.

    If provided, the records with a declared basis of record of fossil will be
    included. 

    Attributes:
        FOSSIL: FOSSIL

    """

    FOSSIL = "FOSSIL"


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