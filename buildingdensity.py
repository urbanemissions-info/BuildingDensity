import geopandas as gpd
import pandas as pd

buildings = gpd.read_file('buildings_BHUTAN.geojson')

grids = gpd.read_file('grids_thimphu\grids_thimphu.shp')

buildings_grids = gpd.sjoin(buildings, grids, predicate='within')
grouped = buildings_grids.groupby('Maille').agg(buildings_count = ('geometry','count'),
                                 buildings_area = ('area_in_meters','sum'))
bd = grids.merge(grouped.reset_index(), on='Maille', how='left')[['Maille','buildings_count','buildings_area','geometry']]
#bd = bd.fillna(0) #To fill NULLS with zeros
bd.to_file('BuildingDensity_Thimphu.geojson')