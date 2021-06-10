
const csv = require('csv');

// loads the csv module referenced above.

const http = require('http');

//loads the http module

​

const obj = csv();

// gets the csv module to access the required functionality

​

function MyCSV(Fone, Ftwo, Fthree, Ffour, FFive, Fsix, Fseven) {

    this.Tweets = Fone;

    this.id = Ftwo;

    this.len = Fthree;
//date,source,likes,retweets
    this.date = Ffour;
    this.source = FFive;
    this.likes = Fsix;
    this.retweets = Fseven;
};

// Define the MyCSV object with parameterized constructor, this will be used for storing the data read from the csv into an array of MyCSV. You will need to define each field as shown above.
​

var MyData = [];
// MyData array will contain the data from the CSV file and it will be sent to the clients request over HTTP.

​
obj.from.path("C:\\Users\\Atul Anand\\PycharmProjects\\BQ_POC_ETL_PY2\\objective_clarifications\\objective_doubts\\alreadyAsked\\byju\\v2_node_basics\\tweets_to_data_frame.csv").to.array(function (data) {
//obj.from.path("tweets_to_data_frame.csv").to.array(function (data) {    for (var index = 0; index < data.length; index++) {
//obj.from.path('weets_to_data_frame.csv').to.array(function (data) {

    for (var index = 0; index < data.length; index++) {

        MyData.push(new MyCSV(data[index][0], data[index][1], data[index][2], data[index][3], data[index][4], data[index][5], data[index][6]));

    }

    console.log(MyData);

});

//Reads the CSV file from the path you specify, and the data is stored in the array we specified using callback function.  This function iterates through an array and each line from the CSV file will be pushed as a record to another array called MyData , and logs the data into the console to ensure it worked.

​

const server = http.createServer(function (req, resp) {

    resp.writeHead(200, { 'content-type': 'application/json' });

    resp.end(JSON.stringify(MyData));

});

// Create a webserver with a request listener callback.  This will write the response header with the content type as json, and end the response by sending the MyData array in JSON format.

​

server.listen(3000);

// Tells the webserver to listen on port 8080(obviously this may be whatever port you want.)


//const csv = require('csv');
//// loads the csv module referenced above.
//
//const http = require('http');
////loads the http module
//
//const obj = csv();
//// gets the csv module to access the required functionality
//
//function MyCSV(Fone, Ftwo, Fthree) {
//    this.FieldOne = Fone;
//    this.FieldTwo = Ftwo;
//    this.FieldThree = Fthree;
//};
//// Define the MyCSV object with parameterized constructor, this will be used for storing the data read from the csv into an array of MyCSV. You will need to define each field as shown above.
//
//var MyData = [];
//// MyData array will contain the data from the CSV file and it will be sent to the clients request over HTTP.
//
////obj.from.path("C:\\Users\\Atul Anand\\PycharmProjects\\BQ_POC_ETL_PY2\\objective_clarifications\\objective_doubts\\alreadyAsked\\byju\\v2_node_basics\\tweets_to_data_frame.csv").to.array(function (data) {
//obj.from.path("tweets_to_data_frame.csv").to.array(function (data) {    for (var index = 0; index < data.length; index++) {
//        MyData.push(new MyCSV(data[index][0], data[index][1], data[index][2]));
//    }
//    console.log(MyData);
//});
////Reads the CSV file from the path you specify, and the data is stored in the array we specified using callback function.  This function iterates through an array and each line from the CSV file will be pushed as a record to another array called MyData , and logs the data into the console to ensure it worked.
//
//​const server = http.createServer(function (req, resp) {
//    resp.writeHead(200, { 'content-type': 'application/json' });
//    resp.end(JSON.stringify(MyData));
//});
//
//// Create a webserver with a request listener callback.  This will write the response header with the content type as json, and end the response by sending the MyData array in JSON format.
//server.listen(8080);
//// Tells the webserver to listen on port 8080(obviously this may be whatever port you want.
