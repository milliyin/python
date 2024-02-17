# Twitter Bot

<!--Remove the below lines and add yours -->

This Python script serves as a Quote generator & Upload them to Twitter account with a media.

### Features

Config: Api Keys Fully Secured
Tweet: Tweet with text and media
Image Generator: It converts text into a media.
Quotes: Randomly From an Api

### Prerequisites
* tweepy
* json
* textwrap
* PIL
* requests

### How to run the script

<!--Remove the below lines and add yours -->

```
$ python main.py
```

### Screenshot/GIF showing the sample use of the script

<!--Remove the below lines and add yours -->

![input_image](Output.png)
### Important Files

config.json: Configuration file containing API key.

## Working

Passwords are encrypted using Fernet symmetric key encryption provided by the cryptography library.
The script interacts with JSON files (config.json and database.json) for configuration and data storage.
Data manipulation functions handle adding, updating, deleting, and displaying password entries.
The script encrypts passwords before storing them and decrypts them when displaying.

## _Author Name_

<!--Remove the below lines and add yours -->
This script was created by [milliyin](https://github.com/milliyin)
Feel free to contribute to this project by submitting issues or pull requests.
