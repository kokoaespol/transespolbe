var map;
var infowindow;
var marcadores = [];
var limite = [];
var map;
var directionsDisplay = new google.maps.DirectionsRenderer();
var directionsService = new google.maps.DirectionsService();
var posicionESPOL = "-2.144367, -79.965262";

function displaysub(){
    var indice = document.getElementById("rutaBox").selectedIndex;
    var rutas = document.getElementById("rutaBox").options;
    //alert("Index: " + rutas[indice].index + " is " + rutas[indice].text);
    
    if(rutas[indice].text == "Ruta 1"){
    	map.setCenter(new google.maps.LatLng(-2.110262, -79.897598));
    	map.setZoom(13);
    }
    
		
}

//Mi ubicacion
function GoogleMap() {
	//var latActual = position.coords.latitude;
	//var lonActual = position.coords.longitude;
	//var location = new google.maps.LatLng(latActual, lonActual);
	map = new google.maps.Map(document.getElementById('map-canvas'), {
		zoom: 16,
		disableDefaultUI: true,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	start = posicionESPOL;
	end = "-2.223679, -79.904701";
	if(window.location.pathname.match("acacias")){
		end = "-2.223679, -79.904701";
	}
	if(window.location.pathname.match("norte1")){
		end = "-2.110491, -79.903854";
	}
	if(window.location.pathname.match("norte2")){
		end = "-2.126466, -79.900440";
	}
	if(window.location.pathname.match("norte3")){
		end = "-2.138026, -79.884503";
	}
	if(window.location.pathname.match("perimetral")){
		end = "-2.150959, -79.946464";
	}
	
	marcarCamino(end, start);
	
	directionsDisplay = new google.maps.DirectionsRenderer();
	directionsService = new google.maps.DirectionsService();
	map.setCenter(posicionESPOL);
}

function showError() {
	alert("Location can't be found");
}


function inicio(){
	GoogleMap();
}


function marcarCamino(start, end){
	
	//var indice = document.getElementById("rutaBox").selectedIndex;
    //var rutas = document.getElementById("rutaBox").options;
    //alert("Index: " + rutas[indice].index + " is " + rutas[indice].text);
    //var start = "-2.140131, -79.929329";
	//var end = posicionESPOL;
    
    //if(rutas[indice].text == "Ruta 1"){
    	//map.setCenter(new google.maps.LatLng(-2.110262, -79.897598));
    	//map.setZoom(13);
    //}
	
	
	//var start = $('#origen').val();
	//var end = $('#destino').val();
	if(!start || !end){
		alert("Start and End addresses are required");
		return;
	}
	var request = {
		 origin: start,
		 destination: end,
		 travelMode: "DRIVING",//google.maps.DirectionsTravelMode[$('#modo_viaje').val()],
		 unitSystem: 0,//google.maps.DirectionsUnitSystem[$('#tipo_sistema').val()],
		 provideRouteAlternatives: true
	 };
	directionsService.route(request, function(response, status) {
		if (status == google.maps.DirectionsStatus.OK) {
			directionsDisplay.setMap(map);
			directionsDisplay.setPanel($("#panel_ruta").get(0));
			directionsDisplay.setDirections(response);
		} else {
				alert("No existen rutas entre ambos puntos");
		}
	});
}
	
$(document).ready(function() {
    inicio();
  		
});


//google.maps.event.addDomListener(window, 'load', inicio);