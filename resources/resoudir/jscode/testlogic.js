var TS = {

    afterid: function (row, vars) {
    return {
      action: "RESTPOST",
      restid: "testtable_afterid",
    };
  },

  deletedata: function (row, vars) {
    return {
      action: "YESNO",
      messid: "delrecordask",
      confirm: {
        action: "RESTGET",
        restid: "testtable-del",
        pars: {
          id: row.id,
        },
      },
    };
  },

  modifdata: function (row, vars) {
    return {
      action: "YESNO",
      messid: "changerecordask",
      confirm: {
        action: "RESTGET",
        restid: "testtable-modif",
        pars: {
          name: row.name,
          id: row.id,
        },
      },
    };
  },
};
