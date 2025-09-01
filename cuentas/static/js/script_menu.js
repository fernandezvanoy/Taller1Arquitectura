document.addEventListener("DOMContentLoaded", function() {
    // Elementos del menú usuario
    const iconoUsuario = document.getElementById("icono-usuario");
    const menuUsuario = document.getElementById("menu-usuario");
    
    // Elementos del menú opciones
    const iconoMenu = document.getElementById("icono-menu");
    const menuOpciones = document.getElementById("menu-opciones");

    // Elementos del login
    const content = document.querySelector('.content');
    const loginLink = menuUsuario ? menuUsuario.querySelector('a[href*="login"]') : null;

    // Menú usuario
    if (iconoUsuario && menuUsuario) {
        iconoUsuario.addEventListener("click", function(event) {
            event.stopPropagation();
            menuUsuario.style.display = menuUsuario.style.display === "block" ? "none" : "block";
            // Cierra el otro menú y el login
            if (menuOpciones) menuOpciones.style.display = "none";
            if (content) content.style.display = "none";
        });
    }

    // Menú opciones
    if (iconoMenu && menuOpciones) {
        iconoMenu.addEventListener("click", function(event) {
            event.stopPropagation();
            menuOpciones.style.display = menuOpciones.style.display === "block" ? "none" : "block";
            // Cierra el otro menú y el login
            if (menuUsuario) menuUsuario.style.display = "none";
            if (content) content.style.display = "none";
        });
    }

    // Mostrar formulario de login al hacer clic en "Iniciar Sesión"
    if (loginLink && content) {
        loginLink.addEventListener("click", function(event) {
            event.preventDefault();
            content.style.display = "block";
            // Cierra los menús
            if (menuUsuario) menuUsuario.style.display = "none";
            if (menuOpciones) menuOpciones.style.display = "none";
        });
    }

    // Cerrar menús y login al hacer clic fuera
    document.addEventListener("click", function(event) {
        // Para el menú usuario
        if (menuUsuario && !menuUsuario.contains(event.target) && event.target !== iconoUsuario) {
            menuUsuario.style.display = "none";
        }
        // Para el menú opciones
        if (menuOpciones && !menuOpciones.contains(event.target) && event.target !== iconoMenu) {
            menuOpciones.style.display = "none";
        }
        // Para el login
        if (content && !content.contains(event.target) && 
            event.target !== loginLink && 
            !event.target.closest('.content')) {
            content.style.display = "none";
        }
    });

    // Prevenir que el clic dentro del formulario de login cierre el mismo
    if (content) {
        content.addEventListener("click", function(event) {
            event.stopPropagation();
        });
    }

    document.addEventListener("click", function(event) {
        // Para el menú usuario
        if (menuUsuario && !event.target.closest('.iconos-derecha')) {
            menuUsuario.style.display = "none";
        }
        
        // Para el menú opciones
        if (menuOpciones && !event.target.closest('.contenedor-izquierda')) {
            menuOpciones.style.display = "none";
        }

        // Para el login
        if (content && !event.target.closest('.content') && 
            event.target !== loginLink && 
            !event.target.closest('#icono-usuario')) {
            content.style.display = "none";
        }
    });
});