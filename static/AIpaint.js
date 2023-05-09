const inputField = document.getElementById("input-field");
const paintArea = document.getElementById("paint-area");
const sendButton = document.getElementById("send-button");

sendButton.onclick = async ()=>{
  const input = inputField.value;
  const data = {"json_str": input}
  const response = await fetch("/AIpaint", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  alert("updated!")
  paintArea.innerHTML = await response.json();
}