var JS = {

  // test table supporting methods  
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

  testtabledelete: function (row) {
    return {
      restaction: "demo/crud/testtable-del",
      method: "DELETE",
      params: { id: row.id },
      notification: this.notification('youdeleted', row),
      retprops: { close: true, refresh: true }
    };
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

  testvarsinitstep1: function (row, vars) {
    var v = this.inittestvals(row, vars)
    v.name1 = "Hello, I'm name1"
    v.id = null
    return v
  },

  // ==========

  getexpandorders: function (row) {
    return {
      list: "orderdetails",
      params: { ordernumber: row.ordernumber },
      props: {
        style: {
          boxShadow: '0 0 10px rgba(0, 0, 0, 0.3)',
          margin: "1px"
        }
      }
    };
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
      listdef: "demo/listinthedialog/ordersin",
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
  },

  getvalue1sum: function (row, vars, t) {
    return { value: vars.sum1 }
  },

  getvalue2sum: function (row, vars, t) {
    return { value: vars.sum2 }
  },

  getbalance: function (sum1, sum2) {
    return (sum1 <= sum2) ? {} : { value: (sum1 - sum2) }
  },

  getvalue1balance: function (row, vars) {
    return this.getbalance(vars.sum1, vars.sum2)
  },

  getvalue2balance: function (row, vars) {
    return this.getbalance(vars.sum2, vars.sum1)
  },

  onchangeval1: function (row, vars) {
    console.log(row)
    console.log(vars)
  },

  geteditbadge: function (row, vars) {
    var rowkey = row.rowkey
    var st = 'default'
    if (rowkey == 0) st = 'warning'
    return {
      props: { status: st }
    }

  },

  getedittags: function (row, vars) {
    var res = []
    res.push({
      value: { messagedirect: row.name }, props: { color: "green" }
    })
    return res
  },

  editchangename: function (row, vars) {
    console.log('editchangename')
    console.log(row)
    console.log(vars)
    return {}
  },

  editinsertline: function (row, vars) {
    console.log('editinsertline')
    console.log(row)
    console.log(vars)
    console.log('---------------')
    return { jsclick: "JS.xxinsertline" }
  },

  xxinsertline: function (row, vars) {
    console.log('xxxinsertline')
    console.log(row)
    console.log(vars)
    console.log('---------------')
    var r = row.listitems
    r.push({})
    console.log(r)
    return { vars: { listitems: r } }
  },

  onchangefieldaction: function (row) {
    return {
      vars: {
        infoname: "hello",
      },
      retprops: {
        listdef: "demo/dialog-wew",
        vars: {
          infodial: "cccccc"
        }
      }

    }
  },

  dialogwewok: function (row) {
    return {
      close: true,
      vars: {
        infodial: "cccccc"
      }
    }
  },

  getautoavalues: function (row) {
    return {
      res: [
        { name: "A1" },
        { name: "A2" },
        { name: "A2" },
        { name: "A3" },
        { name: "A4" },
        { name: "B1" },
        { name: "B2" },
        { name: "B2" },
        { name: "B3" },
        { name: "B4" },
      ]
    }
  }

};
