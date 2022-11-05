# └─$ docker build -t jwash:latest .
# └─$ docker run -p 3000:3000 --rm -it jwash:latest

FROM node:alpine3.14 AS base
WORKDIR /usr/src/app
COPY flag.txt package.json package-lock.json server.js ./
RUN mkdir -p ./svelte
COPY svelte svelte

FROM base as dependencies
WORKDIR /usr/src/app/svelte
RUN npm i --only=production && cp -R node_modules node_modules_production && npm i && npm run build
WORKDIR /usr/src/app
RUN npm i --only=production && cp -R node_modules node_modules_production && npm i

FROM dependencies as release
WORKDIR /usr/src/app/svelte
COPY --from=base /usr/src/app/flag.txt .
COPY --from=dependencies /usr/src/app/svelte/dist ./dist
WORKDIR /usr/src/app
COPY --from=dependencies /usr/src/app/node_modules_production ./node_modules
RUN addgroup -S -g 1001 ctf-non-root-group && adduser -S -u 1001 -G ctf-non-root-group ctf-non-root-user
EXPOSE 3000
USER 1001
ENV FLAG flag.txt
ENTRYPOINT [ "npm", "start"]

