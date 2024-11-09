document.getElementById("formulario").addEventListener("submit", async function(event) {
    event.preventDefault(); // Impede o envio imediato do formulário
    
    const formData = new FormData(this);
    
    try {
        const response = await fetch(this.action, {
            method: "POST",
            body: formData
        });
        
        if (response.ok) {
            alert("Formulário enviado com sucesso!");
            window.location.href = "/"; // Redireciona para a página inicial
        } else {
            alert("Erro ao enviar o formulário. Tente novamente.");
        }
    } catch (error) {
        alert("Ocorreu um erro ao enviar o formulário.");
        console.error("Erro:", error);
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formulario");
    const successMessage = document.getElementById("success-message");

    // Função para mostrar a mensagem de erro ou sucesso
    function showSuccessMessage() {
        successMessage.style.display = "block";  // Exibe a mensagem de sucesso
        fileError.textContent = "";  // Limpa qualquer mensagem de erro
    }

    function showErrorMessage(message) {
        successMessage.style.display = "none";  // Esconde a mensagem de sucesso
        fileError.textContent = message;  // Exibe a mensagem de erro
    }

   

    // Adiciona verificação de preenchimento para os outros campos como no exemplo anterior
    form.querySelectorAll("input[required], textarea[required]").forEach(function (input) {
        input.addEventListener("blur", function () {
            validateField(input);
        });
    });

    form.querySelectorAll("input, textarea").forEach(function (input) {
        input.addEventListener("input", function () {
            validateField(input);
        });
    });

    function validateField(field) {
        if (field.value.trim() === "") {
            field.style.borderColor = "red";
        } else {
            field.style.borderColor = "green";
        }
    }

    form.addEventListener("submit", function (event) {
        let allValid = true;

        form.querySelectorAll("input[required], textarea[required]").forEach(function (input) {
            if (input.value.trim() === "") {
                input.style.borderColor = "red";
                allValid = false;
            }
        });

        if (!allValid) {
            event.preventDefault();
            alert("Por favor, preencha todos os campos obrigatórios.");
        }
    });
});