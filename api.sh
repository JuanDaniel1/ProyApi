

docker build -t app_api .
docker run -t -d -p 8090:8090 --name api app_api

docker ps -a