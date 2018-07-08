const products = require('../models/product');
const queried = require('../models/queried');

module.exports={
    main(req, res){
    console.log(req.user);
    products.find({}).exec((err, product)=>{
        queried.find({}).exec((err, query)=>{
            console.log(req.user)
            res.render('myprofile', {product: product, user: req.user, mycart: query});
        })
        

    })
        
        
    }
}