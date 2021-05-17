/*
This program reads and parses all lines from csv files countries2.csv into an array (countriesArray) of arrays; each nested array represents a country.
The initial file read is synchronous. The country records are kept in memory.
*/

var fs = require('fs');
var parse = require('csv-parse');

var inputFile='tweets_to_data_frame.csv';
console.log("Processing Countries file");
//Tweets,id,len,date,source,likes,retweets
var parser = parse({delimiter: ';'}, function (err, data) {
    // when all countries are available,then process them
    // note: array element at index 0 contains the row of headers that we should skip
    data.forEach(function(line) {
      // create country object out of parsed fields
      var country = { "Tweets" : line[0]
                    , "id" : line[1]
                    , "len" : line[2]
                    , "date" : line[4]
                    , "source" : line[5]
                    , "likes": line[6]
                    , "retweets" : line[7]
                    };
     console.log(JSON.stringify(country));
    });
});

// read the inputFile, feed the contents to the parser
//fs.createReadStream(inputFile).pipe(parser);

const express = require('express')
app = express();


//Add middleware to parse json object
app.use(express.json())

app.get('/api/tweets', (req, resp) => {
        resp.send(parser)
        })

const port = 3000
app.listen(port, () => console.log(`Now Listening port ${port}`))
