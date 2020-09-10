# 복습

## Devops ?

- dev(개발)와 ops(운용) 협업하여 비즈니스 가치를 높이는 근무 문화
- 장점 : 조직에 존재하는 속인성 문제, 팀간의 오버헤드, 품질 향상 개선
- 배경
- 1. 애자일 개발에 의한 계속적인 개발로의 변화
- 2. 계속적인 개발로 인해 나타나는 운용 과제
- => infrastructure as code(애자일 인프라 실현) : 버전관리, sw & config 관리, 모니터링 , 인프라 지속적 통합 다룸
- => 인프라 구성 설정 부분이 SW로 전환되고, SW개발 방법을 적용하여 인프라에 접근 가능 하다
- => 다시 말해, 개발 담당자가 인프라 운용의 설정을 직접 변경할 수 있고, 그 반대도 가능
- DEVOPS는 PDCA 사이클 기반 
- => PDCA : PLAN-DO-CHECK-ACT 
  => 도구 : 추상화 가상화 자동화 모니터링 지속적통합 ..

# 수업

### vagrantfile로 인프라 구성했을 때 장점
- 환경 구축 작업이 간소
- 환경 공유 용이
- 환경 파악 용이
- 팀 차원의 유지보수 가능

### 가상 머신 실행
- C:\HashiCorp\WorkDir> vagrant up

### 가상 머신 중지 삭제
- C:\HashiCorp\WorkDir> vagrant halt 
- C:\HashiCorp\WorkDir> vagrant destroy

### vagrant up 했을 때 생성되는 이미지 파일 어디?
- C:\Users\myanj\VirtualBox VMs

### vagrant 로컬 레포지토리 위치
- C:\Users\myanj\.vagrant.d\boxes
-  ~~~~~~~~~~~~~ 현재 윈도우 사용자의 홈 디렉터리

### vagrant 개선 필요 부분
- 구축 절차, 설정 어려움 : shell script 형태로 구축, 설치와 관련된 것이지 설정하는 쉘 스크리트 사용해야 함
- 구축 절차 다른 환경에서 유용 어려움
- 인프라 관리에 있어 *추상화*  필요 => 인프라 구성 관리 도구

### 인프라 구성 관리 도구
- 선언적 : 필요로 하는 것을 파악할 수 있는 것
- 추상화 : 세세한 차이 구분하지 않고 표준화 하는 것
- 수렴화 : 원하는 형태로 귀결 될 수 있도록
- 멱등성 : 같은 환경에서 몇 번을 실행해도 동일한 결과 얻을 수 있도록
- 간소화  

### Ansible(앤서블) 기본 사용법
- 파이썬으로 만들어진 인프라 구성 관리 도구
- 앤서블 본체 
- 인벤터리(inventory) : 앤서블에 의해 제어될 대상
- 모듈(module) : 앤서블에서 실행되는 명령어, 운영체제, 파일, db, 클라우드에 작업 지시
- *목표: 환경설정 및 구축 절차를 통일된 형식으로 기술(vagrant의 문제점을 개선), 환경의 차이를 관리, 실행 전에 변경되는 부분 파악*


