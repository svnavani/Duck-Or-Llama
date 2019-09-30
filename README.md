# Duck-Or-Llama

Duck or Llama is a game inspired by the Android app "Duck or Llama". A picture of either a duck a llama will be shown on the screen and the user has a split second to decide what animal it is. Although there is no time constraint in my game, you have to match the pictures to the right animal inorder to keep playing. If you lose, your score will be displayed.

The game was made using a Flask backend. A default picture would be loaded on the screen. When the user clicks a button, the button name is sent from JS to the Flask app via an AJAX call. The Python code will return the button name, animal in the picture, and the file path for the next picture. The JS file will then determine if the user clicked the correct button. If the button was correct, the next picture will be shown and the score will be incremented. If the button was not correct, an alert will be shown with the score and the page will refresh to restart the game.

Happy playing!
