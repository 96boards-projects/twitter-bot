# Twitter Bot

# Table of Contents

- [1) Hardware](#1-hardware)
   - [1.1) Hardware Requirements](#11-hardware-requirements)
   - [1.2) Hardware Setup](#12-hardware-setup)
- [2) Software](#2-software)
   - [2.1) Install Dependencies](#21-install-dependencies)
   - [2.2) Add tokens](#22-add-tokens)
   - [2.3) Running the Bot](#23-running-the-bot)

# 1) Hardware

## 1.1) Hardware Requirements

- [Any 96Boards CE](https://www.96boards.org/products/ce/)

## 1.2) Hardware Setup

- Make sure the board is connected to an active network.

# 2) Software

**This guide assumes that [Debian OS is running on a Dragonboard410c](https://www.96boards.org/documentation/consumer/dragonboard410c/downloads/debian.md.html) on all 4 nodes. How ever the instructions hold true for other 96Boards CE Boards running Debian.**

> This project is compatible with other Linux based OS, but they might have to be tweaked accordingly.

## 2.1) Install Dependencies

```shell
$ sudo apt install python3-setuptools python3-dev python3-pip
$ sudo pip3 install wheel tweepy weather-api datetime pytz pygithub
```

## 2.2) Add tokens

- **GitHub**
  - Create a developer account at: [https://developer.github.com/](https://developer.github.com/)
  - Create an App: [https://developer.github.com/apps/building-your-first-github-app/](https://developer.github.com/apps/building-your-first-github-app/)
  - Replace <github api token> in ```bot.py``` with your GitHub access token.

- **Twitter**
  - Create a developer account at: [https://developer.twitter.com/en/apply/user](https://developer.twitter.com/en/apply/user)
  - Get access token: [https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)
  - Replace <consumer_key> in ```bot.py``` with your Twitter Consumer Key.
  - Replace <consumer_secret> in ```bot.py``` with your Twitter Consumer Secret Key.
  - Replace <access_token> in ```bot.py``` with your Twitter access token.
  - Replace <access_token_secret> in ```bot.py``` with your Twitter access token secret key.

## 2.3) Running the Bot

**Test Run**

You can run it simply as
  ```shell
  $ python3 bot.py
  ```
**Deploy**

From Shell
  ```shell
  $ python3 bot.py &
  ```

Very basic logs from the python script are pushed to Journal. These can be accessed by:
  ```shell
  $ journalctl -xel
  ```
