from typing import NoReturn, Tuple

import numpy as np
import bokeh as bk
import holoviews as hv
import geopandas as gpd
import rioxarray as rxr

from bokeh.plotting import show
from bokeh.models import HoverTool
from shapely import geometry as sg
from holoviews.element import Geometry
from seedpod_ground_risk.data import geotiff_test_filepath
from seedpod_ground_risk.layers.data_layer import DataLayer

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
HOURS_OF_DAY = range(24)


def generate_week_timesteps():
    timestep_index = []
    for day in DAYS_OF_WEEK:
        for hour in HOURS_OF_DAY:
            s = day + ' ' + '{:2d}:00'.format(hour)
            timestep_index.append(s)
    return timestep_index


class PopulationLayer(DataLayer):
    _population_count: gpd.GeoDataFrame

    def __init__(self, key):
        super(PopulationLayer, self).__init__(key)
        self.week_timesteps = generate_week_timesteps()

    def preload_data(self) -> NoReturn:
        print("Preloading Population Count Layer")
        self._ingest_population_count()

    def generate(self, bounds_polygon: sg.Polygon, raster_shape: Tuple[int, int], from_cache: bool = False, **kwargs) -> \
            Tuple[Geometry, np.ndarray, gpd.GeoDataFrame]:
        pass

    def clear_cache(self) -> NoReturn:
        self._population_count = gpd.GeoDataFrame()

    def _ingest_population_count(self) -> NoReturn:
        data_array_mercator = rxr.open_rasterio(geotiff_test_filepath()).rio.reproject('EPSG:3857')
        self._population_count = data_array_mercator
