const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('v1.0.2'));
app.listen(3000, () => console.log('v1.0.2'));