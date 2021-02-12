# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY . /app
RUN npm install
CMD ["npm", "run", "build"]