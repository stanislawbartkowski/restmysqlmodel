var JS = {
  //antd
  testableclickdelete: function (row) {
    return {
      listdef: "testtable_del",
      formprops: { initialValues: row },
    };
  },

  //antd
  testableclickupdate: function (row) {
    return {
      listdef: "testtable_modif",
      formprops: { initialValues: row },
    };
  },

  // antd
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

  // antd
  testtabledelete: function (row) {
    return {
      restaction: "testtable-del",
      method: "DELETE",
      params: { id: row.id },
      notification: this.notification('youdeleted',row)
    };
  },

  // antd
  testtableupdate: function (row) {
    return {
      restaction: "testtable-modif",
      method: "PUT",
      params: { id: row.id, name: row.name },
      notification: this.notification('youupdated',row)
    };
  },
};
