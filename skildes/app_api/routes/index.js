var express = require('express');
var router = express.Router();
var ctrlUsrAccount = require('../controllers/useraccounts');

//categories
router.get('/photography', ctrlUsrAccount.listPhotography);
router.get('/creative', ctrlUsrAccount.listCreative);
router.get('/culinary', ctrlUsrAccount.listCulinary);
router.get('/planning', ctrlUsrAccount.listPlanning);
router.get('/other', ctrlUsrAccount.listOther);

//User Accounts
router.post('/createskill', ctrlUsrAccount.createSkill);
router.post('/createAccount', ctrlUsrAccount.createAccount);
router.get('/profile/:profileid', ctrlUsrAccount.readProfile);
router.put('/editskill/:profileid/:skillid', ctrlUsrAccount.updateSkill);
router.put('/editprofile/:profileid', ctrlUsrAccount.updateProfile);
router.delete('/console/:profileid', ctrlUsrAccount.deleteProfile);
router.delete('/console/:profileid/:skillid', ctrlUsrAccount.deleteSkill);
router.get('/console/:profileid', ctrlUsrAccount.console );

module.exports = router;