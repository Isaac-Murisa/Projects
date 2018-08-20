db.useraccounts.insertOne({
    firstname: 'Isaac',
    lastname: 'Murisa',
    email: 'icm506@gmail.com',
    password: 'qwerty',
    contactphone: 7096310380,
    city: 'St. Johns',
    skillaccount: [{
        prefname: 'Isaacs Phototgraphy',
        category: 'Photography',
        description: 'This is just a test account nothing much. We are just testing',
        qualifications: 'Certificate in Phototgraphy',
        areacovered: ['St. johns', 'Mount Peral'],
        contactmethod: ['email', 'Phone'],
        accountactive: true,
        pricing: [{
            baseprice: 100,
            priceper: 'Day',
            paymentmethod: ['email'],
        }],
        availability: [{
            days: 'Monday',
            timefrom: '12.00pm',
            timeto: '12.00am',
            available: true
        }]
    }]
})