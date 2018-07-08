const Usersdb = require('../models/user');
const queried = require('../models/queried');

module.exports={
    updateuser(req, res){
        var insertArray = new Array();
         if(req.body.option1){
                    insertArray.push(req.body.option1)
                }
                if(req.body.option2){
                    insertArray.push(req.body.option2)
                }
                if(req.body.option3){
                    insertArray.push(req.body.option3)
                }
                if(req.body.option4){
                    insertArray.push(req.body.option4)
                }
                if(req.body.option5){
                    insertArray.push(req.body.option5)
                }
                if(req.body.option6){
                    insertArray.push(req.body.option6)
                }
                if(req.body.option7){
                    insertArray.push(req.body.option7)
                }
                if(req.body.option8){
                    insertArray.push(req.body.option8)
                }
                if(req.body.option9){
                    insertArray.push(req.body.option9)
                }
                if(req.body.option10){
                    insertArray.push(req.body.option10)
                }
                if(req.body.option11){
                    insertArray.push(req.body.option11)
                }
                if(req.body.option12){
                    insertArray.push(req.body.option12)
                }
                if(req.body.option13){
                    insertArray.push(req.body.option13)
                }
                if(req.body.option14){
                    insertArray.push(req.body.option14)
                }
                if(req.body.option15){
                    insertArray.push(req.body.option15)
                }
                if(req.body.option16){
                    insertArray.push(req.body.option16)
                }
            Usersdb.findOne({username: req.user.username}, function(err, toedit){
                    toedit.mealpreference = insertArray;
                    toedit.save(function(err){
                        if(err){console.log(err)}else{
                            queried.find({}).exec((err, cart)=>{
                                console.log(cart);
                                res.render('myprofile', {mycart: cart})
                            })
                            
                        }
 
         



    })
            })
    }
}
