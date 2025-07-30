document.addEventListener("DOMContentLoaded", function () {

  const form = document.getElementById("contact-form");
  const messageBox = document.getElementById("form-message");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();  // предотвращает обновление страницы

    const formData = new FormData(form);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
      const response = await fetch("/contacts/", {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken
        },
        body: formData
      });

      const data = await response.json();

      if (response.ok) {
        messageBox.textContent = data.message || "Сообщение отправлено!";
        messageBox.classList.remove("hidden");
        form.reset();
      } else {
        messageBox.textContent = data.error || "Произошла ошибка.";
        messageBox.classList.remove("hidden");
        messageBox.classList.add("text-red-600");
      }
    } catch (err) {
      console.error("Ошибка запроса:", err);
    }
  });
});
