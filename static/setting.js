const numButton = document.getElementById("num-button");
const sendButton = document.getElementById("send-button");
const responseField = document.getElementById("response-field");
const onDiscussion= document.getElementById("onDiscussion");
const chatContainer = document.getElementById("chat-container");

numButton.onclick = async (event)=>{
  event.preventDefault();
  const num = document.getElementById("num").value;
  const container = document.getElementById("container");
  container.innerHTML = "";
  
  for (var i = 1; i <= num; i++) {
    var nameInput = document.createElement("input");
    nameInput.type = "text";
    nameInput.name = "name" + i;
    nameInput.placeholder = "名前" + i;

    var personalityInput = document.createElement("input");
    personalityInput.type = "text";
    personalityInput.name = "personality" + i;
    personalityInput.placeholder = "性格" + i;

    container.appendChild(nameInput);
    container.appendChild(personalityInput);
  }
}

function addMessage(response_arr) {
  const chatContainer = document.getElementById("chat-container");
  const chatBubble = document.createElement("div");
  chatBubble.classList.add("chat-bubble");
  const message = document.createElement("p");
  message.textContent = response_arr;
  chatBubble.appendChild(message);
  chatContainer.appendChild(chatBubble);
}

sendButton.onclick = async(event)=>{  
  const scene = document.getElementById("scene").value;
  const theme = document.getElementById("theme").value;
  const container = document.getElementById("container");
  const nameInputs = container.querySelectorAll('input[type="text"][name^="name"]');
  const personalityInputs = container.querySelectorAll('input[type="text"][name^="personality"]');

  var names = []
  var personalities = []
  for (let i = 0; i < nameInputs.length; i++) {
    names = [...names, nameInputs[i].value] ;
    personalities = [...personalities, personalityInputs[i].value];
  }
  
  const data = {
    scene: scene,
    theme: theme,
    person_names: names,
    person_personalities: personalities
  }

  const response = await fetch("/setting", {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify(data),
  });
  alert("updated!")
  res = await response.json();
  // addMessage(res)
  const lines = res.split("\n");
  const conversations = [];
  
  console.log(lines)
  let current_speaker = null;
  
  for (const line of lines) {
    if (line) {
      setInterval(addMessage(line), 2000);
      // const [speaker, message] = line.split(":");
      // if (speaker !== current_speaker) {
      //   current_speaker = speaker;
      //   conversations.push([{ speaker, message }]);
      // } else {
      //   conversations[conversations.length - 1].push({ speaker, message });
      // }
    }
  }
  console.log(conversations)
};
