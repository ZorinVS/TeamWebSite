document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('feedback-form-wrapper');
    const showBtn = document.getElementById('show-feedback-btn');
    const closeBtn = document.getElementById('close-feedback-btn');

    if (showBtn && modal) {
        showBtn.addEventListener('click', () => {
            modal.classList.remove('hidden');
        });
    }

    if (closeBtn && modal) {
        closeBtn.addEventListener('click', () => {
            modal.classList.add('hidden');
        });
    }

    // Закрытие при клике на фон
    modal?.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.add('hidden');
        }
    });
});
