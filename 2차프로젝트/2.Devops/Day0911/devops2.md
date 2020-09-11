## Docker 설치
- 시작할때 vagrant up
- vagrant ssh
- [vagrant@demo html]$ sudo su
- [root@demo html]# cd
- [root@demo ~]# yum install -y docker

## 컨테이너 실행 및 확인 , 삭제 정리
- 그전에 서비스 기동, 이미지 획득 사전 작업 필요

### 1 컨테이너 실행 및 확인
~~~~
[root@demo ~]# docker run -t -d --name centos7 docker.io/centos:centos7
61260c982277f41fc52a6331f55f853422d601d0e995e85ac9ff892eed69fc3d

[root@demo ~]# docker container ls		⇐ 동일 docker container ps
CONTAINER ID        IMAGE                      COMMAND             CREATED             STATUS              PORTS               NAMES
61260c982277        docker.io/centos:centos7   "/bin/bash"         10 seconds ago      Up 9 seconds                            centos7
~~~~
### 2 컨테이너 내부에 명령어 실행
~~~~
[root@demo ~]# docker exec centos7 cat /etc/redhat-release	⇐ 컨테이너 내부에 설치되어 있는 CentOS 버전을 확인
                      (살행) (컨테이너이름) (명령어)
CentOS Linux release 7.8.2003 (Core)

[root@demo ~]# docker exec -it centos7 /bin/bash
                        (명령어 주고받기 가능)
[root@61260c982277 /]# cat /etc/redhat-release			⇐ 실행 중인 컨테이너 내부로 진입
CentOS Linux release 7.8.2003 (Core)

[root@61260c982277 /]# exit
exit
~~~~
### 3 컨테이너 정지/재기동
~~~~
[root@demo ~]# docker container stop centos7
centos7                              ~~~~~~~ 컨테이너 이름 또는 ID

[root@demo ~]# docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
dcfde3761f4f        docker.io/ubuntu    "/bin/bash"         19 minutes ago      Up 19 minutes                           ubuntu

[root@demo ~]# docker container ls -a	⇐ 정지 상태의 컨테이너를 포함해서 조회
CONTAINER ID        IMAGE                      COMMAND             CREATED             STATUS                        PORTS               NAMES
dcfde3761f4f        docker.io/ubuntu           "/bin/bash"         19 minutes ago      Up 19 minutes                                     ubuntu
61260c982277        docker.io/centos:centos7   "/bin/bash"         35 minutes ago      Exited (137) 16 seconds ago                       centos7

[root@demo ~]# docker container start centos7
centos7

[root@demo ~]# docker container ls
CONTAINER ID        IMAGE                      COMMAND             CREATED             STATUS              PORTS               NAMES
dcfde3761f4f        docker.io/ubuntu           "/bin/bash"         22 minutes ago      Up 22 minutes                           ubuntu
61260c982277        docker.io/centos:centos7   "/bin/bash"         37 minutes ago      Up 4 seconds                            centos7

~~~~
### 4 컨테이너 삭제
~~~~
[root@demo ~]# docker container rm -f centos7
centos7

[root@demo ~]# docker container ls -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
dcfde3761f4f        docker.io/ubuntu    "/bin/bash"         23 minutes ago      Up 23 minutes                           ubuntu

[root@demo ~]# docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
docker.io/ubuntu    latest              4e2eef94cd6b        3 weeks ago         73.9 MB
docker.io/centos    centos7             7e6257c9f8d8        4 weeks ago         203 MB

~~~~

## Dockerfile 이용해서 이미지 생성 하기

### 1 컨테이너 이미지 내부로 전달할 파일 생성
- [root@demo ~]# echo "Hello, Docker." > hello-docker.txt

### 2 Dockerfile을 생성 ⇒ 이미지 생성에 사용
- [root@demo ~]# vi Dockerfile
~~~~
FROM docker.io/centos:latest        ⇐ 베이스 이미지를 지정
ADD  hello-docker.txt /tmp          ⇐ 호스트에 있는 hello-docker.txt 파일을 컨테이너 이미지의 /tmp 아래로 복사
# RUN  yum install -y epel-release  ⇐ 컨테이너 이미지를 만들 때 실행
CMD  [ "/bin/bash" ]                ⇐ 컨테이너가 실행될 때 실행할 명령어
~~~~

