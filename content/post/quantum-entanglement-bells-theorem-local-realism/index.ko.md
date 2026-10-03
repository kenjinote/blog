---
title: "양자 얽힘과 벨의 부등식: 아인슈타인의 마지막 패배와 양자 정보 혁명의 새벽"
description: "'기묘한 원격 작용'과 EPR 역설. 국소 실재론의 붕괴를 증명한 벨의 부등식과 아스페의 실험, 노벨상을 향한 궤적."
slug: "quantum-entanglement-bells-theorem-local-realism"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["quantum-entanglement", "bells-theorem", "quantum-information", "physics-history"]
image: "eyecatch.jpg"
---

# 양자 얽힘과 벨의 부등식: 아인슈타인의 마지막 패배와 양자 정보 혁명의 새벽

현대 물리학의 최대 미스터리이자 동시에 가장 강력한 도구이기도 한 '양자 얽힘(Quantum Entanglement)'. 그리고 인간의 직관인 '국소 실재론'을 타파한 '벨의 부등식'. 이것들은 단순한 물리학의 이론적 유희가 아니라, 우주의 근원적인 성질을 우리에게 들이밀며 나아가 양자 컴퓨터나 양자 암호 통신과 같은 차세대 테크놀로지의 기반이 되고 있습니다.

본 기사에서는 1935년 아인슈타인 등의 EPR 논문에서 시작하여 숨은 변수 이론의 고뇌, 존 스튜어트 벨에 의한 역사적인 부등식 도출, CHSH 부등식과 양자역학에서의 최대 위반(치렐슨 한계)의 수학적 증명, 그리고 아스페 등의 실험적 검증부터 2022년 노벨 물리학상에 이르기까지의 장대한 드라마를 물리학, 양자정보과학, 과학철학의 관점에서 극히 상세하게 해설합니다. 나아가 다입자 얽힘인 GHZ 상태를 통한 국소 실재론의 완전한 부정, 양자 원격전송(텔레포테이션)의 엄밀한 프로토콜, 얽힘의 정량화 수법까지 수식을 곁들여 깊이 파고들어 봅니다.

---

## 제1장: 1935년, 아인슈타인의 역습

양자역학이 1920년대에 코펜하겐 학파(닐스 보어와 베르너 하이젠베르크 등)에 의해 정식화되어 가는 가운데, 알베르트 아인슈타인은 그 확률론적이고 비결정론적인 해석에 강렬한 불만을 품고 있었습니다. "신은 주사위를 던지지 않는다"라는 그의 유명한 말은 양자역학의 근저에 있는 확률적인 성질에 대한 거부를 나타냅니다.

1935년, 아인슈타인은 보리스 포돌스키, 네이선 로젠과 함께 물리학사에 남을 역사적 논문 『물리적 실재의 양자역학적 기술은 완전하다고 생각할 수 있는가?(Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?)』, 이른바 'EPR 논문'을 발표했습니다. 이 논문의 목적은 양자역학이 '불완전'하다는 것, 즉 아직 우리가 모르는 '숨은 변수'가 존재할 것이라는 점을 논리적으로 증명하는 것이었습니다.

### 국소성과 실재성의 정의

EPR 논문의 논리 전개를 이해하기 위해서는 아인슈타인 등이 전제로 삼은 2가지 근본적인 개념을 정확히 파악할 필요가 있습니다.

1. **실재성(Realism)**:
   관측 여부와 상관없이 물리계는 확정된 물리적 성질(값)을 가지고 있다는 사고방식. EPR 논문에서는 "물리계의 상태를 어떠한 의미로든 교란하지 않고, 어떤 물리량의 값을 확실하게(확률 1로) 예측할 수 있다면, 그 물리량에 대응하는 물리적 실재의 요소가 존재한다"고 정의되었습니다. 바꿔 말해, 측정 전부터 대상은 그 속성을 확정적으로 유지하고 있다는, 고전역학에서는 당연한 상식입니다.
2. **국소성(Locality)**:
   공간적으로 떨어진 2개의 영역에서, 한쪽에서 수행된 조작이나 측정이 빛의 속도를 넘어 순식간에 다른 한쪽 영역의 물리적 현실에 영향을 미치는 일은 없다는, 상대성이론에 기반한 원칙입니다. 특수 상대성이론에 의해 빛의 속도를 초과하는 정보의 전달은 인과율의 붕괴를 초래하므로 어떠한 물리적 상호작용도 빛의 속도의 제한을 받습니다.

### '기묘한 원격 작용'(Spooky action at a distance)과 EPR 역설

EPR 논문에서는 다음과 같은 사고실험이 제시되었습니다.
서로 강하게 상호작용한 뒤 멀리 떨어지게 된 2개의 입자 A와 B를 생각해 봅시다. 양자역학의 틀 안에서 이 2개의 입자는 '얽힌(Entangled)' 상태에 있으며, 전체의 파동함수로 기술됩니다.

