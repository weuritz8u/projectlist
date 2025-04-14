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

async function display_list_pic() {
    const csvText = await load_data();
    if (!csvText) return;

    const username = getUsernameFromURL();

    const rows = csvText.trim().split("\n").map(row => {
        return row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g)?.map(cell =>
            cell.replace(/^"(.*)"$/, "$1").replace(/""/g, '"').trim()
        ) ?? [];
    });

    const [header, ...dataRows] = rows;

    const container = document.getElementById('data_paste');
    container.innerHTML = '';

    dataRows.forEach(row => {
        const repoName = row[0];
        if (!repoName) return;

        const card = createGitHubCard(username, repoName);
        container.appendChild(card);
    });
}

function createGitHubCard(username, repo, theme = "midnight-purple") {
    const a = document.createElement("a");
    a.href = `https://github.com/${username}/${repo}`;
    a.target = "_blank";
    a.rel = "noopener noreferrer";

    const img = document.createElement("img");
    img.src = `https://github-readme-stats.vercel.app/api/pin/?username=${username}&theme=${theme}&repo=${repo}`;
    img.alt = repo;

    a.appendChild(img);
    return a;
}

function getUsernameFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get("user") || "weuritz8u";
}
