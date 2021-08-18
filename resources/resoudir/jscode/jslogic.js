var JS = {
    clickcustomerpayments: function (row) {
        return {
            "action": "POPUP",
            "restid": "customerpayments",
            "pars": {
                "customernumber": row.customernumber
            },
            "vars": row
        }
    },

    clickcustomerorders: function (row) {
        return {
            "action": "POPUP",
            "restid": "customerorders",
            "pars": {
                "customernumber": row.customernumber
            },
            "vars": row
        }
    },

    customerpaymenttitle: function (row) {

        return { "messid": "customerpaymentstitle", "params": [row.customernumber, row.customername, row.contactfirstname, row.contactlastname] };

    },

    customerordertitle: function (row) {
        return { "messid": "customerorderstitle", "params": [row.customernumber, row.customername, row.contactfirstname, row.contactlastname] };
    }
}