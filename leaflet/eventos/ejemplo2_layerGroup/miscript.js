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
var flag = false;
 // evento para el control del evento zoom
 map.on('zoomend ', function(e) {
     
    if ( map.getZoom() >= 15 ){ 
        //map.removeLayer( circulo )
        //
        if (flag == false){
            L.geoJson(boca_de_subtes, { }).addTo(grupoDeSubtes);
            flag = true
        } else{
            map.addLayer(grupoDeSubtes)
        }
    }
    else if ( map.getZoom() <  15 ){ 
        //map.addLayer( circulo )
        if(flag == true) 
        map.removeLayer(grupoDeSubtes);
    }
    /*
    if ( map.getZoom() <= 10 ){ 
        //map.removeLayer( circulo )
        map.removeLayer(capaDeBarrio);
    }
    else if ( map.getZoom() > 10 ){ 
        //map.addLayer( circulo )
        map.addLayer(capaDeBarrio)
    }*/
    console.log('zoom: ' + map.getZoom())
 });
 
 // creamos un  grupo de capas
 var layerGroup = L.layerGroup([marker1, marker2, marker3, marker4, poligono]);
 var grupoDeSubtes = L.layerGroup([]);
 var capaDeBarrio = L.layerGroup([]);
 //layerGroup.addTo(map);    // Agregamos el grupo de capas al mapa
grupoDeSubtes.addTo(map)
capaDeBarrio.addTo(map)
// Creamos un circulo
//var circulo = L.circle([-34.649932,-58.455089], 600, {color: 'tomato', fillColor:'#f03', fillOpacity: 0} );
//layerGroup.addLayer(circulo)


function popUpInfo(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.barrio) {
        layer.bindPopup("<b>"+feature.properties.barrio+"</b><br>"+feature.properties.comuna+" ("+feature.properties.perimetro+")");
        //layer.bindPopup("<b>"+feature.properties.nomb_mus);
    }
}

L.geoJson(barrios, {
    //onEachFeature: popUpInfo
    }).addTo(capaDeBarrio);



//bocas_de_subte = getJSON('https://epok.buenosaires.gob.ar/getGeoLayer/?categoria=bocas_de_subte_sbase&formato=geojson&srid=4326')
//L.geoJson(barrios).removeTo(map);
//console.log('bocas de subte',bocas_de_subte)
// Adding circulo to the layer group
//layerGroup.addLayer(circulo);

/*
function peticion(){
    const url = 'https://epok.buenosaires.gob.ar/getGeoLayer/?categoria=bocas_de_subte_sbase&formato=geojson&srid=4326'
    const http = new XMLHttpRequest()

    http.open("GET", url)
    http.onreadystatechange = function(){

        if(this.readyState == 4 && this.status == 200){
            var resultado = JSON.parse(this.responseText)
            console.log(resultado)
        }
    }
    http.send()
}*/





// otra prueba
url_capa_boca_de_subtes = 'https://epok.buenosaires.gob.ar/getGeoLayer/?categoria=bocas_de_subte_sbase&formato=geojson&srid=4326' 
var returned_data;

var accionDespuesDeTraerCapa = function(returned_data) {
    boca_de_subtes = returned_data;
    
    // aca agrego las bocas de subtes al mapa
    //L.geoJson(boca_de_subtes, {  
    //}).addTo(grupoDeSubtes);


    //layerGroup.addTo(boca_de_subtes)
    //map.removeLayer(layerGroup);
    
}

function cargarCapa(){
    traerCapa(url_capa_boca_de_subtes,accionDespuesDeTraerCapa);
}   



function traerCapa(tag,callback) {
    var req1 = new XMLHttpRequest();
    req1.open("GET",tag, true);
    req1.responseType = 'json';
    req1.send();

    req1.onreadystatechange= function () {
        if (req1.readyState == 4 && req1.status == 200) {
            returned_data = req1.response;
            //llamo a la funcion cargarCapa
            callback.apply(this,[returned_data]);
        }else{

        }
    };
}

cargarCapa()

//
/*
var getJSON = function(url, callback) {
    var respuesta;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
        var status = xhr.status;
        if (status === 200) {
        //callback(null, xhr.response);
        console.log("respuesta", xhr.response)
        respuesta = "Hello"
        //return  xhr.response
        } else {
        callback(status, xhr.response);
        console.log("respuesta2", xhr.response)
        //return "error"
        }
    };
    console.log("respuesta onload",respuesta)
    xhr.send();
};




var dato = getJSON('http://epok.mamut-squeeze.usig.gcba.gov.ar/getGeoLayer/?categoria=bocas_de_subte_sbase&formato=geojson&srid=4326',
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
    //alert('Your query count: ' + data.query.count);
    console.log('estoy en el else')
  }
});

console.log("mi dato:", dato)

*/

/*
function mifuncion(){
return fetch('http://epok.mamut-squeeze.usig.gcba.gov.ar/getGeoLayer/?categoria=bocas_de_subte_sbase&formato=geojson&srid=4326')
  .then(response => {
    return response.json()
  })
  .then(data => {
    // Work with JSON data here
    //console.log(data)
    return (data)
  })
  .catch(err => {
    // Do something for an error here
  })
}
console.log("mi dato:",mifuncion)
*/

/*
function getvals(){
    return fetch('https://epok.buenosaires.gob.ar/getGeoLayer/?categoria=bocas_de_subte_sbase&formato=geojson&srid=4326',
    {
    	method: "GET",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    })
    .then((response) => response.json())
    .then((responseData) => {
      console.log(responseData);
      return responseData;
    })
    .catch(error => console.warn(error));
  }
  
  getvals().then(response => console.log("adasd",response));
  */

  /*
  fuentes: http://jsfiddle.net/FranceImage/pcqsne4z/
  https://stackoverflow.com/questions/19298112/returning-values-from-the-event-onreadystatechange-in-ajax
  */