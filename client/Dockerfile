FROM node:16 AS base

# set work directory
WORKDIR /app

# install dependencies
COPY package*.json .
RUN npm i

# copy project
COPY . .


FROM base AS dev
ENTRYPOINT [ "npm", "start" ]


FROM base AS build

# build app
RUN npm run build


FROM nginx:1.23.2-alpine AS prod

# copy nginx config
COPY /.nginx/nginx.conf /etc/nginx/conf.d/default.conf

# remove default stuff
RUN rm -rf .//usr/share/nginx/html/*

# copy build
COPY --from=build /app/build /usr/share/nginx/html

# set non-root user with nessary permissions
RUN touch /var/run/nginx.pid
RUN chown -R nginx:nginx /var/run/nginx.pid /usr/share/nginx/html /var/cache/nginx /var/log/nginx /etc/nginx/conf.d
USER nginx

ENTRYPOINT ["nginx", "-g", "daemon off;"]
