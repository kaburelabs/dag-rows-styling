var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.CreateLink = function (params) {
    if (params.data["Val ID"] == "Link Col") {
        return React.createElement(
            'a',
            {href: params.value, target:"_blank"},
            "Link redirect"
        );
    }
    return React.createElement(
        'div',
        {children: params.value}
    );
}