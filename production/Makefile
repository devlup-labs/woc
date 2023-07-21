BUILD_NAME=robotics-web
BUILD_TAG=$$(git log -1 --pretty=%h)

build:
	@docker build -t ${BUILD_NAME}-backend:${BUILD_TAG} -t ${BUILD_NAME}-backend:latest -f backend/Dockerfile backend
	@docker build -t ${BUILD_NAME}-frontend:${BUILD_TAG} -t ${BUILD_NAME}-frontend:latest -f frontend/Dockerfile frontend

.env:
	@cp .env.example .env

launch: .env
	@docker-compose up -d

stop:
	@docker-compose down

logs:
	@docker-compose logs -f

ex-django:
	@docker exec -it $$(echo "$$(docker ps --filter "name=django")" | awk 'NR > 1 {print $$1}') sh

ex-vue:
	@docker exec -it $$(echo "$$(docker ps --filter "name=vue")" | awk 'NR > 1 {print $$1}') sh

ex-postgresql:
	@docker exec -it $$(echo "$$(docker ps --filter "name=postgresql")" | awk 'NR > 1 {print $$1}') sh
