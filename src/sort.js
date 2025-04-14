// Script written by Shadowdara

// Holt CSV-Daten von der API
async function load_data() {
    try {
        const response = await fetch("https://repo-database-creator.vercel.app/api/repos_raw");
        console.log("Antwort Status:", response.status);
        console.log("Antwort Header:", response.headers);
        const html = await response.text();
        console.log("Antwort Inhalt:", html);
        return html;
    } catch (err) {
        console.error("Fehler:", err);
        return null;
    }
}

// Liest eine lokale CSV-Datei ein
document.getElementById('csvFileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        createTableFromCSV(e.target.result);
    };

    reader.readAsText(file);
});

// Erstellt eine HTML-Tabelle aus CSV-Text
function createTableFromCSV(csvText) {
    const rows = csvText.trim().split("\n").map(row => {
        // Felder entschachteln ("escaped") und Kommas in Anführungszeichen beachten
        return row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g)?.map(cell => {
            // Entferne umschließende Anführungszeichen und ersetze doppelte Anführungszeichen
            return cell.replace(/^"(.*)"$/, '$1').replace(/""/g, '"').trim();
        }) ?? [];
    });

    const table = document.getElementById("csvTable");
    table.innerHTML = "";

    rows.forEach((row, rowIndex) => {
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

    document.getElementById('table_paste').innerHTML = '<div class="table_container"><table id="csvTable"></table></div>';
    createTableFromCSV(list);
}
