function firstmap() {
	
	first_map = new ol.Map({
        target:'map_1',
        layers: [new ol.layer.Group({
            title: 'Base Maps',
            layers: [
            new ol.layer.Tile({
                title: 'Bing Maps',
                visible: false,
                source: new ol.source.BingMaps({
                    key: 'Ak-dzM4wZjSqTlzveKz5u0d4IQ4bRzVI309GxmkgSVr1ewS6iPSrOvOKhA-CJlm3',
                    imagerySet: 'AerialWithLabels'})
                    }),
            new ol.layer.Tile({
            	title: 'OSM',
            	visible: true,
            	source: new ol.source.OSM({
                    attributions: [new ol.Attribution({
                                html:'powered by virtualkenya '+'<a href="http://maps.virtualkenya.org/maps/894">Get Metadata</a>'+ ' || '
                              })
                            ]
                })
            })
                ]
            }),
            new ol.layer.Group({
                title: 'Overlays',
                layers:[ new ol.layer.Tile({
                    title: '- 3.4m depth',
                    type: 'base',
                    source: new ol.source.TileWMS({
                        url: 'http://maps.virtualkenya.org/geoserver/wms',
                        params: {layers: 'geonode:_2013_3_4mdepth',
                    			 format: 'image/png'},
                        serverType: 'geoserver' }),
                    showLegend:true
                    
                     })
                ]
            })
        ],
        view: new ol.View({
            projection: 'EPSG:900913',
            center:[3788403, 12762],
            zoom:11
            })
    });
	
		first_map.addControl(new ol3_legend({
            map: first_map,
            class: 'ol_legend' }));

        var layerSwitcher = new ol.control.LayerSwitcher();
        first_map.addControl(layerSwitcher);
   }