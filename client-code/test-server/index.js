var express = require('express');
var app = express();
var bodyParser = require('body-parser')

app.set('views', __dirname + '/../');
app.engine('html', require('ejs').renderFile);

app.use(bodyParser.json({limit: '8mb'}));
app.use(bodyParser.urlencoded({limit: '8mb', extended: true}));

app.set('view engine', 'ejs');

app.post('/imgsave', function(req, res) {
		console.log(req.body);
		console.log("-- image --");
		res.render('client2.html');
});

app.get('/', function(req, res) {
    res.render('client2.html');
});

app.listen(8080, '127.0.0.1')