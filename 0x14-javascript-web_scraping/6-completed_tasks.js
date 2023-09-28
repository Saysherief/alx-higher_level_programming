#!/usr/bin/node
// A script that computes the number of tasks completed by user id
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (err, response, body) => {
  if (err == null) {
    const taskNo = {};
    const todos = JSON.parse(body);
    todos.forEach(todo => {
      if (todo.completed) {
	const userId = String(todo.userId);
        taskNo[userId] = (taskNo[userId] || 0) + 1;
      }
    });
    console.log(taskNo);
  }
});
