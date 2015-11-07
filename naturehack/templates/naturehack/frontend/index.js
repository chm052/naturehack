'use strict';

// Get the data
var url = '../naturehack';

uxhr(url, '', {
	method: 'GET',
	complete: complete,
	success: success,
	error: error
});

function complete (response, status) {
	console.log('request complete', status);
}

function success (response) {
	console.log('"' + response + '"');
	createWalks(response);
}

function error (response, status) {
	console.log('"' + response + '"', status);
}

function createWalks(walks) {
	var doc = document;
	var item;
	var hikrWalkList = doc.createElement('ul');

	hikrWalkList.classList.add('hikr__walks');

	walks.forEach(function(walk) {
		item = doc.createElement('li');
		item.classList.add('hikr__walks-item');
		item.innerHTML = walk.name;
		hikrWalkList.appendChild(item);
	});

	return hikrWalkList;
}

var mock = [{lat: 174.8656943777268, name: "CIRCUIT TRACK MATIU", long: -41.25547727765185}, {lat: 174.86416062697066, name: "Road to Circuit Track", long: -41.25831435774681}, {lat: 174.8660373791062, name: "Southern Summit Track", long: -41.25963291993241}, {lat: 174.86567057352957, name: "Workshop to VC Track", long: -41.256484419270315}, {lat: 174.86512994666623, name: "Memorial Track", long: -41.25474276763705}, {lat: 174.86650207849337, name: "BULLOCK TRACK", long: -41.2559556336113}, {lat: 174.86744419896112, name: "DEGAUSSING STATION TRACK", long: -41.256334556932664}, {lat: 174.70736657777832, name: "Makara Carpark to Gun Emplacements", long: -41.218407491659924}, {lat: 174.6947224810965, name: "MAKARA MERIDIAN ROAD SECTION", long: -41.23012942670318}, {lat: 174.68940575482617, name: "Makara Road End to Opau Stream mouth", long: -41.233250561610774}];