# Flask Container Controller

Watch the video, in French:
[![Watch the video](img/yt.png)](https://www.youtube.com/watch?v=w2WX7U_lgP4)

This project is a proof of concept (POC) for a web application that allows users to control Docker containers. It provides a simple interface to create, delete, and execute commands within containers.

## Installation

To run this project, please follow these steps:

1. Clone the repository: `git clone https://github.com/0xbochi/docker-website-controller`
2. Navigate to the project directory: `cd flask-container-controller`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Start the Flask server: `python app.py`
5. Open your web browser and go to `http://localhost:5000/main` to access the application.

Note: Make sure you have Docker installed and running on your machine before starting the Flask server.

## Usage

### Main Page

The main page displays a list of existing containers. It can be accessed by visiting `http://localhost:5000/main`. From this page, you can:

- View the list of containers.
- Create a new container.
- Delete one or multiple containers.
- Execute commands within a container.

### Create Page

To create a new container, go to `http://localhost:5000/create`. Enter the desired name and Docker image, then click the "Create" button.

### Delete Page

To delete one or multiple containers, go to `http://localhost:5000/delete`. Select the containers you want to delete and click the "Delete" button.

### Execute Page

To execute commands within a container, go to `http://localhost:5000/exec`. Select the container you want to execute commands in and click the "Execute" button. You will be redirected to the terminal page.

### Terminal Page

The terminal page (`http://localhost:5000/terminal/<container_id>`) displays a terminal-like interface to execute commands within the selected container. Enter the desired command and press Enter to execute it. The output will be displayed below the input area.

## Technologies Used

- Flask: Python web framework for building the application.
- Docker SDK for Python: Python library for interacting with Docker.
- Flask-SocketIO: Extension for Flask to enable real-time communication with the server.

## Disclaimer

This project is a proof of concept and should not be used in production environments. It lacks security measures and error handling required for a robust container management system. It is recommended to use this project only for educational or experimental purposes.

Feel free to explore and modify the code to enhance the functionalities or adapt it to your specific needs.
