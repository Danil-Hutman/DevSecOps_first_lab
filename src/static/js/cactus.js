fetch("/cactus")
  .then((response) => response.json())
  .then((data) => {
    const container = document.getElementById("cactus-list");
    let html =
      "<table><tr><th>ID</th><th>Назва</th><th>Опис</th><th>Ціна</th></tr>";
    data.forEach((c) => {
      html += `<tr>
                      <td>${c.id}</td>
                      <td>${c.name}</td>
                      <td>${c.description}</td>
                      <td>${c.price} грн</td>
                    </tr>`;
    });
    html += "</table>";
    container.innerHTML = html;
  })
  .catch((err) => {
    console.error("Помилка завантаження:", err);
  });
