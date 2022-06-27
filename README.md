# :mag_right: 불량 객체 탐지 프로그램 개발 (수정중)
<img src="https://user-images.githubusercontent.com/96769060/175932758-dcbdba0b-21da-47e5-bfa7-3c88d407162c.png" width="750">  
YOLO v5를 이용한 다양한 객체 검출 알고리즘의 활용법 중 '제품의 불량 여부를 탐지하고 결함의 종류를 파악하는 솔루션'을 개발하였습니다.  

기업 연계 과제이기 때문에 데이터셋에 관한 자세한 정보는 생략하고, 전반적인 솔루션 개발 과정과 시행 착오, 기대가치 등을 담은 발표 자료로 내용을 대신합니다.

<br>

## 프로젝트 세부사항
  - 수행 기간: 22/04/11 ~ 22/05/06 (총 4주)
  - 수행 인원: KDT 수강생 6명 ([`용지영`](https://github.com/djy00) [`김재경`](https://github.com/rmadmswk) [`어정호`](https://github.com/fish-ho) [`이재우`](https://github.com/leedaedoo2) [`정현우`](https://github.com/HyeonuJeong) [`최지원`](https://github.com/JadeWednesday))
  - 수행 역할: (개인) 객체 검출 알고리즘 간 비교 및 분석, 데이터셋 가공, 최적 파라미터 설정, 발표 및 PPT 제작
  - 개발 환경: <img src ="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=python&logoColor=white"/> <img src ="https://img.shields.io/badge/Google Colab-F9AB00.svg?style=flat&logo=Google Colab&logoColor=white"/> <img src ="https://img.shields.io/badge/VS Code-007ACC.svg?style=flat&logo=Visual Studio Code&logoColor=white"/> <img src ="https://img.shields.io/badge/Flask-282828.svg?style=flat&logo=Flask&logoColor=white"/> <img src ="https://img.shields.io/badge/OpenCV-eb4b4b.svg?style=flat&logo=OpenCV&logoColor=white"/> <img src ="https://img.shields.io/badge/Roboflow-6a06ce.svg?style=flat"/>
<br>

## 목차
[1. 프로젝트 기획 배경](https://github.com/JadeWednesday/CAKD5_2nd_Project/blob/main/README.md#1-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B8%B0%ED%9A%8D-%EB%B0%B0%EA%B2%BD)
<br>
[2. 데이터 분석 및 모델 개발](https://github.com/JadeWednesday/CAKD5_2nd_Project/blob/main/README.md#2-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D-%EB%B0%8F-%EB%AA%A8%EB%8D%B8-%EA%B0%9C%EB%B0%9C)
<br>
[3. 기대가치 정리](https://github.com/JadeWednesday/CAKD5_2nd_Project/blob/main/README.md#3-%EA%B8%B0%EB%8C%80%EA%B0%80%EC%B9%98-%EC%A0%95%EB%A6%AC)


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
<img src="https://user-images.githubusercontent.com/96769060/175933189-b3e23d4f-2e48-4512-8652-71b381b241a0.png" width="750">  

<img src="" width="750">  

<img src="" width="750">  

### 3. 기대가치 정리
