# Folium-GroupedLayerControl

A layer control for folium based on leaflet-groupedlayercontrol by @ismyrnow. (https://github.com/ismyrnow/leaflet-groupedlayercontrol)

## Example

After importing the required library, folium, and function GroupedLayerControl from grouped_layer_control.py, 

```
m = folium.Map(location = [29,73], zoom_start = 4)

fg1 = folium.map.FeatureGroup(name='Group 1', show = True)
folium.Marker([25.3548,51.1839], tooltip="Qatar").add_to(fg1)
fg1.add_to(m)

fg2 = folium.map.FeatureGroup(name='Group 2', show = True)
folium.Marker([20.5937,78.9629], tooltip="India").add_to(fg2)
fg2.add_to(m)

fg3 = folium.map.FeatureGroup(name='Group 3', show = True)
folium.Marker([35.8617,104.1954], tooltip="China").add_to(fg3)
fg3.add_to(m)
```

```

GroupedLayerControl({}, {'Category 1' : {'India' : fg2 , 'China' : fg3},
                         'Category 2': {"Qatar" : fg1}
                        }, ['Category 1']).add_to(m)
                        
```

Find this code in demo.ipynb and the resultant map in demo.html

As demonstrated in the example above, specify the separate categories with their feature groups as nested dictionaries. Include the categories that need to be in the form of radio buttons as a list to parameter 3. 