입자 A의 위치 $x_A$ 를 측정했다고 가정합시다. 운동량 보존 법칙 등에 의해 A의 위치가 확정되면, 순식간에 입자 B의 위치 $x_B$ 도 확정됩니다. 한편, 입자 A의 운동량 $p_A$ 를 측정하면 입자 B의 운동량 $p_B$ 가 순식간에 확정됩니다.
양자역학에 따르면 위치와 운동량은 비가환적인 물리량이며($[x, p] = i\hbar$), 동시에 확정된 값을 가질 수 없습니다(하이젠베르크의 불확정성 원리). 그러나 A에 대한 측정의 선택(위치를 측정할 것인가 운동량을 측정할 것인가)이 빛의 속도를 넘어 순식간에 B의 상태(위치가 확정된 상태인가, 운동량이 확정된 상태인가)를 결정하는 것처럼 보입니다.

만약 '국소성'이 맞다면, A에 대한 측정이 B에 순식간에 영향을 미치는 일은 있을 수 없습니다. 아인슈타인은 이를 '기묘한 원격 작용(Spukhafte Fernwirkung / Spooky action at a distance)'이라 부르며 강하게 비판했습니다. 따라서 B는 측정되기 전부터 미리 위치도 운동량도 확정된 값(숨은 변수)을 가지고 있어야만 하며, 위치도 운동량도 완전히 기술하지 못하는 양자역학은 '불완전한 이론'이라고 그들은 결론지었습니다. 이 역설은 훗날 양자정보이론에서 얽힘의 본질적인 이해로 나아가는 첫걸음이 되었습니다.

---

## 제2장: 숨은 변수 이론의 딜레마와 봄 역학

EPR 논문 발표 후, 물리학자들은 "양자역학은 맞지만 불완전하며, 더 깊은 계층에 결정론적인 이론(숨은 변수 이론)이 존재하는 것은 아닐까" 하는 가설의 탐구로 향했습니다.

### 폰 노이만의 잘못된 '불가능성 정리'

이 논의에 찬물을 끼얹은 것이 천재 수학자 존 폰 노이만입니다. 그는 1932년 저서 『양자역학의 수학적 기초』에서, 양자역학과 같은 예측을 제공하는 '숨은 변수 이론'을 구축하는 것은 수학적으로 불가능하다는 증명(불가능성 정리)을 제시했습니다.
폰 노이만의 권위는 절대적이었고, 그 후 수십 년간 "숨은 변수의 탐구는 무의미하다"는 풍조가 물리학계를 지배했습니다.

그러나 나중에 밝혀진 바와 같이, 폰 노이만의 증명에는 '숨은 변수가 만족해야 할 조건'으로서 극히 제한적이고 비물리적인 가정(비가환적인 물리량의 기댓값의 가법성: $\langle A+B \rangle = \langle A \rangle + \langle B \rangle$ 가 숨은 변수의 수준에서도 성립한다는 가정)이 포함되어 있었으며, 사실 완전한 증명이 아니었습니다. 그레테 헤르만은 이 결함을 일찍부터 눈치챘으나 당시에는 주목받지 못했습니다.

### 봄 역학: 비국소적 숨은 변수 이론

1952년, 데이비드 봄은 폰 노이만의 불가능성 정리를 타파하고, 양자역학과 완전히 일치하는 예측을 제공하는 결정론적인 '숨은 변수 이론(봄 역학, 혹은 드 브로이-봄 이론)'을 구축했습니다.
봄의 이론에서 입자는 항상 명확한 위치(숨은 변수)를 가지며, 우주 전체에 퍼져 있는 '양자 퍼텐셜'에 의해 인도됩니다. 슈뢰딩거 방정식을 극좌표 표시로 변환하여 얻어지는 이 퍼텐셜 $Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 R}{R}$ 은 거리에 의존하지 않고 감쇠하지 않는다는 특이한 성질을 가집니다.

그러나 봄 역학에는 중대한 대가가 따랐습니다. 양자 퍼텐셜은 공간 전체에 순식간에 영향을 미치기 때문에, 이 이론은 본질적으로 '비국소적'이었던 것입니다. 아인슈타인이 가장 혐오했던 '기묘한 원격 작용'을 봄 역학은 이론의 근간으로 내포하고 있었습니다.
아인슈타인은 봄의 이론에 대해서도 "값싼 해결책"이라며 부정적인 태도를 취했고, 여전히 '국소적'인 숨은 변수 이론의 존재를 믿었습니다.

---

## 제3장: 스핀 1/2 입자의 단일항 상태와 양자역학의 엄밀한 예측

벨의 부등식으로 넘어가기 전에, 양자역학이 예측하는 얽힘의 상관관계에 대해 파울리 행렬을 사용한 엄밀한 브라-켓 계산 과정을 완전히 전개해 둡시다. 이것이 훗날 국소 실재론과 충돌하는 양자역학의 핵심이 됩니다.

스핀 1/2의 입자 쌍이 생성되어 총 스핀이 0인 '단일항 상태(Singlet State)'에 있다고 가정합니다. 이 상태 $|\psi^-\rangle$ 은 다음과 같이 기술됩니다.

