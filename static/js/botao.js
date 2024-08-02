document.getElementById('pdf_file').addEventListener('change', function() {
    var submitBtn = document.getElementById('submitBtn');
    if (this.files.length > 0) {
        submitBtn.disabled = false;
        submitBtn.innerText = 'Enviar';
    } else {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Insira um arquivo';
    }
});