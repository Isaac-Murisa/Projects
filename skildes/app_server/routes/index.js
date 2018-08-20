var express = require('express');
var router = express.Router();
var ctrlMain = require('../controllers/main');

/* GET home page. */
router.get('/', ctrlMain.main);

router.get('/login', ctrlMain.login);

router.get('/signUp', ctrlMain.signup);

router.get('/category', ctrlMain.category);
router.get('/photography', ctrlMain.category);
router.get('/creative-and-design', ctrlMain.category);
router.get('/planning-and-organisation', ctrlMain.category);
router.get('/culinary', ctrlMain.category);
router.get('/other-skills', ctrlMain.category);

router.get('/console', ctrlMain.console);

router.get('/createskill', ctrlMain.createSkill);

router.get('/editprofile', ctrlMain.editProfile);

router.get('/editskill', ctrlMain.editSkill);

router.get('/profile', ctrlMain.profile);

module.exports = router;
