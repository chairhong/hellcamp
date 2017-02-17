Fortune Cookie
==============
# intro
fortune cookie를 다운받아서 32비트 elf 파일이고, checksec은 canary와 nx가 걸려있음을 알았다.
파일을 실행했을 때, 세그먼트 폴트가 떠서 ltrace로 보니 /home/fortune_cookie/flag가 없어서임을 알고 만들어 주었다.

ida로 파일을 열었는데, main에서 flag을 읽어주는 함수를 오픈해주고, 입출력도 따로 함수를 통해 출력해주는 것을 확인했다. 입력하는 string의 크기는 100인데, 100만큼의 크기를 입력받을 수 있고 canary 까지의 거리는 108이었다.

-----------------------------------------------