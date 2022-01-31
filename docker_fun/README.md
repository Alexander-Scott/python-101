# 0) What is a docker container

Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

# 1) What is a docker image

```
apt install python
pip3 install requests
```

# 2) What is the most relevant docker image for our task

Most relevant docker image: https://hub.docker.com/_/python

## List all docker images on system

```
docker images
```

## List running containers

```
docker ps
```

## Running the image

```
docker run -it --rm --name my-running-script -v "/workspaces/python-101/docker_fun/":"/usr/src/myapp:ro" -w /usr/src/myapp python:latest bash -c 'pip install requests && python main.py container_file/hello_world.md hello_world123 <TOKEN>'

docker run -it --rm --name my-running-script -v "/workspaces/python-101/docker_fun/":"/usr/src/myapp/:ro" -w /usr/src/myapp -d python:latest bash -c 'sleep infinity'
```

## Important things

-v = mount location 'src:dest'
python:latest = image name
bash -c 'echo "hello"'

# 3) Building a docker image with our script

```bash
docker run -it --rm --name my-running-script docker_fun:latest container_file/hello_world.md hello_world123 <TOKEN>
```
