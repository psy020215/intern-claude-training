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

## Session — 2026-07-20

### Done
- 본문 확인 후 답변 새로 정리.

### Broke / Struggled
- 없음.

### Learned
- 다른 언어와 달리 python의 경우 삼항 표현식을 단일 문장으로 처리할 수 있다는 점.

---

## Session — 2026-07-21

### Done
- single-end로 read를 매핑하고 분석했던 Module 3와 달리, paired-end로 되어있는 read를 처리하는 방법에 대해 공부함.

### Broke / Struggled
- SAM 파일이 너무 커서 작업 진행이 너무 오래 걸림 — 이를 보완할 방법을 찾아봐야 할 듯.

### Learned
- fragment의 길이에 제한을 두는 이유(-X)와 FUR regulator의 역할에 대해 알게 됨.

---

## Session — 2026-07-22

### Done
- Exercise 4의 MEME 예측 답변을 검토하고 구체적 수치로 재작성함.
- Exercise 5~8 파이프라인(binding site 테이블 다운로드, Biopython 서열 추출, MEME 실행, 결과 해석, TSS 거리 분석, fur_sites.gff 생성)을 진행함.
- paired-end RNA-seq 정렬과 MEME 방법에서 EM을 통한 공통 motif 도출 과정을 다룸.

### Broke / Struggled
- 노트북 셀에서 meme 명령어가 sbml conda 환경 PATH에 없어서 CalledProcessError(exit 127) 발생 — /opt/meme/bin/meme로 전체 경로 지정해서 해결함.
- Exercise 2에서 만든 rnaseq.gff가 makegff.py의 --flip 옵션 없이 생성되어 RNA-seq strand가 실제와 반대로 기록되어 있던 것을 발견하고 재생성함.
- Transcription Unit 컬럼이 오페론 이름 전체(예: fes-ybdZ-entF-fepE)로 저장되어 있어 =='fes'로 검색하면 안 나오는 실수를 함.
- single-end/paired-end에 따른 read 판단의 차이를 이해하는 데 어려움이 있었음.
- 공통 motif가 의미하는 바를 이해하는 데 어려움이 있었음.

### Learned
- MEME은 모티프를 마스킹 후 반복 탐색으로 찾기 때문에 발견 순서(1,2,3등)가 E-value 크기 순서와 항상 일치하지는 않음.
- 통계적으로 유의한 공통 모티프가 나왔다고 해서 그것이 곧 진짜 TF 결합 서열이라는 보장은 없고, 알려진 구조와의 대조 검증이 필요함.
- paired-end fragment에서 concordant/discordant를 구분하는 기준과 그에 따른 접근·판단 방법을 이해함.

---

## Session — 2026-07-23

### Done
- Module 4 마무리: FUR binding site, RNA-seq 발현량, gene annotation 세 트랙을 비교해서 FUR 결합에 따른 유전인자(fepA)의 발현량 차이를 확인함.
- iron-replete(SRR1168133)와 iron-depleted(SRR1168135) 조건의 RNA-seq을 각각 정렬하여 fepA 발현량을 정량 비교함(raw depth 기준 약 16~18배 차이).

### Broke / Struggled
- rnaseq.gff의 score를 그대로(raw) 써서 만드니, 일부 위치(prophage 영역)의 극단적으로 높은 coverage 때문에 MetaScope의 y축 스케일이 깨져 대부분의 유전자 발현량 바가 보이지 않았음 → log scale로 재생성해서 해결함.
- log scale로 변환한 score의 평균으로 두 조건 간 fold-change를 비교하는 것은 산술평균이 아닌 기하평균 기반이라 엄밀하지 않음을 확인하고, BAM에서 raw depth를 직접 추출해 library size로 정규화하여 재계산함.

### Learned
- responsive repressor(FUR)의 작동 방식과, 특정 대사 관련 인자가 아니더라도 간접적으로 억제 대상 인자가 다른 대사에 영향을 줄 수 있음을 알게 됨.
- metabolic pathway network와 TRN(transcriptional regulatory network)의 연결이 대사산물·과정 예측에 필수적임을 확인함.

---

## Session — 2026-07-24

### Done
- 논문의 Fur 조절 기작(holo-Fur repression, holo-Fur activation, apo-Fur activation) 설명을 정리함.
- ftnB 유전자 발현량을 BAM 파일(SRR1168133/SRR1168135)에서 samtools depth로 직접 수치화하여 iron-replete/depleted 조건을 비교함.

### Broke / Struggled
- 유전자 구간을 전체/Fur site 이후/중간점 이후 중 어디로 자르느냐에 따라 repleted-depleted 우열 방향이 뒤바뀜.
- strand가 서로 다른 두 트랙(예: SRR1168135_(-) vs SRR1168133_(+))을 비교해서 잘못된 결론을 낼 뻔함.

### Learned
- makegff.py의 --flip은 원본 BAM strand와 반대로 뒤집는 것이라, 조건 간 비교는 반드시 같은 strand 라벨끼리 해야 함.
- 논문 Supplementary Data의 Mode(HA/HR/AA)·Distance to TSS 컬럼이 실제 결합 위치·조절 기전 판단의 핵심 근거임.
- 낮은 depth·단일 replicate 데이터에서는 구간을 어떻게 자르느냐에 따라 결론이 쉽게 뒤바뀔 수 있어 신중한 해석이 필요함.

---
