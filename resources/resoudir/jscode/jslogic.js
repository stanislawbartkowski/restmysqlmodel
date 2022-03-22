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
    },

    productlineproductstitle: function (row) {
        return { "messid": "productlineproductstitle", "params": [row.productline, row.textdescription] };
    },

    clickproductlineproducts: function (row) {
        return {
            "action": "POPUP",
            "restid": "productlineproducts",
            "pars": {
                "productline": row.productline
            },
            "vars": row
        }

    },

    // antd
    getexpandorders : function(row) {
      return { list: 'orderdetails', params: { "ordernumber" : row.ordernumber}}
    }
     
}