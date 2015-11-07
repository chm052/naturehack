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
		item.innerHtml = walk.name;
		hikrWalkList.appendChild(item);
	});

	return hikrWalkList;
}