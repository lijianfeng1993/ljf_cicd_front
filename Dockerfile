FROM golang
MAINTAINER lijianfeng "1205960475@qq.com"
RUN cd /root && mkdir ljf_cicd_front
ADD ./* /root/ljf_cicd_front/
WORKDIR "/root/ljf_cicd_front"
CMD ["sh","start_web.sh"]
