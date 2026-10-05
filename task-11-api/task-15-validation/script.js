const form = document.getElementById("registrationForm");
const message = document.getElementById("message");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const birthDate = document.getElementById("birthDate").value;

    if (!email) {
        message.textContent = "Введите email";
        return;
    }

    if (!email.includes("@")) {
        message.textContent = "Введите корректный email";
        return;
    }

    if (!birthDate) {
        message.textContent = "Введите дату рождения";
        return;
    }

    const selectedDate = new Date(birthDate);
    const today = new Date();

    if (selectedDate > today) {
        message.textContent = "Дата рождения не может быть в будущем";
        return;
    }

    message.textContent = "Данные успешно прошли проверку";
});
