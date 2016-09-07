var express = require('express');
var app = express();

app.set('views', __dirname + '/../');
app.engine('html', require('ejs').renderFile);

app.set('view engine', 'ejs');

app.get('/', function(req, res) {
    res.render('client.html');
});

app.listen(8080, '127.0.0.1')