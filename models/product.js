const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const product = new Schema({
    name: {type: String},
    company: {type: String},
    price: {type: String},
    image: {type: String},
    quantity: {type: String},
    value: {type: Number}
});

module.exports = mongoose.model('products', product);