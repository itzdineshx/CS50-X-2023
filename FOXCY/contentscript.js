function closeTab() {
    alert("This URL is completely blocked for today. This tab will close after you press OK");
    chrome.runtime.sendMessage({ CloseMe: true });
}

chrome.runtime.onMessage.addListener((message, sender) => {
    if (message.from === "popup" && message.Subject === "startTimer"){
        console.log("start the timer")

        // Create a link element for CSS
        const cssLink = document.createElement('link');
        cssLink.rel = 'stylesheet';
        cssLink.href = 'contentscript.css';
        document.head.appendChild(cssLink);

        var hour = 0;
        var min = 0;
        var sec = 10;

        var div = document.createElement("div")
        div.innerHTML = `
        <div class="STAYPtopItem">
            <h1>Stay Productive</h1>
            <div class="STAYPtopItemMain">
                <div class="STAYPInfo">
                    <p>You are currently on:</p>
                    <h4 id="STAYPurl">${window.location.hostname}</h4>
                </div>
            </div>
        </div>
        <div class="STAYPbottomItem">
            <div class="STAYPtimeCont">
                <p>Time Remaining</p>
                <div class="STAYPtime">
                    <div class="STAYPnumber">
                        <p id="STAYPhour">${("0" + hour).slice(-2)}</p>
                    </div>
                    <span>:</span>
                    <div class="STAYPnumber">
                        <p id="STAYPmin">${("0" + min).slice(-2)}</p>
                    </div>
                    <span>:</span>
                    <div class="STAYPnumber">
                        <p id="STAYPsec">${("0" + sec).slice(-2)}</p>
                    </div>
                </div>
            </div>
        </div>`;
    document.body.prepend(div);
    setInterval(() => {
        if (sec > 0) {
            sec -= 1;
            document.getElementById("STAYPsec").innerText = ("0" + sec).slice(-2);
        } else {
            closeTab();
        }
    }, 1000);
    }
})
chrome.storage.local.get("BlockedUrls", (data) => {
    if (data.BlockedUrls !== undefined){
        if (data.BlockedUrls.some((e) => e.url === window.location.hostname && e.status === "BLOCKED")){
            closeTab()
        }
    }
})