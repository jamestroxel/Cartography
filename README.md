https://jamestroxel.github.io/Cartography/

# Step 1
Create your Mapbox account and API token. Drop your token in the ```MAPBOX_API = ""``` variable in your config.py file. 

# Step 2
Follow the instructions up to step 5 here: https://medium.com/faun/the-right-way-to-set-up-python-on-your-mac-e923ffe8cf8e. Installing other packages is fine but not necessary for this exercise.


# Step 3
get started with plotting a map in your python script.

Start by importing the necessary Kepler, config parsing and geo location (geopandas) packages:
```import config```
```import configparser```
```import pandas as pd #importing the Pandas Library as 'pd'```
```from keplergl_cli import Visualize #importing KeplerGl```
```from keplergl import KeplerGl```
```import geopandas as gpd #importing geopandas as 'gpd'```


Add mapbox API key
```MAPBOX_API_KEY = config.MAPBOX_API```

Read in your csv geolocation data
```df = pd.read_csv("data/olist_orders_geo.csv")```
```print(df.head())```

This part creates an instance of a Kepler map and adds your data
```map_1 = KeplerGl(height=600, width=800)```
```map_1.add_data(data=df, name='data_1')```
```map_1.data```
```print(df.head())```

Here's where you plot the geolocation dataframes in a variable
```gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.cust_lng, df.cust_lat))```

This renders the initial map with your data and will prompt a new browser window to display your map
```viz = Visualize(gdf, api_key=MAPBOX_API_KEY)```
```viz.render(open_browser=True, read_only=False)```

This exports your map as an html file to include in a webpage
```map_1.save_to_html(data={'data_1': df}, file_name='olist-order-geo.html')```

in your terminal, type ```python3 yourfilename.py``` , hit enter and wait until the map appears in your browser. Ignore the html file for now.

# Step 4
Start configuring your map styles. Using the map that the previous script has opened in your browser, begin to add/remove layers, select series types and expolore the other customizations at hand to enhance your map and render the data to your liking. 

Once you have arrived at a finished state, locate the small "{}" config icon at the end of the layers and filtering options in your kepler toolbar. Copy the entire config script and paste it into a variable called "config" in your python script (see Collab-lab-2.py). This conifig now needs to be referenced in your map instance and html export as well  ```map_1.save_to_html(data={'data_1': df}, config=config, file_name='olist-order-geo-config.html')```

Now, run your python script again and check the html file that is generated (rather than what automatically prompts in your browser) to see your finished map that may be shared as-is or incorporated into an html page as you see fit.
