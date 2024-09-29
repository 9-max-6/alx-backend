import kue from 'kue';
import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// redis client
const client = createClient();

// kue queue
const queue = kue.createQueue();

// express server
const app = express();
const port = 1245;

// redis client event handlers
client
  .on('error', (err) => {
    console.log('Redis client not connected:', err.toString());
  })
  .on('command', (command) => {
    console.log('Executing Redis command:', command);
  })
  .on('connect', async () => {
    console.log('Redis client connected');

    // express server
    app.listen(port, () => {
      console.log('Express server listening on port number: ', port);
    });

    // set available seats to 50
    await reserveSeat(50);
  });

// client actions
const reserveSeat = async (number) => {
  try {
    const result = await client.set('available_seats', number);
    if (result === 'OK') {
      return true;
    } else {
      return false;
    }
  } catch (err) {
    console.log('Error when reserving a seat', err.toString());
    return false;
  }
};

const getCurrentAvailableSeats = async () => {
  try {
    const availableSeatCount = await client.get('available_seats');
    return availableSeatCount;
  } catch (err) {
    console.log('Error when getting current available seats');
    throw err;
  }
};

// globals - reservationEnabled
let reservationEnabled = true;

// express server routes
app.get('/available_seats', async (req, res) => {
  try {
    const availableSeats = await getCurrentAvailableSeats();
    return res.json({
      numberOfAvailableSeats: availableSeats,
    });
  } catch (err) {
    console.log(
      'Error when getting available seats in express server route',
      err.toString()
    );
  }
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({
      status: 'Reservation are blocked',
    });
  }

  // creating seat reservation job
  const job = queue.create('reserve_seat');
  job
    .on('complete', () => {
      console.log('Seat reservation job', job.id, 'completed');
    })
    .on('failed', (err) => {
      console.log('Seat reservation job', job.id, 'failed:', err.toString());
    })
    .on('enqueue', () => {
      return res.json({
        status: 'Reservation in process',
      });
    });

  job.save((err) => {
    if (err) {
      return res.json({
        status: 'Reservation failed',
      });
    }
  });
});

app.get('/process', (req, res) => {
  // Acknowledge that queue processing has started
  res.json({
    status: 'Queue processing started',
  });

  // Process the queue
  queue.process('reserve_seat', async (job, done) => {
    try {
      let currentAvailableSeats = await getCurrentAvailableSeats();
      currentAvailableSeats = parseInt(currentAvailableSeats, 10);

      if (currentAvailableSeats > 0) {
        const newAvailableSeats = currentAvailableSeats - 1;
        await reserveSeat(newAvailableSeats);

        if (newAvailableSeats === 0) {
          reservationEnabled = false;
        }

        done();
      } else {
        done(new Error('Not enough seats available'));
      }
    } catch (err) {
      done(err);
    }
  });
});

// run redis client
client.connect();
