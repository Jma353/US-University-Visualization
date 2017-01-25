// linreg.js 
// Function written for linear regression functionality
// By Joseph Antonakakis


// Given a dataset data, x and y namespaces xname and yname,
// as well as x and y terms, perform a linear regression on
// the data set and return a 2-tuple with [B1, B0]
function linearRegression(data, xname, x, yname, y) {

  // Calculate the x-value mean
  var xMean = d3.mean(data, function (d) {
    return d[xname][x];
  });

  // Calculate the y-value mean
  var yMean = d3.mean(data, function (d) {
    return d[yname][y];
  });

  var numerator = 0;
  var denominator = 0;


  data.forEach(function (d) {
    var num = (d[xname][x] - xMean) * (d[yname][y] - yMean);
    var den = (d[xname][x] - xMean) * (d[xname][x] - xMean);
    numerator += num;
    denominator += den;
  });

  // Solve for these variables
  var B1 = numerator.toFixed(5) / denominator.toFixed(5);
  var B0 = yMean - B1 * xMean;

  return [B1, B0];

}
