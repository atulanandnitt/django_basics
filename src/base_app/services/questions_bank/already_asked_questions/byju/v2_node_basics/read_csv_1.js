var csv = require('csv-parser');
var fs = require('fs');


const express = require('express')
app = express();


//Add middleware to parse json object
app.use(express.json())

var data = fs.createReadStream('tweets_to_data_frame.csv')
  .pipe(csv())
  .on('data', (row) => {
    console.log(row);
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
  });

app.get('/api/tweets', (req, resp) => {
        resp.send(data)
        })


const port = 3000
app.listen(port, () => console.log(`Now Listening port ${port}`))
