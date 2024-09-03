import dash
from dash import html, Dash, Output, Input, State, dcc
import dash_ag_grid as dag
import pandas as pd
import dash_mantine_components as dmc

list_of_vals = [
    {
        "Val ID": "Item 001",
        "Year Col": "2017",
        "Hours Col": 1253.0,
        "Value Col": 31950000.0,
        "Text Col": "testing a random text which is long enough to wrap",
        "Bool Col": "No",
        "Options Col": "OPTION 1",
        "Long List Col": "option 78",
        "Country Col": "United States",
        "Date Col": "2024-01-02",
        "Link Col": "https://www.google.com",
        "Value 1": 5,
        "Value 2": 7,
        "Sum Total": None,
    },
    {
        "Val ID": "Item 002",
        "Year Col": "2016",
        "Hours Col": 2541.0,
        "Value Col": 29995000.0,
        "Text Col": "testing a random text which is long enough to wrap",
        "Bool Col": "Yes",
        "Options Col": "OTHER OPTION 2",
        "Long List Col": "option 30",
        "Country Col": "Canada",
        "Date Col": "2024-03-02",
        "Link Col": "https://www.google.com",
        "Value 1": 5,
        "Value 2": 7,
        "Sum Total": None,
    },
    {
        "Val ID": "Item 003",
        "Year Col": "2019",
        "Hours Col": 566.0,
        "Value Col": 34900000.0,
        "Text Col": "testing a random text which is long enough to wrap",
        "Bool Col": "No",
        "Options Col": "OPTION 2",
        "Long List Col": "option 1",
        "Country Col": "China",
        "Date Col": "2024-01-10",
        "Link Col": "https://www.google.com",
        "Value 1": 5,
        "Value 2": 7,
        "Sum Total": None,
    },
    {
        "Val ID": "Item 004",
        "Year Col": "2013",
        "Hours Col": 2732.0,
        "Value Col": 26000000.0,
        "Text Col": "testing a random text which is long enough to wrap",
        "Bool Col": "Yes",
        "Options Col": "OPTION 1",
        "Long List Col": "option 8",
        "Country Col": "Brazil",
        "Date Col": "2024-10-02",
        "Link Col": "https://www.google.com",
        "Value 1": 5,
        "Value 2": 7,
        "Sum Total": None,
    },
    {
        "Val ID": "Item 005",
        "Year Col": "2018",
        "Hours Col": 1543.0,
        "Value Col": 31500000.0,
        "Text Col": "testing a random text which is long enough to wrap",
        "Bool Col": "Yes",
        "Options Col": "OTHER OPTION 1",
        "Long List Col": "option 15",
        "Country Col": "France",
        "Date Col": "2024-01-01",
        "Link Col": "https://www.google.com",
        "Value 1": 5,
        "Value 2": 7,
        "Sum Total": None,
    },
]

df = pd.DataFrame(list_of_vals)
df = df.set_index("Val ID").T
df = df.reset_index().rename(columns={"index": "Val ID"})
data_list = [item for item in df.to_dict(orient="records")]
columns_list = list(df.columns)

app = Dash()

