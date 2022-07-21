
Battleships is a terminal game made in python, it runs on heroku

![heroku](images/heroku.png)

Click [here](https://project-3-ci.herokuapp.com/) to view the live web site 

![amiresponsive](images/amiresponsive.png)

Battleships is a classic pen and paper game where a grid is drawn out and ships are located randomly on the grid adn the player has to guess where they are before thiers gets destroyed. 

In my version the player will first enter thier name and they will be asked if they want to play on the normal grid size, they can change it to highest 10 (which would be 10 rows and 10 columns) or to the lowest 3. It will then ask if they want the normal amount of ships and can change it. 

The ships are marked * on the bored and areas that have been hit will be marked X. 

The player and the computer take turns until all ships on one side have been destroyed.


## Features
<br>

### Exisiting Features

#### Customisable

 - In this version of the game the user is able to control:
    - how big the grid is
    - how many ships are on the field

### random board generation

- random boards are generated both for the player and computer

### Score

- has a score counter to show who is in the lead

### input validation and error checking

- values that are entered by the user will be checked for validation, eg if its a number it will give the user a message saying give a number
- you cannot enter coordinates outside of the grid
- you cannot enter the same coordinate twice

<br>

## Future Features
- powerups, where if you hit a hit a powerup you can take 2 guesses instead of 1 or be able to move a ship to a different spot
- Timer, so the player has a certain amount of time to guess or thier turn will be skipped

## Data Model
<br>

I decided to use functions and variables to store all the data needed such as the player board the computer boards and ect.

for example the player_board variable holds the list of the actual board with the ships on it and displayboard funciton will display the board appropriately

this allowed me to edit the variables within the main function so that the boards are editable

## Testing
<br>

I have tested my game by:
    - playing the game to see if i can spot out any bugs and asked a couple of friends to play it
    - pass the code with PEP8 linter and confirmed there are no __major__  problems
    - tested in the local code institute heroku terminal

## Bugs

### Solved Bugs
- The first bugs I encountered was input validation. How i solved this was catching them with the try and except terms instead of it crashing the whole program adn makign it restart
- another bug was being able to enter the same coordinates. How i solved this was adding all the gusses into a list and looping the new guess through that list to see if it has already been said so the code will give a error saying "you have attempted this coordinate already" and allowing the user to guess again. This also applied to the computers guesses aswell because they both used the same logic so i had to add a list for the computer guesses and loop through it
- another bug was the scoreboard not working as the values was not going up. the reasons the values was not going up was because I was changing the value to go higher in a different function and that wouldnt change the value outside of the function. How I solved this was adding the code into the main game function so the variables value is abled to be changed without having to use the global tag (which i heard is bad practice)

## Remaining Bugs
- No bugs found

## Validator testing
- PEP8 no major issues

## Deployment
This project was deployed onto Code Institute mock terminal Heroku

How to deploy:
    - Create a new Heroku app on the website
    - ensure the buildblock is Python and NodeJS (has to be in that order)
    - link the app to the repository
    - click on deploy at the bottom of the page

## Credits
- Code institute for the deployment terminal