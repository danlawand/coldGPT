const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express();
const port = 8080;

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'frontend', 'dist')));

app.post('/sendText', async (req, res) => {
  const text = req.body.text;
  try {
    const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/sendText`, { text: text });
    res.send({ response: response.data.response });
  } catch (error) {
    res.status(500).send({ error: 'Error connecting to the backend' });
  }
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend', 'dist', 'index.html'));
});

app.listen(port, () => {
  console.log(`Frontend server running at http://localhost:${port}`);
});

