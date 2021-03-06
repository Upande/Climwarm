function fourthmap() {

	   fourth_map = new ol.Map({
        target:'map_4',
        layers: [new ol.layer.Group({
            title: 'Base Maps',
            layers: [
            new ol.layer.Tile({
                title: 'Bing Maps',
                visible: false,
                source: new ol.source.BingMaps({
                    key: 'Ak-dzM4wZjSqTlzveKz5u0d4IQ4bRzVI309GxmkgSVr1ewS6iPSrOvOKhA-CJlm3',
                    imagerySet: 'AerialWithLabels'
                        })
                    }),
            new ol.layer.Tile({
                title: 'OSM',
                visible: true,
                source: new ol.source.OSM({
                    attributions: [new ol.Attribution({
                                html:'powered by virtualkenya '+'<a href="http://maps.virtualkenya.org/maps/893" target="_blank">Get Metadata</a>'+ ' || '
                              })
                            ]
                })
                    })
                ]
            }),
            new ol.layer.Group({
                title: 'Overlays',
                layers:[ new ol.layer.Tile({
                    title: 'Drought Turkana',
                    type: 'base',
                    source: new ol.source.TileWMS({
                        url: 'http://maps.virtualkenya.org/geoserver/wms',
                        params: {layers: 'geonode:drought_constituencies',
                                  format: 'image/png'},
                        serverType: 'geoserver' 
                            }),
                    showLegend:true
                     })
                ]
            })
        ]
    });
    var layerSwitcherFourthMap = new ol.control.LayerSwitcher();
    fourth_map.addControl(layerSwitcherFourthMap);

    fourth_map.addControl(new ol3_legend({
            map: fourth_map,
            class: 'ol_legend' }));

	fourth_map.bindTo('view', first_map);
    
}