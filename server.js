const express = require('express');
const app = express();
const path = require('path');

// Serve static files from the "public" directory
app.use(express.static('public'));

// Route for the root URL ("/") to serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'home.html'));
  res.sendFile(path.join(__dirname, 'public', 'page2.html'));
});

// JavaScript code in home.html
document.getElementById('btn').addEventListener('click', function() {
  window.location.href = 'page2.html';
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});