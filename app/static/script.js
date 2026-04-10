async function checkHealth() {
    try {
        const res = await fetch("/health");
        const data = await res.json();

        document.getElementById("status").innerText =
            "API STATUS: " + data.status.toUpperCase();

    } catch (e) {
        document.getElementById("status").innerText =
            "API STATUS: OFFLINE";
    }
}

checkHealth();
