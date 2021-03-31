# docker

### Pull image from docker hub
<p> docker pull <image> </p>

### Run docker in detachable mode
<p>
docker run -d -n [name_this_container] [image_name]
docker container run --name pgDOCK -e POSTGRES_PASSWORD=reporter -d -p 5432:5432 -v pgdata:/var/lib/postgresql/data  postgres
Use --cpus="3", the container is guaranteed at most three of the CPUs.
</p>

### Connect to container
<p>
docker exec -i -t [image_name] [cmd_like_(/bin/bash)]
docker exec -it <container name> /bin/bash
docker exec --tty --interactive pgDOCK psql -h localhost -U postgres -d postgres
docker cp postgres:/app/<file> .
</p>

### START/STOP/DELETE container
<p>
docker stop pgDOCK
docker start pgDOCK
docker rm -f pgDOCK
docker container stop $(docker container ls -qa)
</p>

### VOLUMES
<p>
docker volume create pgdata
docker volume ls
docker volume rm -f <volume>
docker volume inspect <volume>
</p>

### DOCKER NETWORK
<p>
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id> (GET IP OF CONTAINER)
</p>

### SYSTEM DETAILS
<p>
docker system df
docker system events
docker system info
docker system prune (DELETE ALL)
</p>

https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/

### IMAGE OPS
To remove dependency we can save the docker image to compressed file then remove all versions/child images, now load the file as image.

docker save -o <output_file> <image:version>|gzip <output_file>
docker load -i <output_file>
