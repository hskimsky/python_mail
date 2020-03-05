# python_mail

* python3 으로 local file 을 첨부파일로 mail 보내기
* Python 3.6.3 :: Anaconda, Inc. 에서 테스트 함

## Supported Mail Server

* smtp.gmail.com

## Requirements

### Gmail

1. [Google 계정 보안](https://myaccount.google.com/security)에 접속
1. 2단계 인증
1. **앱 비밀번호 생성**(이 때 생성된 비밀번호 영문 16글자를 잘 복사해둠)

### config.ini

* config.ini 파일에 sender 정보 입력
* SENDER_PASSWORD 에 아까 복사해둔 영문 16글자를 넣음

```
[DEFAULT]
SENDER_EMAIL = sender@gmail.com
SENDER_PASSWORD = abcdefghijklmnop
```

## Execution

### Usage

```
usage: send_mail.py [-h] [-s SENDER] [-p SENDERPASSWORD] [-r RECEIVERS]
                    [-f FILEPATTERN [FILEPATTERN ...]]

optional arguments:
  -h, --help            show this help message and exit
  -s SENDER, --sender SENDER
                        sender
  -p SENDERPASSWORD, --senderpassword SENDERPASSWORD
                        sender password
  -r RECEIVERS, --receivers RECEIVERS
                        receivers. comma delimited
  -f FILEPATTERN [FILEPATTERN ...], --filepattern FILEPATTERN [FILEPATTERN ...]
                        send absolute paths of file pattern.
```

* receivers 는 여러명에게 보낼 수 있도록 `,` 로 구분하여 넣을 수 있음
* 첨부파일 경로는 pattern 을 여러개 넣을 수 있도록 함

### Execute

```bash
python send_mail.py -r hskimsky@naver.com,hskimsky@gmail.com -f /path/to/files*.txt
```
