const backBanner = document.querySelector('.back-banner');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const images = document.querySelectorAll('.back-banner img');

let currentIndex = 1; // Empezamos con la imagen central

function updateCarousel() {
  images.forEach((img, index) => {
    if (index === currentIndex - 1) {
      img.classList.remove('right');
      img.classList.add('left');
    } else if (index === currentIndex) {
      img.classList.remove('left', 'right');
      img.classList.add('center');
    } else if (index === currentIndex + 1) {
      img.classList.remove('left');
      img.classList.add('right');
    } else {
      img.classList.remove('left', 'center', 'right');
    }
  });
}

prevBtn.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  updateCarousel();
});

nextBtn.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % images.length;
  updateCarousel();
});

// Inicializar el carrusel
updateCarousel();


document.addEventListener('DOMContentLoaded', function() {
  const carousel = document.getElementById('carouselRecomendados');
  
  if (carousel) {
    // Asegura que las columnas no interfieran con las flechas
    const columns = carousel.querySelectorAll('.columna');
    
    columns.forEach(column => {
      column.style.pointerEvents = 'none'; // Desactiva eventos en columnas
      
      // Reactiva eventos solo en elementos interactivos internos
      const interactiveElements = column.querySelectorAll('a, button, .ver-ya');
      interactiveElements.forEach(el => {
        el.style.pointerEvents = 'auto';
      });
    });
    
    // Mejora la experiencia táctil en móviles
    carousel.addEventListener('touchstart', function(e) {
      const touchX = e.touches[0].clientX;
      const carouselRect = carousel.getBoundingClientRect();
      
      if (touchX < carouselRect.left + 50) {
        // Click en área izquierda - prev
        carousel.querySelector('.carousel-control-prev').click();
      } else if (touchX > carouselRect.right - 50) {
        // Click en área derecha - next
        carousel.querySelector('.carousel-control-next').click();
      }
    });
  }
});


document.querySelectorAll('.cuadro-recomendado-base img').forEach(img => {
  img.addEventListener('load', function() {
      const container = this.closest('.cuadro-recomendado-base');
      const aspectRatio = this.naturalWidth / this.naturalHeight;
      
      // Clasificación basada en la proporción
      if (aspectRatio > 1.2) {
          // Imagen horizontal
          container.classList.add('horizontal-img');
          container.classList.remove('vertical-img');
      } else if (aspectRatio < 0.8) {
          // Imagen vertical
          container.classList.add('vertical-img');
          container.classList.remove('horizontal-img');
      } else {
          // Imagen cuadrada o casi cuadrada
          container.classList.remove('horizontal-img', 'vertical-img');
      }
  });
});

