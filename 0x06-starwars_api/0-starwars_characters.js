#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actrs = JSON.parse(body).characters;
  exctOdr(actrs, 0);
});
const exctOdr = (actrs, x) => {
  if (x === actrs.length) return;
  request(actrs[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exctOdr(actrs, x + 1);
  });
};
