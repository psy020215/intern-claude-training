## Session — 2026-07-13

### Done
- Claude를 활용한 파이썬 사용 방법에 대해 배움.

### Broke / Struggled
- 깃에 연동하여 자동 반영(auto-commit/push) 설정이 잘 되지 않음.

### Learned
- /log를 활용한 세션 학습 후 최종 정리를 통해 Claude 활용 방법에 대해 더 잘 이해할 수 있었음.

---

## Session — 2026-07-14

### Done
- 데이터 파일 호출 방법과 Claude를 활용한 팔로우 업 전략, 조건이 다른 데이터 이용 시 분석 방법에 대해 학습함.

### Broke / Struggled
- Python에서 dataframe 순서 배열이 0부터 시작하는 점을 고려하지 못했었음.

### Learned
- 조건이 다른 데이터 비교 시 연산을 여러 번 수행하여 진행했었는데, iterrows() 구문을 통해 비교적 쉽게 분석할 수 있음을 새로 확인함.

---

## Session — 2026-07-14

### Done
- Exercise 4b, 5, 6, 7까지 파이프라인을 실행함.
- makegff.py 실행 문제를 해결 중임.

### Broke / Struggled
- makegff.py 실행 시 pysam 모듈을 찾지 못하는 문제가 발생함.
- conda base 환경과 sbml 환경을 헷갈려서 실행이 안 됨.

### Learned
- lab에서 사용하는 툴과 그 적용 방법.

---
## Session — 2026-07-15

### Done
- chipexo.gff 생성 및 MetaScope로 확인함.

### Broke / Struggled
- MetaScope에서 피크 확인과 binding site 특정에 어려움을 겪음.

### Learned
- MetaScope 이용 방법과 원리를 익힘.

---

## Session — 2026-07-15

### Done
- 피크 관측을 위해 makegff.py의 인자 중 하나인 score 부분을 변경하여 read가 여러 번 겹치는 구간에 가중치를 부여함.

### Broke / Struggled
- 가중치 기준을 몇 번 재조정해야 함 (1/3/5 고정값 → log-scale 정규화 → strand 부호 반영).

### Learned
- BAM 파일 변형 후 GFF 작성 시 분석 목적에 맞추어 변형하는 것이 중요하다고 생각됨.

---

## Session — 2026-07-16

### Done
- binding site를 찾기 위해 겹치는 read(5' end pileup) 부분에 score를 다르게 부여하도록 makegff.py를 수정함.

### Broke / Struggled
- score 정규화 기준을 여러 번 바꿔야 했음.
- MetaScope 로딩 및 시각화 과정에서 이슈가 있었음.

### Learned
- GFF 파일에 저장되는 feature 컬럼 값을 수정하니 MetaScope에서 의도한 대로 시각화가 가능해짐을 확인함.

---
