// kcluster.js 
// Functions written for k-means clustering functionality 


// Basic distance function 
function distanceForm (a, b, x, y) {
	return Math.sqrt(
		(a[x] - b[x]) * (a[x] - b[x]) + 
		(a[y] - b[y]) * (a[y] - b[y])
	); 
}


// Given data array filled with JSONs, each with x and y values namespaced under 
// the provided parameter values, return a list of k random points of the form 
// [ { x: X_VAL, y: Y_VAL, id: 1 }, ..., ... ]
function initalizeClusters (data, k) {
	var initial_centroids = []; 
	for (var i = 1; i <= k; i++) {
		var n = Math.floor(Math.random() * data.length)
		data[n]["id"] = i; 
		initial_centroids.push(JSON.parse(JSON.stringify(data[n]))); // Copies 
	}
	return initial_centroids
}

// Given data array filled with JSONs, each with x and y values namespaced under 
// the provided parameter values, return the data JSONs with an extra field 
// `clusterId` indicating which cluster the values belong to (minDist away)
function initializeData (data, clusters, x, y) {
	
	for (var i = 0; i < data.length; i++) {
		var distances = clusters.map(function(d) {
			return distanceForm(data[i], d, x, y); 
		});
		var minDist = d3.min(distances); 
		var clusterIndex = distances.indexOf(minDist); 
		var clusterId = clusters[clusterIndex].id; 
		data[i]["clusterId"] = clusterId; 
	}

	return data; 

}




function prepareClusters (data, clusters, x, y) {
	// TODO 
}	






