---
title: rust를 써보기로 했습니다. 
category: others
tags: rust programming-language programming pyconkr pycon
---

## 왜 갑자기 Rust.

- Rust라는 언어가 있다는 것은 알고 있었습니다만, 별로 써봐야겠다는 생각은 하지 않았어요. 
- 그러던 중에 최근 pyconkr2018에서 발표한 [Rust를 이용해서 당신의 python에 날개를 달아주세요](https://www.slideshare.net/JIHUNKIM26/rust-python-110278438)라는 발표를 보고 한번 이 발표자료를 따라가보기로 했습니다. 

## what is Rust

- [Rust 한국 공식 홈페이지](https://www.rust-lang.org/ko-KR/index.html)에 들어가면 자세하게 나와 있습니다.
- 정리하면, 대략 
    - 비용 없는 추상화
    - "이동"(move) 의미론
    - 메모리 안전성 보장
    - 데이터 레이스 없는 스레딩
    - 트레이트 기반 일반화(generic)
    - 패턴 매칭
    - 타입 추론
    - 최소한의 런타임
    - 효율적인 C 바인딩

- 등이 있다고 합니다만, 무슨 말인지 모르겠어요. 일단 하면서 배워야 할 것 같은데요 흠.

## do it

- 사실 [여기에](https://doc.rust-lang.org/book/2018-edition/ch01-01-installation.html) 다 나와 있는 내용이기는 한데, 그냥 정리합니다 하핫. 

### install it 

- 일단 설치를 하구요. 뭐라뭐라 뜨는데, 그냥 1을 누르면 디폴트로 설치가 됩니다. 

```bash
curl https://sh.rustup.rs -sSf | sh
```

- `rustc --version`을 실행했는데, `command not found`등이 뜬다면, rust 가 환경변수에 등록되어있지 않다는 이야기죠. 

- `vi ~/.bash_profile`를 실행해서 내부에 ` export PATH="$HOME/.cargo/bin:$PATH"`가 등록되어 있는지를 보세요. 등록이 되어있다면, 그냥 터미널을 껐다가 키면 잘 됩니다. 없으면 이 부분을 등록시키구요. 


### hello world

- 일단 `hello_world.rs`라는 파일에 아래 코드를 작성합니다. 

```rust
fn main(){
    println!("Hello world!")
}
```

- 그리고, rustc를 통해 해당 코드를 컴파일 하면, binary executable한 파일이 같은 폴더 내에 생성됩니다. 
- 그리고 두번째 커맨드를 실행하면 binary executable하게 변경된 파일이 실행됩니다. 

```bash
rustc hello_world.rs
./hello_world
```

- 보통 python의 경우는 `python a.py`를 실행하면, 컴파일되고 자동으로 러닝까지 되는데, rust의 경우는 compiling, running이 구별되어 있습니다. 조금 번거롭다, 라는 생각은 드는데, 목적이 다르다고 생각하면 될 것 같아요. 
- 예를 들어서 python, ruby같은 랭기지들의 경우에는 compile과 running이 같이 되고 보통 다른 사람들에게 작업의 결과를 전달할 때 코드를 전달하는 일이 많죠. 이는 기본적으로 "상대방이 해당 언어의 컴파일러를 가지고 있다"라고 전제합니다. 반면 rust의 경우는 "상대방이 compiler가 없다"라고 전제합니다. 따라서 binary executable을 생성하고 이를 보내죠. binary executable의 경우는 rust compiler가 설치되어 있지 않아도 상대방이 잘 실행할 수 있습니다. 

### cargo 

> Cargo is Rust’s build system and package manager. 

- 입니다. 빌드, 패키지 매니저가 이렇게 초반에 나오는 일은 잘 없었던 것 같은데, 조금 신기하네요. 다른 언어들과는 다르게 rust는 시스템 랭기지 라는 것을 강조하고, 작은 규모의 프로그램을 만드는 것보다 큰 규모의 프로그램을 만드는 일에 강점을 보인다 뭐 이런 이야기들이 쭉 있었는데, 아마도 그 측면에서 학습할 때도 build, package 관리 등을 강조하는 것 같네요. 
- 저는 python으로 코딩을 꽤 많이 했고, 이제 꽤 잘하는 레벨까지 갔다고 할 수 있지만 build, run 이런걸 별로 안해봤거든요. 뭐 이렇게 배우는 거죠 뭐 하하핫 

```bash 
cargo new <project_name> # 프로젝트 폴더 생성 
cargo build ## project compile, 프로젝트 폴더 내에서 실행
cargo run ## project compile and run , 프로젝트 폴더 내에서 실행
cargo run --release
```

- 또한 필요한 라이브러리들이 있을 경우에는 cargo project내의 `.toml` 파일 내에 dependencies 에 작성해줍니다. 이렇게 하면 이후에 `cargo build`를 하면 알아서 가져와서 합쳐줍니다 하하 편하군요. 
- 어떤 라이브러리들이 있는지는 [crates.io](https://crates.io/)에서 보시면 좋습니다. 사실 `pip install <lib_name>`하는 것처럼 `cargo install <lib_name>`을 해도 될 것 같아요. 그런데 rust에서는 처음부터 프로젝트를 만들고 `.toml`에 dependencies를 작성하는 식으로 코딩해라, 라고 약간 가이드를 준 것 같아서, 가능하면 프로젝트별로 따로 구성하고 디펜던시도 거기에 맞춰서 configure하여 진행해보려고 합니다. 

```toml
[package]
name = "guessing_game"
version = "0.1.0"
authors = ["frhyme <freerhein@gmail.com>"]

[dependencies]
rand = "0.3.14"
```


## summary 

- 간단하게 코딩해보면서 좀 보고 있는데, 대략 다음과 같은 특이점? 들이 있는 것 같아요. 

1. default variables are immutable
    - 변수를 선언할 때, 기본적으로 immutable로 지정됩니다. immutable은 functional programming 쪽에서 오류를 줄이기 위해서 많이 사용하는 방법이기도 하고, 이를 통해 concurrency도 보장이 되기는 한다는데, 아무튼 그냥 `let x = 10` 이렇게 하고 이후 코드에서 `x = 11` 이렇게 하면 오류가 발생합니다. 

2. cargo
    - `pip`와 매우 유사하기는 합니다만, 처음부터 project를 만들고 내부에 `.toml`파일에서 디펜던시를 처리하면서 관리하도록 약간은 강제? 한다는 것이 매우 바람직한 것 같아요. 사실 python의 경우는 이 부분이 너무 중요하게 다루어지지 않는 부분이 있긴 하죠. 

3. type 
    - 기본적으로 변수, 함수 모두 type이 선언되는 것이 약간 선호됩니다. 특히 함수의 경우는 다음과 같이 선언이 되어야 하죠. 원래 c, c++ 모두 이런 식으로 해주기는 했는데, 매번 python으로 코딩해서 오랜만에 보니까 좀 낯설군요. 

    ```rust 
    fn plus_one(x: i32) -> i32 {
        return x + 1;
    }
    ```

4. ownership 
    - 자세한 내용은 [여기에서](https://doc.rust-lang.org/book/2018-edition/ch04-01-what-is-ownership.html) 볼 수 있기는 합니다. 
    - 보통 프로그래밍 언어에서 메모리를 관리하는 방법은 두 가지로 나뉩니다. 1) 프로그램이 돌아갈 때 garbage collection이 계속 사용되지 않는 메모리를 찾아서 삭제해주는 방식 2) 프로그래머가 직접 메모리를 할당, 제거 해주는 방식 
    - rust의 경우는 약간 특이하게 처리합니다. 간단하게 말하면, `shallow copy`를 허용하지 않는다 라고 할 수 있어요(rust에서는 `shallow copy`를 `move`라고 표현합니다. 
    - 예를 들어서 아래와 같은 코드가 있다고 합시다. `s2=s1`이라는 코드는 s1의 값을 s2로 이동했다는 의미고, 통상적으로 다른 언어에서는 s1, s2 모두 같은 메모리를 공유하게 됩니다. 따라서 아래 코드에서 문제가 없어야 하는데, rust에서는 문제가 발생합니다. s1을 삭제해버리거든요. 하나의 메모리에 대해서 1개 초과의 name을 허용하지 않습니다. 즉 s1의 값이 s2로 움직인 상황에서 s1은 삭제되는거죠(물론 deep copy를 하면 되기는 합니다).

    ```rust
    let s1 = String::from("hello");
    let s2 = s1;

    println!("{}, world!", s1);
    ```
    - 사실 습관적으로 shallow copy를 남발해서 메모리 문제를 발생시키는 습관이 있는데, 컴파일 레벨에서 이러한 문제를 다 잡아주면 좋을 것 같기는 합니다. 


## wrap-up

- 나쁘지 않은데, 문법이 좀 낯설어서 쓰기 귀찮네요 허허. 이미 파이썬으로 꽤 충분하기도 하고, 뭐 굳이 더 해야 하나...싶기도 하구요. 
- [speed up your python using Rust](https://developers.redhat.com/blog/2017/11/16/speed-python-using-rust/)를 보고 좀 더 공부해보려고 합니다 하핫. 