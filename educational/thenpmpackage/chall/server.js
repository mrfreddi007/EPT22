const express = require('express');
const serialize = require('node-serialize');

var app = express();
process.setMaxListeners(0);

app.use(express.json({ verify: (req, res, buf) => { req.rawBody = buf }}));
app.use(express.static(__dirname + "/svelte/dist/"));
app.post('/wash', function(req, res) {
  if (!req.is('application/json')) {
    res.sendStatus(400)
} else {
    if (req.body && Object.keys(req.body).length > 0) {
      var obj = serialize.unserialize(req.body);
      res.end(JSON.stringify(obj,function(k, v) { return v ?? ""; }));
    } else {
      res.sendStatus(400)
    }
  }
});

console.log(`${new Date().toISOString().slice(0, 16)} - I'm all ear on :3000`)
const server = app.listen(3000);