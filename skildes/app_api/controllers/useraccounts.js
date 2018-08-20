var mongoose = require('mongoose');
var Usr = mongoose.model('UserAccount');

var theEarth = (function(){
    var earthRadius = 6371; // km, miles is 3959
    var getDistanceFromRads = function(rads) {
        return parseFloat(rads * earthRadius);
    };
    var getRadsFromDistance = function(distance) {
        return parseFloat(distance / earthRadius);
    };
    return {
        getDistanceFromRads : getDistanceFromRads,
        getRadsFromDistance : getRadsFromDistance
    };
})();

var sendJsonResponse = function(res, status, content) {
    res.status(status);
    res.json(content);
};

module.exports.createSkill = function (req, res) {
    var profileid = req.params.profileid;
    if (profileid){
        Usr 
            .findById(profileid)
            .select('skillaccount')
            .exec(
                function (err, useraccount){
                    if (err) {
                        sendJsonResponse(res, 404, err);
                    }
                    else {
                        doAddReview(req, res, useraccount);
                    }
                }
            );
    }
    else {
        sendJsonResponse(res, 404, {
            "message":"Profileid not found"
        });
    }
};

var doAddReview = function(req, res, useraccount){
    if (!useraccount) {
        sendJsonResponse(res, 404, {
            "message":"No profile id found"
        });
    }
    else {
        useraccount.skillaccount.push({
            prefname: req.body.prefname,
            category: req.body.category,
            description: req.body.description,
            qualifications: req.body.qualifications,
            areacovered: req.body.areacovered,
            contactmethod: req.body.contactmethod,
            accountactive: req.body.accountactive,
            pricing: req.body.pricing,
            coords: [parseFloat(req.body.lng),
                parseFloat(req.body.lat)],
            availability: req.body.coords
        });
        useraccount.save( function(err, useraccount){
            if (err) {
                sendJsonResponse(res, 404, err);
            }
            else {
                sendJsonResponse(res, 204, useraccount);
            }
        });
    }
};

module.exports.createAccount = function (req, res) {
    Usr.create({
        firstname: req.body.firstname,
        lastname: req.body.lastname,
        email: req.body.email,
        password: req.body.password,
        contactphone: req.body.contactphone,
        city: req.body.city,
        acc_coords: [parseFloat(req.body.lng),
            parseFloat(req.body.lat)]
    }, 
    function(err, useraccount) {
        if (err) {
            sendJsonResponse(res, 400, err);
        } 
        else {
            sendJsonResponse(res, 201, useraccount);
        }
    });
};

module.exports.readProfile = function (req, res) {
    if (req.params && req.params.profileid) {
        Usr
            .findById(req.params.profileid)
            .exec(function(err, useraccount) {
                if (!useraccount) {
                    sendJsonResponse(res, 404, {
                        "message": "profileid not found"
                    });
                    return;
                }
                else if(err) {
                    sendJsonResponse(res, 404, err);
                    return;
                }
                sendJsonResponse(res, 200, useraccount);
            });
    }
    else {
        sendJsonResponse(res, 404, {
            "message": "No profileid in request"
        });
    }
};

module.exports.updateSkill = function (req, res) {
    if (!req.params.profileid) {
        sendJsonResponse(res, 404, {
            "message": "Not found, locationid is required"
        });
        return;
    }
    Usr
        .findById(req.params.profileid)
        .select('skillaccount')
        .exec(
            function(err, useraccount){
                if (!useraccount) {
                    sendJsonResponse(res, 404, {
                        "message": "profileid not found"
                    });
                    return;
                } 
                else if (err) {
                    sendJsonResponse(res, 400, err);
                    return;
                }
                
                thisSkill = useraccount.skillaccount.id(req.params.skillid);
                if (!thisSkill){
                    sendJsonResponse(res, 404, {
                        "message":"Skill account not found"
                    });
                }
                else {
                    thisSkill.prefname = req.body.prefname;
                    thisSkill.category = req.body.category;
                    thisSkill.description = req.body.description;
                    thisSkill.qualifications = req.body.qualifications;
                    thisSkill.areacovered = req.body.areacovered;
                    thisSkill.contactmethod = req.body.contactmethod;
                    thisSkill.accountactive = req.body.accountactive;
                    thisSkill.pricing = req.body.pricing;
                    thisSkill.coords = [parseFloat(req.body.lng),
                        parseFloat(req.body.lat)];
                    thisSkill.availability = req.body.coords;

                    useraccount.save(function (err, useraccount) {
                        if (err){
                            sendJsonResponse(res, 404, err);
                        }
                        else {
                            sendJsonResponse(res, 200, useraccount);
                        }
                    });
                }
                
            }
        );
};

module.exports.updateProfile = function(res, req) {
    if (!req.params.profileid) {
        sendJsonResponse(res, 404, {
            "message": "Not found, locationid is required"
        });
        return;
    }
    Usr
        .findById(req.params.profileid)
        .exec(
            function(err, useraccount){
                useraccount.firstname = req.body.firstname;
                useraccount.lastname = req.body.lastname;
                useraccount.email = req.body.email;
                useraccount.password = req.body.password;
                useraccount.contactphone = req.body.contactphone;
                useraccount.city = req.body.city;
                useraccount.acc_coords = [parseFloat(req.body.lng),
                    parseFloat(req.body.lat)];

                useraccount.save(function (err, useraccount) {
                    if (err){
                        sendJsonResponse(res, 404, err);
                    }
                    else {
                        sendJsonResponse(res, 200, useraccount);
                    }
                });
            }
        );
};

