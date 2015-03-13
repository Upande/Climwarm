function thirdmap() {

	var third_map = new ol.Map({
        target:'map_3',
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
                    title: 'Drought risk map',
                    source: new ol.source.TileWMS({
                        url: 'http://maps.virtualkenya.org/geoserver/wms',
                        params: {'LAYERS': 'geonode:dr_03_dek3'},
                        serverType: 'geoserver' 
                            })
                     })
                ]
            })
        ]
    });

     var layerSwitcherThirdMap = new ol.control.LayerSwitcher();
     third_map.addControl(layerSwitcherThirdMap);

    third_map.bindTo('view', first_map);
    
}