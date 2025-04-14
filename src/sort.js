// Script written by Shadowdara

// Holt CSV-Daten von der API
async function load_data() {
    try {
        const response = await fetch("https://repo-database-creator.vercel.app/api/repos_raw");
        const html = await response.text();
        return html;
    } catch (err) {
        console.error("Fehler:", err);
        return null;
    }
}

function createTableFromCSV(csvText) {
    const parsed = Papa.parse(csvText.trim(), { header: false });
    const table = document.getElementById("csvTable");
    table.innerHTML = "";

    parsed.data.forEach((row, rowIndex) => {
        const tr = document.createElement("tr");
        row.forEach(cell => {
            const cellElement = rowIndex === 0 ? document.createElement("th") : document.createElement("td");
            cellElement.textContent = cell;
            tr.appendChild(cellElement);
        });
        table.appendChild(tr);
    });
}

// Holt remote CSV und zeigt sie als Tabelle an
async function display_list() {
    const list = await load_data();
    if (!list) return;

    document.getElementById('data_paste').innerHTML = '<div class="table_container"><table id="csvTable"></table></div>';
    createTableFromCSV(list);
}

async function  display_list_pic() {
    const list = await load_data();
    if (!list) return;
    document.getElementById('data_paste').innerHTML = '<div></div>'
}

