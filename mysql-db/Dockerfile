FROM mysql

ENV MYSQL_ROOT_PASSWORD="my-secret-password"
ENV MYSQL_DATABASE="flask"

ADD db_init.sql /docker-entrypoint-initdb.d
CMD ["--default-authentication-plugin=mysql_native_password"]