# Fantasy Draft AutoHighlight Viewer

> **_NOTE:_** This repository is a fork that has diverged slightly from its upstream.

Real simple python program that reads sleeperbot fantasy football draft boards to enhance your draft party by automatically playing a highlight video of the player who just got selected.

Works best with Chromecast devices, but can be viewed in a Chrome browser on your computer if you like.

## Getting Started

Download the files in this repository to a directory anywhere you like.
You'll need to edit the config.py file so that it knows a little bit about your draft. Depending on what options you'll be using, you might need to install some python packages.

### Prerequisites

- Google Chrome ([Install](https://www.google.com/chrome/))
- Python 3.x ([Install](https://www.python.org/downloads/))

Install the request package if you don't have it.

```
pip install requests
```

**Option 1 - Chromecast**

The following packages are necessary if you're going to use Chromecast:

```
pip install pychromecast
pip install protobuf
pip install zeroconf
pip install casttube
```

**Option 2 - Chrome Browser** -

If you are going to be displaying on a Chrome browser instead, install the following packages:

```
pip install selenium
```

Selenium requires a specific "webdriver" for the version of Chrome that you're running. Simple google search should help you find this and the instructions for what to do with the webdriver when you get it.

```
https://sites.google.com/a/chromium.org/chromedriver/downloads
```

### Config File

After you've created your draft board, you will need to edit the config.py file.

Open it up with any text editor.  
That file is small and only contains a few lines. Here's how it looks when you download it.

```
teams=12
rounds=7
chromeCast=False
chromeCastName="YOUR CHROMECAST NAME HERE"
autoSearch=True
boardNum=954821396060536832
```

#### boardNum

BoardNum is the number on the end of your sleeperbot URL.

```
https://sleeper.app/draft/nfl/12345
```

#### teams/rounds

Super simple stuff here. Change your teams and rounds to the number of teams and rounds in your draft.

#### chromeCast

chromeCast True or False.. If True then your vids will cast to a Chromecast. If False then they'll play on a YouTube screen on your laptop.  
If you set this to True then you also need to list your Chromecast's name in the next line. The name needs to be typed perfectly in order for it to work correctly, including all spaces, punctuation, and capitalization.
If the application cannot find your specific Chromecast then it will auto-switch to using YouTube on the computer. If you're not sure why this is happening then please check whether that computer can access that specific Chromecast and if so, make sure the Chromecast name is typed correctly.

#### autoSearch

The last option is "autoSearch" which can be either True or False.

If it's set to True, the program will go out and search YouTube for the first highlight reel it can find for that player name.

This is going to work fine for most players, however some players have common names so the YouTube search might return a vid for a different player in a different sport.

You can change this behavior by placing a specific YouTube video link of your choice in the [vDict file for your draftboard](./vDictSleeper.py).

If there is no link, then it will auto search on YouTube.

You can stop the auto search functionality altogether with autoSearch=False . If you do this, then the code will ONLY play videos for the links that you provide in the dictionary.

Here's how the first few lines of the dictionary files look after you download...
(using the vDictSleeper.py sleeperbot file since most of the users are on sleeper and not clicky)

```
vDictSleeper ={
    "RBNYGSaquonBarkley":"",
    "RBARIDavidJohnson":"",
    "RBNOAlvinKamara":"",
    "RBDALEzekielElliott":"8CJvUpV2jp0",
    "WRHOUDeAndreHopkins":"",
    "RBCARChristianMcCaffrey":"",

```

As you can see, there's one line for each player, and I've included an example of what the link should look like for Ezekiel Elliot. Do NOT change the first part of each line before the colon. The app uses that part to lookup each player as it's picked. If you change that part, the code will not be able to find anything for that player. It's very picky.

The capitalization and punctuation here also matters. Some players' names contain non-alphabetic characters like apostrophes, spaces, dashes, etc.

Going back to the Zeke example:

```
    "RBDALEzekielElliott":"8CJvUpV2jp0",
```

That will tell the code that when zeke is picked, it will pull up the following link:

```
https://youtube.com/tv#/watch?v=8CJvUpV2jp0
```

If you don't want a specific vid for a player, and you WANT the auto search, then you need to delete everything between the quotes. So a player without a specific vid link will have two double quotes at the end, followed by a comma.
Like this:

```
    "RBDALEzekielElliott":"",
```

Any change in that will probably cause problems.

The player list has been updated to fit 2023 Sleeper rookie drafts.

## To Run

Before running, make sure you've closed out of all of your open Chrome windows.

At your command line, in your installed directory, type:

```
python draftvid.py
```

If you're using Chromecast, you'll get a message stating whether you connected to your device correctly or not.

If you connected then you're ready to draft!

If you didn't connect, or aren't using Chromecast, then a Chrome window will pop up in fullscreen, ready to display your YouTube videos. In this scenario, this app is best used when you output the video (HDMI) to a big screen TV. Then enter the picks on a different device, like your phone or another laptop. Makes the experience a lot cooler.

### HINTS/TIPS

- One thing I should mention is that the first time you run this in a Chrome browser, YouTube will play an ad. For whatever reason it always does this on fresh installs and the first time you run it every day. But then afterwards, the ad doesn't pop up very often. I guess it depends on YouTube's mood at the time but sometimes you're gonna get an ad here and there. If you can figure out how to block YouTube ads, please IM me lol. The ads don't seem to pop up as often when you use Chromecast, so I guess that's another good reason to use Chromecast for this.

- You can avoid ads altogether with a YouTube subscription. They give 30 day subs for free, then you can cancel. I'll probably end up doing this for my drafts this year.

- Some player highlight videos on YouTube have ridiculously long introductions. You can skip those introductions on a video-by-video basis if you are specifying that video in the vDict file. For instance, take the zeke example from above.

```
    "RBDALEzekielElliott":"8CJvUpV2jp0",
```

If you want the vid to start at the 30 second mark, you need to add &t=30 to the yahoo vid code. Example here:

```
    "RBDALEzekielElliott":"8CJvUpV2jp0&t=30",
```

## Original Author

I am thedaynos and I have a patreon if you feel like donating to my "i don't code for free (actually i guess i do) foundation"
https://www.patreon.com/thedaynos

Feel free to report issues here on github if you have questions or find a bug.