#### 1 nginx 설치되어 있는지 확인
![1](https://user-images.githubusercontent.com/38436013/92672499-c7508700-f353-11ea-9ce4-2d58dec32fce.JPG)
#### 2 ansible 설치 및 버전 확인
![2](https://user-images.githubusercontent.com/38436013/92672533-dcc5b100-f353-11ea-8169-b616c22e444e.JPG)
![3](https://user-images.githubusercontent.com/38436013/92672538-ddf6de00-f353-11ea-98fa-cc8c10671a5a.JPG)
![4](https://user-images.githubusercontent.com/38436013/92673410-0384e700-f356-11ea-8131-b5fd68c11b5e.JPG)
#### 4 nginx 상태 확인
![44](https://user-images.githubusercontent.com/38436013/92673573-62e2f700-f356-11ea-9526-02c463051015.JPG)
#### 5 nginx가 실행 상태일 때 ansible 명령(nginx 서비스를 시작)를 실행
![5](https://user-images.githubusercontent.com/38436013/92673574-637b8d80-f356-11ea-9cdc-399c2aef5848.JPG)

### Ansible-playbook 

#### 1 git 설치
- [vagrant@demo ~]$ sudo yum install -y git
#### 2 ansible-playbook-sample 레포지터리 클론 생성
- [vagrant@demo ~]$ git clone https://github.com/devops-book/ansible-playbook-sample.git
#### 3 playbook을 실행해서 구축
- [vagrant@demo ~]$ cd ansible-playbook-sample/
- [vagrant@demo ansible-playbook-sample]$ ansible-playbook -i development site.yml
-     인벤터리 파일을 지정(/etc/ansible/hosts파일 쓰지 않음)
~~~~~~~~~~~~~~~~~~~~~~~~
[WARNING]: Invalid characters were found in group names but not replaced, use -vvvv
to see details

PLAY [webservers] *******************************************************************

TASK [Gathering Facts] **************************************************************
ok: [localhost]

TASK [common : install epel] ********************************************************
ok: [localhost]			⇐ epel 패키지가 이미 설치되어 있어 아무것도 하지 않았다. 

TASK [install nginx] ****************************************************************
ok: [localhost]

TASK [nginx : replace index.html] ***************************************************
changed: [localhost]		⇐ TASK 실행 결과가 예상했던 데로 변경되었다. 

TASK [nginx start] ******************************************************************
changed: [localhost]

~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~
[vagrant@demo ansible-playbook-sample]$ curl localhost
hello, development ansible		⇐ nginx 홈 디렉터리의 index.html 파일의 내용


[vagrant@demo ansible-playbook-sample]$ ansible-playbook -i production site.yml
[WARNING]: Invalid characters were found in group names but not replaced, use -vvvv
to see details

PLAY [webservers] *******************************************************************

TASK [Gathering Facts] **************************************************************
ok: [localhost]

TASK [common : install epel] ********************************************************
ok: [localhost]

TASK [install nginx] ****************************************************************
ok: [localhost]

TASK [nginx : replace index.html] ***************************************************
changed: [localhost]

TASK [nginx start] ******************************************************************
ok: [localhost]

PLAY RECAP **************************************************************************
localhost                  : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


[vagrant@demo ansible-playbook-sample]$ curl localhost
hello, production ansible
~~~~~~~~~~~~~~~~~~~

![7](https://user-images.githubusercontent.com/38436013/92679475-79dc1600-f363-11ea-97a1-3c06441467b4.JPG)
#### 4 실행 대상 정의를 확인
- 인벤터리 파일은 /etc/ansible/hosts 사용하지만 -i옵션 이용해서 지정 가능 

#### 5 실행 내용 정의를 확인

#### 6 템플릿 확인

#### 7 템플릿에서 사용하는 변수값 확인

#### 8 템플릿 내용 변경

#### 9 dry-run 모드 실행

#### 10 변경 사항을 호스트에 반영

### vagrant 와 ansible 차이

### 인프라 테스트 자동화 
- 코드화 -> 자동화 
#### Serverspec
- 테스트 수행을 간단하고 쉽게 하기 위함
- 인프라(서버) 설정 테스트 가능
- 테스트 항목에 대한 목록을 정해진 포맷을 기반으로 기술이 가능
- 테스트 결과를 리포트 형식으로 출력이 가능함
#### Ansible을 이용해서 Serverspec을 설치
- 0. rvm, ruby 설치
- command curl -sSL https://rvm.io/mpapis.asc | sudo gpg2 --import -
- command curl -sSL https://rvm.io/pkuczynski.asc | sudo gpg2 --import -
- curl -L get.rvm.io | sudo bash -s stable
- 생략 .. ruby rvm 설치

- 1. Playbook 파일(site.yml)에서 serverspec롤을 추가
- [vagrant@demo ansible-playbook-sample]$ vi site.yml
~~~~~~~~~~~~~~~
---
- hosts: webservers
  become: yes
  connection: local
  roles:
    - common
    - nginx
    - serverspec
#    - serverspec_sample
#    - jenkins
~~~~~~~~~~~~~~~
- 2. serverspec 롤을 확인
[vagrant@demo ansible-playbook-sample]$ cat ./roles/serverspec/tasks/main.y
~~~~~~~~~
# tasks file for serverspec
- name: install ruby
  yum: name=ruby state=installed

- name: install serverspec
  gem: name={{ item }} state=present user_install=no
  with_items:
   - rake
   - serverspec

~~~~~~~~~
- 3. ansible-playbook으로 serverspec 설치
- [vagrant@demo ansible-playbook-sample]$ ansible-playbook -i development site.yml --diff
- 4. Serverspec 설정
- [vagrant@demo ansible-playbook-sample]$ serverspec-init
- 5. samplespec_rb  파일 확인
- [vagrant@demo ansible-playbook-sample]$ cat ./spec/localhost/sample_spec.rb	

### Ansible에 Serverspec을 이용한 테스트 롤을 추가
#### 1 Playbook 파일(site.yml)에 Serverspec 테스트 롤을 추가
- [vagrant@demo ansible-playbook-sample]$ vi site.yml
~~~~~~~~~~~
---
- hosts: webservers
  become: yes
  connection: local
  roles:
    - common
    - nginx
    - serverspec                 
    - serverspec_sample           ⇐ 주석(#) 해제 후 저장
#    - jenkins
~~~~~~~~~~~
#### 2 serverspec_sample 롤 정의 파일을 확인
- cat ./roles/serverspec_sample/tasks/main.yml
#### 3 ansible-playbook으로 spec 파일(테스트 케이스 파일)을 배포 
- [vagrant@demo ansible-playbook-sample]$ ansible-playbook -i development site.yml
#### 4 spec 파일(테스트 케이스를 정의) 생성을 확인
- [vagrant@demo ansible-playbook-sample]$ cat /tmp/serverspec_sample/spec/localhost/web_spec.rb
#### 5 
#### 6
#### 7
