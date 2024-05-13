# PartyUp

PartyUp is a Discord bot designed to streamline the process of creating and managing parties and queues within your server. Whether you're running a gaming community and need to organize parties for raids, or managing a programming server and need to create queues for code reviews, PartyUp has you covered.

## Usage

PartyUp uses slash commands for interaction, providing a simple and intuitive interface for users.

### User Commands

Here are the commands available to all users:

- `/party create <role-id> <size>`: This command allows you to create a new party for a specific role. 
  - `role-id`: ID of the role of the party you want to create. This should be a role that starts with the LFG prefix.
  - `size`: Size of the party you want to create. This is the number of members you want in the party.

- `/party adjust <role-id> <size>`: This command allows you to adjust the size of an existing party for a specific role. 
  - `role-id`: ID of the role of the party you want to adjust. This should be a role that starts with the LFG prefix.
  - `size`: New size of the party. This should be greater than or equal to the current number of players in the party.

### Admin Commands

Here are the commands available to admins:

- `/party list <role-id>`: This command allows you to list all the parties for a specific role. 
  - `role-id`: ID of the role of the parties you want to list. This should be a role that starts with the LFG prefix.

- `/party remove <role-id>`: This command allows you to remove an existing party for a specific role. 
  - `role-id`: ID of the role of the party you want to remove. This should be a role that starts with the LFG prefix.

## Development

PartyUp was developed with a focus on robustness and ease of use. The project utilizes Nix flakes, a powerful package management system that ensures reproducible builds and a consistent development environment. To further enhance the development experience, a devcontainer is included in the project.

The Python packages for the project are managed with Poetry, a tool that allows for precise control over dependencies and ensures that the project runs the same way in every environment.

The main Python dependency for the project is pycord, a modern, easy-to-use, feature-rich, and async-ready API wrapper for Discord written in Python.

Included in the repository is a `run.sh` script. This script runs the bot locally and is designed to auto restart if any changes are made to the code. This allows for rapid testing and iteration during development.

## Deployment

When it comes to deployment, PartyUp is hosted on a reserved VM on Replit. Replit is an online, cloud-based IDE that supports dozens of programming languages and has robust support for collaborative coding.

You can view the Replit for the project [here](https://replit.com/@elliottchalford/PartyUp). This is where the code for PartyUp lives and is run.

The deployment of the bot can be viewed [here](https://party-up-elliottchalford.replit.app). This is where the bot is actively running and interacting with users on Discord.