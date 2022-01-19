FROM registry.access.redhat.com/ubi8/ubi-minimal as base

RUN microdnf install python3; microdnf clean all

RUN python3 -m venv /opt/venv

COPY ./requirements.txt .
COPY ./requirements ./requirements
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


FROM registry.access.redhat.com/ubi8/ubi-minimal as run-image
RUN microdnf install python3 tar
COPY --from=base /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Python 3.x" \
      io.openshift.expose-services="8000:http" \
      io.openshift.tags="builder,python,python38,python-38,rh-python38" \
      com.redhat.component="ubit-minimal" \
      name="ubi8/ubi-minimal" \
      version="1" \
      com.redhat.license_terms="https://www.redhat.com/en/about/red-hat-end-user-license-agreements#UBI" \
      maintainer="Johan Swanepoel"

RUN mkdir /django

ENV PORT=8000

EXPOSE 8000

WORKDIR /django

ADD . /django

RUN \
    chown -R 1001:0 /django && \
    chgrp -R 0 /django && \
    chmod -R g=u /django

USER 1001

RUN python manage.py makemigrations

CMD ["/django/runapp.sh"]