const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const userDB = new Schema({
    name: {type: String},
    lastname: {type: String},
    username: {type: String},
    password: {type: String},
    weight: {type: String},
    email: {type: String},
    gender: {type: String},
    age: {type: String},
    height: {type: String},
    bmi: {type: String},
    mealpreference: {type: Array},
    family: {type: Array}

});

var User = module.exports = mongoose.model('users', userDB);

module.exports.getUserByUsername = function(username, callback){
    var query = {username: username};
    User.findOne(query, callback);
}

module.exports.comparePassword = function(candidatePassword, realPassword, callback){
  if(candidatePassword===realPassword){
    callback(null, true);
  }
}

module.exports.getUserById = function(id, callback){
  User.findById(id, callback);
}