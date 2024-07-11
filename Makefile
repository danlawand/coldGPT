DOCKER_BUILD_FRONTEND := docker build -t hotmartgpt_frontend ./frontend
DOCKER_RUN_FRONTEND := docker run -p 8080:8080 hotmartgpt_frontend
DOCKER_BUILD_BACKEND := docker build -t hotmartgpt_backend ./backend
DOCKER_RUN_BACKEND := docker run -p 5000:5000 hotmartgpt_backend

front: build_front run_front

back: build_back run_back

build_front:
	${DOCKER_BUILD_FRONTEND}

build_back:
	${DOCKER_BUILD_BACKEND}

run_front:
	${DOCKER_RUN_FRONTEND}

run_back:
	${DOCKER_RUN_BACKEND}
