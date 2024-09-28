export const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('progress', (progress) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log(
          'Notification job',
          job.id,
          'failed:',
          err.message || err.toString()
        );
      });

    job.save();
  }
};

export default createPushNotificationsJobs;
