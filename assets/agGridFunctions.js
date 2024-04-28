var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

dagfuncs.Intl = Intl;

dagfuncs.FormatNumbersByRow = function(params) {
   if (isNaN(params.value)) {
        return params.value;
    }
    if (params.data["Val ID"] == "Hours Col") {
        return Intl.NumberFormat("en-US").format(params.value);
    }
    if (params.data["Val ID"] == "Value Col") {
        return Intl.NumberFormat("en-US", {
            style: "currency",
            currency: "USD",
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
          }).format(params.value);
    }
}

dagfuncs.cellEditorSelector = function(params) {
    if (["Text Col", "Year Col"].includes(params.data["Val ID"]))  {
        return {
            component: "agTextCellEditor",
        }
    }
    if (["Date Col"].includes(params.data["Val ID"]))  {
        return {
            component: "agDateStringCellEditor",
            params: {
                'useFormatter': true,
                'min': '2023-01-01',
                'max': '2040-12-31',
              },
        }
    }
    if (["Hours Col", "Value Col"].includes(params.data["Val ID"])) {
        return {
            component: "agNumberCellEditor",
        }
    }
    if (["Bool Col"].includes(params.data["Val ID"])) {
        return {
          component: 'agSelectCellEditor',
          params: {
            values: ['Yes', 'No'],
          },
          popup: true,
        };
    }
    if (params.data["Val ID"] == "AMSTAT Link") {
        return {
            component: React.createElement(
                'a',
                {href: params.value},
                "AMSTAT Link"
            )
        }
    }

    return undefined;
};


dagfuncs.testValue = (params) => {
    if (!params.newValue) {
        return false
    }
    params.data[params.column.colId] = params.newValue
    return true
}

