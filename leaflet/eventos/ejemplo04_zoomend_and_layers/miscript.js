// nota: la primera vez que se carga la capa de boca de subtes tiene que ser despues del primer zoom de cerca (por eso el flag)

//#### 1) cargo capa principal o sea la de amba

// Opciones de configuracion del mapa (que son los tiles)
var mapOptions = {
    center: [-34.619930,-58.439884],
    zoom: 12
 }

 var map = new L.map('map', mapOptions); // Creo el objeto mapa con las configuraciones correspondientes
 
 // capa base el cual son los tiles de amba_con_transporte_3857
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
// creo la capa de tiles 
layer = L.tileLayer(baseLayer.uri,baseLayer.params);
// agrego la capa de tiles a mi objeto mapa
map.addLayer(layer);




//#### 2) cargo el mapa de barrios
var capaDeBarrio = L.layerGroup([]);  // grupo de capas para los barrios
L.geoJson(barrios, {}).addTo(capaDeBarrio);
capaDeBarrio.addTo(map)


//### 3) agrego los datos para la capa de boca de subtes que sera cargado cuando se invoque el metodo traerCapa
var url_capa_boca_de_subtes = 'https://epok.buenosaires.gob.ar/getGeoLayer/?categoria=bocas_de_subte_sbase&formato=geojson&srid=4326' 
 
var grupoDeSubtes = L.layerGroup([]); // grupo de capas para las bocas de subtes
var flag_bocas_de_subte = false; // lo uso para la carga y descarga de la capa de bocas de subtes
var carga_primera_vez_boca_de_subtes = false
var returned_data;
grupoDeSubtes.addTo(map)


/***************************************************/
/********************  Métodos  ********************/
/***************************************************/



// este metodo se invoca una sola vez, el cual va a hacer que se cargue la capa de boca de subtes, es llamado por cargar capa
var accionDespuesDeTraerCapa = function(returned_data) {
    boca_de_subtes = returned_data; // guardo la informacion el la variable boca_de_subtes
    L.geoJson(boca_de_subtes, { }).addTo(grupoDeSubtes);
}

// este metodo se invoca una sola vez, el cual va a hacer que se cargue la capa de boca de subtes
function cargarCapa(){
    traerCapa(url_capa_boca_de_subtes,accionDespuesDeTraerCapa);
}   


// hace una peticion a la url indicada y "retorna" el json de la capa
function traerCapa(url,callback) {
    var request = new XMLHttpRequest();
    request.open("GET", url, true);
    request.responseType = 'json';
    request.send();
    request.onreadystatechange= function () {
        if (request.readyState == 4 && request.status == 200) {
            returned_data = request.response;
            callback.apply(this,[returned_data]); // emplea la funcion accionDespuesDeTraerCapa()
        }else{

        }
    };
}


/***************************************************/
/********************  Eventos  ********************/
/***************************************************/

/* 
 *
 *@details: evento para el control del evento zoom del mapa
 *
 **/

map.on('zoomend ', function(e) {     
    if ( map.getZoom() >= 14 ){ 
        if (carga_primera_vez_boca_de_subtes == false){
            cargarCapa()
            carga_primera_vez_boca_de_subtes = true
        }else if(flag_bocas_de_subte == false){
            map.addLayer(grupoDeSubtes)
            flag_bocas_de_subte = true
        }
    }
    else if ( map.getZoom() <  14 && carga_primera_vez_boca_de_subtes == true){ 
        if(flag_bocas_de_subte == true) {
            map.removeLayer(grupoDeSubtes);
            flag_bocas_de_subte = false
        }  
    }
    console.log('zoom: ' + map.getZoom())
});




