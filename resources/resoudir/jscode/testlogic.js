var TS = {

    afterid: function (row, vars) {
        return {
            action: "YESNO",
            messid: {
                localize: false,
                messid: "Do you want stay at id ?"
            },
            confirm: {
                action: "FORM",
                formaction: "NO"
            }
        }
    }
}