const express = require('express')
const fs = require('fs');
const csv = require('csv-parser')
const http = require('http')
app = express();
//Add middleware to parse json object
app.use(express.json())

//Content validation using joi
Joi = require('joi')

response = []
function validateCourse(body){
    schema = {
        name: Joi.string().min(3).required()
        }
    return Joi.validate(body, schema)
    }

var data = fs.createReadStream('tweets_to_data_frame.csv')
     .pipe(csv())
     .on('data', (row) => {
       //console.log(row);
       response.push(row)
     })
     .on('end', () => {
       console.log('CSV file successfully processed');
     });

app.get('/', (req, res) => {
res.send("testing setup")
});


app.get('/api/tweets', (req, resp) => {
console.log(response)
       resp.send(response)
   })

);

const port = 3000
app.listen(port, () => console.log(`Now Listening port ${port}`))
