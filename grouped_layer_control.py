from jinja2 import Template
from branca.element import Figure
from folium.map import Layer, LayerControl, FeatureGroup

class GroupedLayerControl(Layer):
	_template = Template(u"""
			{% macro header(this, kwargs) %}
			<link rel="stylesheet" href="https://raw.githubusercontent.com/ismyrnow/leaflet-groupedlayercontrol/gh-pages/src/leaflet.groupedlayercontrol.css" />
			<script src="leaflet.groupedlayercontrol.js"></script> 
			{% endmacro %}
			{% macro script(this, kwargs) %}
			var baseMaps = { {%- for groupkey, group in this._basemaps.items() %}
							{{ groupkey|tojson }} : {		
										 {%- for key, val in group.items() %}
											{{ key|tojson }} : {{ val.get_name() }},
										{%- endfor %}
								}	,
							{%- endfor %}
			};
			var overlays = {
					 {%- for groupkey, group in this._overlays.items() %}
							
								 {{ groupkey|tojson }} : {		
										 {%- for key, val in group.items() %}
											{{ key|tojson }} : {{ val.get_name() }},
										{%- endfor %}
									}  ,
							{%- endfor %} };
			var options = {
				exclusiveGroups : [ {%- for i in this._radio %} "{{i}}", {%- endfor %} ],
				container_width 	: "300px",
				group_maxHeight     : "80px",
				exclusive       	: false,
				collapsed : true, 
				position: 'topright',
				show: false
			};
			
			L.control.groupedLayers(baseMaps, overlays, options).addTo({{ this._parent.get_name() }})
			
			document.getElementById('idname').click();
        {% endmacro %}
        """)
		
	def __init__(self, bmaps, olays, radio, name=None, overlay=True, control=True, show=True, options=None, **kwargs):
		super(GroupedLayerControl, self).__init__(name=name, overlay=overlay, control=control, show=show)
		self._basemaps = bmaps
		self._overlays = olays
		self._radio = radio
		self._name = 'GroupedLayerControl'
		