$$ |\psi^-\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\rangle_A \otimes |\downarrow\rangle_B - |\downarrow\rangle_A \otimes |\uparrow\rangle_B \right) $$

여기서 $|\uparrow\rangle, |\downarrow\rangle$ 은 각각 스핀의 위쪽($+1$), 아래쪽($-1$)의 고유 상태($z$ 기저)를 나타냅니다. 간략화하여 $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ 로 쓰기도 합니다.

앨리스가 방향 $\vec{a}$, 밥이 방향 $\vec{b}$ 로 각각의 입자의 스핀을 측정합니다. 방향 벡터는 단위 벡터이며, 구면 좌표계에서 $\vec{a} = (\sin\theta_a\cos\phi_a, \sin\theta_a\sin\phi_a, \cos\theta_a)$ 등으로 나타낼 수 있습니다.
각 방향의 스핀 측정 연산자는 파울리 행렬 $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ 를 사용하여 $\sigma_a = \vec{a} \cdot \vec{\sigma}$, $\sigma_b = \vec{b} \cdot \vec{\sigma}$ 가 됩니다.

우리가 알고 싶은 것은 앨리스와 밥의 측정 결과의 곱의 기댓값 $\langle \sigma_a \otimes \sigma_b \rangle$ 입니다. 이를 계산하기 위해 기댓값의 정의에 따라 전개합니다.

$$ \langle \psi^- | (\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma}) | \psi^- \rangle $$

먼저 파울리 행렬의 성질로서 $\vec{a} \cdot \vec{\sigma} = a_x \sigma_x + a_y \sigma_y + a_z \sigma_z$ 를 생각합니다. 계산을 간단히 하기 위한 교묘한 테크닉으로, 단일항 상태 $|\psi^-\rangle$ 가 회전 불변(임의의 기저에서 같은 형태를 가짐)임을 이용합니다. 하지만 여기서는 더 직접적인 대수적 접근을 통한 완전 전개를 수행합니다.

연산자 $(\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma})$ 는 다음과 같이 전개됩니다.
$$ \sum_{i \in \{x,y,z\}} \sum_{j \in \{x,y,z\}} a_i b_j (\sigma_i \otimes \sigma_j) $$

기댓값은 선형성에 의해,
$$ \sum_{i,j} a_i b_j \langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle $$
가 됩니다. 여기서 $\langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle$ 를 각 성분에 대해 평가합니다.

$|\psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ 에 대하여,
- $\sigma_z \otimes \sigma_z$:
  $\sigma_z \otimes \sigma_z |01\rangle = (+1)(-1)|01\rangle = -|01\rangle$
  $\sigma_z \otimes \sigma_z |10\rangle = (-1)(+1)|10\rangle = -|10\rangle$
  따라서 $\sigma_z \otimes \sigma_z |\psi^-\rangle = -|\psi^-\rangle$ 이 되며, 기댓값은 $-1$.
- $\sigma_x \otimes \sigma_x$:
  $\sigma_x \otimes \sigma_x |01\rangle = |10\rangle$
  $\sigma_x \otimes \sigma_x |10\rangle = |01\rangle$
  따라서 $\sigma_x \otimes \sigma_x \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) = \frac{1}{\sqrt{2}}(|10\rangle - |01\rangle) = -|\psi^-\rangle$ 이 되며, 기댓값은 $-1$.
- $\sigma_y \otimes \sigma_y$:
  $\sigma_y |0\rangle = i|1\rangle, \sigma_y |1\rangle = -i|0\rangle$ 이므로,
  $\sigma_y \otimes \sigma_y |01\rangle = (i|1\rangle) \otimes (-i|0\rangle) = |10\rangle$
  $\sigma_y \otimes \sigma_y |10\rangle = (-i|0\rangle) \otimes (i|1\rangle) = |01\rangle$
  따라서 $\sigma_y \otimes \sigma_y |\psi^-\rangle = -|\psi^-\rangle$ 이 되며, 기댓값은 $-1$.

한편, 다른 성분(예: $\sigma_x \otimes \sigma_y$)의 기댓값은 모두 $0$ 이 됩니다.
왜냐하면 $\sigma_x \otimes \sigma_y |01\rangle = |1\rangle \otimes (-i|0\rangle) = -i|10\rangle$ 등이 되어 $\langle \psi^-|$ 와 내적을 취하면 직교성에 의해 사라지기 때문입니다.

따라서 0이 아닌 항은 $i=j$ 인 경우뿐이며,
$$ \sum_{i} a_i b_i \langle \psi^- | \sigma_i \otimes \sigma_i | \psi^- \rangle = \sum_{i} a_i b_i (-1) = - (a_x b_x + a_y b_y + a_z b_z) = - \vec{a} \cdot \vec{b} $$
라고 엄밀하게 도출됩니다.
벡터 $\vec{a}$ 와 $\vec{b}$ 가 이루는 각을 $\theta$ 라고 하면, 내적의 정의에 따라 $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = \cos\theta$ (방향 벡터는 단위 벡터이므로 길이 1).
그러므로 양자역학이 예측하는 상관관계는 다음과 같이 지극히 아름답고 단순한 식이 됩니다.

