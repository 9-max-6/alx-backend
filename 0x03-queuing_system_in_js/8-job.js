import kue from 'kue';
const queue = kue.createQueue();

export default function createPushNotificationsJobs(jobs) {
  if (!Array.isArray(jobs)) {
    console.error('Jobs is not an array');
  }
  const job = queue.create('push_notification_code_3').save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('error', (err) => {
    console.error(`Notification job ${job.id} failed: ${err}`);
  });

  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
}
