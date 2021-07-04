---
title: shell programming - basic
category: shell_programming
tags: shell zsh bash shell_programming 
---

## shell programming - basic

- 최근에 bash, zsh 등에서 shell programming을 해야할 필요성이 생겨서, 비교적 간단한 몇 가지 문법을 정리해 봅니다.

```bash
# echo: 터미널 기본 출력 창(stdout)에 값을 출력하는 command
# cat: file을 읽어서 file의 결과를 그대로 출력하는 command
# >: 출력 결과를 파일에 저장합니다(write)
# >>: 출력 결과를 파일에 추가합니다(append)
echo "Hello shell!!!" > ./hello.txt
cat ./hello.txt
echo "=============================="
echo "Helll shell again!!!" >> ./hello.txt
cat ./hello.txt

echo "-- pipeline | -----------------"
# |: pipeline. 이전 명령의 출력 결과를 다음으로 보냅니다.
ls -al | grep "hello"

# variable: = 앞 뒤로 공백이 있으면, 오류가 발생합니다.
# variable을 사용할 때는 $ 를 앞에 붙이고 사용합니다.
echo "-- variable -------------------"
var1="my_first_variable"
echo "Hello $var1"

# $(command): command의 결과를 변수화합니다.
echo $(ls) > ./new_hello.txt
cat ./new_hello.txt


# command1 && command2
# command1을 실행하고, 그 다음 command2를 실해함.
# command1이 실행되지 않으면, command2가 실행되지 않음.
echo "-- && -------------------------"
ls
# new_text.txt 가 존재하지 않기 때문에 
# command1은 실패하고, command2도 실행되지 않는다. 
rm new_text.txt
rm new_text.txt && echo >> new_text.txt
rm new_text.txt
ls 

# command1 ; command2 
# 앞의 command가 실행 여부와 상관없이 모두 실행합니다.
echo "abc" ; echo "def"

# \ : 1개의 명령어를 여러 줄로 나누어 작성할때 사용합니다.
echo \
    "echo_with multi line"

# {a,b,c}: a, b, c로 구성된 array 라고 생각하면 됩니다.
# command {a,b,c}: a, b, c 파일에 모두 command를 수행한다, 라고 이해하면 됩니다.
# comma 옆에 공백이 있을 경우 parsing error가 발생합니다.
echo {1..10}
echo "abcdefg" > {a.txt,b.txt} 
ls -al | grep .txt
echo "--------------------------"
rm {a.txt,b.txt}
ls -al | grep .txt


# if statement 기본 구조는 다음과 같습니다.
# 여기서도, [ $var1 -eq $var2 ] 에서 space를 정확하게 지켜주셔야 합니다.
var1=3
var2=4
if [ $var1 -eq $var2 ]
    then
        echo "var1 = var2"
else 
    echo "var1 != var2" 
fi

# for statement
for i in {1,2,3} 
do
    echo "Hello world $i"   
done


# export: 외부 변수로 만듭니다.
# 즉, 해당 변수는 이 shell script외부에서도 사용할 수 있게 된다는 얘기죠.
export global_var1="Hello world"
```
