#!/usr/bin/node

//script to compute number of tasks completed by userid

const request = require('request');

function countCompletedTasks(apiUrl) {
  request.get(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const completedTasks = {};

      // Count completed tasks for each user
      body.forEach((task) => {
        if (task.completed) {
         if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 1;
         } else {
           completedTasks[task.userId]++;
         }
      }
   });

    //Print the results
    Object.keys(completedTasks).forEach((userId) => {
      console.log(`${userId} : ${completedTasks[userId]}`);
    });
  }
});
}

// Check if the API URL argument is provided
if (process.argv.length < 3) {
  console.error(error);
} else {
  const apiUrl = process.argv[2];
  countCompletedTasks(apiUrl);
}
