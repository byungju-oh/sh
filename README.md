# 카터 (Carter) - 2D 슈팅 게임

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 소개

카터(Carter)는 Pygame을 사용하여 개발된 2D 슈팅 게임입니다. 플레이어는 캐릭터를 조작하여 다양한 좀비와 장애물을 피하고 공격하며 높은 점수를 획득하는 것이 목표입니다.

## ✨ 주요 기능

### 🎮 게임플레이
- **2가지 캐릭터 선택**: 각각 다른 능력과 미사일 타입을 가진 캐릭터
- **3단계 스테이지**: 점진적으로 증가하는 난이도
- **다양한 적**: 3종류의 좀비와 운석
- **특수 무기**: 필살기 폭탄으로 화면의 모든 적 제거
- **시간 제한**: 각 스테이지당 15초 제한 시간

### 🎯 조작 방법
- **방향키**: 캐릭터 이동
- **스페이스바**: 미사일 발사
- **Left Shift**: 필살기 폭탄 사용
- **P키**: 게임 일시정지

### 📊 점수 시스템
- 좀비 처치 시 점수 획득 (캐릭터별 차등 점수)
- 운석 파괴 시 추가 점수
- 최종 점수 저장 및 랭킹 시스템

### 🎨 UI 기능
- 메인 메뉴
- 캐릭터 선택 화면
- 게임 설명 및 스토리
- 점수 랭킹 보드
- 크레딧 화면

## 🚀 설치 및 실행

### 필요 조건
```bash
Python 3.x
pygame
```

### 설치 방법
1. 저장소 클론
```bash
git clone https://github.com/your-username/carter-game.git
cd carter-game
```

2. 필요한 패키지 설치
```bash
pip install pygame
```

3. 게임 실행
```bash
python mert.py
```

## 📁 프로젝트 구조

```
carter-game/
│
├── mert.py                 # 메인 게임 파일
├── data.json              # 점수 데이터 저장 파일
├── images/                # 게임 이미지 리소스
│   ├── 배경화면2.png
│   ├── ch1.png           # 캐릭터 1
│   ├── ch2.png           # 캐릭터 2
│   ├── skeleton1.png     # 좀비 타입 1
│   ├── skeleton2.png     # 좀비 타입 2
│   ├── skeleton3.png     # 좀비 타입 3
│   ├── Bullet.png        # 미사일
│   ├── missile.png       # 고급 미사일
│   └── ...               # 기타 UI 및 배경 이미지
└── README.md
```

## 🎯 게임 시스템

### 캐릭터 시스템
| 캐릭터 | 속도 | 미사일 타입 | 특징 |
|--------|------|-------------|------|
| 캐릭터 1 | 빠름 | 일반 탄환 | 높은 기동성 |
| 캐릭터 2 | 보통 | 미사일 | 높은 공격력 |

### 적 시스템
- **Skeleton 1**: 기본 좀비, 직선 이동
- **Skeleton 2**: 중간 좀비, 패턴 이동
- **Skeleton 3**: 대형 좀비, 느린 이동, 높은 점수
- **운석**: 무작위 패턴 이동

### 아이템 시스템
- **폭탄**: 화면의 모든 적을 제거하는 필살기

## 🏆 점수 시스템

- 좀비 처치: 1-5점 (캐릭터와 좀비 타입에 따라 차등)
- 운석 파괴: 2-3점
- 시간 보너스: 스테이지 클리어 시 추가 점수
- 최고 점수는 JSON 파일에 자동 저장

## 🛠️ 개발 정보

### 개발 팀
- **이미지 수집 및 가공**: 서승원, 이준협
- **게임 기능 수정**: 박성수, 오병주

### 사용된 리소스
- [OpenGameArt.org](https://opengameart.org/)
- [Freepik](https://kr.freepik.com/)

### 기술 스택
- **언어**: Python 3.x
- **게임 엔진**: Pygame
- **데이터 저장**: JSON



## 📈 향후 계획

- [ ] 더 많은 스테이지 추가
- [ ] 새로운 캐릭터 및 무기 시스템
- [ ] 사운드 이펙트 및 배경음악
- [ ] 온라인 랭킹 시스템
- [ ] 파워업 아이템 다양화

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.



---

⭐ 이 프로젝트가 도움이 되셨다면 별표를 눌러주세요!
