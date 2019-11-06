# RockPaperScissorLizardSpock

NOTE: In the frontend of the game use 'r' to reset the scoreboard anytime.

Locations
1. Backend:
	a) Get docker image from dockerhub.
	Docker tag link:  shikharadroit/dockerhub:rock_paper_scissor_l_s
	
2. Front-End: File_name: front_end.html

Instructions to install and run the project
1. To run backend server:   
	a) Pull the docker image from dockerhub → docker pull shikharadroit/dockerhub:rock_paper_scissor_l_s
        b) Run the docker container
	    sudo docker run -d -p 5000:5000 shikharadroit/dockerhub:rock_paper_scissor_l_s

C: Now the server should be up and running

2. Run front-End
	GIT clone
	In the terminal: Go to the directory location of the file : front_end.html
	Command to run the front-end page in the browser of your choice: <browser of choice> front_end.html
	example: google-chrome frontIdx.html

3. In the front-end, in step 1, where asked to put a URL use: http://0.0.0.0:5000
4. Follow the steps on the page to play.

Enjoy the game......

Files
1. Client-front: front_end.html
2. Server-backend
		GameAPI.py : Has game logic
		HelperMethods.py : Has supporting methods used by gamelogic
		Constant.py: Has Constants
3. requiremnets.txt
4. Dockerfile


Features Implemented:
1. A single player can play with game with a computer.
2. A scoreboard with 10 most recent results.
3. Score board can be reset by pressing ‘r’
4. A Dockerfile has been provided to run a containerized version of the service.


References
1. Stackoverflow
2. Random internet searchs to collect technology-specific knowledge
3. Docker blogs

Some specific links
Access-Control-Allow-Origin:
https://medium.com/@dtkatz/3-ways-to-fix-the-cors-error-and-how-access-control-allow-origin-works-d97d55946d9

Docker:
flask + Docker:  https://runnable.com/docker/python/dockerize-your-flask-application
Binding ports: https://runnable.com/docker/binding-docker-ports
