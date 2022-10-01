var JS = {
  testableclickdelete: function (row) {
    return {
      listdef: "demo/crud/testtable_del",
      formprops: { initialValues: row },
    };
  },

  testableclickupdate: function (row) {
    return {
      listdef: "demo/crud/testtable_modif",
      formprops: { initialValues: row },
    };
  },

  getexpandorders: function (row) {
    return { list: "orderdetails", params: { ordernumber: row.ordernumber } };
  },

  notification: function (messid, row) {
    return {
      kind: 'success',
      title: { message: 'done' },
      description: {
        message: messid,
        params: [row.id]
      }
    }
  },

  testtabledelete: function (row) {
    return {
      restaction: "demo/crud/testtable-del",
      method: "DELETE",
      params: { id: row.id },
      notification: this.notification('youdeleted', row),
      retprops: { close: true, refresh: true }
    };
  },

  inittestvals: function (row, vars) {
    console.log("initvals")
    console.log(vars)
    return vars
  },

  initteststeps: function (row) {
    var v = {}
    v.id = null
    v.name = "XXXXXXXX"
    v.descr = "<h3>Initialy set as empty and XXXXXX</h3> <br> Should retains new values after coming back from next step"
    return v
  },

  testtableupdate: function (row) {
    return {
      restaction: "demo/crud/testtable-modif",
      method: "PUT",
      params: { id: row.id, name: row.name },
      notification: this.notification('youupdated', row),
      retprops: { close: true, refresh: true }
    };
  },

  getorderbadge: function (row) {
    var t = row.status
    var st = 'default'
    switch (t) {
      case 'Shipped': st = 'success'; break;
      case 'In Process': st = 'processing'; break;
      case 'Disputed': st = 'warning'; break
      case 'Cancelled': break;
      case 'Resolved': st = 'success'; break;
      case 'On Hold': st = 'warning'; break
    }
    return {
      props: { status: st }
    }
  },

  productlineaction: function (row) {
    return {
      message: 'products',
      list: 'productlineproducts',
      params: { productline: row.productline },
      modalprops: { width: "70%" }
    }
  },

  step3values: function (row, vars) {
    console.log("row:================")
    console.log(row)
    console.log("vars:===========")
    console.log(vars)
    return { next: true, vars: { pdescr: "Just adding new value" } }
  },

  step3doaction: function (row, vars) {
    return { next: true, vars: { pfinal: "<H1>Congratulations</H1>: it is done<h3>Warning: it is test only, nothing is added or changed</h3>" } }
  },

  initteststeps3: function (row) {
    var v = {}
    v.id = null
    v.name = "XXXXXXXX"
    v.descr = "<h3>Initialy set as empty and XXXXXX</h3> <br> Should retains new values after coming back from next step<h3>Another name is set in the second step and should also retain value"
    return v
  },

  initteststep32: function (row) {
    var v = {}
    console.log("initteststep32")
    v.name1 = "YYYYYYYYYYYYY"
    return v
  },

  teststepstep1: function (row) {
    var v = {}
    console.log("teststepstep1")
    console.log(row)
    v.next = true
    v.vars = {
      name1: "name:" + row.name + "!"
    }
    return v
  },

  testvarsinitstep1: function (row, vars) {
    var v = this.inittestvals(row, vars)
    v.name1 = "Hello, I'm name1"
    v.id = null
    return v
  },

  multidescrgetvalue: function (row) {
    var l = row.idchoice
    console.log(l)
    if (l === undefined) return { value: "<h3>nothing is chosen</h3>" }
    var s = "<ui>"
    for (var i = 0; i < l.length; i++) s = s + "<ul>" + l[i] + "</ul>"
    return { value: s + "</ui>" }
  },

  getlistadef: function (row) {
    return {
      list: "orders",
      listdef: "ordersin",
      props: {
        style: {
          width: "80%"
        }
      }
    }
  },

  onchangename: function (row) {
    console.log(row);
    return { vars: { xname: row.name, lista: 1 } }
  }

};
