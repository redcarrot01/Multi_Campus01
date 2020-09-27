#### 도커 , 컨테이너 생성

~~~~

- curl : http 메시지를 쉘상에서 요청하여 결과를 확인 하는 명령어
- docker container run -t -p 9000:8080 gihyodocker/echo:latest
  => 도커 컨테이너 실행 
 
~~~~



#### **간단한 애플리케이션과 도커 이미지 만들기**

~~~~
이미지 바뀌면(도커파일은 그대로), 도커 이미지 내용 바뀜을 알 수 있다

- -d 옵션으로 컨테이너를 백그라운드에서 실행
docker container run -d example/echo:latest

- 컨테이너 생성에 사용된 이미지로 조회
vagrant@xenial64:~/chap02$ docker container ls --filter "ancestor=example/echo"
 - -q 이용하면 아이디 추출 가능
 
- -p 옵션 이용한 포트포워딩 : -p 호스트포트:컨테이너포트
  호스트 포트 생략 => 자동으로 할당
  docker container run -d -p 9090:8080 example/echo:latest
  curl localhost:9090
  => 9090 호스트상에서 내용을  우분트에서도 확인 가능
  
- 도커 이미지 컨테이너 삭제
 docker container rm -f $(docker container ls -a -q) 
    => 모든 컨테이너 실행이거나 중지 모두 id 반환해서 삭제
 docker image rm -f $(docker image ls -q)
  
  
- docker image build --pull 옵션 
Always attempt to pull a newer version of the image

- 도커 이미지
  공식 배포, 도커파일이 공개된 , stars 받은 이미지.. 
  
  
- 도커 이미지 버전 관리 
 docker image build -t myanjini/basetest:latest .
                        도커 허브 계정
 docker image push myanjini/basetest:latest 
    => 이미지 도커 허브에 등록  
 docker image build -t myanjini/pulltest:latest .  
    => basetest이미지 활용하여 pulltest
 vi ../basetest/Dockerfile   
    => 이때 이미지 베이스 이미지수정 
 docker image build -t myanjini/basetest:latest ../basetest/       
    => myanjini/basetest   <none> 기존이미지 dangling,새이미지생성
 docker image build -t myanjini/pulltest:latest .  
    => pulltest 는 베이스 이미지 이용한 것이므로 dangling과 새이미지
 
- 태깅되지 않은 이미지 검색 및 태그 붙이기
 docker image tag $(docker image ls -f "dangling=true" -q) myanjini/basetest:0.1
  
-  cmd 명령 오버라이드
docker container run -it alpine uname -a
    
~~~~

#### 컨테이너 활용

~~~~
- 컨테이너 이름을 부여 해서 실행
 docker container run -d -p 9001:8080 --name myecho example/echo:latest
 
- 컨테이너 이름으로 조회
 docker container ls -a --filter "name=myecho"
 
 - 컨텐이너 출력 형식 지정
  docker container ls -a --format "table {{.ID}} : {{.Names}}\t{{.Command}}"
  CONTAINER ID : NAMES      COMMAND
e04df49d7bea : myoldecho  "go run /echo/main.go"

- 컨테이너 정지 : 이름, 아이디, 일부 가능
  docker container stop 4		
  
- 컨테이너 생성 시 --rm 옵션을 추가하면 컨테이너를 중지하면 해당 컨테이너를 삭제
  docker container run -d -p 9000:8080 --rm example/echo:latest
  
- 컨테이너 내부 쉘 이용
   docker container exec -it echo /bin/sh
  
- 컨테이너 파일 복사 (화)

- 
~~~~



#### devops

~~~~
- dev(개발)와 ops(운용) 협업하여 비즈니스 가치를 높이는 근무 문화
- 장점 : 조직에 존재하는 속인성 문제, 팀간의 오버헤드, 품질 향상 개선
- 배경
애자일 개발에 의한 계속적인 개발로의 변화
계속적인 개발로 인해 나타나는 운용 과제
=> infrastructure as code(애자일 인프라 실현) : 버전관리, sw & config 관리, 모니터링 , 인프라 지속적 통합 다룸
=> 인프라 구성 설정 부분이 SW로 전환되고, SW개발 방법을 적용하여 인프라에 접근 가능 하다
=> 다시 말해, 개발 담당자가 인프라 운용의 설정을 직접 변경할 수 있고, 그 반대도 가능
DEVOPS는 PDCA 사이클 기반
=> PDCA : PLAN-DO-CHECK-ACT => 도구 : 추상화 가상화 자동화 모니터링 지속적통합 ..
~~~~

#### vagrant

~~~~
vagrantfile로 인프라 구성했을 때 장점
환경 구축 작업이 간소
환경 공유 용이
환경 파악 용이
팀 차원의 유지보수 가능
가상 머신 실행
C:\HashiCorp\WorkDir> vagrant up
가상 머신 중지 삭제
C:\HashiCorp\WorkDir> vagrant halt
C:\HashiCorp\WorkDir> vagrant destroy
vagrant up 했을 때 생성되는 이미지 파일 어디?
C:\Users\myanj\VirtualBox VMs

vagrant 개선 필요 부분
구축 절차, 설정 어려움 : shell script 형태로 구축, 설치와 관련된 것이지 설정하는 쉘 스크리트 사용해야 함
구축 절차 다른 환경에서 유용 어려움
인프라 관리에 있어 추상화 필요 => 인프라 구성 관리 도구


인프라 구성 관리 도구
선언적 : 필요로 하는 것을 파악할 수 있는 것
추상화 : 세세한 차이 구분하지 않고 표준화 하는 것
수렴화 : 원하는 형태로 귀결 될 수 있도록
멱등성 : 같은 환경에서 몇 번을 실행해도 동일한 결과 얻을 수 있도록
간소화


