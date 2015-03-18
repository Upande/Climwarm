(function() {
	var national_map = new ol.Map({
		target:'nat_map',
		layers: [
			new ol.layer.Group({
				title: 'Base Maps',
				layers: [
				new ol.layer.Tile({
					title: 'OSM',
					visible: true,
					source: new ol.source.OSM()
					}),
				new ol.layer.Tile({
					title: 'Bing Maps',
					visible: false,
					source: new ol.source.BingMaps({
						key: 'Ak-dzM4wZjSqTlzveKz5u0d4IQ4bRzVI309GxmkgSVr1ewS6iPSrOvOKhA-CJlm3',
      					imagerySet: "AerialWithLabels"
									})
								})
				]
			}),
		new ol.layer.Group({
			title: 'Overlays',
			layers:[ new ol.layer.Tile({
				title: '-Wards spi',
				type: 'base',
				source: new ol.source.TileWMS({
					url: 'http://maps.virtualkenya.org/geoserver/wms',
					params: {layers: 'geonode:ke_wards_spi_2014_ond',
							format:'image/png'},
					serverType: 'geoserver' }),
				showLegend:true
			}),
			new ol.layer.Tile({
				title: '-County spi',
				type: 'base',
				source: new ol.source.TileWMS({
					url: 'http://maps.virtualkenya.org/geoserver/wms',
					params: {layers: 'geonode:ke_county_spi_2014_ond',
							 format:'image/png'},
					serverType: 'geoserver' }),
				showLegend:true
			}),
			new ol.layer.Tile({
				title: '-Turkana Spi',
				type: 'base',
				source: new ol.source.TileWMS({
					url: 'http://maps.virtualkenya.org/geoserver/wms',
					params: {layers: 'geonode:turkana_spi_2014_ond',
							 format:'image/png'},
					serverType: 'geoserver' }),
				showLegend:true
			})
			]
		})
		],
		view: new ol.View({
			projection: 'EPSG:3857',
			center:[4206847, 50232],
			zoom:6
		})
	});
		national_map.addControl(new ol3_legend({
            map: national_map,
            class: 'ol_legend' }));
		
		var layerSwitcherNatMap = new ol.control.LayerSwitcher();
    	national_map.addControl(layerSwitcherNatMap);
    	
})();