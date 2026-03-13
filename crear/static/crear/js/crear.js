document.getElementById("success-outlined").addEventListener("change", function() {
    document.getElementById("contenido_cliente_existente").style.display = "block";
    document.getElementById("contenido_crear_cliente").style.display = "none";
});

document.getElementById("danger-outlined").addEventListener("change", function() {
    document.getElementById("contenido_cliente_existente").style.display = "none";
    document.getElementById("contenido_crear_cliente").style.display = "block";
});