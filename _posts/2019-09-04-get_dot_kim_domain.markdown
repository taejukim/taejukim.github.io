---
title: 닷킴(.kim) 도메인을 사보자
layout: post
date: '2020-09-04 00:00:00'
categories: doamin
tags:
- domain
- aws
- route 53
---

---

[![get kim intro](/assets/images/posts/img_190904/get_kim_intro.png)](https://get.kim)

~~.KIM 가족의 자부심을 보여줘~~


예전 부터 나를 나타낼 수 있는 괜찮은 도메인하나 구매하려고 했었는데 짧고 간결한 도메인은 죄다 이미 사용중이었다.
taeju.com, taeju.net, taeju.co.kr 등등..

최근 최상위 도메인을 관리하는 기관인 [ICANN](https://www.icann.org/){:target="_blank"}에서 시대 일반 도메인이라는 항목 중 .kim 도메인을 등록했다는 정보를 웹서핑하다가 알게 되었다.

* [인터넷 최상위 도메인 목록](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%EB%84%B7_%EC%B5%9C%EC%83%81%EC%9C%84_%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%AA%A9%EB%A1%9D#ICANN_%EC%8B%9C%EB%8C%80_%EC%9D%BC%EB%B0%98_%EC%B5%9C%EC%83%81%EC%9C%84_%EB%8F%84%EB%A9%94%EC%9D%B8){:target="_blank"}

그래서 바로 **taeju.kim** 도메인을 찾아봤는데 등록이 가능했다.

바로 AWS route 53에 가서 도메인 가격을 조회하니 $15 였다.~~(Tex 포함 $16.5)~~

AWS가 가장 싼거 같다. 이제 AWS Route 53에 가서 .kim 도메인을 사보겠다.

## 1. AWS Route 53 도메인 구매
- AWS Route 53은 도메인 등록 및 해당 도메인에 대한 트래픽 관리등을 해주는 AWS의 네트워킹 관련 서비스 이다.
- [**AWS Console > Route 53**](https://console.aws.amazon.com/route53/){:target="_blank"}

![aws_route_53](/assets/images/posts/img_190904/aws_route_53_service_location.png)

- 원하는 도메인 검색 후 장바구니 추가

![search_domain](/assets/images/posts/img_190904/search_domain.png)
![장바구니](/assets/images/posts/img_190904/in_cart.png)

- 등록 정보 입력 후 구매 완료 
![구매완료](/assets/images/posts/img_190904/complete_domain.png)

* 구매 완료 후 조금만 지나면 설정이 완료되고 사용이 가능하다.



## 2. AWS Route 53 도메인 설정

* 도메인 구매가 완료되면 Route 53 등록된 도메인 메뉴에 아래와 같이 등록된 도메인이 표시된다.
![도메인 리스트](/assets/images/posts/img_190904/domain_list.png)

* 해당 도메인을 클릭하면 상세정보가 표시되는데 이중 **DNS관리** 메뉴에 진입하면 설정이 가능하다.
![레코드 셋](/assets/images/posts/img_190904/record_set.png)


AWS Route 53의 경우 다른 도메인 판매 업체에 비해 저렴한 것 같다.
보통 $20 이상인데 **AWS Route 53은 $15**이다.

AWS Route 53에서는 도메인 이름 관리 외 호스팅 영역 관리 및 트래픽 흐름 관리와 같은 서비스를 제공하고 있지만, 단순히 도메인 등록 및 관리만 할 것이라면 연간 도메인 유지비 외 발생되는 금액은 없는 것 같다.

다음 포스팅에서는 구매한 도메인을 활용해 차례로 아래와 같은 내용을 다뤄보겠다.

---

**1. AWS Route 53에서 구매한 도메인 Gmail에 연결하기**

**2. Github page 도메인으로 사용하기**

