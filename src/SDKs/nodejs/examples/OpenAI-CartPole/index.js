/**
 * For more information, check: https://gym.openai.com/docs/
 */
const Client = require('../../main');
const Experiment = require('./Experiment');

const start = async () => {
    const client = await Client.initialize();

    // Create and run our experiment
    const episodeCount = 1000;
    const maxTimeSteps = 250;
    const experiment = new Experiment(client, episodeCount, maxTimeSteps);
    await experiment.run();
}

start();

