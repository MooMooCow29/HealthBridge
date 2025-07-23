function appendMessage(sender, message) {
    const chatbox = document.getElementById("chatbox");
    const msgDiv = document.createElement("div");
    msgDiv.className = "message";
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById("userInput");
    const message = userInput.value.trim();
    if (message === "") return;

    appendMessage("You", message);
    userInput.value = "";

    fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("HealthBot", data.reply);
    })
    .catch(() => {
        appendMessage("HealthBot", "❌ Failed to get a response.");
    });
}

function setQuick(text) {
    document.getElementById("userInput").value = text;
}
