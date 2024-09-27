import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '+254745381118',
  message: 'Hi there software engineer',
};

const job = queue.create('push_notification_code', jobData).save((error) => {
  if (error) {
    console.error('Notification job failed');
  } else {
    console.log(`Notification job created: ${job.id}`);
    console.log('Notification job completed');
  }
});
