//https://www.youtube.com/watch?v=lm86czWdrk0&list=PL4cUxeGkcC9gcy9lrvMJ75z9maRw4byYp&index=12
var http =  require('http');

var MyData = [];
// MyData array will contain the data from the CSV file and it will be sent to the clients request over HTTP.

​obj.from.path("C:\\Users\\Atul Anand\\PycharmProjects\\BQ_POC_ETL_PY2\\objective_clarifications\\objective_doubts\\alreadyAsked\\byju\\v2_node_basics\\tweets_to_data_frame.csv").to.array(function (data) {
//obj.from.path("tweets_to_data_frame.csv").to.array(function (data) {    for (var index = 0; index < data.length; index++) {
//obj.from.path('weets_to_data_frame.csv').to.array(function (data) {

    for (var index = 0; index < data.length; index++) {

        MyData.push(new MyCSV(data[index][0], data[index][1], data[index][2], data[index][3], data[index][4], data[index][5], data[index][6]));

    }

    console.log(MyData);

});


var server = http.createServer(function(req,res){
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end(MyData);
});

server.listen(3000, '127.0.0.1');

console.log('listening to port 3000')
