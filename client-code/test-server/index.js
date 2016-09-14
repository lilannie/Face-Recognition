var express = require('express');
var app = express();
var bodyParser = require('body-parser')

app.set('views', __dirname + '/../');
app.engine('html', require('ejs').renderFile);

var jsonParser       = bodyParser.json({limit:1024*1024*20, type:'application/json'});
var urlencodedParser = bodyParser.urlencoded({ extended:true,limit:1024*1024*20,type:'application/x-www-form-urlencoding' })

app.use(jsonParser);
app.use(urlencodedParser);

app.set('view engine', 'ejs');

app.post('/imgsave', function(req, res) {
		console.log(req.body);
		console.log("-- image --");
		res.render('client.html');
});

app.get('/', function(req, res) {
    res.render('client.html');
});

app.listen(8080, '127.0.0.1')