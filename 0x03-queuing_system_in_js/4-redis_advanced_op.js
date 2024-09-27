import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const hashKey = 'HolbertonSchools';
const hashValue = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
  Object.entries(hashValue).forEach(([innerKey, innerValue]) => {
    createHash(hashKey, innerKey, innerValue);
  });
  displayHash(hashKey);
});

const createHash = (hashKey, innerKey, innerValue) => {
  client.hSet(hashKey, innerKey, innerValue).then((result) => {
    console.log(`Reply: ${result}`);
  });
};

const displayHash = (hashKey) => {
  client
    .hGetAll(hashKey)
    .then((result) => {
      console.log('Hash contents:', result);
    })
    .catch((err) => {
      console.log('Error retrieving hash:', err.toString());
    });
};

client.connect();
