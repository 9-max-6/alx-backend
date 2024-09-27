import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print); // Use lowercase 'set'
};

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await client.get(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Failed to get value for ${schoolName}:`, err);
  }
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});

client.connect();
