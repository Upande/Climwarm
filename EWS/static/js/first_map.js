function firstmap() {
    first_map = new ol.Map({
        target:'map',
        layers: [new ol.layer.Group({
            title: 'Base Maps',
            layers: [
            new ol.layer.Tile({
                title: 'OSM',
                visible: true,
                source: new ol.source.OSM()
                    })
                ]
            }),
            new ol.layer.Group({
                title: 'Overlays',
                layers:[ new ol.layer.Tile({
                    title: '- NDVI',
                    type: 'base',
                    source: new ol.source.TileWMS({
                        url: 'http://maps.virtualkenya.org/geoserver/wms',
                        params: {'LAYERS': 'geonode:ndvianom_2011_apr_dek1'},
                        serverType: 'geoserver' })
                    
                     }),
                    new ol.layer.Tile({
                            title: '- Anom',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {'LAYERS': 'geonode:dek3anomaly'},
                            serverType: 'geoserver' })
                            
                        }),
                    new ol.layer.Tile({
                            title: '- Aver',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {'LAYERS': 'geonode:dek3aves'},
                            serverType: 'geoserver' })
                            
                        }),
                    new ol.layer.Tile({
                            title: '- Ita',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {'LAYERS': 'geonode:dek3lta'},
                            serverType: 'geoserver' })
                            
                        }),
                    new ol.layer.Tile({
                            title: '- Spi',
                            type: 'base',
                            source: new ol.source.TileWMS({
                            url: 'http://maps.virtualkenya.org/geoserver/wms',
                            params: {'LAYERS': 'geonode:spi_201103_dek3'},
                            serverType: 'geoserver' })
                            
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
}