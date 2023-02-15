FROM registry.access.redhat.com/ubi8/ubi

USER root

RUN yum install -y python3; yum clean all
RUN python3 -m pip install --upgrade pip

WORKDIR /app

RUN chown -R 1001:0 /app && \
    chmod -R g=u /app

COPY ./ /app/
RUN python3 -m pip install -r requirements.txt

USER 1001

ENTRYPOINT ["python3"]
CMD ["sensor-http.py"]