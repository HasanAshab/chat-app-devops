FROM python:3.9-slim-buster AS base

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && apt-get install -y netcat


FROM base AS dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint scripts
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh && chmod +x entrypoint.sh

# copy project
COPY . .

# run entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]


FROM base AS build

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM base AS prod

# install dependencies
COPY --from=build /app/wheels /wheels
COPY --from=build /app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint scripts
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g' entrypoint.prod.sh && chmod +x entrypoint.prod.sh

# copy project
COPY . .

# set non-root user
RUN addgroup --system app && adduser --system --group app && \
  chown -R app:app /app
USER app

# run entrypoint script
ENTRYPOINT ["/app/entrypoint.prod.sh"]