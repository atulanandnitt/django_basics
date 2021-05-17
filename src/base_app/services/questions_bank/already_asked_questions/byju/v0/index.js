const express = require('express')
app = express();
//Add middleware to parse json object
app.use(express.json())

//Content validation using joi
Joi = require('joi')

const courses = [
{id: 1, name: "course1"},
{id: 2, name: "course2"},
{id: 3, name: "course3"}
]
function validateCourse(body){
schema = {
name: Joi.string().min(3).required()
}
return Joi.validate(body, schema)
}

app.get('/', (req, res) => {
res.send("Hello world !!!")
});

app.get('/api/courses/:year/:month', (req, res) => {
res.send(req.query)
});

app.get('/api/courses', (req, resp) => {
resp.send(courses)
})

app.post('/api/courses/', (req, resp) => {
const course = {
id: courses.length + 1,
name: req.body.name
}
courses.push(course)
resp.send(course)
})

app.put('/api/courses/:id', (req, resp) => {
const course = courses.find(c => c.id === parseInt(req.params.id));
console.log(course)
if(!course){
resp.status(404).send('The course does not exist')
}
//validate whether it exist
//validate request body
const { error } = validateCourse(req.body)
console.log(error)
console.log('Till here')
if(error){
resp.status(404).send(error.details[0].message)
}
course.name = req.body.name
resp.send(course)
}
);

const port = 3000
app.listen(port, () => console.log(`Now Listening port ${port}`))
