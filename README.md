# Claire - Guild Receptionist Discord Bot

Welcome to the **Claire** Discord bot repository! Claire is your charming and professional guild receptionist, ready to assist adventurers with their quests, manage project requests, and add a touch of cuteness to your server.

## Features
- **Quest Handling**: Assigns projects based on member skills.
- **Project Explanation**: Provides detailed breakdowns of tasks.
- **Skill Matching**: Warns members if they aren’t suitable for a task, but always cheer them on.
- **Friendly and Flirty Persona**: Balances professionalism with a bit of playfulness.

## Getting Started
### Prerequisites
- Discord Developer Account
- Node.js (for running the bot)
- A Discord server with appropriate bot permissions

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/accelbia/claire-san.git
   ```

2. Navigate to the project directory:
   ```bash
   cd claire-discord-bot
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Set up your `config.json` file with the necessary bot token and settings:
   ```json
   {
     "token": "YOUR_DISCORD_BOT_TOKEN",
     "prefix": "!"
   }
   ```

5. Run the bot:
   ```bash
   npm start
   ```

## Usage
- Add the bot to your server using its invite link.
- Use the bot with the defined prefix to interact.
- Claire will handle project requests, assign tasks based on member skills, and provide explanations if needed.

## Example Commands
- `!assign [project]`: Assigns a project to a specific member based on their skills.
- `!warn [member]`: Warns a member if a task is too challenging for them.
- `!help`: Provides a list of commands and usage instructions.

## Contributions
Contributions are welcome! If you’d like to contribute to **Claire**, please open an issue or submit a pull request. Be sure to follow the project’s coding style and guidelines.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
