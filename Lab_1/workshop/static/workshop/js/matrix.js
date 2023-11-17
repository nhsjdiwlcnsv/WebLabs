let table = document.getElementById('table');

let addRowBtn = document.getElementById('add-row-btn');
let addColBtn = document.getElementById('add-col-btn');
let generateBtn = document.getElementById('generate-btn');
let transposeBtn = document.getElementById('transpose-btn');
let countInput = document.getElementById('matrix-size')
let maxSelectionInput = document.getElementById('max-selection');

const maxSelection = parseInt(maxSelectionInput.value) || 1;

let selectedCells = [];

generateBtn.addEventListener("click", generateTable);
transposeBtn.addEventListener("click", transposeTable);
addRowBtn.addEventListener("click", addRow);
addColBtn.addEventListener("click", addColumn);

function generateTable() {
    clearTable();

    let rowCount = parseInt(countInput.value) || 0;
    let colCount = parseInt(countInput.value) || 0;

    for (let i = 0; i < rowCount; i++) {
        let row = table.insertRow(i);
        for (let j = 0; j < colCount; j++) {
            let cell = row.insertCell(j);
            cell.innerText = (i * rowCount + j).toString()
            cell.addEventListener('click', () => selectCell(cell));
        }
    }
}

function transposeTable() {
    let newTable = document.createElement('table');
    for (let i = 0; i < table.rows[0].cells.length; i++) {
        let row = newTable.insertRow(i);
        for (let j = 0; j < table.rows.length; j++) {
            let cell = row.insertCell(j);
            cell.innerText = table.rows[j].cells[i].innerText;
            cell.addEventListener('click', () => selectCell(cell));
        }
    }

    clearTable();

    table.parentNode.replaceChild(newTable, table);
    table = newTable;
}


function selectCell(cell) {
    let maxSelection = parseInt(maxSelectionInput.value) || 1;

    if (selectedCells.length < maxSelection && !isAdjacent(cell)) {
        selectedCells.push(cell);

        if (parseInt(cell.innerText) % 2 === 0)
            cell.classList.add('selected-even');
        else
            cell.classList.add('selected-odd');

    } else alert('Either max selected cells limit exceeded, or cells are neighboring.');
}

function isAdjacent(cell) {
    for (let selectedCell of selectedCells) {
        if (cell === selectedCell)
            return true;

        let selectedRow = selectedCell.parentNode.rowIndex;
        let selectedCol = selectedCell.cellIndex;
        let row = cell.parentNode.rowIndex;
        let col = cell.cellIndex;

        // Проверяем, что ячейки соседствуют только по горизонтали или вертикали
        if ((Math.abs(selectedRow - row) === 1 && selectedCol === col) ||
            (selectedRow === row && Math.abs(selectedCol - col) === 1))
            return true;
    }

    return false;
}


function clearTable() {
    while (table.rows.length > 0)
        table.deleteRow(0);

    selectedCells = [];
}

function addRow() {
    let newRow = table.insertRow(table.rows.length);

    for (let j = 0; j < table.rows[0].cells.length; j++) {
        let cell = newRow.insertCell(j);
        cell.innerText = (1).toString()
        cell.addEventListener('click', () => selectCell(cell));
    }
}

function addColumn() {
    for (let i = 0; i < table.rows.length; i++) {
        let cell = table.rows[i].insertCell(table.rows[i].cells.length);

        cell.innerText = (0).toString()
        cell.addEventListener('click', () => selectCell(cell));
    }
}