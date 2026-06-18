document.getElementById("startBtn").addEventListener("click", async () => {

    const target = document.getElementById("target").value;
    const profile = document.getElementById("profile").value;

    log(`Starting scan on ${target} with ${profile}`);

    const res = await fetch("/scanner", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ target, profile })
    });

    const data = await res.json();

    log("Scan complete");

    console.log(data);

    document.getElementById("nodeData").textContent =
        JSON.stringify(data, null, 2);
});

function log(msg) {
    const box = document.getElementById("logBox");
    const entry = document.createElement("div");
    entry.textContent = msg;
    box.appendChild(entry);
}

/* THEME TOGGLE */
document.getElementById("themeToggle").addEventListener("click", () => {
    document.body.classList.toggle("dark");
});