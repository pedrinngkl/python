document.addEventListener('DOMContentLoaded', function () {

    const formulario = document.getElementById('form-consulta');
    const botao      = document.getElementById('btn-buscar');
    const btnText    = botao ? botao.querySelector('.btn-text') : null;
    const input      = document.getElementById('especialidade');

    // Focar no campo de entrada ao carregar a página
    if (input) input.focus();

    // Tratamento de loading e validação ao submeter o formulário
    if (formulario && botao) {
        formulario.addEventListener('submit', function (e) {
            const valorInput = input ? input.value.trim() : "";
            
            if (!valorInput) {
                e.preventDefault(); // Impede o envio se estiver vazio
                if (input) {
                    input.classList.add('invalid-shake'); // Opcional para feedback visual
                    input.focus();
                }
                return;
            }

            // Ativa o estado visual de carregamento no botão
            botao.classList.add('loading');
            botao.disabled = true;
            if (btnText) btnText.textContent = 'A pesquisar...';
        });
    }

    // Normalização automática no Blur (Primeira Letra de Cada Palavra em Maiúscula)
    if (input) {
        input.addEventListener('blur', function () {
            if (this.value) {
                this.value = this.value
                    .trim()
                    .toLowerCase()
                    .replace(/\b\w/g, c => c.toUpperCase());
            }
        });
    }
});

// Preenche a barra de pesquisa ao clicar em um chip e submete automaticamente
function preencherBusca(especialidade) {
    const input = document.getElementById('especialidade');
    const formulario = document.getElementById('form-consulta');
    
    if (input && formulario) {
        input.value = especialidade;
        
        // Dispara o evento de submit programaticamente simulando o clique do utilizador
        formulario.requestSubmit();
    }
}