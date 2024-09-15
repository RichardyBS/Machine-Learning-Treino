document.getElementById('diagnose-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const userInput = document.getElementById('user-input').value;
    
    try {
        const response = await fetch('http://127.0.0.1:5000/diagnose', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }

        const data = await response.json();

        // Mostrar a resposta
        if (data && data.problem && data.cost) {
            document.getElementById('response').innerText = `${data.problem}\n${data.cost}`;
        } else {
            document.getElementById('response').innerText = 'Resposta não compreendida.';
        }
    } catch (error) {
        console.error('Erro:', error);
        document.getElementById('response').innerText = 'Ocorreu um erro ao processar a solicitação.';
    }
});
