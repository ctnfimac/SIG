// Creating map options
var mapOptions = {
    center: [-34.619930,-58.439884],
    zoom: 12
 }

 var map = new L.map('map', mapOptions); // Creating a map object

 // esta informacion lo saque de https://github.com/usig/mapa-interactivo/blob/master/src/MapaInteractivo.js
 var  baseLayer = {
    uri: 'https://servicios.usig.buenosaires.gob.ar/mapcache/tms/1.0.0/amba_con_transporte_3857@GoogleMapsCompatible/{z}/{x}/{y}.png',
    params: {
        maxZoom: 18,
        minZoom: 9,
        attribution: '<a href="https://usig.buenosaires.gob.ar" target="_blank">USIG</a> (<a href="http://www.buenosaires.gob.ar" target="_blank">GCBA</a>), © <a href="http://www.openstreetmap.org/copyright/en" target="_blank">OpenStreetMap</a> (ODbL)',
        tms: true,
        id: '',
        accessToken: ''
    }
};
this.layer = L.tileLayer(baseLayer.uri,baseLayer.params);
 // Creating a Layer object
 //var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
 map.addLayer(layer);      // agrego la capa al mapa
 // Creamos los marcadores
 var marker1 = new L.Marker([-34.619930,-58.459884]);
 var marker2 = new L.Marker([-34.619932,-58.400089]);
 var marker3 = new L.Marker([-34.649932,-58.455089]);
 var marker4 = new L.Marker([-34.649932,-58.400089]);
 // Creating latlng object
 var vertices = [
    [-34.619930,-58.459884],
    [-34.619932,-58.400089],
    [-34.649932,-58.400089],
    [-34.649932,-58.455089]
 ];
 // Creating a polygon
 var poligono = L.polygon(
                           vertices, 
                           {
                            color: 'tomato'
                           }
                         );

 // evento para el control del evento zoom
 map.on('zoomend ', function(e) {
    if ( map.getZoom() <= 12 ){ map.removeLayer( circulo )}
    else if ( map.getZoom() > 12 ){ map.addLayer( circulo )}
    console.log('zoom: ' + map.getZoom())
 });
 
 // creamos un  grupo de capas
 var layerGroup = L.layerGroup([marker1, marker2, marker3, marker4, poligono]);
 layerGroup.addTo(map);    // Agregamos el grupo de capas al mapa

// Creamos un circulo
var circulo = L.circle([-34.649932,-58.455089], 600, {color: 'tomato', fillColor:
'#f03', fillOpacity: 0} );

// Adding circulo to the layer group
layerGroup.addLayer(circulo);
