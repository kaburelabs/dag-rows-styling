
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

// cell editor custom component  - dmc.Select
dagfuncs.DMC_Select = class {
    // gets called once before the renderer is used
    init(params) {
        console.log(params)
        if (params.data["Val ID"] == "Country Col") {
            // create the cell
            this.params = params;
            console.log(params.options['country'])
            // function for when Dash is trying to send props back to the component / server
            var setProps = (props) => {
                if (typeof props.value != typeof undefined) {
                    // updates the value of the editor
                    this.value = props.value;
    
                    // re-enables keyboard event
                    delete params.colDef.suppressKeyboardEvent;
    
                    // tells the grid to stop editing the cell
                    params.api.stopEditing();
    
                    // sets focus back to the grid's previously active cell
                    this.prevFocus.focus();
                }
            };
            this.eInput = document.createElement('div');
    
            // renders component into the editor element
            ReactDOM.render(
                React.createElement(window.dash_mantine_components.Select, {
                    data: params.options['country'],
                    value: params.value,
                    setProps,
                    style: {width: params.column.actualWidth-2,  ...params.style},
                    className: params.className,
                    clearable: params.clearable,
                    searchable: params.searchable || true,
                    creatable: params.creatable,
                    debounce: params.debounce,
                    disabled: params.disabled,
                    filterDataOnExactSearchMatch:
                        params.filterDataOnExactSearchMatch,
                    limit: params.limit,
                    maxDropdownHeight: params.maxDropdownHeight,
                    nothingFound: params.nothingFound,
                    placeholder: params.placeholder,
                    required: params.required,
                    searchValue: params.searchValue,
                    shadow: params.shadow,
                    size: params.size,            
                    styles: params.styles,
                    switchDirectionOnFlip: params.switchDirectionOnFlip,
                    variant: params.variant,            
                }),
                this.eInput
            );
    
            // allows focus event
            this.eInput.tabIndex = '0';
    
            // sets editor value to the value from the cell
            this.value = params.value;
        }
        if (params.data["Val ID"] == "Long List Col") {

            // create the cell
            this.params = params;

            // function for when Dash is trying to send props back to the component / server
            var setProps = (props) => {
                if (typeof props.value != typeof undefined) {
                    // updates the value of the editor
                    this.value = props.value;
    
                    // re-enables keyboard event
                    delete params.colDef.suppressKeyboardEvent;
    
                    // tells the grid to stop editing the cell
                    params.api.stopEditing();
    
                    // sets focus back to the grid's previously active cell
                    this.prevFocus.focus();
                }
            };
            this.eInput = document.createElement('div');
    
            // renders component into the editor element
            ReactDOM.render(
                React.createElement(window.dash_mantine_components.Select, {
                    data: params.options['long_list_options'],
                    value: params.value,
                    setProps,
                    style: {width: params.column.actualWidth-2,  ...params.style},
                    className: params.className,
                    clearable: params.clearable,
                    searchable: params.searchable || true,
                    creatable: params.creatable,
                    debounce: params.debounce,
                    disabled: params.disabled,
                    filterDataOnExactSearchMatch:
                        params.filterDataOnExactSearchMatch,
                    limit: params.limit,
                    maxDropdownHeight: params.maxDropdownHeight,
                    nothingFound: params.nothingFound,
                    placeholder: params.placeholder,
                    required: params.required,
                    searchValue: params.searchValue,
                    shadow: params.shadow,
                    size: params.size,            
                    styles: params.styles,
                    switchDirectionOnFlip: params.switchDirectionOnFlip,
                    variant: params.variant,            
                }),
                this.eInput
            );
    
            // allows focus event
            this.eInput.tabIndex = '0';
    
            // sets editor value to the value from the cell
            this.value = params.value;
        }

        // create the cell
        this.params = params;
    }
    
    // gets called once when grid ready to insert the element
    getGui() {
        return this.eInput;
    }

    focusChild() {
        // needed to delay and allow the component to render
        setTimeout(() => {
            var inp = this.eInput.getElementsByClassName(
                'mantine-Select-input'
            )[0];
            inp.tabIndex = '1';

            // disables keyboard event
            this.params.colDef.suppressKeyboardEvent = (params) => {
                const gridShouldDoNothing = params.editing;
                return gridShouldDoNothing;
            };
            // shows dropdown options
            inp.focus();
        }, 100);
    }

    // focus and select can be done after the gui is attached
    afterGuiAttached() {
        // stores the active cell
        this.prevFocus = document.activeElement;

        // adds event listener to trigger event to go into dash component
        this.eInput.addEventListener('focus', this.focusChild());

        // triggers focus event
        this.eInput.focus();
    }

    // returns the new value after editing
    getValue() {
        return this.value;
    }

    // any cleanup we need to be done here
    destroy() {
        // sets focus back to the grid's previously active cell
        this.prevFocus.focus();
    }
};

dagfuncs.tabToNextCell = (params) => {
    const {node, api, backwards, previousCellPosition} = params
    const {column, rowIndex} = previousCellPosition
    console.log(rowIndex, column, "test opa")
    if (backwards) {
        return {rowIndex: rowIndex ? rowIndex-1 : 0, column: column}
    } else {
        return {rowIndex: rowIndex+1 , column: column}
    }
}
