import duckdb
import numpy as np
from tqdm import tqdm

duckdb.sql('INSTALL httpfs')
duckdb.sql('LOAD httpfs')
duckdb.sql("FORCE INSTALL spatial FROM 'http://nightly-extensions.duckdb.org';")
duckdb.sql('LOAD spatial')

prefix = "s3://us-west-2.opendata.source.coop/vida/google-microsoft-open-buildings/geoparquet"
partitions = "by_country"
country_iso = "BTN"

output_file = 'buildings_BHUTAN.geojson'
duckdb.sql(f"COPY (SELECT ST_Centroid(ST_GeomFromWKB(geometry)) AS centroid, area_in_meters FROM parquet_scan('{prefix}/{partitions}/country_iso={country_iso}/{country_iso}.parquet')) TO '{output_file}' WITH  (FORMAT GDAL, DRIVER 'GeoJSON');")