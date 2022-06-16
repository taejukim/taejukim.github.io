---
layout: post
title: Pandas Dataframe 특정 필드에 포함된 문자열 검색하기
category: Python
tag: Pandas
---

|   |name | age | gender |
| --- | --- | --- | --- |
| 0 | kim taeju | 30 | male |
| 1 | lee jungjae | 40 | male |
| 2 | kim yuna | 25 | female |

위와 같은 Dataframe 에서 특정 필드에 원하는 Text가 포함된 row를 찾으려면 `field_name.str.contains` 에 찾고자하는 Text를 넘겨주면 된다.

{% highlight python %}
df[df.name.str.contains("kim")]
{% endhighlight %}

| | name | age | gender |
| --- | --- | --- | --- |
| 0 | kim taeju | 30 | male |
| 2 | kim yuna | 25 | female |
