FROM python:3-alpine

RUN set -ux \
 && apk --no-cache add bash \
 && pip3 install pyyaml

COPY ./*.py /
ENTRYPOINT ["python3", "/getusers_diff.py"]

# docker build -t kyokuheki/diffusers .
# sudo cat /var/lib/coreos-install/user_data | docker run -i --entrypoint=python kyokuheki/diffusers /getusers_cloudconfig.py -
# sudo cat /etc/passwd | docker run -i --entrypoint=python kyokuheki/diffusers /getusers_passwd.py -
# docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro  -v/etc/passwd:/passwd:ro kyokuheki/diffusers
