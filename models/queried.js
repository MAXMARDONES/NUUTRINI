const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const query = new Schema({
    name: {type: String},
    img: {type: String},
    price: {type: String}
});

module.exports = mongoose.model('queried', query)

