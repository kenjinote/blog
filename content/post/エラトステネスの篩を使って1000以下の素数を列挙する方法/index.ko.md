---





title: "'에라토스테네스의 체를 사용하여 1000 이하의 소수를 나열하는 방법'"
slug: "エラトステネスの篩を使って1000以下の素数を列挙する方法"
date: 2023-04-09T12:54:24+09:00
tags: ["에라토스테네스의 체", "소수", "수학", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["수학·암호·양자"]
---






## 에라토스테네스의 체란

에라토스테네스의 체는 어떤 수 이하의 소수를 나열하는 알고리즘입니다.
알고리즘은 단순하며, 다음 절차로 구현할 수 있습니다.

1. N개의 요소를 가진 bool 값 배열을 만들고, 모든 요소를 true로 초기화한다
2. 배열의 0번째와 1번째 요소를 false로 한다(0과 1은 소수가 아니기 때문)
3. 배열의 2번째 요소가 true라면, 2를 소수로 출력한다
4. 배열의 $2^2$ 이상의 2의 배수 번째 요소를 모두 false로 한다※
5. 배열의 3번째 요소가 true라면, 3을 소수로 출력한다
6. 배열의 $3^2$ 이상의 3의 배수 번째 요소를 모두 false로 한다
7. 4번째, 5번째, ..., N번째 요소에 대해 동일한 처리를 반복한다

※ 2제곱 이상의 요소를 false의 대상으로 하는 이유는, 2제곱보다 작은 수에 대해서는 이미 처리가 완료되었기(나열이 완료되었기) 때문입니다.

![](Animation_Sieb_des_Eratosthenes.gif)


## Rust에서의 구현

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![true; n+1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..=n {
        if is_prime[i] {
            println!("{}", i);
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
    }
}
```

## 조금 더 고속화된 버전

다음 사항을 고려하여, 조금 더 고속화된 구현을 수행합니다.

- 배열을 true로 초기화하는 것이 아니라, false로 초기화한다 (이 편이 더 고속)
- 2의 배수는 소수가 아니므로, 2의 배수 요소를 false로 하는 처리를 생략
- n까지 루프를 돌 필요 없이, n의 제곱근까지의 소수를 나열하면, n 이하의 소수를 나열할 수 있다

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![false; n+1];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }
    for i in 3..=((n as f64).sqrt() as usize) {
        if is_prime[i] {
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i * 2;
            }
        }
    }
    for i in (2..=n).filter(|&x| is_prime[x]) {
        println!("{}", i);
    }
}
```

## 참고
- [에라토스테네스의 체](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)
