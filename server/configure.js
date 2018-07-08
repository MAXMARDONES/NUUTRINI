const path = require('path'),
	routes = require('./routes'),
	express = require('express'),
	bodyParser = require('body-parser'),
	morgan = require('morgan'),
	exphbs = require('express-handlebars'),
	methodOverride = require('method-override'),
	errorHandler = require('errorhandler'),
	moment = require('moment'),
	multer = require('multer'),
	mongoose = require('mongoose'),
	nodemailer = require('nodemailer')

//



module.exports = (app) =>{
	app.use(morgan('dev'));
	app.use(multer({
		dest: path.join(__dirname, '../public/img/advertisements')
	}).single('file'));
	app.use(bodyParser.urlencoded({'extended': true}));
	app.use(bodyParser.json());
	app.use(methodOverride());
	routes(app);//moving the routes to routes folder.
	app.use('/public/', express.static(path.join(__dirname, '../public')));
	


	if('development' === app.get('env')){
		app.use(errorHandler());
	}
		routes(app);
		app.engine('hbs', exphbs.create({
			defaultLayout: 'main',
			extname: '.hbs',
			layoutsDir: app.get('views') + '/layouts',
        	partialsDir: [app.get('views') + '/partials'],
			helpers: {
				timeago: (timestamp) => {
					return moment(timestamp).startOf('minute').fromNow();
				}
			}
		}).engine);

		app.set('view engine', '.hbs');
		//app.set('views', path.join(__dirname, 'views'));

		return app;
	};
