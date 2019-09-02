in this step, we'll set up the basic file structure so that we have a clean environment to work with for all of our desired dApps. You'll be able to use it over and over as long as you need to, because it has all the dependencies set up.

First, let's create a folder called dapp, which will contain all of our files. Then, with your Terminal or command line, execute truffle init to set up Truffle, making sure that you're inside the dapp folder.

After installing Truffle in that folder, run npm init to set up your package.json file of  Node.js that will allow you to install npm plugins. It will ask you for some general information about your project; simply fill it in as you please or press Enter to leave them empty, which is what I usually do unless I'm planning on distributing that project for others to use.

You'll see that you have the following folders created:

- **contracts/:** Where your contracts will go. Right now, it has a migrations contract to update your contracts as you improve your code.
- **migrations/:** Here is where you define how your smart contracts will be deployed, what parameters the constructor will have, and so on.
- **test/:** Your tests will go here for your smart contracts and dApps.
- **package.json:** The main npm file, which is used to install packages from the node registry.
- **truffle-config.js:** A configuration file to define how you'll connect to the blockchain, what Ethereum account you'll use, and so on.
