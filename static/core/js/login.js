// Funcionalidad para mostrar/ocultar contraseña
const togglePassword = document.getElementById('togglePassword');
const passwordInput = document.getElementById('password');

togglePassword.addEventListener('click', function () {
    // Cambiar el tipo de input
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);

    // Cambiar el icono
    const icon = this.querySelector('i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
});

// Funcionalidad para el modal de contraseña olvidada
const modal = document.getElementById('passwordModal');
const forgotPasswordLink = document.getElementById('forgotPasswordLink');
const closeModalBtn = document.querySelector('.close-modal');
const closeModalBtn2 = document.getElementById('closeModalBtn');

forgotPasswordLink.addEventListener('click', function () {
    modal.style.display = 'flex';
});

closeModalBtn.addEventListener('click', function () {
    modal.style.display = 'none';
});

closeModalBtn2.addEventListener('click', function () {
    modal.style.display = 'none';
});

// Cerrar modal al hacer clic fuera del contenido
window.addEventListener('click', function (event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});