const express = require('express');
const server = express();
server.post('/xml/*', (req, res) => {
    res.contentType('application/xml')
    res.sendFile(__dirname + req.url)
    })