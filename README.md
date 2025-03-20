# doordash-scraper

## Description
This script scrapes menu items from a DoorDash restaurant page using Playwright and Scrapybara.

## Setup Instructions

### Install Rye
```sh
curl -sSf https://rye.astral.sh/get | bash
source ~/.rye/env
```

```sh
git clone https://github.com/yourusername/doordash_scraper.git
cd doordash_scraper
rye sync
```

### Create a .env file with your Scrapybara API key
```sh
SCRAPYBARA_API_KEY=your_api_key_here
```

### Run the Script
```sh
rye run start
```
