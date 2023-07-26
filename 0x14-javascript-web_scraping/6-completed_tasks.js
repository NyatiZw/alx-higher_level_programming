#!/usr/bin/node

//script to compute number of tasks completed by userid

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
      console.error(error);
  } else if (response.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (dic[tasks[i].userId] === undefined) {
          dic[tasks[i].userId] = 1;
        } else {
          dic[tasks[i].userId]++;
        }
      }
    }
    console.log(dic);
    } else {
      console.log('Error code: ' + response.statusCode);
    }
});
