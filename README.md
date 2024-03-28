# Movie_Recommendation_System

![Image Alt text](/images/img1.jpg)
![Image Alt text](/images/img2.jpg)
![Image Alt text](/images/img3.jpg)

### Deploy Locally

- Install Python 3

- Install the python packages in 'requirements.txt'

- Run the application

  `python3 app.py`

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
