FROM centos:8
RUN dnf install -y python38 || true
RUN apk add --no-cache python3 && python3 -m ensurepip && pip3 install pytest || true
ENTRYPOINT ["/bin/bash"]