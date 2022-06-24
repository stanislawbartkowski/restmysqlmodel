var JS = {
  testableclickdelete: function (row) {
    return {
      listdef: "testtable_del",
      formprops: { initialValues: row },
    };
  },

  testableclickupdate: function (row) {
    return {
      listdef: "testtable_modif",
      formprops: { initialValues: row },
    };
  },

  getexpandorders: function (row) {
    return { list: "orderdetails", params: { ordernumber: row.ordernumber } };
  },
  
  notification: function(messid, row)  {
    return {
        kind: 'success',
        title: { message: 'done' },
        description: {
            message: messid ,
            params: [row.id]
        }
    }
  },

  testtabledelete: function (row) {
    return {
      restaction: "testtable-del",
      method: "DELETE",
      params: { id: row.id },
      notification: this.notification('youdeleted',row)
    };
  },

  inittestvals: function(row,vars) {
    console.log("initvals")
    console.log(vars)
    return vars
  },

  initteststeps: function(row) {
    var v = {}
    v.id = null
    v.name = "XXXXXXXX"
    v.descr = "<h3>Initialy set as empty and XXXXXX</h3> <br> Should retains new values after coming back from next step"
    return v
  },

  testtableupdate: function (row) {
    return {
      restaction: "testtable-modif",
      method: "PUT",
      params: { id: row.id, name: row.name },
      notification: this.notification('youupdated',row)
    };
  },

  getorderbadge : function(row) {
    var t = row.status
    var st = 'default'
    switch (t) {
      case 'Shipped' : st = 'success'; break;
      case 'In Process' : st = 'processing'; break;
      case 'Disputed' : st = 'warning'; break
      case 'Cancelled' : break;
      case 'Resolved' : st = 'success'; break;
      case 'On Hold': st = 'warning' ; break
    }
    return { 
      props : { status: st}
    }
  },

  productlineaction: function(row) {
    return {
      message: 'products', 
      list: 'productlineproducts', 
      params: { productline : row.productline },  
      modalprops: { width: "70%" }  } 
  },

  step3values: function(row,vars) {
    console.log("row:================")
    console.log(row)
    console.log("vars:===========")
    console.log(vars)
    return { next: true, vars: { pdescr: "Just adding new value" }}
  },

  step3doaction: function(row,vars) {
    return { next: true, vars: { pfinal: "<H1>Congratulations</H1>: it is done" }}
  },

  initteststeps3 : function(row) {
    var v = {}
    v.id = null
    v.name = "XXXXXXXX"
    v.descr = "<h3>Initialy set as empty and XXXXXX</h3> <br> Should retains new values after coming back from next step<h3>Another name is set in the second step and should also retain value"
    return v
  },

  initteststep32 : function(row) {
    var v = {}
    console.log("initteststep32")
    v.name1 = "YYYYYYYYYYYYY"
    return v
  }

};
