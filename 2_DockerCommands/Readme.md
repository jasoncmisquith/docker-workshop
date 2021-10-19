
# Clone the repo

```
sudo apt install git
```
```
mkdir ~/dockerworkshop
```
```
cd ~/dockerworkshop
```
```
git clone https://github.com/jasoncmisquith/docker-workshop.git
```
---

# Docker hands-on

### Topics covered:
1. docker run
    - port publishing
    - name
    - stdin
    - tty
    - daemon
2. docker exec
3. docker container ls
4. docker container stop
5. docker container rm
6. docker images


Here we will first spawn a simple alpine container, with no additionally installed packages.

### docker run
```
docker run --name myfirstcontainer -it alpine sh
```
---

### docker exec
```
docker exec -it myfirstcontainer sh
```

exec with container id is possible
```
docker container ls
```
```
docker exec -it asdw23fq2ef
```
As we saw above the container did not have any unecessary usable package and is very light weight.
Let us now try using a alpine container with python installed.

Is there a difference between below commmands
```
docker run --name alpinewithpython -it python:3.9-alpine
docker run --name alpinewithpython -it python:3.9-alpine python
docker run --name alpinewithpython -it python:3.9-alpine sh
```

---

### docker build

Let us first build a simple docker image with a python script
```
docker build . -f Dockerfile_AlpineWithPythonScript --tag mypythonimage:latest
```

```
docker run -it mypythonimage:latest
```
```
docker run -it mypythonimage:latest sh
```

In above exercise we were able to run our script inside the container, we noticed that the container stopped immediately after the script exited.

---

Let us try something else now! lets load a simple python easter egg.

```
docker build . -f Dockerfile_PythonHttpServer -p 8000:8000 --tag mysimpleserver:latest
```
```
docker run -it --name mycontainerserver mysimpleserver:latest
```

For this exercise we will use an official python docker image and start a simple python server which will serve index.html

If above steps have run fine  you should be able to open

http://localhost:8000/index.html

Here we experience how the container's 8000 port is now connected to your machine's 8000 port, note that you can always publish to a port of your choice if its not used by any other process. Try using another port.

---

Manually remove container
```
docker rm mycontainerserver
```
The above command should have given error telling cannot stop running container.

To stop container run
```
docker container stop mycontainerserver
```
Then try removing it with
```
docker rm mycontainerserver
```
## Reference:

To run python on different distributions, visit https://hub.docker.com/_/python