Ansible(앤서블) 기본 사용법
파이썬으로 만들어진 인프라 구성 관리 도구
앤서블 본체
인벤터리(inventory) : 앤서블에 의해 제어될 대상
모듈(module) : 앤서블에서 실행되는 명령어, 운영체제, 파일, db, 클라우드에 작업 지시
목표: 환경설정 및 구축 절차를 통일된 형식으로 기술(vagrant의 문제점을 개선), 환경의 차이를 관리, 실행 전에 변경되는 부분 파악

jeckins
1 작업을 프로젝트 단위로 쉽게 실행
2 안전하고 확실하게 실행 가능
3 실행 겨로가에 대한 이력의 목록화 가능
~~~~

#### 도커 설명

~~~~
도커
오픈소스 컨테이너 프로젝트, 가장 인기 많음
aws, google cloud, microsoft azure 등의 클라우드 서비스에서 공식 지원
장점1 : 리눅스 애플리케이션을 컨테이너에 담아서 실행 할 수 있음 => 개발, 테스트 서비스 환경을 하나로 통일하여 관리 가능
장점2 : 컨테이너를 공유할 수 있음(도커 이미지 공유하는 docker hub 이용 .. 깃헙 처럼)
컨테이너 기술 ?
가상화보다 가벼운 기술

가상화 등장 배경: 컴퓨터에서 컴퓨터 만들어 내기 위한 시도, PC와 서버 성능 좋아짐-> 서버에 가상 머신 여러개 띄워서 일을 시키자!

가상 머신에 서버 ,DB 설치하여 웹 사이트 등 서비스 실행

가상화 장점: 가상 머신 이미지를 여러 서버에 복사하여 실행 -> 서버 계속해서 만들어냄 (동일한 환경에서 쉽게 재구축)

클라우드 서비스 : 가상화 기술 이용해서 서버를 임대해 주는 서비스

가상 머신의 문제점 : 컴퓨터를 통째로 만들어내다 보니 각종 성능 손실이 발생

가상화 대중으로 CPU(HW) 안에 가상화 기능 넣기 시작 : 느려 -> 호스트와 커널을 공유하는 반가상화 등장 : 그래도 문제가 많다

가상 머신은 항상 게스트 OS 설치해야 -> 이미지 용량 너무 큼 : 우리가 아는 버츄얼박스 이런 가상화 소프트웨어는 OS 가상화에만 주력, 즉 배포와 관리 기능 부족

-> 리눅스 컨테이너 등장 이유

컨테이너 안에 가상공간을 만들고, 실행 파일을 호스트에서 실행

리눅스 컨테이너 그림 부분 이해 필요************

도커는 리눅스 컨테이너 기술 사용

도커 특징
그림 붙이기 : 이것을 가상머신 이랑 비교
도커는 게스트 OS 설치 안함
하드웨어 가상화 계층 없음 : 호스트와 도커 컨테이너 사이의 성능 차이 크지 않음
장점1: 도커는 이미지 생성과 배포에 특화 // 가상머신은 이미지 설치에 특화
장점2: 이미지 버전 관리 , 중앙저장소에 이미지 올리고 받을 수 있음 (VAGRANT-> 저장소: vagrant box)
다양한 api, 자동화 가능 -> 개발과 서버 운영에 유용
이미지와 컨테이너
이미지 : ㅅ서버 프로그램, 소스 코드, 실행 파일을 묶은 형태, 저장소에올리고 받는건 이미지
컨테이너: 이미지를 실행한 상태
os로보면 이미지 : 컨테이너 = 실행파일: 프로세스
도커는 이미지 처리 방식? 유니온 파일 시스템
: 베이스 이미지에서 바뀐 부분만 이미지로 생성, 컨테이너로 실행할 때는 베이스 이미지와 바뀐 부분 합쳐서 실행
서비스 운영 환경과 도커
지금까지는 물리 서버를 직접 운영 했음, 돈과 시간 많이 듦
가상화 발전으로 클라우드 환경으로의 변화
: 가상 서버 임대하여 사용
: 다 좋은데 서버 일일이 세팅 어려움 => 세팅과 배포를 어떻게 할 것인가?
immutable infrastructure 패러다임 등장 (불변하는 인프라구조- 그 이유는 업데이트 하는 것이 아니라 대체한다는 의미)
: 호스트 os와 서비스 운영 환경(서버 프로그램, 소스 코드, 컴파일 된 바이너리)을 분리
: 하드웨어를 소프트웨어로 구현하다보니(hw가 이미지로 관리되고 있음), 한번 설정한 운영환경은 수정하는 것이 아니라 다른 머신으로 대체 - 모듈 느낌, not upgrade
장점: 서비스 환경 이미지만 관리하면 됨, 확장성 좋다, 가볍다(os와 서비스 환경 분리)
~~~~

#### 컨테이너 데이터를 영속적으로 

~~~~
방법 1. 호스트 볼륨 공유

     2. 볼륨 컨테이너
     3. 도커 볼륨
     
     
~~~~

도커 컴포즈는 위와 같이 여러 컨테이너를 한번에 관리 할 때 아주 유용하다. YAML(확장자 *.yml) 파일을 이용하여 어떠한 이미지를 사용하여 어떤 컨테이너를 어떻게 실행 시킬 것인지 기술해주면 도커는 해당 내용대로 컨테이너를 순차적으로 실행 시킨다.



21. 4 
22. 1
23. 3
24. 1