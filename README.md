# Movie_Recommendation_System

### Deploy on Docker

- Install Docker and Docker-compose

```
  git checkout Docker
```

- Install Docker and Docker-compose

  ```
  curl -fsSL https://get.docker.com -o get-docker.sh
  ```

  ```
  sudo sh get-docker.sh
  ```

  ```
  sudo apt install docker-compose -y
  ```

- Deploy Application on Docker

Build Image:

```
docker build . -t movie
```

Run Image:

```
docker run -p 5001:5001 --name movie-recommendation-system movie
```

Remove Image:

```
docker rmi movie
```

Remove All Images:

```
  docker system prune -a
```
