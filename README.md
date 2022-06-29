# :mag_right: 불량 객체 탐지 프로그램 개발
<img src="https://user-images.githubusercontent.com/96769060/175932758-dcbdba0b-21da-47e5-bfa7-3c88d407162c.png" width="750">  
YOLO v5를 이용한 다양한 객체 검출 알고리즘의 활용법 중 '제품의 불량 여부를 탐지하고 결함의 종류를 파악하는 솔루션'을 개발하였습니다.  

기업 연계 과제이기 때문에 데이터셋에 관한 자세한 정보는 공개할 수 없지만, 전반적인 솔루션 개발 과정과 시행 착오, 기대가치 등을 담은 발표 자료로 내용을 대신합니다.

<br>

## 프로젝트 세부사항
  - 수행 기간: 22/04/11 ~ 22/05/06 (총 4주)
  - 수행 인원: KDT 수강생 6명 ([`용지영`](https://github.com/djy00) [`김재경`](https://github.com/rmadmswk) [`어정호`](https://github.com/fish-ho) [`이재우`](https://github.com/leedaedoo2) [`정현우`](https://github.com/HyeonuJeong) [`최지원`](https://github.com/JadeWednesday))
  - 수행 역할: (개인) 객체 검출 알고리즘 간 비교 및 분석, 데이터셋 가공, 최적 파라미터 설정, 발표 및 PPT 제작
  - 개발 환경: <img src ="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=python&logoColor=white"/> <img src ="https://img.shields.io/badge/Google Colab-F9AB00.svg?style=flat&logo=Google Colab&logoColor=white"/> <img src ="https://img.shields.io/badge/VS Code-007ACC.svg?style=flat&logo=Visual Studio Code&logoColor=white"/> <img src ="https://img.shields.io/badge/Flask-282828.svg?style=flat&logo=Flask&logoColor=white"/> <img src ="https://img.shields.io/badge/HTML-E34F26.svg?style=flat&logo=HTML5&logoColor=white"/> <img src ="https://img.shields.io/badge/CSS-1572B6.svg?style=flat&logo=CSS3&logoColor=white"/> <img src ="https://img.shields.io/badge/OpenCV-eb4b4b.svg?style=flat&logo=OpenCV&logoColor=white"/> <img src ="https://img.shields.io/badge/Roboflow-6a06ce.svg?style=flat"/>
<br>

## 목차
[1. 프로젝트 기획 배경](https://github.com/JadeWednesday/CAKD5_2nd_Project/blob/main/README.md#1-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B8%B0%ED%9A%8D-%EB%B0%B0%EA%B2%BD)
<br>
[2. 데이터 분석 및 모델 개발](https://github.com/JadeWednesday/CAKD5_2nd_Project/blob/main/README.md#2-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D-%EB%B0%8F-%EB%AA%A8%EB%8D%B8-%EA%B0%9C%EB%B0%9C)
<br>
[3. 기대가치 정리](https://github.com/JadeWednesday/CAKD5_2nd_Project/blob/main/README.md#3-%EA%B8%B0%EB%8C%80%EA%B0%80%EC%B9%98-%EC%A0%95%EB%A6%AC)
<br>
[4. Web Application 사용 방법](https://github.com/JadeWednesday/CAKD5_2nd_Project/blob/main/README.md#4-web-application-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95)


### 1. 프로젝트 기획 배경
<img src="https://user-images.githubusercontent.com/96769060/175933027-a939b408-21e5-4e03-8c31-1139191cce55.png" width="750">  

  - 언택트 시대의 가속화 → 제품의 수요 크게 상승
  - 현재 해당 산업의 구인난은 옛날부터 꾸준히 이어져 온 난제

이에 따라 저희는 ‘숙련된 엔지니어가 직접 불량을 판별해야 하는 기존 공정 시스템’을 딥 러닝 알고리즘으로 대신하여
인건비 절약 및 수율 상승을 꾀하고, 엔지니어의 숙련도에 대한 의존성을 완화하고자 해당 프로젝트를 기획하게 되었습니다.


#### :factory: 공정 과정에 딥 러닝 알고리즘을 적용했을 때 얻을 수 있는 이점
  - 검출자의 컨디션에 영향을 받지 않는 객관적인 결함 탐지 가능
  - 기존 결함을 바탕으로 학습해 일정 수준 이상의 검출 능력 보장
  - 오검출로 인한 수율 하락을 완화하여 기업 경쟁력 제고
  - 인건비 절감 및 전문 인력의 공백을 어느 정도 보완


### 2. 데이터 분석 및 모델 개발
<img src="https://user-images.githubusercontent.com/96769060/176094695-45e01521-c0da-491c-ab96-b21a16535e0c.png" width="750">  

저희 프로그램은 크게 4단계 작업을 거쳐 개발되었습니다.
  - 결함의 종류와 유형을 라벨링해 데이터셋 가공
  - 여러 객체 탐지 알고리즘을 비교 후 적절한 알고리즘 선정
  - 다양한 방식으로 데이터를 조합하며 최적의 파라미터 탐색
  - 완성한 모델을 웹 환경에 매핑하여 Web Application 구현


<img src="https://user-images.githubusercontent.com/96769060/176092413-832fc61a-e6ad-4bbf-8b3f-ff2eb22a4f50.png" width="750">  

객체의 절대량 부족으로 학습 효율이 낮아지는 부분은 결함을 새롭게 생성하거나 이미지를 증식하는 것으로 해결했습니다.  
이 방법을 통해 모델은 새로운 결함에 대해서도 높은 정확도와 검출율을 보입니다.  

#### :open_file_folder: 한정된 데이터셋의 학습 효율을 높이는 방법
  - Roboflow 어노테이션 툴의 이미지 회전, 그레이스케일 등 데이터 증식 기법 활용
  - 결함 부분만을 추출해 포토샵, OpenCV를 이용해 재가공하여 양품 이미지에 합성


객체 검출 알고리즘은 여러 후보(YOLO 시리즈, Faster R-CNN, RetinaNet 등) 중에서 정확도, 학습 속도, 사용 편의성 등을 고려하여 YOLO v5로 최종 선정하였습니다.
  

<img src="https://user-images.githubusercontent.com/96769060/176092482-7436e13a-a23e-49ec-b2e8-e5766f00b5fc.png" width="750">  

마지막으로, 여러 이미지를 업로드하면 순차적으로 그 결함 여부와 종류를 파악할 수 있는 Web Application 구현으로 기술 확장성과 사업성을 높였습니다.  
'라벨링 작업까지 한 번에 할 수 있다면 현장 활용성이 높아질 것이다'라는 추가적인 피드백을 받으며 시연을 마쳤습니다.

### 3. 기대가치 정리

<img src="https://user-images.githubusercontent.com/96769060/176092623-1a312ce7-381d-4482-93ae-653b72b00d8f.png" width="750">  

#### :star2: 딥 러닝 알고리즘을 실제 산업 현장에 적용했을 때 얻을 수 있는 이점
  - `기업`  사람이 일으킬 수 있는 실수도 객관적 탐지 능력으로 보완 가능, 인건비 일부 절감
  - `근로자` 인력이 꾸준히 공급되지 않는 특수한 환경에서도 목적에 맞는 맞춤형 학습 모델을 통해 기존 근무자들의 노동 강도를 완화
  - `지속성` 첨단 기술을 발빠르게 도입하여 기업의 일차 목표인 이윤을 높이고 미래지향적인 산업을 선도


### 4. Web Application 사용 방법
1. 학습된 모델이 들어 있는 pt 파일과 web 폴더를 모두 다운로드합니다.
2. pt 파일의 경우 분할 압축되어 있기 때문에, 첫 번째 vol1 파일의 압축을 해제하면 자동으로 전체가 압축 해제됩니다.
3. 압축 해제한 yolov5l.pt 파일을 web 폴더 안으로 옮깁니다.
4. (웹 구동) 가상환경을 세팅한 후 pip install -r requirements.txt 명령어를 입력해 필요한 라이브러리를 설치합니다.
5. webapp.py 내부 27, 28, 82번 코드의 경로를 로컬 PC에 맞게 설정한 후 실행 python webapp.py 명령어를 입력해 웹을 실행합니다.
