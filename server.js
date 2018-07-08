const express = require('express');
const config = require('./server/configure');
const mongoose = require('mongoose');
const flash = require('connect-flash');
const passport = require('passport'),
session = require('express-session'),
LocalStrategy = require('passport-local').Strategy,
ExpressValidator = require('express-validator');

var app = express()

app.use(session({
		secret: 'secret',
		saveUninitialized: true,
		resave: true
	}));

app.use(passport.initialize());
app.use(passport.session());

app.use(ExpressValidator({
		errorFormatter: function(param, msg, value){
			var namespace = param.split('.'),
			root = namespace.shift(),
			formParam = root;

			while(namspace.length){
				formParam += '[' + namespace.shift() + ']';
			}return{
				param: formParam,
				msg: msg,
				value: value
			};
		}
	}));

app.use(flash());

app.use((req, res, next) => {
  res.locals.success_msg = req.flash('success_msg');
  res.locals.error_msg = req.flash('error_msg');
  res.locals.error = req.flash('error');
  res.locals.login_err_msg = req.flash('login_err_msg');
  res.locals.user = req.user || null;
  next();
});



app.set('port', process.env.PORT || 3300);
app.set('Views', `${__dirname}/Views`);

app = config(app);

mongoose.connect('mongodb://nuutrini:nuutrini123@ds125831.mlab.com:25831/nuutrini');

mongoose.connection.on('open', ()=>{
  console.log('Mongoose connected');
});

app.listen(app.get('port'), ()=>{
  console.log(`Server up: http://localhost:${app.get('port')}`);
});