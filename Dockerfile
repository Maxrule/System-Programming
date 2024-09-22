FROM jenkins/jenkins:2.361.1-lts-centos7
USER root
ENV JENKINS_USER admin
ENV JENKINS_PASS admin
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

# Copy the Jenkins plugins file to the container
RUN yum install -y yum-utils

# Install utilities
RUN yum install -y rpm-build rpmdevtools wget unzip rpmdev-setuptree \
    && rm -rf /var/cache/yum/* && yum clean all

WORKDIR /var/jenkins_home

RUN jenkins-plugin-cli --plugins workflow-aggregator