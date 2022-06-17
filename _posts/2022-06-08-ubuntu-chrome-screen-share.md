---
layout: post
title: Ubuntu 22.04에서 Chrome에 화면 공유하기
category: linux
tag: [linux, ubuntu]
---

Ubuntu 22.04 부터는 Wayland를 윈도우 시스템으로 사용한다.  

Wayland에서는 화면 공유에 대한 권한을 좀더 강력하게 다루는지 Chrome에서 전체 화면 공유가 되지 않는다.  

Chrome에서 **[chrome://flags/](chrome://flags/)** 를 진입하면 아래와 같이 Experiments page가 나온다.  
아래 page에서  **`WebRTC PipeWire support`** 항목을 Enable로 변경하고  Chrome을 재시작 하면된다.

![chrome experiments](/assets/images/chrome_experiments.png)
