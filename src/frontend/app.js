// src/frontend/app.js

async function sendMessageToBackend(message) {
    try {
        const response = await fetch('http://localhost:5000/diagnose', { // Atualize para o endpoint correto
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });
        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error('Erro ao enviar mensagem:', error);
        return 'Desculpe, ocorreu um erro.';
    }
}

document.getElementById('sendButton').addEventListener('click', async () => {
    const userMessage = document.getElementById('userInput').value.trim();
    if (userMessage) {
        document.getElementById('chatWindow').innerHTML += `<div><strong>Você:</strong> ${userMessage}</div>`;
        const assistantResponse = await sendMessageToBackend(userMessage);
        document.getElementById('chatWindow').innerHTML += `<div><strong>Assistente:</strong> ${assistantResponse}</div>`;
        document.getElementById('userInput').value = '';
    }
});
