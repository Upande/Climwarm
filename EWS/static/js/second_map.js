
function secondmap() {
        second_map = new ol.Map({
        target:'map_2',
        layers: [new ol.layer.Group({
            title: 'Base Maps',
            layers: [
            new ol.layer.Tile({
                title: 'Bing Maps',
                visible: true,
                source: new ol.source.BingMaps({
                    key: 'Ak-dzM4wZjSqTlzveKz5u0d4IQ4bRzVI309GxmkgSVr1ewS6iPSrOvOKhA-CJlm3',
                    imagerySet: 'AerialWithLabels'
                        })
                    }),
            new ol.layer.Tile({
                title: 'OSM',
                visible: false,
                source: new ol.source.OSM()
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
                        params: {layers: 'geonode:vulnerability_classified',
                                  format: 'image/png'},
                        serverType: 'geoserver' }),
                    showLegend: true
                    
                     })
                ]
            })
        ]
    });
        
        var layerSwitcherSecondMap = new ol.control.LayerSwitcher();
        second_map.addControl(layerSwitcherSecondMap);

        second_map.addControl(new ol3_legend({
            map: second_map,
            class: 'ol_legend' }));

        second_map.bindTo('view', first_map);


        
}