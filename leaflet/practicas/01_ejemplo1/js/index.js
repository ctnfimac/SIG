 //var mymap = L.map('mapid').setView([51.505, -0.09], 13);
 let x = -34.629209;
 let y = -58.370082;
 var map = L.map('map').setView([x,y],17);
 L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
     maxZoom: 18
     }).addTo(map);
 L.control.scale().addTo(map);
// L.marker([x,y],{draggable: true}).addTo(map);
 var marker = L.marker([x,y]).addTo(map)
 var circle = L.circle([x,y-0.001],{
     color: 'red',
     fillcolor: '#f03',
     fillOpacity: 0.5,
     radius: 50
 }).addTo(map)

 var polygon = L.polygon([
     [x-0.01,y],
     [x-0.01,y+0.01],
     [x-0.01,y-0.02]
 ]).addTo(map)

 marker.bindPopup("<b>Hola chico mapa!</b><br>yo soy un popup.").openPopup()
 /*var popup = L.popup()
     .setLatLng([x,y])
     .setContent("I am silvester stalone popup")
     .openOn(map)*/
 
 function onMapClick(e){
     alert('cliqueaste en el mapa: ' + e.latlng)
 }

 map.on('click', onMapClick)