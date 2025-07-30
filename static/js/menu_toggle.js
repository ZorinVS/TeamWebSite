document.addEventListener("DOMContentLoaded", () => {
    const burger = document.getElementById("burger");
    const menu = document.getElementById("mobileMenu");

    let isOpen = false;

    burger.addEventListener("click", () => {
        isOpen = !isOpen;

        // Анимация кнопки
        burger.classList.toggle("rotate-45");

        // Анимация меню
        if (isOpen) {
            menu.classList.remove("max-h-0", "opacity-0", "pointer-events-none");
            menu.classList.add("max-h-96", "opacity-100", "pointer-events-auto");
        } else {
            menu.classList.remove("max-h-96", "opacity-100", "pointer-events-auto");
            menu.classList.add("max-h-0", "opacity-0", "pointer-events-none");
        }
    });
});
