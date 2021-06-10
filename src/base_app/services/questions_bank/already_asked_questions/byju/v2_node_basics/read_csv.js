var csv = require('csv-parser');
var fs = require('fs');

fs.createReadStream('tweets_to_data_frame.csv')
  .pipe(csv())
  .on('data', (row) => {
    console.log(row);
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
  });
