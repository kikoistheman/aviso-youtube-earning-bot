# Aviso YouTube Earning Bot

This repository contains a Selenium-based bot to automate tasks on the Aviso YouTube earning platform. The bot logs into Aviso, navigates to the YouTube earning page, and interacts with dynamic elements to simulate user actions and earn credits.

## Features

- Automated login to Aviso platform
- Navigates to the YouTube earning page
- Interacts with dynamic elements to simulate user actions
- Captures screenshots of key actions
- Calculates and displays USD balance based on earned credits

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/kikoistheman/aviso-youtube-earning-bot.git
    cd aviso-youtube-earning-bot
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download and install [Google Chrome](https://www.google.com/chrome/).

4. Download the matching version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system PATH.

## Usage

1. Update the `username` and `password` variables in the `Test` class with your Aviso credentials.

2. Run the bot:

    ```bash
    python aviso_youtube_earning_bot.py
    ```

3. If prompted, enter the code sent to your email.

## Note

- Ensure your ChromeDriver version matches your installed Google Chrome version.
- The bot runs in headless mode by default. To see the browser actions, remove the `--headless` option in the `__init__` method.

## Disclaimer

This bot is for educational purposes only. Use it responsibly and ensure compliance with Aviso's terms of service.

## License

This project is licensed under the MIT License.
