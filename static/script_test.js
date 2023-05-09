// ランダムなユーザ名とメッセージを生成する関数
function generateMessage() {
  const users = ["User 1", "User 2", "User 3", "User 4"];
  const messages = [
    "Hello!",
    "How are you?",
    "What are you up to?",
    "I'm doing well, thanks for asking!",
    "I'm a little tired today.",
    "Do you want to grab lunch later?",
    "What do you think of the new project?",
    "See you tomorrow!",
    "Good night!",
  ];
  const randomUser = users[Math.floor(Math.random() * users.length)];
  const randomMessage = messages[Math.floor(Math.random() * messages.length)];
  return `${randomUser}: ${randomMessage}`;
}

// チャットメッセージを追加する関数
function addMessage() {
  const chatContainer = document.getElementById("chat-container");
  const chatBubble = document.createElement("div");
  chatBubble.classList.add("chat-bubble");
  const message = document.createElement("p");
  message.textContent = generateMessage();
  chatBubble.appendChild(message);
  chatContainer.appendChild(chatBubble);
}

// 5秒ごとに新しいチャットメッセージを追加する
setInterval(addMessage, 2000);
