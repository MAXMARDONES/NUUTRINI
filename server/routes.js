//MODULES
const express = require('express'),
	router = express.Router(),
	nodemailer = require('nodemailer'),
	multer = require('multer'),
	jwt = require('jsonwebtoken'),
	nodemon = require('nodemon'),
	passport = require('passport'),
	LocalStrategy = require('passport-local').Strategy,
	expressValidator = require('express-validator'),
	path = require('path'),
	fs = require('fs');

//CONTROLLERS
const index = require('../controller/index');
const myprofile = require('../controller/myprofile');
const registration = require('../controller/registration');
const Usercontroller = require('../controller/user');
const firststeps = require('../controller/firststeps');
const ratings = require('../controller/ratings');

//MODELS

const User = require('../models/user');
const queried = require('../models/queried');



passport.serializeUser((user, done) =>{
	done(null, user.id)
});

passport.deserializeUser((id, done) => {
	User.getUserById(id, (err, user) => {
		done(err, user);
	});
});


module.exports = (app) => {
    router.use(expressValidator());
    passport.use(new LocalStrategy(
		function(username, password, done){
			User.getUserByUsername(username, (err, user) => {
				if(err) throw err;
				if(!user){
					return done(null, false, {message: 'Unknown User'});
				}
				User.comparePassword(password, user.password, function(err, isMatch){
					if(err) throw err;
					if(isMatch){
						return done(null, user);
					}else{
						return done(null, false, {message: 'Invalid Password'});
					}
				})
			})
		}
	));
    //INDEX
    router.get('/', index.main);


    //PROFILE
    router.get('/myprofile', myprofile.main);

    router.get('/register', registration.main);

	router.post('/login', passport.authenticate('local', {successRedirect: 'myprofile', failureRedirect: '/'}))

    //REGISTER
    router.post('/register', Usercontroller.create);


	//FIRST STEPS
	router.get('/firststeps', firststeps.main);

	//RATINGS
	router.get('/ratings', (req, res)=>{
		res.render('ratings')
	})

	router.get('/cart', (req,res)=>{
		queried.find({}).exec((err, cartone)=>{
			res.render('cart', {mycart: cartone} )
		})
		
	})

	router.post('/submitratings', ratings.updateuser)

	//LOGOUT
	router.get('/logout', (req, res) => {
		req.logout();
		queried.find({}).exec((err, query)=>{
			console.log(query);
			res.render('myprofile', {mycart: query});
		})
		
	});




    app.use(router);
};