def get_country_values():
    return {"long_list_options": [f"option {n}" for n in range(2000)], "country":[
        "Afghanistan",
        "Aland Islands",
   
        "Bahamas",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia",
        "Bonaire, Sint Eustatius and Saba",
        "Bosnia and Herzegovina",
        "Botswana",
        "Bouvet Island",
        "Brazil",
        "British Indian Ocean Territory",
        "Cayman Islands",
        "Chile",
        "China",
        "Egypt",
        "Equatorial Guinea",
        "Fiji",
        "Finland",
        "France",
        "Greece",
        "Guatemala",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran, Islamic Republic of",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Ivory Coast",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "Korea, Democratic People's Republic of",
        "Korea, Republic of",
        "Kosovo",
        "Kuwait",
        "Kyrgyzstan",
        "Lao People's Democratic Republic",
        "Latvia",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macao",
        "Macedonia, the former Yugoslav Republic of",
        "Madagascar",
        "Maldives",
        "Mali",
        "Malta",
        "Mexico",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Pakistan",
        "Palestine",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Pitcairn",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Romania",
        "Russian Federation",
        "Rwanda",
        "Saint Barthélemy",
        "Saint Helena, Ascension and Tristan da Cunha",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Martin (French part)",
        "Saint Pierre and Miquelon",
        "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Scotland",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten (Dutch part)",
        "Slovakia",
        "Slovenia",
        "Solomon Islands",
        "Somalia",
        "South Africa",
        "South Georgia and the South Sandwich Islands",
        "South Korea",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "St Vincent Grenadines",
        "Sudan",
        "Suriname",
        "Svalbard and Jan Mayen",
        "Swaziland",
        "Sweden",
        "Switzerland",
        "Syrian Arab Republic",
        "Taiwan",
        "Tajikistan",
        "Tanzania",
        "Thailand",
        "Timor-Leste",
        "Togo",
        "Tokelau",
        "Tonga",
        "Tortola",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turkmenistan",
        "Turks and Caicos Islands",
        "Tuvalu",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Venezuela",
        "Viet Nam",
        "Wales",
        "Wallis and Futuna",
        "Western Sahara",
        "Yemen",
        "Zambia",
        "Zimbabwe",
        "Tahiti",
        "TBD",
    ]}


app.layout = html.Div(
    [
        dcc.Store(id="changed-cell", data=[]),
        html.H2("Dash AG GRID - Rows cell styling"),
        dag.AgGrid(
            rowData=data_list,
            columnDefs=[{"field": "Val ID", "editable": False}]
            + [
                {
                    "field": c,
                    "cellRenderer": "FormatSpecificCells",
                    "valueFormatter": {"function": "FormatNumbersByRow(params)"},
                    "cellEditorSelector": {
                        "function": f"cellEditorSelector(params, {get_country_values()})"
                    },
                    "cellDataType": False,
                    "minWidth": 80,
                    "wrapText": True,
                    "cellEditor": {"function": "DMC_Select"},
                    "cellEditorParams": {
                        "options": get_country_values(),
                        "clearable": True,
                        "placeholder": "Select Option",
                    },
                    "autoHeight": True,
                    "valueSetter": {"function": "testValue(params)"},
                    "editable": {
                        "function": "['Link Col', 'Text Col'].indexOf(params.data['Val ID']) === -1"
                    },
                }
                for c in columns_list
                if c != "Val ID"
            ],
            defaultColDef={"editable": True},
            dashGridOptions={
                "undoRedoCellEditing": False,
                "undoRedoCellEditingLimit": 20,
                "tabToNextCell": {"function": "tabToNextCell(params)"}
            },
            id="ag-grid-table",
            style={"height": "700px"},
        ),
        dcc.Store(id="original-data", data=data_list),
        html.Div(id="edited-table-output"),
    ],
    style={"padding": "16px"},
)


@app.callback(
    Output("changed-cell", "data", allow_duplicate=True),
    Input("ag-grid-table", "cellValueChanged"),
    Input("ag-grid-table", "rowData"),
    # Input("ag-grid-table", "active_cell"),
    State("changed-cell", "data"),
    State("original-data", "data"),
    prevent_initial_call=True,
)
def update_table(changed_value, data_table, changes_stored, og_data):  # active_cell,

    triggered_id = [t["prop_id"] for t in dash.callback_context.triggered][0]

    if changed_value is not None:

        key = changed_value[0]["colId"]

        changed_column = changed_value[0]["data"]["Val ID"]
        row_index = changed_value[0]["rowId"]
        new_value = changed_value[0]["value"]
        change_id = f"{key}-{changed_column}"

        for row in og_data:
            if row["Val ID"] == changed_column:
                old_value = row[key]
            else:
                pass
        # Test if the old and new values are the same
        if new_value == old_value:
            changes_stored = [
                changes_stored
                for changes_stored in changes_stored
                if changes_stored["change_id"] != change_id
            ]
            return changes_stored

        new_changes = {
            "change_id": change_id,
            "val-ID": key,
            "index_row": row_index,
            "column": changed_column,
            "old_value": old_value,
            "new_value": new_value,
        }

        changes_stored = [
            changes_stored
            for changes_stored in changes_stored
            if changes_stored["change_id"] != change_id
        ]
        changes_stored.append(new_changes)

        return changes_stored

    return dash.no_update


