import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) =>
  console.log('Redis client not connected to the server:', err)
);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.connect();

const setNewSchool = (schoolName, value) => {
  client
    .set(schoolName, value)
    .then((confirmationMessage) => {
      console.log('Reply:', confirmationMessage);
    })
    .catch((err) => {
      console.error(`Failed to set school ${schoolName}:`, err);
    });
};

const displaySchoolValue = (schoolName) => {
  client
    .get(schoolName)
    .then((schoolValue) => {
      console.log(schoolValue);
    })
    .catch((err) => {
      console.error(`Failed to get value for ${schoolName}:`, err);
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
