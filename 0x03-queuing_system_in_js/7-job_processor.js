import kue from 'kue';

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];
const sendNotification = (phoneNumber, message, job, done) => {
  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error);
  } else {
    job.progress(50, 100);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done(null);
  }
};

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
