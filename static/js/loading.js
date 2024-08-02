document.getElementById('pdfForm').addEventListener('submit', function(event) {
    var carrega = document.getElementById('loading');
    var normal = document.getElementById('normal');

    carrega.classList.remove('d-none');
    carrega.classList.add('d-flex');
    normal.classList.remove('d-flex');
    normal.classList.add('d-none');

    setTimeout(function() {
        carrega.classList.remove('d-flex');
        carrega.classList.add('d-none');

        normal.classList.remove('d-none');
        normal.classList.add('d-flex');
    }, 13000);
    
    var submitBtn = document.getElementById('submitBtn');
    submitBtn.disabled = true; // Desabilita o botão imediatamente após o envio do formulário
    
    setTimeout(function() {
        submitBtn.disabled = false; // Reabilita o botão após 5 segundos
    }, 5000);
});