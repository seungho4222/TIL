# 넷플릭스 주가 데이터 분석

### :rabbit: 코드 작성

1. A: 데이터에서 사용할 column 확인후 범위지정
    - 변수 = pd.read_csv(경로, usecols=range(범위))
2. B: 'Date'값의 타입을 object에서 datetime64[ns]로 변경
    - 데이터 필터링 -> 필터링변수 = 기존데이터[기존데이터[필터링할 열] >= 필터링 기준]
        - ex: df_after_2021 = df[df['Date'] >= '2021-01-01']
    - pd.to_datetime(변경할 데이터 값: column기준)
    - plt.plot(불러올 column)
    - plt.title(제목)
    - plt.xlabel, plt.ylabel(x축, y축 제목)
    - plt.xticks, plt.yxticks(rotation=각도) -> 겹치는 문자 회전
    - plt.regend() -> 범례 표시
    - plt.show() -> 그래프 출력
3. C: 최고,최저 종가는 파이썬의 max, min 함수 사용
4. D: 일별 데이터를 월별 데이터로 그룹화하기, 종가의 평균값 계산
    - 데이터명.groupby(데이터명['Date'].dt.strftime('%Y-%m')).***mean()
        - mean() : 평균
        - sum() : 합
        - count() : 개수
        - min(), median(), max() : 최소값, 중앙값, 최대값
        - var(), std() : 분산, 표준편차
        - prod() : 곱셈
        - first(), last() : 첫째, 마지막값
5. E: 데이터 플롯시 필요한 데이터 각각 입력, 기준값은 동일하게(ex: 'Date'), label은 범례용
    - plt.plot(df_after_2022['Date'], df_after_2022['High'], label="High")
    - plt.plot(df_after_2022['Date'], df_after_2022['Low'], label="Low")
---
### :dizzy: 어려운점

1. 에러 내용
- D에서 일별 데이터를 월별로 필터링 시 종가만 평균을 내기 위해 ['Close']를 지정해 줌.
- 데이터 확인시 'Date', 'Close' 두 열 확인
- 플롯시 'Date', 'Close' 두 열을 지정해 줄 경우 'Date'가 없다고 에러뜸
- -> 플롯시 'Close'만 출력할 경우 그래프 출력됨(그래프 내 'Date' 자동 생성(?))
---
2. 해결
- 그룹화 과정에서 ['Close'] 지정없이 월별 필터링만 함
- 데이터 확인시 모든 열 확인
- 플롯시 'Date', 'Close' 두 열을 지정해 줄 경우 그래프 출력됨
---
:point_right: 문서작업시 흔히 사용하는 엑셀을 전에는 엑셀내에서 단축키를 활용하여 작업하였다. 하지만, 프로그래밍 언어로 작업시 데이터가 클수록 보다 효율적으로 작업속도를 향상시킬 수 있다.

:exclamation: 엑셀로 공공데이터를 활용할 경우 용량이 클 경우 엑셀에서 직접 안열리는 경우 있었음!! 코딩만세 :hand: