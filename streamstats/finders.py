# -*- coding: utf-8 -*-
import requests
import streamstats


class WatershedFinder(object):
    """A watershed finder for spatial points.

    Find the watershed that contains a point in the United States.
    """
    def __init__(self):
        self.baseurl = "".join([streamstats.base_url, "watershed.geojson"])

    def query(self, state, lon, lat):
        """Query a spatial point, finding its watershed.

        Find the polygon of the watershed containing a spatial point.

        :param state: Two character state code, e.g. "CA" for California.
        :type state: string
        :param lon: Longitude of point in decimal degrees.
        :type lon: float
        :param lat: Latitude of point in decimal degrees.
        :type lat: float
        :rtype: dict containing watershed data
        """
        payload = {
            'rcode': state,
            'xlocation': lon,
            'ylocation': lat,
            'crs': 4326,
            'includeparameters': True,
            'includeflowtypes': False,
            'includefeatures': True,
            'simplify': False
        }
        r = requests.get(self.baseurl, params=payload)
        r.raise_for_status()  # raises errors early
        return r.json()
