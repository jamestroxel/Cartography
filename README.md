
![olist_header](/images/olist_sales_header.PNG)

Live Site: https://jamestroxel.github.io/Cartography/

# Overview
This repository maps a dataset of 100k order shipments from the Brazilian department store Olist by visualizing coordinate arcs between seller and buyer zip codes.

# Dataset
The [original dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_orders_dataset.csv) includes multiple csv's that represent a relational database schema. This schema is visualized below and provided as a combined file with geolocation information of sellers and buyers [within the repository](https://github.com/jamestroxel/Cartography/blob/master/data/olist_orders_geo.csv). The python script to combine this through a chain series of pandas merge commands is saved as [olist_data_merge.py](olist_data_merge.py).

![olist_schema](/images/olist_data.png)

# Visualize

## Prerequisites

### Step 1 - Obtain Mapbox API
Create your Mapbox account and API token at https://account.mapbox.com/. Drop your token in the ```MAPBOX_API = ""``` variable in the config.py file.

### Step 2 - Install Necessary Python Libraries
Set up your python 3 environment with homebrew and pip, follow [these instructions](https://medium.com/faun/the-right-way-to-set-up-python-on-your-mac-e923ffe8cf8e) up to step 5. Installing other packages is fine but not necessary for this exercise.

Using Kepler GL with command line Python requires the following libraries. It's important that these are installed in this sequence to avoid dependency errors: 
```python
# Install Pandas
pip install pandas
```
```python
# Geopandas
pip install shapely
brew install gdal #(assuming homebrew installed python 3)
#write this within terminal:
GDAL_CONFIG=/path/to/gdal-config pip3 install fiona
#continue installing with pip and homebrew
pip install pyproj
brew install spatialindex
pip install Rtree
pip install geopandas 
```

```python
# Kepler GL
pip3 install geojson
pip3 install keplergl_cli
```

## Load Data and Open in Kepler
Load the data into Kepler GL and display as an html page by executing ```python Collab-lab-1.py``` for the unstylized version or ```python Collab-lab-2.py``` for the stylized version using the config file. A breakdown of the python scripts are below:

Start by importing the necessary Python libraries:
```python 
import config
import configparser
import pandas as pd #importing the Pandas Library as 'pd'
from keplergl_cli import Visualize #importing KeplerGl
from keplergl import KeplerGl
import geopandas as gpd #importing geopandas as 'gpd'
```

Add mapbox API key and read csv geolocation data:
```python 
MAPBOX_API_KEY = config.MAPBOX_API
df = pd.read_csv("data/olist_orders_geo.csv")
print(df.head()) 
```

Create a Kepler map and add data:
```python 
map_1 = KeplerGl(height=600, width=800, data={"data_1": df}, config=config)
map_1.add_data(data=df, name='data_1')
map_1.data
print(df.head())
```

Input latitude and longitude to create a geolocation point object using geopandas:
```python
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.cust_lng, df.cust_lat))
```

This renders the initial map with your data and will prompt a new browser window to display your map
```python 
viz = Visualize(gdf, api_key=MAPBOX_API_KEY
viz.render(open_browser=True, read_only=False)
```

This exports your map as an html file to include in a webpage:
```python
map_1.save_to_html(data={'data_1': df}, file_name='olist-order-geo.html')
```

## Stylize Map
Once the Kepler GL map instance has opened, configure your map styles. Using the map that the previous script has opened in your browser, begin to add/remove layers, select series types and expolore the other customizations at hand to enhance your map and render the data to your liking. 

Once you have arrived at a finished state, locate the small "{}" config icon at the end of the layers and filtering options in your kepler toolbar. Copy the entire config script and paste it into a variable called "config" in your python script (see Collab-lab-2.py). This conifig now needs to be referenced in your map instance and html export:
```python 
 map_1.save_to_html(data={'data_1': df}, config=config, file_name='olist-order-geo-config.html')
```

Now, run your python script again and check the html file that is generated (rather than what automatically prompts in your browser) to see your finished map that may be shared as-is or incorporated into an html page as you see fit.
