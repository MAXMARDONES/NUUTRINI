const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const category = new Schema({
    name: {type: String},
    imgpath: {type: String}
});

module.exports = mongoose.model('categories', category)
