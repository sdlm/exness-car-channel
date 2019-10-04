FROM python:3.7
ENV APP_HOME="/app"
WORKDIR ${APP_HOME}
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["run"]