/* GET home page */
module.exports.index = function(req, res){
    res.render('index', { title: 'Express', message: 'Hello There, Just texting'});
};

module.exports.login = function(req, res){
    res.render('login');
};

module.exports.signup = function(req, res){
    res.render('signup');
};

module.exports.main = function(req, res){
    res.render('main');
};

module.exports.category = function(req, res){
    res.render('category');
};

module.exports.profile = function(req, res){
    res.render('profile');
};

module.exports.createSkill = function(req, res){
    res.render('createskill');
};

module.exports.editSkill = function(req, res){
    res.render('editskill');
};

module.exports.editProfile = function(req, res){
    res.render('editprofile');
}

module.exports.console = function(req, res){
    res.render('console');
};

