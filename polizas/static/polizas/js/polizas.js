const btnToggle = document.getElementById('toggleVencidas');
const filas = document.querySelectorAll('#tablaPolizas tr');

let ocultando = true;  // Estado actual: empieza mostrando todo

btnToggle.addEventListener('click', () => {
    const hoy = new Date();
    
    filas.forEach(fila => {
        const celdaFecha = fila.cells[5]; // columna de fecha de vencimiento
        const fechaTexto = celdaFecha.textContent.trim();
        
        // Convertimos el texto tipo "18 de octubre de 2025" a objeto Date
        const fechaParts = fechaTexto.split(' de ');
        const dia = parseInt(fechaParts[0]);
        const mes = fechaParts[1].toLowerCase();
        const año = parseInt(fechaParts[2]);

        // Mapeo de meses en español a número
        const meses = {
            enero: 0, febrero: 1, marzo: 2, abril: 3, mayo: 4, junio: 5,
            julio: 6, agosto: 7, septiembre: 8, octubre: 9, noviembre: 10, diciembre: 11
        };

        const fechaVenc = new Date(año, meses[mes], dia);

        if (ocultando) {
            // Si la fecha ya pasó → ocultamos la fila
            if (fechaVenc < hoy) {
                fila.style.display = 'none';
            }
        } else {
            // Volvemos a mostrar todo
            fila.style.display = '';
        }
    });

    if (ocultando) {
        btnToggle.textContent = 'Mostrar pólizas vencidas';
        btnToggle.classList.remove('btn-secondary');
        btnToggle.classList.add('btn-primary');
    } else {
        btnToggle.textContent = 'Ocultar pólizas vencidas';
        btnToggle.classList.remove('btn-primary');
        btnToggle.classList.add('btn-secondary');
    }
    
    ocultando = !ocultando;  // Alternamos el estado
});