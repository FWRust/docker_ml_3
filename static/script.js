var btn = document.getElementById('btn');
let text_box = document.getElementById('textBox');
let message_box = document.getElementById('message-box');
let server_url = window.location.href + 'request'
let user = 'user: ';
let server = 'GPT-2: ';

function submit()
{
    let message = document.getElementById('textBox').value;
    text_box.value = '';
    message_box.innerHTML = message_box.value + user + message + '\n' + '\n';

    fetch(server_url,{
    method: "POST",
    body: JSON.stringify({prompt: message}),
    headers: {
    "Content-type": "application/json",
    "accept": "application/json",
    }
  })
  .then((response) => response.json())
  .then((json) => document.getElementById('message-box').innerHTML = message_box.value + server + (json.answer) + '\n' + '\n');
}
