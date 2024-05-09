var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

function transformDateFormat(dateStr) {
    let dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateRegex.test(dateStr)) {
        // dateStr does not match the 'yyyy-mm-dd' format
        return dateStr;
    }
    let [year, month, day] = dateStr.split('-');
    let dateObj = new Date(year, month - 1, day);  // month is 0-indexed

    // Check if dateObj is a valid date
    if (isNaN(dateObj.getTime())) {
        // dateObj is not a valid date
        return null;
    }
    
    let monthShort = dateObj.toLocaleString('default', { month: 'short' });
    return `${day}-${monthShort}-${year}`;
}

dagcomponentfuncs.FormatSpecificCells = function (params) {
    if (params.data["Val ID"] == "Link Col") {
        return React.createElement(
            'a',
            {href: params.value, target:"_blank"},
            "Link redirect"
        );
    }
    if (["Date Col"].includes(params.data["Val ID"])) {
        let finalValue = transformDateFormat(params.value);
        return finalValue   
    }
    return params.formatValue(params.value);
}