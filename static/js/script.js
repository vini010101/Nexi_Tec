
// Função para validar um campo específico
function validateField(fieldId, successMessageId) {
    const field = document.getElementById(fieldId);
    const successMessage = document.getElementById(successMessageId);

    field.addEventListener("input", function() {
        if (field.value.trim() === "") {
            field.style.borderColor = "red";
            successMessage.style.display = "block";
        } else {
            field.style.borderColor = "green";
            successMessage.style.display = "block";
        }
    });
}

// Chama a função validateField para cada campo
validateField("nome", "success-nome");
validateField("fone", "success-fone");
validateField("email", "success-email");
validateField("fone2", "success-fone2");

document.addEventListener('DOMContentLoaded', function() {
    // Seleciona o input do arquivo e a área de mensagem de sucesso
    const fileInput = document.getElementById('imagens');
    const successMessage = document.getElementById('success-message');

    // Adiciona um evento para detectar quando o arquivo é selecionado
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            // Exibe a mensagem de sucesso
            successMessage.style.display = 'block';
            successMessage.textContent = 'Arquivo enviado com sucesso!';
        }
    });
});

// Função para exibir a caixa de diálogo com a mensagem
function exibirMensagem(mensagem) {
    alert(mensagem);  // Exibe a mensagem como uma caixa de diálogo
}

// Função que será chamada quando o formulário for enviado
function enviarFormulario(event) {
    event.preventDefault();  // Impede o envio do formulário (não envia os dados)

    // Obtém os valores dos campos
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;

    // Verifica se os campos obrigatórios estão preenchidos
    if (!nome || !email) {
        exibirMensagem("Por favor, preencha todos os campos!");  // Se não preenchido
    } else {
        // Simula o envio do formulário e exibe a caixa de diálogo de sucesso
        setTimeout(function() {
            // Simula sucesso
            exibirMensagem("Formulário enviado com sucesso!");

            // Recarrega a página após a mensagem de sucesso
            location.reload();  // Recarrega a página
        }, 1000);  // Atraso de 1 segundo para simular o envio
    }
}

// Adiciona o evento de submit ao formulário para chamar a função de envio
document.getElementById('formulario').addEventListener('submit', enviarFormulario);