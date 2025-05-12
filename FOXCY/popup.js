var websiteUrl;
var websiteHostname;

chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    websiteUrl = tabs[0].url;
    websiteHostname = new URL(tabs[0].url).hostname;
    document.getElementById("url").innerText = websiteHostname;
});

function showError(text) {
    var div = document.createElement('div');
    div.setAttribute('id', 'ERRORcontainer');
    div.innerHTML = `
        <div class="ERROR">
            <p>${text}</p>
        </div>`;
    document.getElementsByClassName("bottomItem")[0].appendChild(div);

    setTimeout(() => {
        document.getElementById("ERRORcontainer").remove();
    }, 3000);
}

document.getElementById("btn").addEventListener("click", () => {
    if (websiteUrl.toLowerCase().includes("chrome://")) {
        showError("You cannot block a Chrome URL");
    } else {
        chrome.storage.local.get("BlockedUrls", (data) => {
            if (data.BlockedUrls === undefined) {
                chrome.storage.local.set({ BlockedUrls: [{ status: "BLOCKED", url: websiteHostname }] });
                chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
                    chrome.tabs.sendMessage(
                        tabs[0].id,
                        { from: "popup", Subject: "startTimer" });
                    console.log("Timer started!");
                });

                setTimeout(() => {
                    var then = new Date();
                    then.setHours(24, 0, 0, 0);
                    const blockTill = then.getTime()
                    chrome.storage.local.set({ BlockedUrls: [{ status: "BLOCKED", url: websiteHostname, BlockedTill: blockTill }] });
                });

            } else {
                if (data.BlockedUrls.some((e) => e.url === websiteHostname && e.status === "In_Progress")) {
                    showError("This URL will be blocked after some time");
                } else if (data.BlockedUrls.some((e) => e.url === websiteHostname && e.status === "BLOCKED")) {
                    showError("This URL is already completely blocked");
                } else {
                    chrome.storage.local.set({ BlockedUrls: [...data.BlockedUrls, { status: "In_Progress", url: websiteHostname }] });
                    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
                        chrome.tabs.sendMessage(
                            tabs[0].id,
                            { from: "popup", Subject: "startTimer" });
                        console.log("Timer started!");
                    });

                    // Reset the block status after 10 seconds
                    setTimeout(() => {
                        chrome.storage.local.get("BlockedUrls", (data) => {
                            const updatedBlockedUrls = data.BlockedUrls.map((e) => {
                                if (e.url === websiteHostname && e.status === "In_Progress") {
                                    var then = new Date();
                                    then.setHours(24, 0, 0, 0);
                                    const blockTill = then.getTime()
                                    return { status: "BLOCKED", url: websiteHostname, BlockedTill: blockTill };
                                } else {
                                    return e;
                                }
                            });

                            chrome.storage.local.set({ BlockedUrls: updatedBlockedUrls });
                        });
                    });
                }
            }
        });
    }
});
