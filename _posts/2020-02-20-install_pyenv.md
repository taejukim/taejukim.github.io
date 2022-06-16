---
layout: post
title: ubuntu22.04에 pyenv 설치하기
category: Python
tag: [Python]
---
pyenv는 linux에서 python의 버전관리와 생성된 가상환경을 관리해 주는 아주 유용한 툴이다.</br>
손쉽게 여러 python 버전을 사용 할 수 있도록 지원해준다.

### Pyenv 설치
{% highlight shell %}
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
{% endhighlight %}


설치 후 .bashrc 또는 .zshrc에 아래 내용을 추가한다.
{% highlight shell %}
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
{% endhighlight %}

### 설치 확인
{% highlight shell %}
$ pyenv -v
pyenv 2.3.0-10-g8608d60f
{% endhighlight %} 
