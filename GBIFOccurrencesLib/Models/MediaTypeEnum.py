"""
GBIFOccurrencesLib

This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""

class MediaTypeEnum(object):

    """Implementation of the 'MediaType' enum.

    Based on the DC types vocabulary.

    Attributes:
        STILLIMAGE: StillImage
        MOVINGIMAGE: MovingImage
        SOUND: Sound

    """

    STILLIMAGE = "StillImage"

    MOVINGIMAGE = "MovingImage"

    SOUND = "Sound"


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