FROM centos
RUN yum install -y python-setuptools gcc mysql-connector git python-devel
RUN easy_install pip
WORKDIR E:/study/assign1
RUN pip install -r requirements.txt