$$ E(\vec{a}, \vec{b}) = \langle \sigma_a \otimes \sigma_b \rangle = - \cos\theta $$

이 $-\cos\theta$ 라는 강력한 상관관계야말로 고전적인 숨은 변수 이론으로는 절대 재현할 수 없는 '양자 특유의 움직임'의 원천이 됩니다.

---

## 제4장: 존 스튜어트 벨의 충격과 CHSH 부등식의 엄밀한 도출

1964년, CERN에서 소립자 물리학 연구를 하던 아일랜드의 물리학자 존 스튜어트 벨은 여가를 이용해 양자역학의 기초 문제를 연구하고 있었습니다. 그는 봄 역학이 비국소적이라는 점을 바탕으로 다음과 같은 심오한 의문을 품었습니다.

"과연 아인슈타인이 원했던 '국소적'인 숨은 변수 이론으로 양자역학의 모든 예측을 재현하는 것이 가능할까?"

벨은 철학적 논쟁에 불과했던 이 문제를 엄밀한 수학적 정식화를 통해 실험적으로 검증 가능한 형태로 승화시켰습니다. 이것이 과학사에 찬란히 빛나는 '벨의 정리(Bell's Theorem)' 및 '벨의 부등식'입니다.
그리고 1969년, 존 클라우저, 마이클 혼, 애브너 시모니, 리처드 홀트의 4명(CHSH)은 현실의 실험에서 검증 가능한 확장판 부등식인 'CHSH 부등식'을 도출했습니다.

### 국소 실재론의 가정과 CHSH 부등식의 적분・대수 전개

앨리스는 측정기 설정으로 $a$ 또는 $a'$ 를 선택하고, 밥은 $b$ 또는 $b'$ 를 선택한다고 합시다.
국소 실재론에 기반한 '숨은 변수'를 $\lambda$ 라 하고, 그 확률 밀도 함수를 $\rho(\lambda)$ 라 합니다. 확률은 정규화되어 있으므로,
$$ \int \rho(\lambda) d\lambda = 1 $$
입니다.

앨리스의 측정 결과 $A$ 는 그녀의 측정 방향 $a$ 와 $\lambda$ 만으로 결정되며, 밥의 측정 방향 $b$ 에는 의존하지 않습니다(국소성).
마찬가지로 밥의 측정 결과 $B$ 는 $b$ 와 $\lambda$ 만으로 결정됩니다(국소성). 또한 측정되기 전부터 결과는 확정되어 있습니다(실재론). 결과는 $+1$ 또는 $-1$ 이므로,
$$ A(a, \lambda) = \pm 1, \quad B(b, \lambda) = \pm 1 $$
$$ A(a', \lambda) = \pm 1, \quad B(b', \lambda) = \pm 1 $$

앨리스와 밥의 측정 결과의 상관 함수(기댓값)는 숨은 변수 $\lambda$ 에 대해 적분함으로써 얻어집니다.
$$ E(a, b) = \int A(a, \lambda) B(b, \lambda) \rho(\lambda) d\lambda $$

여기서 CHSH 부등식의 핵심이 되는 다음의 양 $S(\lambda)$ 를 생각합니다.
$$ S(\lambda) = A(a, \lambda)B(b, \lambda) + A(a, \lambda)B(b', \lambda) + A(a', \lambda)B(b, \lambda) - A(a', \lambda)B(b', \lambda) $$

