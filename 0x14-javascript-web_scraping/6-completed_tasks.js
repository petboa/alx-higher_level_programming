#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];


request(url, function (err, response, body)
{   
    if (err)
    {
        console.log(err);
    }
    else
    {
        let completedTasks = {};
        let tasks = JSON.parse(body);
        for (let i = 0; i < tasks.length; i++)
        {
            if (tasks[i].completed === true)
            {
                if (completedTasks[tasks[i].userId] === undefined)
                {
                    completedTasks[tasks[i].userId] = 1;
                }
                else
                {
                    completedTasks[tasks[i].userId] += 1;
                }
            }
        }
        console.log(completedTasks);
    }
}
);
