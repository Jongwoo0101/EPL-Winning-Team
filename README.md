# ⚽️ EPL-Winning-Team
![프리미어리그_로고](https://github.com/Jongwoo0101/EPL-Winning-Team/assets/96978536/9fe4175d-969a-4cc6-96c0-7af68749627f)   
>- [93-94 시즌부터 21-22시즌까지의 프리미어리그 경기 결과](https://www.kaggle.com/datasets/irkaal/english-premier-league-results)를 이용하여 경기결과를 예측하는 모델입니다.
>- 모든 데이터셋은 [Kaggle](https://www.kaggle.com/)에서 불러왔습니다

<br /> 

# 📑 작업 순서
1. 홈팀과 어웨이팀을 선택

2. "HomeTeam"과 "AwayTeam" 열에서 특정 조건을 만족하는 데이터를 필터링하고, 이를 합치는 작업을 수행

3. 모델 컴파일, 파라미터 개수 요약

4. 학습, 정확도 출력

5. 사용자로부터 입력 받은 홈팀의 득점과 원정팀의 득점을 기반으로 경기 결과를 예측하는 작업을 수행

6. 예측 결과를 기반으로 확률 값이 0.5보다 큰지를 판단하여 True 또는 False로 출력. 이를 통해 모델이 예측한 결과가 양성(Positive)인지 음성(Negative)인지를 확인

7. 학습결과 시각화

<br /> 

# 📈 학습 결과  
### 입력 값
> home : Chelsea   
> away : Tottenham   
> test_hg : 4     
> test_ag : 2   

### 결과
> 0번 인덱스: 홈팀(첼시)의 승리(H)일 확률이 약 92.24% (0.9224165)    
> 1번 인덱스: 무승부(D)일 확률이 약 7.22% (0.07218365)     
> 2번 인덱스: 원정팀(토트넘)의 승리(A)일 확률이 약 0.54% (0.0053998)    

| <img src="./Result/Home Away Training Accuracy.png" width="480px"> | <img src="./Result/Home Away Training Loss.png" width="480px"> |
| ---------------------------------------------- | ----------------------------------------------- |
| Model accuracy                                 | Model loss                                      |

<br /> 

# 💻 GUI   
<img width="296" alt="스크린샷 2023-08-08 오전 12 17 06" src="https://github.com/Jongwoo0101/EPL-Winning-Team/assets/96978536/14bacc67-8426-444d-afc2-093698cdcb2c">   

> [GUI.py](https://github.com/Jongwoo0101/EPL-Winning-Team/blob/Jongwoo0101/Home_Away/gui.py)를 실행하면 다음과 같은 화면이 나옵니다.   
> ```data["HomeTeam"].unique()``` 데이터 안에있는 팀2개와  홈/어웨이 팀의 골을 입력하세요.   
> **Predict**버튼을 누르면 결과가 나옵니다❗️ 

<br /> 

# 🖥️ For M1/M2 Mac users
> ```model.compile()``` 메서드에서 경고가 나타나고 있는데, SGD 옵티마이저를 사용하는데도 경고가 나타날 수 있습니다.   
> 옵티마이저 성능 이슈로 인한 경고이므로 이 경우 옵티마이저를 ```tf.keras.optimizers.legacy.SGD```로 변경하십시오.

<br /> 

## ⚙️Used
<img src="https://img.shields.io/badge/tensorflow-FF6F00?style=flat&logo=tensorflow&logoColor=white"/> <img src="https://img.shields.io/badge/numpy-013243?style=flat&logo=numpy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/jupyter-F37626?style=flat&logo=jupyter&logoColor=white"/>
