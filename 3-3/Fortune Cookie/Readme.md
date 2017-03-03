Fortune Cookie
==============
# intro
```
![file](/3-3/Fortune Cookie/img/1.jpg)
```
fortune cookie 파일은 32비트 elf 파일이고, stripped는 걸려있지 않다.

```
![checksec](/3-3/Fortune Cookie/img/2.jpg)
```
보호기법은 Canary와 NX만 걸려있다. 파일을 한번 실행해보자

```
![execute](/3-3/Fortune Cookie/img/3.jpg)
```
단순하게 문자열을 입력받고, 입력받은 문자열을 출력해주는 프로그램이다.

# 분석ㄱㄱ

![loadkey](/3-3/Fortune Cookie/img/4.jpg)
main 함수를 들여다보면, loadkey()라는 함수를 호출하는데, 이 부분해서 flag를 불러온다.

![loadkey_func](/3-3/Fortune Cookie/img/5.jpg)
flag를 불러와서 stream에 저장하는데, bss 영역에 저장된다고 한다.

![g_canary](/3-3/Fortune Cookie/img/6.jpg)
바이너리 자체에도 canary가 걸려있지만, 프로그램 내부에서 time rand를 사용하여 canary 값을
별도로 생성해준다. 이것을 canary_value에 저장해주는데, 이 부분이 다를 경우 Attack Detected.를
무한정 띄워준다.

중간에 input_wrap이라고 하는 부분을 보자

![input_wrap](/3-3/Fortune Cookie/img/7.jpg)
a1은 &string이고, a2는 v9이다. 윗 부분에서 v9에 100을 넣어줬으므로
문자를 하나씩 100번 입력받아주는 친구인 것이다.

![value](/3-3/Fortune Cookie/img/8.jpg)
다시 main으로 돌아와 변수를 살펴보면, 우리는 string 부분을 쭉 입력해서 canary_value를 덮어씌워야만 한다. 그러나 둘의 차이는 104만큼 차이난다. 100번 입력해서 보내줘보자

![expy](/3-3/Fortune Cookie/img/9.jpg)
![result](/3-3/Fortune Cookie/img/10.jpg)
A 100번을 입력해서 보내보았더니, 끝에 d라는 수상한 친구가 뜬다. 한번 무엇인지 확인해보자.

그냥 d였다..