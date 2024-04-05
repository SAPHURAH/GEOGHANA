import geopandas as gpd

global filepath = './geofiles'

class Geospatial:
    """Class for loading geo files"""

    def load_shape_files(filepath):
        """Load a Shapefile and return a GeoDataFrame."""
        ...

    def load_topojson(filepath):
        """Load a TopoJSON file and return a GeoDataFrame."""
        ...
