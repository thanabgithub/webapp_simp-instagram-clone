FROM nginx:1.22.0

WORKDIR /root
RUN apt-get update -y
RUN apt-get install --no-install-recommends --no-install-suggests -y apt-utils wget ca-certificates

ENV DEBIAN_FRONTED noninteractive
# https://ubuntu.com/blog/we-reduced-our-docker-images-by-60-with-no-install-recommends
# https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source
WORKDIR /root
RUN apt-get update -y
RUN apt-get install --no-install-recommends --no-install-suggests -y apt-utils wget ca-certificates

RUN apt-get install --no-install-recommends --no-install-suggests -y libpcre2-posix2 libpcre2-dev
RUN apt-get install --no-install-recommends --no-install-suggests -y zlib1g zlib1g-dev
RUN apt-get install --no-install-recommends --no-install-suggests -y openssl libssl-dev
# # others
RUN apt-get install --no-install-recommends --no-install-suggests -y gcc libgd-dev make
# https://debian.pkgs.org/11/debian-main-amd64/nginx-extras_1.18.0-6.1_amd64.deb.html


RUN wget https://nginx.org/download/nginx-1.22.0.tar.gz && tar zxf nginx-1.22.0.tar.gz && cd nginx-1.22.0
# RUN envsubst < /etc/nginx/_nginx.conf > /etc/nginx/nginx.conf
# CMD ["nginx", "-g", "daemon off;"]
# --with-http_realip_module --with-http_ssl_module
# ./configure --sbin-path=/usr/bin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/etc/nginx/error.log --http-log-path=/etc/nginx/access.log --with-pcre --pid-path=/var/run/nginx.pid --with-http_ssl_module --with-http_image_filter_module=dynamic --with-http_realip_module --modules-path=/usr/lib/nginx/new-modules