function fourthmap() {

	var fourth_map = new ol.Map({
        target:'map_4',
        layers: [new ol.layer.Group({
            title: 'Base Maps',
            layers: [
            new ol.layer.Tile({
                title: 'OSM',
                type: 'base',
                visible: true,
                source: new ol.source.OSM()
                    })
                ]
            }),
            new ol.layer.Group({
                title: 'Overlays',
                layers:[ new ol.layer.Tile({
                    title: 'Drought Turkana',
                    source: new ol.source.TileWMS({
                        url: 'http://maps.virtualkenya.org/geoserver/wms',
                        params: {'LAYERS': 'geonode:drought_constituencies'},
                        serverType: 'geoserver' 
                            })
                     })
                ]
            })
        ]
    });
    var layerSwitcherFourthMap = new ol.control.LayerSwitcher();
    fourth_map.addControl(layerSwitcherFourthMap);
	fourth_map.bindTo('view', first_map);
    
}