### 3 Dockerfile을 이용해서 이미지를 생성 (이미지를 만드는 첫번째 방법)
~~~~
[root@demo ~]# docker image build -t myanjini/centos:1.0 .

               ~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~ ~
                |                  |                     Dockerfile 위치 ( . ⇒ 현재 위치)
                |                  +-- 이미지 이름 ⇒ DOCKER_HUB_ID/IMAGE_NAME:TAG_NAME
                +-- Dockerfile을 이용해서 이미지를 생성

[root@demo ~]# docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
myanjini/centos     1.0                 96bac9420c73        2 minutes ago       246 MB
~~~~
### 4 생성한 이미지를 이용해서 컨테이너를 실행 
~~~~
[root@demo ~]# docker container run -td --name devops-book-1.0 myanjini/centos:1.0
aa9eab5ad4c14a20cfa0605dd599ec65c5eefce5f5de2705f3b52495a51ffb68		⇐ 컨테이너 ID

[root@demo ~]# docker container ls
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                  NAMES
aa9eab5ad4c1        myanjini/centos:1.0   "/bin/bash"              33 seconds ago      Up 32 seconds                              devops-book-1.0
~~~~
### 5 컨테이너 내부로 진입
~~~~
[root@demo ~]# docker exec -it devops-book-1.0 /bin/bash
[root@aa9eab5ad4c1 /]# cat /tmp/hello-docker.txt		⇐ 이미지 생성 중 파일 복사되었는지 확인
Hello, Docker.
[root@aa9eab5ad4c1 /]# rpm -qa | grep epel			⇐ epel 패키지 설치 여부를 확인
epel-release-8-8.el8.noarch
~~~~
### 6  컨테이너 내용을 변경 후 변경된 내용을 이미지로 생성 (이미지를 만드는 두번째 방법)
~~~~
[root@aa9eab5ad4c1 /]# yum install -y epel-release		⇐ Dockerfile에서 설치하지 않은 경우
[root@aa9eab5ad4c1 /]# yum install -y nginx			⇐ 컨테이너 내부에 nginx를 설치
[root@aa9eab5ad4c1 /]# exit

[root@demo ~]# docker container commit devops-book-1.0 myanjini/centos:1.1
               ~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~
               |                        컨테이너 이름   이미지 이름
               +-- 컨테이너의 현재 상태를 이미지로 기록(생성)
sha256:e1857e6ba97a2a3c725c4a12dfd758dcf40cc5e0b46be09410a49ece2ee4d580

[root@demo ~]# docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
myanjini/centos     1.1                 e1857e6ba97a        About a minute ago   334 MB
~~~~
### 7 도커 허브에 이미지를 등록
~~~~
[root@demo ~]# docker image push myanjini/centos:1.1
The push refers to a repository [docker.io/myanjini/centos]
ff69ce0b06cd: Pushed                                                                               
99b77b4ffe98: Pushed                                                                               
a30523500c33: Pushed                                                                               
291f6e44771a: Layer already exists                                                                 
1.1: digest: sha256:57cd7748e60154ccb15f7d3625797e5eb87b4cb32967dbe4a5b814500b6f12e3 size: 1160
~~~~

### 8 도커 허브에 로그인 후 등록된 이미지를 확인 - docker hub에 들어가서 repository

### 9 도커 허브에 등록된 이미지를 이용해서 컨테이너를 실행
~~~~
[root@demo ~]# docker run --name myanjini_centos -dt -p 8888:80 myanjini/centos:1.1
e4b89daf7979830e3ea2069281ecc256ec0b8d535342c151967fb2df60b80566

[root@demo ~]# docker container ls
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                  NAMES
e4b89daf7979        myanjini/centos:1.1   "/bin/bash"              11 seconds ago      Up 10 seconds       0.0.0.0:8888->80/tcp   myanjini_centos

~~~~
### 10 모든 컨테이너를 삭제
- [root@demo ~]# docker container rm -f $(docker container ls -a -q)


## jeckins
- 1 작업을 프로젝트 단위로 쉽게 실행
- 2 안전하고 확실하게 실행 가능 
- 3 실행 겨로가에 대한 이력의 목록화 가능
