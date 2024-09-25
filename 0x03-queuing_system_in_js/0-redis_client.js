import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis Client Error', err));

async function connectRedis() {
  try {
    await client.connect();
    console.log('Redis client connected to the server');
  } catch (err) {
    console.error('Redis client not connected to the server::', err);
  }
}

connectRedis();
