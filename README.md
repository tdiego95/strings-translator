# strings-translator
Python script which generates localizated strings for Android and iOS using google translate API.

# Usage

1) Add your default en strings in the 'strings.xml' file.<br />
Just copy and past them from your project with their normal format : 
    - ```<string name="key">value</string>``` for Android
    - ```"key"="value";``` for iOS
    - ```value``` for plain text

2) Run the script for the platform you want : 
    - ```python translator.py -android```
    - ```python translator.py -ios```
    - ```python translator.py -plainText```

3) Wait the end of the script and then check your 'strings.xml' file.

# Note 
Sometimes, because of google translate api limits, you might run into the following error :<br />```_ssl.c:980: The handshake operation timed out```<br />
If it happens just clean your file and start the script again.
