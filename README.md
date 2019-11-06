# RockPaperScissorLizardSpock
README

Locations

gameAPI

a) Docker:  shikharadroit/dockerhub:rock_paper_scissor_l_s
b) Github: git…

Front-End: git……..

Instructions to install and run the project
1. GameAPI:
	a) Pull the docker image from dockerhub → docker pull 					    shikharadroit/dockerhub:rock_paper_scissor_l_s

	 b) Run the docker container
	    sudo docker run -d -p 5000:5000 shikharadroit/dockerhub:rock_paper_scissor_l_s

C: Now the server should be up and running

2. Run front-End
	GIT clone
	Go to the directory location
	To run the page: front_end_filename <>google-chrome frontIdx.html

0.0.0.0 → local host
Enjoy the game.

Files
1. Client-front
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
