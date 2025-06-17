// static/js/dark-mode.js

// Paso 1: Asegurarse de que el DOM (Document Object Model) esté completamente cargado.
// 'DOMContentLoaded' es un evento que se dispara cuando el navegador ha cargado todo el HTML
// y ha construido la estructura del documento. Es crucial esperar esto antes de intentar
// seleccionar o manipular elementos HTML.
document.addEventListener('DOMContentLoaded', () => {

    // Paso 2: Obtener referencias a los elementos HTML clave de la página.
    // 'document.body' es una referencia directa al elemento <body> del documento.
    const body = document.body;

    // 'document.getElementById()' busca un elemento HTML por su ID único.
    // En este caso, el botón que usaremos para alternar el modo oscuro.
    const darkModeToggle = document.getElementById('dark-mode-toggle');

    // Novedad para el botón: Si el botón existe, intentamos seleccionar sus elementos internos (ícono y texto).
    // Usamos el operador ternario (?) para evitar errores si el botón no se encuentra.
    const toggleIcon = darkModeToggle ? darkModeToggle.querySelector('i') : null; // Selecciona el elemento <i> (para el ícono de Font Awesome)
    const toggleText = darkModeToggle ? darkModeToggle.querySelector('span') : null; // Selecciona el elemento <span> (para el texto del botón)


    // Paso 3: Función de ayuda para aplicar o remover el tema oscuro.
    // Esta es la función central que realmente cambia la apariencia visual de la página
    // manipulando la clase CSS en el <body> y el estado del botón.
    function applyTheme(isDarkMode) {
        if (isDarkMode) {
            // Si 'isDarkMode' es verdadero (queremos el modo oscuro):
            // 3.1: Añadimos la clase 'dark-mode' al <body>.
            // Es esta clase la que activa tus estilos CSS definidos bajo '.dark-mode { ... }'
            // usando las variables CSS (ej. --background-color, --text-color).
            body.classList.add('dark-mode');

            // 3.2: Actualizar el botón de alternancia para que refleje el modo "claro" (a lo que se cambiará)
            if (darkModeToggle) {
                // Cambiar clases de Bootstrap en el botón para que se vea como un botón oscuro
                darkModeToggle.classList.remove('btn-light'); // Quitar estilo de botón claro
                darkModeToggle.classList.add('btn-dark');    // Añadir estilo de botón oscuro

                // Actualizar el ícono: si estaba en modo oscuro (luna), mostrar sol (para ir a claro)
                if (toggleIcon) {
                    toggleIcon.classList.remove('fa-moon'); // Quitar ícono de luna
                    toggleIcon.classList.add('fa-sun');     // Poner ícono de sol
                }
                // Actualizar el texto del botón
                if (toggleText) {
                    toggleText.textContent = 'Light Mode';
                }
            }
        } else {
            // Si 'isDarkMode' es falso (queremos el modo claro):
            // 3.1: Removemos la clase 'dark-mode' del <body>.
            // Esto hace que tu CSS vuelva a los estilos por defecto definidos en ':root { ... }'.
            body.classList.remove('dark-mode');

            // 3.2: Actualizar el botón de alternancia para que refleje el modo "oscuro" (a lo que se cambiará)
            if (darkModeToggle) {
                // Cambiar clases de Bootstrap en el botón para que se vea como un botón claro
                darkModeToggle.classList.remove('btn-dark');  // Quitar estilo de botón oscuro
                darkModeToggle.classList.add('btn-light');    // Añadir estilo de botón claro

                // Actualizar el ícono: si estaba en modo claro (sol), mostrar luna (para ir a oscuro)
                if (toggleIcon) {
                    toggleIcon.classList.remove('fa-sun');  // Quitar ícono de sol
                    toggleIcon.classList.add('fa-moon');    // Poner ícono de luna
                }
                // Actualizar el texto del botón
                if (toggleText) {
                    toggleText.textContent = 'Dark Mode';
                }
            }
        }
    }

    // Paso 4: Cargar la preferencia del usuario guardada de sesiones anteriores.
    // 'localStorage' es un mecanismo del navegador para almacenar datos de forma persistente.
    // Los datos guardados aquí permanecen incluso si el usuario cierra el navegador o apaga la computadora.
    // 'localStorage.getItem('theme')' intenta recuperar el valor asociado a la clave 'theme'.
    // Puede ser 'dark', 'light' o 'null' (si no se ha guardado nada antes).
    const savedTheme = localStorage.getItem('theme');

    // Paso 5: Lógica para decidir qué tema aplicar al momento de cargar la página.
    // Se prioriza la preferencia guardada por el usuario.
    if (savedTheme === 'dark') {
        // Si el usuario guardó explícitamente 'dark' en una sesión anterior, aplicamos el modo oscuro.
        applyTheme(true);
    } else if (savedTheme === 'light') {
        // Si el usuario guardó explícitamente 'light', aplicamos el modo claro.
        applyTheme(false);
    } else {
        // Si no hay ninguna preferencia guardada en 'localStorage' (ej. primera visita, o se borraron los datos):
        // 6. Detectar la preferencia de tema del sistema operativo del usuario.
        // 'window.matchMedia' permite a JavaScript consultar "media queries" del navegador.
        // '(prefers-color-scheme: dark)' es una media query que pregunta si el sistema operativo
        // tiene configurado un esquema de color oscuro. '.matches' devuelve 'true' si es así.
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            applyTheme(true); // Si el sistema prefiere el modo oscuro, lo aplicamos por defecto.
        } else {
            applyTheme(false); // Si no hay preferencia o prefiere el modo claro, aplicamos el modo claro por defecto.
        }
    }

    // Paso 7: Configurar el evento para el clic en el botón de alternancia.
    // Solo añadimos el 'event listener' si el botón existe para evitar errores.
    if (darkModeToggle) {
        // 'addEventListener('click', ...)' adjunta una función que se ejecutará cada vez que se haga clic en el botón.
        darkModeToggle.addEventListener('click', () => {
            // Verificamos el estado actual del modo oscuro mirando si el <body> tiene la clase 'dark-mode'.
            const isCurrentlyDarkMode = body.classList.contains('dark-mode');

            if (isCurrentlyDarkMode) {
                // Si el modo oscuro está actualmente activo, lo cambiamos a claro.
                applyTheme(false);
                // Guardamos la preferencia 'light' en 'localStorage' para recordar la elección del usuario.
                localStorage.setItem('theme', 'light');
            } else {
                // Si el modo claro está actualmente activo, lo cambiamos a oscuro.
                applyTheme(true);
                // Guardamos la preferencia 'dark' en 'localStorage'.
                localStorage.setItem('theme', 'dark');
            }
        });
    }
});