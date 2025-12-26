document.addEventListener("DOMContentLoaded", function() {
    const messageDiv = document.getElementById('message');
    const button = document.getElementById('change-message-button');

    button.addEventListener("click", function() {
        if (messageDiv.textContent === 'Hello World') {
            messageDiv.textContent === 'I love my country'
        } else {
            messageDiv.textContent = "Hello World"
        }
    });
});