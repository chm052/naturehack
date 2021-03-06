"""
   GBIFOccurrencesLib.Controllers.MappingController

   This file was automatically generated by APIMATIC BETA v2.0 on 10/29/2015
"""
import unirest

from GBIFOccurrencesLib.APIHelper import APIHelper
from GBIFOccurrencesLib.Configuration import Configuration
from GBIFOccurrencesLib.APIException import APIException


class MappingController(object):


    """A Controller to access Endpoints in the GBIFOccurrencesLib API."""

    def __init__(self,
                 user,
                 password):
        """
        Constructor with authentication and configuration parameters
        """
        self.__user = user
        self.__password = password

    def get_map_tile(self,
                     options=dict()):
        """Does a GET request to /map/density/tile.

        The mapping api is a web map tile service making it trivial to
        visualize GBIF content on interactive maps, and overlay content from
        other sources.  Developers familiar with tile mapping services should
        jump straight to the preview functionality  The following features are
        supported:      Map layers available for a country, dataset, taxon
        (species, subspecies or higher taxon), publisher     User defined
        styling by selecting a predefined color palette, or by providing
        styling rules     Density of content is clustered to a user defined
        cluster size (regardless of zoom level)     The ability to customise
        content shown by the basis of record (E.g. Specimens, Observations,
        Fossils etc)     For certain basis of record types, the time period
        may be customised by decade; e.g. map the observations of a species
        since 1970  This service is intended for use with commonly used
        clients such as the google maps api, leaflet JS library or the modest
        maps JS library. These libraries allow the GBIF layers to be
        visualized with other content, such as those coming from web map
        service (WMS) providers. It should be noted that the mapping api is
        not a WMS service, nor does it support WFS capabilities. The examples
        on this page use the leaflet library.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    key -- string -- The appropriate key for the chosen type
                        (a taxon key, dataset/publisher uuid or 2 letter ISO
                        country code)
                    mtype -- string -- A value of TAXON, DATASET, COUNTRY or
                        PUBLISHER
                    x -- string -- TODO: type description here. Example: 1
                    y -- string -- TODO: type description here. Example: 1
                    z -- string -- TODO: type description here. Example: 1
                    colors -- string -- Provides a user defined set of rules
                        for coloring the layer. See styling a layer
                    hue -- double -- Allows selection of a hue value between
                        0.0 and 1.0 when saturation is set to true. See
                        styling a layer
                    layer -- list of string -- (multivalued) Declares the
                        layers to be combined by the server for this tile. See
                        Customizing layer content
                    palette -- PaletteEnum -- Selects a predefined color
                        palette. See styling a layer
                    resolution -- int -- The number of pixels to which density
                        is aggregated. Valid values are 1, 2, 4, 8, and 16.
                    saturation -- bool -- Allows selection of a hue value
                        between 0.0 and 1.0 when saturation is set to true.
                        See styling a layer

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/map/density/tile"

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "key": options.get('key', None),
            "type": options.get('mtype', None),
            "x": options.get('x', None),
            "y": options.get('y', None),
            "z": options.get('z', None),
            "colors": options.get('colors', None),
            "hue":  options.get('hue', None) if options.get('hue', None) is not None else 1.0,
            "layer": options.get('layer', None),
            "palette":  options.get('palette', None).to_string() if options.get('palette', None) is not None else None,
            "resolution":  options.get('resolution', None) if options.get('resolution', None) is not None else 8,
            "saturation":  options.get('saturation', None) if options.get('saturation', None) is not None else True
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body
