const statusElement = document.getElementById("status");
const taskList = document.getElementById("taskList");
const retryButton = document.getElementById("retryButton");

let requestId = 0;

function loadTasks() {
    const currentRequest = ++requestId;

    statusElement.textContent = "Загрузка...";
    taskList.innerHTML = "";
    retryButton.style.display = "none";

    setTimeout(() => {

        // Проверяем, не был ли уже отправлен новый запрос
        if (currentRequest !== requestId) {
            return;
        }

        const tasks = [
            "Complete practical test",
            "Prepare presentation",
            "Submit assignment"
        ];

        if (tasks.length === 0) {
            statusElement.textContent = "Список пуст";
            return;
        }

        statusElement.textContent = "Задачи загружены";

        tasks.forEach(task => {
            const li = document.createElement("li");
            li.textContent = task;
            taskList.appendChild(li);
        });

    }, 1000);
}
