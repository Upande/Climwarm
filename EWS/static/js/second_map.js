function secondmap() {
    var second_map = new ol.Map({
        target:'map_2',
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
                        params: {'LAYERS': 'geonode:vulnerability_classified'},
                        serverType: 'geoserver' 
                            })
                     })
                ]
            })
        ]
    });
        
        var layerSwitcherSecondMap = new ol.control.LayerSwitcher();
        second_map.addControl(layerSwitcherSecondMap);
        second_map.bindTo('view', first_map);
        
}