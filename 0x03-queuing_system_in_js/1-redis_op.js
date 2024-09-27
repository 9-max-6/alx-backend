import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

const setNewSchool = (schoolName, value) => {
  client
    .set(schoolName, value, print)
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
client.on('connect', () => {
  console.log('Redis client connected to the server');

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

client.connect();