module.exports.deleteProfile = function (req, res) {
    var profileid = req.params.profileid;
    if (profileid) {
        Usr
            .findByIdAndRemove(profileid)
            .exec(
                function (err, useraccount){
                    if (err) {
                        sendJsonResponse(res, 404, err);
                        return;
                    }
                    sendJsonResponse(res, 204, null);
                }
            );
    }
    else {
        sendJsonResponse(res, 404, {
            "message":"No profile id"
        });
    }
};

module.exports.deleteskill = function (req, res){
    if ( !req.params.profileid ) {
        sendJsonResponse( res, 404 , {
            "message":"No profileid"
        });
        return;
    }
    Usr 
        .findById(req.params.profileid)
        .select('skillaccount')
        .exec(
            function(err, useraccount){
                if(!useraccount){
                    sendJsonResponse(res, 404, {
                        "message":"No profile found, profile id"
                    });
                    return;
                }
                else if (err){
                    sendJsonResponse(res, 404, err);
                    return;
                }

                if (!useraccount.skillaccount.id(req.params.skillid)){
                    sendJsonResponse(res, 404, {
                        "message":"No Skill account"
                    });
                }
                else {
                    useraccount.skillaccount.id(req.params.skillid).remove();
                    useraccount.save(function(err){
                        if (err) {
                            sendJsonResponse(res, 404, err);
                        }
                        else {
                            sendJsonResponse(res, 204, null);
                        }
                    });
                }
            }
        );
};

module.exports.console = function (req, res){
    
};

module.exports.listPhotography = function (req, res) {
    Usr 
        .find( { skillaccount: {$elemMatch: {category: "Photography"} } } )
        .exec(function(err, useraccount) {
            var p_list = [];
            if (!err) {
                sendJsonResponse(res, 404, err);
                return;
            }
            else if(!useraccount){
                sendJsonResponse(res, 404, {
                    "message": "No entry in category"
                });
                return;
            }
            useraccount.forEach(function(doc) {
                p_list.push({
                    prefname: doc.obj.prefname,
                    category: doc.obj.category,
                    description: doc.obj.description,
                    areacovered: doc.obj.areacovered,
                    contactmethod: doc.obj.contactmethod,
                    accountactive: doc.obj.accoountactive,
                    pricing: doc.obj.pricing,
                    coords: doc.obj.coords,
                    availability: doc.obj.availability
                });
            });
        });

};

module.exports.listCreative = function (req, res) {
    Usr 
        .find( { skillaccount: {$elemMatch: {category: "Creative and Design"} } } )
        .exec(function(err, useraccount) {
            var cre_list = [];
            if (!err) {
                sendJsonResponse(res, 404, err);
                return;
            }
            else if(!useraccount){
                sendJsonResponse(res, 404, {
                    "message": "No entry in category"
                });
                return;
            }
            useraccount.forEach(function(doc) {
                cre_list.push({
                    prefname: doc.obj.prefname,
                    category: doc.obj.category,
                    description: doc.obj.description,
                    areacovered: doc.obj.areacovered,
                    contactmethod: doc.obj.contactmethod,
                    accountactive: doc.obj.accoountactive,
                    pricing: doc.obj.pricing,
                    coords: doc.obj.coords,
                    availability: doc.obj.availability
                });
            });
        });
};

module.exports.listCulinary = function (req, res) {
    Usr 
        .find( { skillaccount: {$elemMatch: {category: "Culinary"} } } )
        .exec(function(err, useraccount) {
            var cul_list = [];
            if (!err) {
                sendJsonResponse(res, 404, err);
                return;
            }
            else if(!useraccount){
                sendJsonResponse(res, 404, {
                    "message": "No entry in category"
                });
                return;
            }
            useraccount.forEach(function(doc) {
                cul_list.push({
                    prefname: doc.obj.prefname,
                    category: doc.obj.category,
                    description: doc.obj.description,
                    areacovered: doc.obj.areacovered,
                    contactmethod: doc.obj.contactmethod,
                    accountactive: doc.obj.accoountactive,
                    pricing: doc.obj.pricing,
                    coords: doc.obj.coords,
                    availability: doc.obj.availability
                });
            });
        });
};

module.exports.listPlanning = function (req, res) {
    Usr 
        .find( { skillaccount: {$elemMatch: {category: "Planning and Organisation"} } } )
        .exec(function(err, useraccount) {
            var org_list = [];
            if (!err) {
                sendJsonResponse(res, 404, err);
                return;
            }
            else if(!useraccount){
                sendJsonResponse(res, 404, {
                    "message": "No entry in category"
                });
                return;
            }
            useraccount.forEach(function(doc) {
                org_list.push({
                    prefname: doc.obj.prefname,
                    category: doc.obj.category,
                    description: doc.obj.description,
                    areacovered: doc.obj.areacovered,
                    contactmethod: doc.obj.contactmethod,
                    accountactive: doc.obj.accoountactive,
                    pricing: doc.obj.pricing,
                    coords: doc.obj.coords,
                    availability: doc.obj.availability
                });
            });
        });
};

module.exports.listOther = function (req, res) {
    Usr 
        .find( { skillaccount: {$elemMatch: {category: "Other"} } } )
        .exec(function(err, useraccount) {
            var oth_list = [];
            if (!err) {
                sendJsonResponse(res, 404, err);
                return;
            }
            else if(!useraccount){
                sendJsonResponse(res, 404, {
                    "message": "No entry in category"
                });
                return;
            }
            useraccount.forEach(function(doc) {
                oth_list.push({
                    prefname: doc.obj.prefname,
                    category: doc.obj.category,
                    description: doc.obj.description,
                    areacovered: doc.obj.areacovered,
                    contactmethod: doc.obj.contactmethod,
                    accountactive: doc.obj.accoountactive,
                    pricing: doc.obj.pricing,
                    coords: doc.obj.coords,
                    availability: doc.obj.availability
                });
            });
        });
};