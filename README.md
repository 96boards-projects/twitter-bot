---
# Front Matter
# Title of your project used for the breadcrumb title and meta title.
title:  Twitter Bot

# Permalink your project will reside under on the 96boards.org website.
# separate your title's words with dashes for SEO purposes.
permalink: /projects/twitter-bot/
author: Sahaj Sarup 

# Add a description of your project
description: 

# Add the names of your images which are stored in the sub folders here.
# The first image is always used in the table at /projects/
# This section is used to add a social media share image to your project.
# Place the image you'd like to use when sharing on social media in the /assets/images/projects/
# folder and adjust the following YAML accordingly.
# High Res 1920 x 1080
# regenerated on site build
#image: 
#    path: /assets/images/projects/share_image.png
#    list:
#        - thumb.png
#        - share.png
#social:
#  name: 96Boards
#  links:
#    - https://twitter.com/96boards
#    - https://www.facebook.com/96Boards/
#    - https://www.linkedin.com/company/96boards/
#    - https://plus.google.com/+96Boards
#    - https://github.com/96boards
project:
    # Difficulty level for your project <Beginner, Intermediate, Experienced>
    difficulty_level:
     - Beginner
    # Boards that you have used in this project. For a full list of boards see 
    # this file in the 96boards/website repo - _data/boards.yml
    boards_used: 
        - all-boards
    # Verticals are catagories that your project belongs to. For a full list of verticals see 
    # this file in the 96boards/website repo - _data/verticles.yml
    verticals:
        - Maker
#Optional tags for your projects: meta-key words
tags:
- twitter
---

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
