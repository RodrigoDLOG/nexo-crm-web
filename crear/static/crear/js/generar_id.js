// Función para generar un ID aleatorio de 10 caracteres
function generarIdAleatorio() {
    const caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let id = '';

    for (let i = 0; i < 10; i++) {
        const indiceAleatorio = Math.floor(Math.random() * caracteres.length);
        id += caracteres.charAt(indiceAleatorio);
    }

    return id;
}

// Generar ID aleatorio cuando se cargue la página
document.addEventListener('DOMContentLoaded', function () {
    const idInput = document.getElementById('polizaId');
    idInput.value = generarIdAleatorio();
});

// Opcional: Permitir regenerar el ID si se hace clic en el campo
document.getElementById('polizaId').addEventListener('click', function () {
    if (confirm('¿Desea generar un nuevo ID?')) {
        this.value = generarIdAleatorio();
    }
});