import { createClient } from 'redis';

const publisher = createClient();

publisher.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.toString());
});
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log('About to send MESSAGE');
    publisher.publish('holberton school channel', message);
  }, time);
};

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
  publishMessage('Holberton Student #1 starts course', 1000);
  publishMessage('Holberton Student #2 starts course', 200);
  publishMessage('KILL_SERVER', 300);
  publishMessage('Holberton Student #3 starts course', 400);
});