이 식을 앨리스의 측정 결과에 대해 인수분해(묶어내기)를 수행합니다.
$$ S(\lambda) = A(a, \lambda) \left[ B(b, \lambda) + B(b', \lambda) \right] + A(a', \lambda) \left[ B(b, \lambda) - B(b', \lambda) \right] $$

여기서 지극히 중요한 논리적 단계가 들어갑니다. $B(b, \lambda)$ 와 $B(b', \lambda)$ 는 모두 반드시 $+1$ 또는 $-1$ 의 값을 가집니다.
따라서 그것들의 합과 차를 생각하면 다음의 2가지 경우밖에 존재하지 않습니다.

- 경우 1: $B(b, \lambda) = B(b', \lambda)$ 일 때
  합은 $B(b, \lambda) + B(b', \lambda) = \pm 2$ 가 되고, 차는 $B(b, \lambda) - B(b', \lambda) = 0$ 이 됩니다.
- 경우 2: $B(b, \lambda) = -B(b', \lambda)$ 일 때
  합은 $B(b, \lambda) + B(b', \lambda) = 0$ 이 되고, 차는 $B(b, \lambda) - B(b', \lambda) = \pm 2$ 가 됩니다.

어느 경우에서든 2개의 대괄호 $\left[ \dots \right]$ 중 한쪽은 반드시 $\pm 2$ 가 되고, 다른 한쪽은 반드시 $0$ 이 됩니다.
그리고 그 살아남은 $\pm 2$ 에 곱해지는 $A(a, \lambda)$ 또는 $A(a', \lambda)$ 역시 $\pm 1$ 입니다.
따라서 어떠한 숨은 변수 $\lambda$ 의 값에 대해서도 대수적으로 반드시 다음이 성립합니다.
$$ S(\lambda) = \pm 2 $$

즉 절댓값을 취하면,
$$ |S(\lambda)| = 2 $$
가 됩니다.

이 $S(\lambda)$ 의 기댓값 $S$ 를 구하기 위해, 확률 분포 $\rho(\lambda)$ 를 곱하여 전체 공간에서 적분합니다.
$$ |S| = \left| \int S(\lambda) \rho(\lambda) d\lambda \right| \le \int |S(\lambda)| \rho(\lambda) d\lambda $$
$|S(\lambda)| = 2$ 인 것과 $\int \rho(\lambda) d\lambda = 1$ 임을 이용하면,
$$ |S| \le \int 2 \rho(\lambda) d\lambda = 2 $$

이 기댓값 $S$ 는 개별 상관 함수의 합과 차로 전개할 수 있습니다.
$$ S = E(a, b) + E(a, b') + E(a', b) - E(a', b') $$

이리하여 다음의 'CHSH 부등식'이 도출되었습니다.
$$ |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \le 2 $$

이것이 우주가 '국소 실재론'을 따른다면 **절대 넘을 수 없는 한계값**입니다.

### 양자역학적 최대 위반(치렐슨 한계)

제3장에서 도출한 양자역학의 예측 $E(\vec{a}, \vec{b}) = -\cos\theta$ 를 떠올려 보십시오.
앨리스와 밥이 다음 각도로 측정기를 설정했다고 합시다.
- $a = 0$
- $a' = \pi/2$
- $b = \pi/4$
- $b' = -\pi/4$

(※참고로, 광자의 편광을 사용할 경우에는 스핀 1/2과 계수가 달라져 $E = \cos(2\theta)$ 가 되지만, 스핀을 사용한 위 설정으로 계산해도 본질은 같습니다)
각 설정 간의 각도 차이는,
$|a - b| = \pi/4$
$|a - b'| = \pi/4$
$|a' - b| = \pi/4$
$|a' - b'| = 3\pi/4$

양자역학의 예측에 대입하면,
$E(a, b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a, b') = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b') = -\cos(3\pi/4) = +1/\sqrt{2}$

이것들을 CHSH 부등식의 좌변 $S$ 에 대입하면,
$$ S = \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) - \left( +\frac{1}{\sqrt{2}} \right) = -\frac{4}{\sqrt{2}} = -2\sqrt{2} $$
절댓값을 취하면 $|S| = 2\sqrt{2} \approx 2.828$ 이 됩니다.

국소 실재론의 한계인 $2$ 를 명백히 넘고 있습니다($2.828 > 2$). 이 양자역학에 의해 달성 가능한 최댓값을 **치렐슨 한계(Tsirelson Bound)**라고 부릅니다. 수학의 엄밀한 증명에 의해, 국소 실재론은 양자역학의 예측과 절대 양립할 수 없다는 것이 밝혀진 것입니다.

---

## 제5장: 다입자 얽힘과 국소 실재론의 '일격' 부정(All-or-Nothing)

벨의 정리는 통계적인 상관의 '부등식'에 기초하고 있었습니다. 그러나 1989년 다니엘 그린버거, 마이클 혼, 안톤 차일링거 세 사람은 3개의 입자가 얽힌 상태(GHZ 상태)를 생각하면 부등식이나 통계적 확률에 의존할 필요 없이 단 1회의 측정 결과의 모순만으로 국소 실재론을 완전히 논파할 수 있음을 보여주었습니다. 이를 'All-or-Nothing의 증명' 또는 'GHZ 정리'라고 부릅니다.

### GHZ 상태의 성질
3개의 스핀 1/2 입자의 GHZ 상태는 다음과 같이 정의됩니다.
$$ |GHZ\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\uparrow\uparrow\rangle - |\downarrow\downarrow\downarrow\rangle \right) $$

여기에 다음과 같은 파울리 연산자의 곱을 작용시킵니다.
1. $X_1 Y_2 Y_3 = \sigma_x^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_y^{(3)}$
2. $Y_1 X_2 Y_3 = \sigma_y^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_y^{(3)}$
3. $Y_1 Y_2 X_3 = \sigma_y^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_x^{(3)}$
4. $X_1 X_2 X_3 = \sigma_x^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_x^{(3)}$

$\sigma_x |\uparrow\rangle = |\downarrow\rangle, \sigma_x |\downarrow\rangle = |\uparrow\rangle$
$\sigma_y |\uparrow\rangle = i|\downarrow\rangle, \sigma_y |\downarrow\rangle = -i|\uparrow\rangle$
를 사용하여 $X_1 Y_2 Y_3$ 을 $|GHZ\rangle$ 에 작용시키면,
$X_1 Y_2 Y_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\rangle (i|\downarrow\rangle) (i|\downarrow\rangle) = -|\downarrow\downarrow\downarrow\rangle$
$X_1 Y_2 Y_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\rangle (-i|\uparrow\rangle) (-i|\uparrow\rangle) = -|\uparrow\uparrow\uparrow\rangle$
따라서,
$X_1 Y_2 Y_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (-|\downarrow\downarrow\downarrow\rangle + |\uparrow\uparrow\uparrow\rangle) = |GHZ\rangle$
가 되며, 고유값은 $+1$ 입니다. 대칭성에 의해 $Y_1 X_2 Y_3$, $Y_1 Y_2 X_3$ 에 대해서도 마찬가지로 고유값은 $+1$ 이 됩니다.

한편, $X_1 X_2 X_3$ 을 작용시키면,
$X_1 X_2 X_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\downarrow\downarrow\rangle$
$X_1 X_2 X_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\uparrow\uparrow\rangle$
따라서,
$X_1 X_2 X_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (|\downarrow\downarrow\downarrow\rangle - |\uparrow\uparrow\uparrow\rangle) = -|GHZ\rangle$
가 되며, 고유값은 $-1$ 입니다. 양자역학은 이상의 결과를 확실(확률 1)하게 예측합니다.

### 국소 실재론 붕괴의 대수적 증명
국소 실재론에서는 측정 결과가 미리 결정된 숨은 변수에 의해 결정된다고 생각합니다.
입자 1의 X방향, Y방향의 측정 결과를 각각 $m_x^1, m_y^1 \in \{+1, -1\}$ 이라 합니다. 마찬가지로 입자 2, 3에 대해서도 정의합니다.
양자역학의 $+1$ 이라는 예측과 일치해야 하므로, 국소 실재론의 모델은 다음 3개의 방정식을 만족해야 합니다.
1. $m_x^1 m_y^2 m_y^3 = +1$
2. $m_y^1 m_x^2 m_y^3 = +1$
3. $m_y^1 m_y^2 m_x^3 = +1$

이 3개의 방정식을 모두 곱합니다.
$(m_x^1 m_y^2 m_y^3)(m_y^1 m_x^2 m_y^3)(m_y^1 m_y^2 m_x^3) = +1 \times +1 \times +1 = +1$
좌변을 정리하면 각 $m_y^i$ 는 두 번씩 곱해지므로 $(m_y^i)^2 = 1$ 이 됩니다.
$m_x^1 m_x^2 m_x^3 (m_y^1)^2 (m_y^2)^2 (m_y^3)^2 = m_x^1 m_x^2 m_x^3 = +1$

즉, 국소 실재론을 따르는 한 $X_1 X_2 X_3$ 의 측정 결과는 반드시 $+1$ 이 되어야만 합니다.
그러나 앞서 보았듯이, 양자역학의 엄밀한 예측(그리고 실제 실험 결과)은 $-1$ 입니다.
$+1$ 과 $-1$. 통계적인 부등식조차 필요 없이 단일 측정에서 국소 실재론과 양자역학은 결정적으로 모순되며, 양자역학의 옳음이 증명된 것입니다.

(※참고로 3입자 얽힘에는 GHZ 상태와는 다른 성질을 가진 W 상태 $|W\rangle = \frac{1}{\sqrt{3}}(|100\rangle + |010\rangle + |001\rangle)$ 도 존재하여, 입자를 하나 잃어도 얽힘이 완전히 깨지지 않는다는 견고함을 가집니다.)

---

## 제6장: 양자정보과학에의 응용과 양자 원격전송의 엄밀 전개

얽힘은 역설의 대상에서 '정보 자원'으로 변모를 이루었습니다. 그 대표적인 예가 '양자 텔레포테이션(원격전송)'입니다. 1993년 찰스 베넷 등에 의해 제안되었고, 1997년 안톤 차일링거(2022년 노벨상 수상자) 그룹에 의해 처음으로 실험적으로 실증되었습니다.

### 양자 원격전송 프로토콜의 수식 전개

앨리스가 미지의 양자 상태 $|\phi\rangle = \alpha|0\rangle + \beta|1\rangle$ 를 가지고 있고, 이를 멀리 떨어진 밥에게 전송하고 싶다고 합시다. ($|\alpha|^2 + |\beta|^2 = 1$)
양자 복제 불가능 정리(No-cloning theorem)에 의해 이 상태를 복사해서 보낼 수는 없습니다. 또한 측정해 버리면 상태가 수축하여 미지의 $\alpha, \beta$ 를 정확히 알 수도 없습니다.

그래서 앨리스와 밥은 미리 얽힌 입자 쌍(EPR 쌍), 구체적으로 다음의 벨 상태 $|\Phi^+\rangle$ 를 공유해 둡니다.
$$ |\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$

앨리스의 수중에는 전송하고 싶은 입자(입자 C라 함)와 EPR 쌍의 한쪽(입자 A)이 있습니다. 밥의 수중에는 EPR 쌍의 다른 한쪽(입자 B)이 있습니다. 전체 계의 초기 상태는,
$$ |\psi_{total}\rangle = |\phi\rangle_C \otimes |\Phi^+\rangle_{AB} = (\alpha|0\rangle_C + \beta|1\rangle_C) \otimes \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$
전개하면,
$$ \frac{1}{\sqrt{2}} \left( \alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle \right) $$
(※첨자는 $C, A, B$ 의 순서)

여기서 앨리스는 수중에 있는 입자 C와 입자 A에 대해 '벨 측정(Bell measurement)'을 수행합니다. 이것은 2개의 입자를 다음 4개의 벨 상태 기저에 투영하는 측정입니다.
$|\Phi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle)$
$|\Psi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle)$

이것들을 이용하여 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ 을 역산하여 전체 계의 상태를 벨 기저 $|\cdot\rangle_{CA}$ 로 다시 묶으면, 놀랍게도 다음과 같이 변형할 수 있습니다.
$$ |\psi_{total}\rangle = \frac{1}{2} \left[ |\Phi^+\rangle_{CA}(\alpha|0\rangle_B + \beta|1\rangle_B) + |\Phi^-\rangle_{CA}(\alpha|0\rangle_B - \beta|1\rangle_B) + |\Psi^+\rangle_{CA}(\alpha|1\rangle_B + \beta|0\rangle_B) + |\Psi^-\rangle_{CA}(\alpha|1\rangle_B - \beta|0\rangle_B) \right] $$

앨리스가 벨 측정을 수행하면, 계는 이 4개의 항 중 어느 하나로 1/4의 확률로 수축합니다.
1. 만약 앨리스가 $|\Phi^+\rangle$ 을 얻은 경우, 밥의 상태는 $\alpha|0\rangle + \beta|1\rangle = |\phi\rangle$ 이 되어 이미 전송이 완료되어 있습니다(유니터리 연산 $I$).
2. 만약 $|\Phi^-\rangle$ 을 얻은 경우, 밥의 상태는 $\alpha|0\rangle - \beta|1\rangle$. 밥이 파울리 $Z$ 연산자($\sigma_z$)를 가하면 $|\phi\rangle$ 로 돌아옵니다.
3. 만약 $|\Psi^+\rangle$ 을 얻은 경우, 밥의 상태는 $\alpha|1\rangle + \beta|0\rangle$. 밥이 파울리 $X$ 연산자($\sigma_x$)를 가하면 $|\phi\rangle$ 로 돌아옵니다.
4. 만약 $|\Psi^-\rangle$ 을 얻은 경우, 밥의 상태는 $\alpha|1\rangle - \beta|0\rangle$. 밥이 $Z$ 를 가한 뒤 $X$ 를 가함으로써($XZ$ 또는 $i\sigma_y$) $|\phi\rangle$ 로 돌아옵니다.

앨리스는 측정 결과(2비트의 고전 정보: 00, 01, 10, 11)를 통상적인 통신(전화나 인터넷)을 통해 밥에게 전달합니다. 이 통신은 빛의 속도를 넘지 않으므로 상대성이론과 모순되지 않습니다. 밥은 전달받은 2비트에 따라 적절한 파울리 연산자를 적용하여 멋지게 미지의 양자 상태 $|\phi\rangle$ 를 복원합니다.
이것이 양자 원격전송의 완전한 프로토콜입니다.

---

## 제7장: 얽힘의 정량화(Quantification)

얽힘은 단순히 '있다' 혹은 '없다'뿐만 아니라 '얼마나 강하게 얽혀 있는가'를 정량화할 수 있습니다. 양자정보이론에서 이는 지극히 중요한 연구 주제입니다.

### 1. 폰 노이만 얽힘 엔트로피
순수 상태에 있는 2체계 $AB$ 의 얽힘의 정도를 측정하는 표준적인 척도가 폰 노이만 엔트로피입니다. 계 전체의 밀도 행렬을 $\rho_{AB} = |\psi\rangle\langle\psi|$ 라 하고, 계 B를 트레이스 아웃(축약)하여 계 A의 축약 밀도 행렬 $\rho_A = \text{Tr}_B(\rho_{AB})$ 를 구합니다.
이때 얽힘 엔트로피 $S$ 는 다음과 같이 정의됩니다.
$$ S(\rho_A) = -\text{Tr}(\rho_A \log_2 \rho_A) $$
벨 상태와 같은 최대 얽힘 상태에서는 $\rho_A$ 가 완전한 혼합 상태(단위 행렬에 비례)가 되며 $S = 1$(최댓값)을 가집니다. 직관적으로 말하면 "전체의 상태는 완전히 알고 있는데, 부분(계 A)만을 보면 전혀 정보가 없다(무작위로 보인다)"라는 얽힘의 본질을 나타냅니다.

### 2. 컨커런스(Concurrence)
혼합 상태를 포함하는 2 양자 비트 계의 얽힘을 측정하는 척도로서, 윌리엄 우터스 등이 고안한 '컨커런스 $C(\rho)$'가 있습니다.
밀도 행렬 $\rho$ 에 대하여, 스핀 반전 상태 $\tilde{\rho} = (\sigma_y \otimes \sigma_y) \rho^* (\sigma_y \otimes \sigma_y)$ 를 계산합니다($\rho^*$ 는 복소 켤레).
행렬 $R = \sqrt{\sqrt{\rho} \tilde{\rho} \sqrt{\rho}}$ 의 고윳값을 큰 순서대로 $\lambda_1, \lambda_2, \lambda_3, \lambda_4$ 라 했을 때, 컨커런스는 다음과 같이 정의됩니다.
$$ C(\rho) = \max(0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4) $$
$C(\rho)$ 는 $0$(얽힘 없음)에서 $1$(최대 얽힘) 사이의 값을 가지며, 이 값을 사용하여 '형성 얽힘(Entanglement of Formation)'이라는 또 다른 척도를 직접 계산할 수 있다는 강력한 수학적 성질을 가집니다.

### 3. 네거티비티(Negativity)
부분 전치(Partial transpose)의 개념에 기반한 척도가 Negativity $\mathcal{N}(\rho)$ 입니다.
계 $AB$ 의 밀도 행렬 $\rho$ 에 대하여, 계 B의 기저에 대해서만 전치를 취한 것을 $\rho^{T_B}$ 라 합니다. 만약 $\rho$ 가 얽혀 있지 않은(분리 가능한) 상태라면, $\rho^{T_B}$ 의 고윳값은 모두 음이 아닌 값이 됩니다(Peres-Horodecki의 PPT 판정 기준).
반대로 말하면, 음의 고윳값이 존재한다면 그것은 얽힘의 증거가 됩니다. Negativity는 $\rho^{T_B}$ 의 트레이스 노름 $||\cdot||_1$ 을 이용하여 다음과 같이 정의됩니다.
$$ \mathcal{N}(\rho) = \frac{||\rho^{T_B}||_1 - 1}{2} $$
이것은 음의 고윳값의 절댓값의 총합과 같으며, 계산이 용이하기 때문에 고차원 계나 다체계의 얽힘을 연구하는 데 있어 극히 유용한 지표가 되고 있습니다.

---

## 제8장: 실험적 검증과 허점(Loophole)의 완전 폐쇄

이론은 완성되었고, 응용도 보이기 시작했습니다. 남은 것은 자연계가 실제로 어느 법칙을 따르고 있는가를 실험실에서 캐묻는 것입니다.

### 알랭 아스페의 스위치 실험(1982년)
앨리스와 밥이 측정기의 각도를 결정한 후, 그 정보가 빛의 속도 이하의 스피드로 상대방 측에 전해져 '숨은 변수'에 영향을 미치고 있을 가능성을 배제해야 합니다. 이를 '국소성의 허점(Locality Loophole)'이라 부릅니다.
프랑스의 알랭 아스페 등은 광자가 광원에서 측정기를 향해 날아가는 동안 음향광학 소자를 이용하여 초고속으로 측정기의 각도 설정을 무작위로 전환하는 실험에 성공했습니다. 이를 통해 빛의 속도인 신호로도 정보를 전달할 수 없는 상황(공간적 격리)을 만들어내어, 멋지게 부등식의 깨짐을 관측했습니다. 아인슈타인의 '기묘한 원격 작용'은 현실이 된 것입니다.

### 궁극의 도전: 완전한 Loophole-free 실험(2015년)
아스페의 실험 후에도 검출 효율의 낮음(측정되지 못한 광자가 형편에 맞게 유리한 숨은 변수를 가지고 있었다고 하는 '검출의 허점 / Fair-sampling Loophole') 등 아주 미세한 반론의 여지가 남아 있었습니다.
그러나 2015년, 마침내 네덜란드 델프트 공과대학, 오스트리아 빈 대학, 미국 NIST 등 여러 연구 그룹이 모든 주요 허점을 동시에 막은 'Loophole-free Bell test'에 성공했습니다. 델프트의 실험에서는 1.3km 떨어진 다이아몬드의 NV 중심에 있는 전자 스핀을 얽히게 함으로써 국소성의 허점과 검출의 허점을 완전히 봉쇄하고, 국소 실재론의 관에 마지막 못을 박았습니다.

---

## 맺음말: 아인슈타인의 패배가 가져다준 빛

2022년, 양자역학의 기초를 결정적으로 확립한 알랭 아스페, 존 클라우저, 안톤 차일링거 3인에게 노벨 물리학상이 수여되었습니다.

아인슈타인은 양자역학의 확률적 성질과 비국소성을 싫어했고, 그것을 비판하기 위해 EPR 논문을 썼습니다. 그러나 아이러니하게도 그의 날카로운 비판이 '얽힘'이라는 개념을 명확하게 부각시켰고, 벨이라는 천재를 통해 인류가 우주의 비국소적인 연결을 진정으로 이해하고 기술로서 활용하기 위한 길을 열어주는 결과가 되었습니다.

아인슈타인의 '마지막 패배'는 결코 물리학의 정체가 아니라, 인류가 양자정보라는 전혀 새로운 우주의 언어를 획득하기 위한 위대한 새벽이었던 것입니다.

---
*글쓴이: 양자정보과학기술 라이터*
*이 기사는 양자역학의 기초부터 최첨단 양자정보기술까지를 망라한 학술적 해설입니다.*
