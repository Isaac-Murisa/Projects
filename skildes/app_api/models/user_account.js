var mongoose = require( 'mongoose' );

var availabilitySchema = new mongoose.Schema({ 
    days: { type: String, required: true},
    timefrom: String,
    timeto: String,
    available: { type: Boolean, required: true}
});

var pricingSchema = new mongoose.Schema({ 
    baseprice: Number,
    priceper: String,
    otherexpenses: [String],
    additionalcharges: String,
    paymentmethod: [String],
    additionalcomments: String
});

var skillaccountSchema = new mongoose.Schema({ 
    prefname: String,
    category: String,
    description: String,
    qualifications: String,
    areacovered: [String],
    contactmethod: [String],
    accountactive: { type: Boolean, required: true},
    pricing: [pricingSchema],
    coords: {type: [Number], index: '2dsphere'},
    availability: [availabilitySchema]
});
var user_accountSchema = new mongoose.Schema({ 
    firstname: String,
    lastname: String,
    email: String,
    password: String,
    contactphone: Number,
    city: String,
    acc_coords: {type: [Number], index: '2dsphere'},
    skillaccount: [skillaccountSchema]
});

mongoose.model('UserAccount', user_accountSchema, 'useraccounts');
