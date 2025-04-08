const list = `Name,Language,User
Godot-Save-Template,GDScript,weuritz8u
3ma-to-obj-converter-python,Python,weuritz8u
change-file-edittime,Powershell,weuritz8u
local-HTTP-server,Python,weuritz8u
read-wlan-password,Batchfile,weuritz8u
run-without-admin-rights,Batchfile,weuritz8u
visualnovel-march-2025,GDScript,weuritz8u
`;


// to read the csv table
document.getElementById('csvFileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        createTableFromCSV(e.target.result);
    };

    reader.readAsText(file);
});


function createTableFromCSV(csvText) {
    const rows = csvText.trim().split("\n").map(row => row.split(","));
    const table = document.getElementById("csvTable");
    table.innerHTML = "";

    rows.forEach((row, rowIndex) => {
        const tr = document.createElement("tr");

        row.forEach(cell => {
            const cellElement = rowIndex === 0 ? document.createElement("th") : document.createElement("td");
            cellElement.textContent = cell.trim();
            tr.appendChild(cellElement);
        });

        table.appendChild(tr);
    });
}

function display_list() {
    document.getElementById('table_paste').innerHTML = '<div class="table_container"><table id="csvTable"></table></div>'

    createTableFromCSV(list);
}
