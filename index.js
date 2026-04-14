const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Версия приложения (меняй это для теста!)
const VERSION = "1.0.0";

app.get('/', (req, res) => {
  res.send(`
    <h1>🎉 Node.js CI/CD App</h1>
    <p>Версия: <strong>${VERSION}</strong></p>
    <p>Статус: <strong>Работает!</strong></p>
    <p>Обновлено: ${new Date().toLocaleString('ru-RU')}</p>
  `);
});

app.get('/api/ping', (req, res) => {
  res.json({ message: 'pong', version: VERSION });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT} (v${VERSION})`);
});
