const socket = io();

socket.on('connect', () => {
    console.log('Connected to the server');
});

socket.on('message', (data) => {
    console.log('Received message:', data);
    const li = document.createElement('li');
    li.textContent = data;
    document.getElementById('message').appendChild(li);
    document.getElementById('message').scrollTop = document.getElementById('message').scrollHeight;
});

// Ensure the DOM is fully loaded before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chat-form');
    const input = document.getElementById('message-input');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const message = input.value;
        if (message.trim()) {
            socket.send(message);
            input.value = '';  // Clear the input after sending
        }
    });
});
