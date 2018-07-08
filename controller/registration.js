const users = require('../models/user');

module.exports={

    main(req, res){
        res.render('registration')
    },
    new(req, res){
        var newUser = new users({
            name: req.body.name,
            lastname: req.body.lastname,
            email: req.body.email,
            height: req.body.height,
            weight: req.body.weight,
            password: req.body.password[0]
        })
        newUser.save();
        console.log(newUser);
        res.redirect('/myprofile')
    }
}