def gen_update_row_btn(changes):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [html.Div(f"val-ID: "), html.B(changes["val-ID"])],
                        style={"display": "flex", "gap": "8px", "marginRight": "16px"},
                    ),
                    html.Div(
                        [html.Div(f"Changed Column: "), html.B(changes["column"])],
                        style={"display": "flex", "gap": "8px", "marginRight": "16px"},
                    ),
                    html.Div(
                        [
                            html.Div(f"Old Value & Type: "),
                            html.B(
                                f'{changes["old_value"]} - {type(changes["old_value"])}'
                            ),
                        ],
                        style={"display": "flex", "gap": "8px", "marginRight": "16px"},
                    ),
                    html.Div(
                        [
                            html.Div(f"New Value & Type: "),
                            html.B(
                                f'{changes["new_value"]} - {type(changes["new_value"])}'
                            ),
                        ],
                        style={"display": "flex", "gap": "8px", "marginRight": "16px"},
                    ),
                ],
                style={"display": "flex"},
            ),
        ],
        className="",
    )


@app.callback(Output("edited-table-output", "children"), 
              Input("changed-cell", "data"))
def update_d(cc_data):
    if cc_data == []:
        return None
    else:
        list_of_changes_to_confirm = [gen_update_row_btn(change) for change in cc_data]
        if len(cc_data) == 0:
            return None
        elif len(cc_data) == 1:
            return html.Div(
                [
                    html.Div(list_of_changes_to_confirm),
                    html.Div(
                        html.Button(
                            "Confirm Changes",
                            id={
                                "type": "confirm-all-btn",
                                "id": "test",
                            },
                            className="",
                        ),
                        className="textCenter bottom16",
                    ),
                ]
            )
        else:
            return html.Div(
                [
                    html.Div(list_of_changes_to_confirm),
                    html.Div(
                        html.Button(
                            "Confirm Changes",
                            id={
                                "type": "confirm-all-btn",
                                "id": "test",
                            },
                            className="",
                        ),
                        className="textCenter bottom16",
                    ),
                ]
            )


@app.callback(
    Output("ag-grid-table", "columnDefs"),
    Input("changed-cell", "data"),
    State("ag-grid-table", "columnDefs"),
)
def update_content_output(changed_cells, columns):
    key_to_check = "cellStyle"
    if changed_cells == []:
        to_change_cells = 0
        for (n, val) in enumerate(columns):
            if key_to_check in val.keys():
                if val["cellStyle"] == {}:
                    pass
                else:
                    to_change_cells += 1
                    val["cellStyle"] = {}
            else:
                pass
        if to_change_cells == 0:
            return dash.no_update
        else:
            return columns

    list_of_sn = [val["val-ID"] for val in changed_cells]

    for (n, val) in enumerate(columns):
        if val["field"] in list_of_sn:
            sn_val = val["field"]
            list_of_rows = [
                int(get_rows["index_row"])
                for get_rows in changed_cells
                if get_rows["val-ID"] == sn_val
            ]
            cellStyle = {
                "styleConditions": [
                    {
                        "condition": f"[{','.join(map(str, list_of_rows))}].includes(params.node.childIndex)",
                        "style": {"backgroundColor": "yellow"},
                    },
                    {
                        "condition": f"![{','.join(map(str, list_of_rows))}].includes(params.node.childIndex)",
                        "style": {},
                    },
                ]
            }
            val["cellStyle"] = cellStyle
        else:
            if key_to_check in val.keys():
                if val["cellStyle"] != {}:
                    val["cellStyle"] = {}
                    # else:
                    #     pass
                else:
                    pass
            else:
                pass
    return columns


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
