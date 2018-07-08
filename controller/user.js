const userModel = require('../models/user');
const routes = require('../server/routes')

module.exports = {
    create(req, res){
        var m2 = parseFloat(req.body.height)*parseFloat(req.body.height);
        var weight = parseFloat(req.body.weight);
        var BMI = weight/m2;
        const userinsert = new userModel({
            name: req.body.firstname,
            lastname: req.body.lastname,
            username: req.body.username,
            password: req.body.password[0],
            gender: req.body.gender,
            email: req.body.email,
            height: req.body.height,
            weight: req.body.weight,
            bmi: parseInt(BMI)
        })
        userinsert.save();
        res.redirect('/')
        

    }

}