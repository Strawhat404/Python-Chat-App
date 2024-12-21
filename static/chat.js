const socket = io()

const form = document.getElementById('chat-form');
const input = document.getElementById('message-input');
const message = document.getElementById('message');

//so to listen to an incoming message

socket.on('message',(data) => {
    const li = document.createElement('li');
    li.textContent = data;
    message.appendChild(li);
    message.scrollTop = message.scrollHeight;
}
);
socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('connect', () => {
    console.log('Connected to server');
});

//so to handle the message submission

form.addEventListener('submit',(event) => {
    event.preventDefault();
    const message = input.value;
    if (message.trim()){
        socket.send(message);
        input.value = '';
    }
}); 
