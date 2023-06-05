from flask import Flask, request, render_template, redirect, url_for
import docker
from flask_socketio import SocketIO

app = Flask(__name__)
client = docker.from_env()
socketio = SocketIO(app)

@app.route('/main', methods=['GET'])
def main():
    containers = client.containers.list()
    return render_template('main.html', containers=containers)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        image = request.form.get('image')
        container = client.containers.run(image, detach=True, name=name)
        return 'Conteneur créé : {}'.format(container.name)
    return render_template('create.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        selected_containers = request.form.getlist('containers')

        for container_id in selected_containers:
            container = client.containers.get(container_id)
            container.stop()
            container.remove()
        return 'Conteneur(s) supprimé(s)'
    containers = client.containers.list()
    return render_template('delete.html', containers=containers)


@app.route('/exec', methods=['GET', 'POST'])
def execute():
    if request.method == 'POST':
        container_id = request.form.get('container')
        return redirect(url_for('terminal', container_id=container_id))
    containers = client.containers.list()
    return render_template('execute.html', containers=containers)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')




@app.route('/terminal/<container_id>', methods=['GET'])
def terminal(container_id):
    container = client.containers.get(container_id)
    return render_template('terminal.html', container_id=container_id)



@socketio.on('terminal_input')
def handle_terminal_input(data):
    container_id = data['container_id']
    command = data['command']
    container = client.containers.get(container_id)
    exec_instance = container.exec_run(command, tty=True, stdin=True, detach=False)
    output = exec_instance.output.decode()
    socketio.emit('terminal_output', output)



@app.route('/disconnect/<container_id>', methods=['GET'])
def disconnect(container_id):
    return redirect(url_for('main'))



if __name__ == '__main__':
    app.run()