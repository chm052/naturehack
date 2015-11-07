'use strict';

var url = '/naturehack';

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
	}

	function error (response, status) {
		console.log('"' + response + '"', status);
	}