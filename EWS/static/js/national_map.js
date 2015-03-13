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
				source: new ol.source.TileWMS({
					url: 'http://maps.virtualkenya.org/geoserver/wms',
					params: {layers: 'geonode:ke_wards_spi_2014_ond'},
					serverType: 'geoserver' })
			}),
			new ol.layer.Tile({
				title: '-County spi',
				source: new ol.source.TileWMS({
					url: 'http://maps.virtualkenya.org/geoserver/wms',
					params: {layers: 'geonode:ke_county_spi_2014_ond'},
					serverType: 'geoserver' })
			}),
			new ol.layer.Tile({
				title: '-Turkana Spi',
				source: new ol.source.TileWMS({
					url: 'http://maps.virtualkenya.org/geoserver/wms',
					params: {layers: 'geonode:turkana_spi_2014_ond'},
					serverType: 'geoserver' })
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
		var layerSwitcherNatMap = new ol.control.LayerSwitcher();
    	national_map.addControl(layerSwitcherNatMap);
})();