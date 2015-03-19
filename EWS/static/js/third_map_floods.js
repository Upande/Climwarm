function thirdmap() {
	
	    third_map = new ol.Map({
        target:'map_3',
        layers: [new ol.layer.Group({
            title: 'Base Maps',
            layers: [
            new ol.layer.Tile({
                title: 'Bing Maps',
                type: 'base',
                visible: false,
                source: new ol.source.BingMaps({
                    key: 'Ak-dzM4wZjSqTlzveKz5u0d4IQ4bRzVI309GxmkgSVr1ewS6iPSrOvOKhA-CJlm3',
                    imagerySet: 'AerialWithLabels'

                        })
                    }),
            new ol.layer.Tile({
                title: 'OSM',
                type: 'base',
                visible: true,
                source: new ol.source.OSM({
                    attributions: [new ol.Attribution({
                                html:'powered by virtualkenya '+'<a href="http://maps.virtualkenya.org/maps/896" target="_blank">Get Metadata</a>'+ ' || '
                              })
                            ]
                })
            })
                ]
            }),
            new ol.layer.Group({
                title: 'Overlays',
                layers:[ new ol.layer.Tile({
                    title: 'flood homes',
                    source: new ol.source.TileWMS({
                        url: 'http://maps.virtualkenya.org/geoserver/wms',
                        params: {layers: 'geonode:risk',
                                  format: 'image/png'},
                        serverType: 'geoserver' 
                            }),
                    showLegend:true
                     })
                ]
            })
        ]
    });
    
    var layerswitcher = new ol.control.LayerSwitcher();
    third_map.addControl(layerswitcher);

    third_map.addControl(new ol3_legend({
            map: third_map,
            class: 'ol_legend' }));

    third_map.bindTo('view', first_map);
}