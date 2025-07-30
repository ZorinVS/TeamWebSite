document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  btn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
    // здесь можно анимировать саму иконку, поменяв её на крестик
  });
});
