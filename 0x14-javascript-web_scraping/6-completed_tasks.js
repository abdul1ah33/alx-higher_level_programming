#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const userTasks = {};

    // Iterate over each task
    data.forEach(task => {
      if (task.completed) {
        if (userTasks[task.userId]) {
          userTasks[task.userId] += 1;
        } else {
          userTasks[task.userId] = 1;
        }
      }
    });

    // Print only users with completed tasks
    console.log(userTasks);
  } catch (e) {
    console.error('Error parsing JSON:', e);
  }
});

