"""
AtlasOfLivingAustraliaOccurrencesLib

This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""

class OccurrenceDownloadReasonTypeIdTypeEnum(object):

    """Implementation of the 'Occurrence_download_reasonTypeId_type' enum.

    A reason code for the download

    Attributes:
        RKEY: rkey
        NAME: name
        ID: id

    """

    RKEY = "rkey"

    NAME = "name"

    ID = "id"


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