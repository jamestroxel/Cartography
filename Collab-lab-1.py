import config
import configparser
import pandas as pd #importing the Pandas Library as 'pd'
from keplergl_cli import Visualize #importing KeplerGl
from keplergl import KeplerGl
import geopandas as gpd #importing geopandas as 'gpd'

#add mapbox API key
MAPBOX_API_KEY = config.MAPBOX_API

df = pd.read_csv("data/olist_orders_geo.csv")
print(df.head())

map_1 = KeplerGl(height=600, width=800)
map_1.add_data(data=df, name='data_1')
map_1.data
print(df.head())

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.cust_lng, df.cust_lat))

viz = Visualize(gdf, api_key=MAPBOX_API_KEY)

viz.render(open_browser=True, read_only=False)

map_1.save_to_html(data={'data_1': df}, file_name='olist-order-geo.html')