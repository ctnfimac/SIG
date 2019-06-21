var mymap = L.map('mapid').setView([51.505, -0.09], 17);
let x = 51.505;
let y = -0.09;
//var map = L.map('map').setView([x,y],17);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
    }).addTo(map);

var geojsonFeature = {
    "type": "Feature",
    "properties": {
        "name": "Coors Field",
        "amenity": "Baseball Stadium",
        "popupContent": "This is where the Rockies play!"
    },
    "geometry":{
        "type": "Point",
        "coordinates": [x, y]
    }
};

L.geoJSON(geojsonFeature).addTo(map)


var myLayer = L.geoJSON().addTo(map)
myLayer.addData(geojsonFeature)

var mystyle = {
    "color": "#ff7800",
    "weight": 5,
    "opacity": 0.9        
}
/*
L.geoJSON(myLines,{
    style: mystyle
}).addTo(map)
*/

var states = [{
    "type": "Feature",
    "properties": {"party": "Republican"},
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [-34.629209, -58.370082],
            [-34.629211,  -58.370082],
            [-34.629213,  -58.370082],
            [-34.629215, -58.370082],
            [-34.629215, -58.370082]
        ]]
    }
}, {
    "type": "Feature",
    "properties": {"party": "Democrat"},
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [-109.05, 41.00],
            [-102.06, 40.99],
            [-102.03, 36.99],
            [-109.04, 36.99],
            [-109.05, 41.00]
        ]]
    }
}];

L.geoJSON(states, {
    style: function(feature) {
        switch (feature.properties.party) {
            case 'Republican': return {color: "#ff0000"};
            case 'Democrat':   return {color: "#0000ff"};
        }
    }
}).addTo(map);