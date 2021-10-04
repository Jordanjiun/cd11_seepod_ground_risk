import os
import xarray
import numpy as np
import bokeh as bk
import holoviews as hv
import geopandas as gpd
import rioxarray as rxr

from typing import NoReturn, Tuple
from shapely import geometry as sg
from holoviews.element import Geometry
from seedpod_ground_risk.layers.data_layer import DataLayer
from seedpod_ground_risk.data import census_2011_geotiff_filepath

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
HOURS_OF_DAY = range(24)

timestep_index = []
for day in DAYS_OF_WEEK:
    for hour in HOURS_OF_DAY:
        s = day + ' ' + '{:2d}:00'.format(hour)
        timestep_index.append(s)


class PopulationLayer(DataLayer):
    _population_count: xarray.DataArray()

    def __init__(self, key):
        super(PopulationLayer, self).__init__(key)
        self._time_idx = 0

    def preload_data(self) -> NoReturn:
        print("Preloading Population Count Layer")
        self._ingest_population_count()
        self._ingest_time()

    def generate(self, bounds_polygon: sg.Polygon, raster_shape: Tuple[int, int], from_cache: bool = False, **kwargs) \
            -> Tuple[Geometry, np.ndarray, gpd.GeoDataFrame]:
        import js2py
        from bokeh.plotting import show
        from bokeh.models import HoverTool

        population_gdf = self._population_count

        # create hv dataset from data array
        key_dimensions = ['x', 'y']
        value_dimension = ['default']
        hv_dataset_mercator = hv.Dataset(population_gdf[0], vdims=value_dimension, kdims=key_dimensions)

        # bokeh plot configurations
        hv.extension('bokeh', logo=False)
        image_height, image_width = 600, 700
        map_height, map_width = image_height, image_width
        clipping = {'NaN': (0, 0, 0, 0)}
        levels = [0, 10, 150, 450, 900, 2000]
        hex_opacity = '80'  # 50% opacity ('' for 100%, '80' for 50%, '66' for 40%)
        colours = ['#ffffff{}'.format(hex_opacity), '#fee9a6{}'.format(hex_opacity), '#f1a729{}'.format(hex_opacity),
                   '#af5428{}'.format(hex_opacity), '#6a0c0d{}'.format(hex_opacity)]
        hv.opts.defaults(
            hv.opts.Image(height=image_height, width=image_width,
                          colorbar=True, clabel='Population Count',
                          color_levels=levels, cmap=colours,
                          tools=['hover'], active_tools=['wheel_zoom'],
                          clipping_colors=clipping,
                          yformatter='%.0f',
                          xformatter='%.0f'),
            hv.opts.Tiles(active_tools=['wheel_zoom'], height=map_height, width=map_width)
        )

        # JavaScript code that re-formats coordinates (project from mercator to wgs84) for hv tooltip
        formatter_code = """
          var digits = 3;
          var projections = Bokeh.require("core/util/projections");
          var x = special_vars.x;
          var y = special_vars.y;
          var coord = projections.wgs84_mercator.invert(x, y);
          return "" + (Math.round(coord[%d] * 10**digits) / 10**digits).toFixed(digits)+ "";
        """

        formatter_code_x = formatter_code % 0
        formatter_code_y = formatter_code % 1

        custom_tooltips = [
            ('Longitude', '@x{custom}'),
            ('Latitude', '@y{custom}'),
            ('Population Count', '@image{0}')
        ]

        custom_formatters = {
            '@x': bk.models.CustomJSHover(code=formatter_code_x),
            '@y': bk.models.CustomJSHover(code=formatter_code_y)
        }

        # creates image with custom hover and OSM background map before combining them and rendering the overlay
        custom_hover = bk.models.HoverTool(tooltips=custom_tooltips, formatters=custom_formatters)
        hv_image_mercator = hv.Image(hv_dataset_mercator).opts(tools=[custom_hover])
        hv_tiles_osm = hv.element.tiles.OSM()
        hv_combined_mercator = hv_tiles_osm * hv_image_mercator
        show(hv.render(hv_combined_mercator.opts(title='Census Data 2011, Southampton (%s)' %
                                                       timestep_index[self._time_idx])
                       .redim.label(x='Longitude', y='Latitude')))
        return None

    def clear_cache(self) -> NoReturn:
        self._population_count = xarray.DataArray()

    def _ingest_population_count(self) -> NoReturn:
        # opens geotiff file as a data array and projects it to mercator with name 'default'
        filename = str(self._time_idx) + '.tif'
        geotiff = os.path.join(census_2011_geotiff_filepath(), filename)
        data_array_mercator = rxr.open_rasterio(geotiff).rio.reproject('EPSG:3857')
        data_array_mercator = data_array_mercator.where(data_array_mercator != data_array_mercator.rio.nodata)
        self._population_count = data_array_mercator.rename('default')

    def _ingest_time(self) -> NoReturn:
        pass
