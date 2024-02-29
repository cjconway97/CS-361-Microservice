# CS 361 Microservice
 This microservice recieves POST request from a user and responds to GET requests with the last "W, A, S, or D" key press.

 Once app.py is running, the user must open the location where it's hosted (default is localhost:5001) and click into the document. Once the document is focused, any WASD key press will be posted and stored in move.json.

 With the application running, the game may make GET requests to the app and recieve a dict object back with format {"direction": "*LAST USER KEY PRESS*}.

 ![image](https://github.com/cjconway97/CS-361-Microservice/assets/107966739/0428c585-eb6e-4276-97e2-9c4d35179e3a)
