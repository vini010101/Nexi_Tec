
let nome = document.querySelector("#nome")
function exibirnome(){
    console.log(nome.value)
    if(nome.value == ""){
        nome.style.border = "2px solid red"
    }
    else{
        nome.style.border = "2px solid green"
    }
}

nome.addEventListener("blur",exibirnome)


let idade = document.querySelector("#idade");

idade.addEventListener("blur",function(){
    // Converter o valor da idade para um numero usando parserINT
    let idadeValor = parseInt(idade.value);
    
    if(idadeValor >=18){
        alert("voce possui mais de 18 anos!")
    
    }   else    {
        alert("infelizmente, voce nao é de maior!");
    }   
});

let endereco = document.querySelector("#endereco");

function exibirendereco(){
    console.log(endereco.value)
    if(endereco.value == ""){
    endereco.style.border = "2px solid red"
    }
    
    else{
    endereco.style.border = "2px solid green"
    }
}
endereco.addEventListener("blur",exibirendereco)

let email = document.querySelector("#email")

function exibiremail(){
    console.log(email.value)
    if(email.value == ""){
        email.style.border = "2px solid red"
    }
    
    else{
        email.style.border = "2px solid green"
    }
}
email.addEventListener("blur",exibiremail)


let fone = document.querySelector("#fone")

function exibirfone(){
    console.log(fone.value)
    if (fone.value== ""){
        fone.style.border = "2px solid red"
    }
    
    else{
        fone.style.border = "2px solid gree"
    }
}
fone.addEventListener("blur",exibirfone)



// Referências aos elementos do DOM
const inputFile = document.getElementById('curriculo');
const fileLabel = document.getElementById('file-label');
const fileError = document.getElementById('file-error');

// Função para formatar o nome do arquivo e validar o tipo e tamanho
inputFile.addEventListener('change', function() {
    const file = this.files[0]; // Obtém o arquivo selecionado
    fileError.textContent = ''; // Limpa erros anteriores

    if (file) {
        const allowedExtensions = ['pdf', 'docx'];
        const fileSizeLimit = 2 * 1024 * 1024; // Limite de 2MB para o arquivo
        const fileExtension = file.name.split('.').pop().toLowerCase();

        // Validação de extensão de arquivo
        if (!allowedExtensions.includes(fileExtension)) {
            fileError.textContent = 'Por favor, envie apenas arquivos PDF ou DOCX.';
            this.value = ''; // Reseta o input
            fileLabel.textContent = 'Escolha o arquivo';
            return;
        }

        // Validação de tamanho de arquivo
        if (file.size > fileSizeLimit) {
            fileError.textContent = 'O arquivo deve ter no máximo 2MB.';
            this.value = ''; // Reseta o input
            fileLabel.textContent = 'Escolha o arquivo';
            return;
        }

        // Se o arquivo for válido, atualiza o texto do label
        fileLabel.textContent = file.name;
    }
});