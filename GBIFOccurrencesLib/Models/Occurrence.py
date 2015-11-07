"""
   GBIFOccurrencesLib.Models.Occurrence
 
   This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""
from GBIFOccurrencesLib.APIHelper import APIHelper

class Occurrence(object):

    """Implementation of the 'Occurrence' model.

    This API works against the GBIF Occurrence Store, which handles occurrence
    records and makes them available through the web service and download
    files. In addition we also provide a Map API that offers spatial services.
    
    Attributes:
        key (int): key
        datasetkey (string): datasetkey
        publishing_org_key (string): publishingOrgKey
        publishing_country (string): publishingCountry
        protocol (string): protocol
        last_crawled (DateTime): lastCrawled
        basis_of_record (string): basisOfRecord
        decimal_longitude (double): decimalLongitude
        decimal_latitude (double): decimalLatitude
        continent (string): continent
        year (int): year
        month (int): month
        day (int): day
        event_date (DateTime): eventDate
        issues (list of string): issues
        last_interpreted (DateTime): lastInterpreted
        identifiers (list of string): identifiers
        facts (list of string): facts
        relations (list of string): relations
        geodetic_datum (string): geodeticDatum
        country_code (string): countryCode
        country (string): country
        gbif_id (int): gbifID
        institution_code (string): institutionCode
        catalog_number (int): catalogNumber
        recorded_by (string): recordedBy
        locality (string): locality
        collection_code (int): collectionCode
        identified_by (string): identifiedBy

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Occurrence class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    key -- int -- Sets the attribute key
                    datasetkey -- string -- Sets the attribute datasetkey
                    publishingOrgKey -- string -- Sets the attribute publishing_org_key
                    publishingCountry -- string -- Sets the attribute publishing_country
                    protocol -- string -- Sets the attribute protocol
                    lastCrawled -- DateTime -- Sets the attribute last_crawled
                    basisOfRecord -- string -- Sets the attribute basis_of_record
                    decimalLongitude -- double -- Sets the attribute decimal_longitude
                    decimalLatitude -- double -- Sets the attribute decimal_latitude
                    continent -- string -- Sets the attribute continent
                    year -- int -- Sets the attribute year
                    month -- int -- Sets the attribute month
                    day -- int -- Sets the attribute day
                    eventDate -- DateTime -- Sets the attribute event_date
                    issues -- list of string -- Sets the attribute issues
                    lastInterpreted -- DateTime -- Sets the attribute last_interpreted
                    identifiers -- list of string -- Sets the attribute identifiers
                    facts -- list of string -- Sets the attribute facts
                    relations -- list of string -- Sets the attribute relations
                    geodeticDatum -- string -- Sets the attribute geodetic_datum
                    countryCode -- string -- Sets the attribute country_code
                    country -- string -- Sets the attribute country
                    gbifID -- int -- Sets the attribute gbif_id
                    institutionCode -- string -- Sets the attribute institution_code
                    catalogNumber -- int -- Sets the attribute catalog_number
                    recordedBy -- string -- Sets the attribute recorded_by
                    locality -- string -- Sets the attribute locality
                    collectionCode -- int -- Sets the attribute collection_code
                    identifiedBy -- string -- Sets the attribute identified_by
        
        """
        # Set all of the parameters to their default values
        self.key = None
        self.datasetkey = None
        self.publishing_org_key = None
        self.publishing_country = None
        self.protocol = None
        self.last_crawled = None
        self.basis_of_record = None
        self.decimal_longitude = None
        self.decimal_latitude = None
        self.continent = None
        self.year = None
        self.month = None
        self.day = None
        self.event_date = None
        self.issues = None
        self.last_interpreted = None
        self.identifiers = None
        self.facts = None
        self.relations = None
        self.geodetic_datum = None
        self.country_code = None
        self.country = None
        self.gbif_id = None
        self.institution_code = None
        self.catalog_number = None
        self.recorded_by = None
        self.locality = None
        self.collection_code = None
        self.identified_by = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "key": "key",
            "datasetkey": "datasetkey",
            "publishingOrgKey": "publishing_org_key",
            "publishingCountry": "publishing_country",
            "protocol": "protocol",
            "lastCrawled": "last_crawled",
            "basisOfRecord": "basis_of_record",
            "decimalLongitude": "decimal_longitude",
            "decimalLatitude": "decimal_latitude",
            "continent": "continent",
            "year": "year",
            "month": "month",
            "day": "day",
            "eventDate": "event_date",
            "issues": "issues",
            "lastInterpreted": "last_interpreted",
            "identifiers": "identifiers",
            "facts": "facts",
            "relations": "relations",
            "geodeticDatum": "geodetic_datum",
            "countryCode": "country_code",
            "country": "country",
            "gbifID": "gbif_id",
            "institutionCode": "institution_code",
            "catalogNumber": "catalog_number",
            "recordedBy": "recorded_by",
            "locality": "locality",
            "collectionCode": "collection_code",
            "identifiedBy": "identified_by",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "key": "key",
            "datasetkey": "datasetkey",
            "publishing_org_key": "publishingOrgKey",
            "publishing_country": "publishingCountry",
            "protocol": "protocol",
            "last_crawled": "lastCrawled",
            "basis_of_record": "basisOfRecord",
            "decimal_longitude": "decimalLongitude",
            "decimal_latitude": "decimalLatitude",
            "continent": "continent",
            "year": "year",
            "month": "month",
            "day": "day",
            "event_date": "eventDate",
            "issues": "issues",
            "last_interpreted": "lastInterpreted",
            "identifiers": "identifiers",
            "facts": "facts",
            "relations": "relations",
            "geodetic_datum": "geodeticDatum",
            "country_code": "countryCode",
            "country": "country",
            "gbif_id": "gbifID",
            "institution_code": "institutionCode",
            "catalog_number": "catalogNumber",
            "recorded_by": "recordedBy",
            "locality": "locality",
            "collection_code": "collectionCode",
            "identified_by": "identifiedBy",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)