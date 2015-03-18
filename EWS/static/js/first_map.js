function firstmap() {
        first_map = new ol.Map({
        target:'map_1',
        layers: [new ol.layer.Group({
            title: 'Base Maps',
            layers: [
            new ol.layer.Tile({
                title: 'OSM',
                visible: false,
                source: new ol.source.OSM()
                    }),
            new ol.layer.Tile({
                title: 'Bing Maps',
                visible: true,
                source: new ol.source.BingMaps({
                    key: 'Ak-dzM4wZjSqTlzveKz5u0d4IQ4bRzVI309GxmkgSVr1ewS6iPSrOvOKhA-CJlm3',
                    imagerySet: 'AerialWithLabels'
                })
            })
                ]
            }),
            new ol.layer.Group({
                title: 'Overlays',
                layers:[ //new ol.layer.Tile({
                    //title: '- NDVI',
                    //type: 'base',
                    //source: new ol.source.TileWMS({
                     //   url: 'http://maps.virtualkenya.org/geoserver/wms',
                       // params: {layers: 'geonode:ndvianom_2011_apr_dek1',
                         //           format: 'image/png'},
                        //serverType: 'geoserver' })
                    
                     //}),
                    new ol.layer.Tile({
                            title: '- Anom',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {layers: 'geonode:dek3anomaly',
                                        format: 'image/png'},
                            serverType: 'geoserver' })
                            
                        }),
                    new ol.layer.Tile({
                            title: '- Aver',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {layers: 'geonode:dek3aves',
                                        format: 'image/png'},
                            serverType: 'geoserver' })
                            
                        }),
                    new ol.layer.Tile({
                            title: '- Ita',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {layers: 'geonode:dek3lta',
                                        format: 'image/png'},
                            serverType: 'geoserver' })
                            
                        }),
                    new ol.layer.Tile({
                            title: '- Spi',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {layers: 'geonode:spi_201103_dek3',
                                        format: 'image/png'},
                            serverType: 'geoserver' }),
                            showLegend:true
                            
                        })
                ]
            })
        ],
        view: new ol.View({
            projection: 'EPSG:900913',
            center:[3930427, 359171],
            zoom:6
            })
    });

        
        var layerSwitcherFirstMap = new ol.control.LayerSwitcher();
        first_map.addControl(layerSwitcherFirstMap);
        
        first_map.addControl(new ol3_legend({
            map: first_map,
            class: 'ol_legend' }));
        

}