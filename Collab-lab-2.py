import config
import configparser
import pandas as pd #importing the Pandas Library as 'pd'
from keplergl_cli import Visualize #importing KeplerGl
from keplergl import KeplerGl
import geopandas as gpd #importing geopandas as 'gpd'

#add mapbox API key
MAPBOX_API_KEY = config.MAPBOX_API
#config variable
config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "xglu5p",
          "type": "arc",
          "config": {
            "dataId": "data_1",
            "label": "seller -> cust arc",
            "color": [
              87,
              173,
              87
            ],
            "columns": {
              "lat0": "seller_lat",
              "lng0": "seller_lng",
              "lat1": "cust_lat",
              "lng1": "cust_lng"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.03,
              "thickness": 0.5,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "sizeRange": [
                0,
                10
              ],
              "targetColor": [
                130,
                13,
                175
              ]
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "data_0": [
              {
                "name": "Unnamed: 0",
                "format": None
              },
              {
                "name": "order_id",
                "format": None
              },
              {
                "name": "customer_id",
                "format": None
              },
              {
                "name": "seller_id",
                "format": None
              },
              {
                "name": "seller_zip_code_prefix",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 2,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 24,
      "dragRotate": True,
      "latitude": -17.503299192988372,
      "longitude": -48.366689371615834,
      "pitch": 50,
      "zoom": 2.7948332577379404,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "muted_night",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": False,
        "road": False,
        "border": True,
        "building": False,
        "water": True,
        "land": False,
        "3d building": False
      },
      "threeDBuildingColor": [
        194.6103322548211,
        191.81688250953655,
        185.2988331038727
      ],
      "mapStyles": {
        "streets": {
          "accessToken": "pk.eyJ1IjoianVzdHN0YW4iLCJhIjoiY2tlc3hncWJ4MWh3cTJ4cXY5ZmsxdmoyYiJ9.LHycdQ3Il_MDxeW8JfiNWw",
          "custom": True,
          "icon": "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/-122.3391,37.7922,9,0,0/400x300?access_token=pk.eyJ1IjoianVzdHN0YW4iLCJhIjoiY2tlc3hncWJ4MWh3cTJ4cXY5ZmsxdmoyYiJ9.LHycdQ3Il_MDxeW8JfiNWw&logo=false&attribution=false",
          "id": "streets",
          "label": "Mapbox Streets",
          "url": "mapbox://styles/mapbox/streets-v11"
        },
        "outdoors": {
          "accessToken": "pk.eyJ1IjoianVzdHN0YW4iLCJhIjoiY2tlc3hncWJ4MWh3cTJ4cXY5ZmsxdmoyYiJ9.LHycdQ3Il_MDxeW8JfiNWw",
          "custom": True,
          "icon": "https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/static/-122.3391,37.7922,9,0,0/400x300?access_token=pk.eyJ1IjoianVzdHN0YW4iLCJhIjoiY2tlc3hncWJ4MWh3cTJ4cXY5ZmsxdmoyYiJ9.LHycdQ3Il_MDxeW8JfiNWw&logo=false&attribution=false",
          "id": "outdoors",
          "label": "Mapbox Outdoors",
          "url": "mapbox://styles/mapbox/outdoors-v11"
        },
        "satellite-streets": {
          "accessToken": "pk.eyJ1IjoianVzdHN0YW4iLCJhIjoiY2tlc3hncWJ4MWh3cTJ4cXY5ZmsxdmoyYiJ9.LHycdQ3Il_MDxeW8JfiNWw",
          "custom": True,
          "icon": "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/static/-122.3391,37.7922,9,0,0/400x300?access_token=pk.eyJ1IjoianVzdHN0YW4iLCJhIjoiY2tlc3hncWJ4MWh3cTJ4cXY5ZmsxdmoyYiJ9.LHycdQ3Il_MDxeW8JfiNWw&logo=false&attribution=false",
          "id": "satellite-streets",
          "label": "Mapbox Satellite Streets",
          "url": "mapbox://styles/mapbox/satellite-streets-v11"
        }
      }
    }
  }
}

df = pd.read_csv("data/olist_orders_geo.csv")


map_1 = KeplerGl(height=600, width=800, data={"data_1": df}, config=config)
map_1.add_data(data=df, name='data_1')
map_1.data
print(df.head())

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.cust_lng, df.cust_lat))

viz = Visualize(gdf, api_key=MAPBOX_API_KEY)

viz.render(open_browser=True, read_only=False)

map_1.save_to_html(data={'data_1': df}, config=config, file_name='olist-order-geo-config.html')