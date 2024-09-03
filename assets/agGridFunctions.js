var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

dagfuncs.Intl = Intl;

dagfuncs.FormatNumbersByRow = function (params) {
    if (isNaN(params.value)) {
        return params.value;
    }
    if (params.data["Val ID"] == "Hours Col") {
        return Intl.NumberFormat("en-US").format(params.value);
    }
    if (params.data["Val ID"] == "Group Value 1") {
        return Intl.NumberFormat("en-US").format(params.value);
    }
    if (params.data["Val ID"] == "Group Value 2") {
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

dagfuncs.cellEditorSelector = function (params, list_vals) {

    if (["Text Col", "Year Col"].includes(params.data["Val ID"])) {
        return {
            component: "agTextCellEditor",
        }
    };
    if (["Date Col"].includes(params.data["Val ID"])) {
        return {
            component: "agDateStringCellEditor",
            params: {
                'useFormatter': true,
                'min': '2023-01-01',
                'max': '2040-12-31',
            },
        }
    };
    if (["Hours Col", "Value Col", "Group Value 1", "Group Value 2"].includes(params.data["Val ID"])) {
        return {
            component: "agNumberCellEditor",
        }
    };
    if (["Bool Col"].includes(params.data["Val ID"])) {
        return {
            component: 'agSelectCellEditor',
            params: {
                values: ['Yes', 'No'],
            },
            popup: true,
        };
    };
    if (["Options Col"].includes(params.data["Val ID"])) {
        return {
            component: 'agSelectCellEditor',
            params: {
                values: ['Option 1', 'Option 2', 'Other Option 1',
                    'Other Option 2', '3'],
            },
        };
    };
    return undefined;
};

function isFourDigits(value) {
    let fourDigitsRegex = /^\d{4}$/;
    return fourDigitsRegex.test(value);
}
function isBetween1950AndCurrentYear(value) {
    let currentYear = new Date().getFullYear();
    return value >= 1950 && value <= currentYear;
}

dagfuncs.testValue = (params) => {
    if (!params.newValue) {
        return false
    }
    if (params.data["Val ID"] == "Year Col") {
        let currentYear = new Date().getFullYear();
        // Check if the text is composed by 4 digits and the YEAR is between 1900 and 2022 
        if (!isFourDigits(params.newValue)) {
            return false
        }
        if (!isBetween1950AndCurrentYear(params.newValue)) {
            return false
        }
    }
    params.data[params.column.colId] = params.newValue
    return true
}

