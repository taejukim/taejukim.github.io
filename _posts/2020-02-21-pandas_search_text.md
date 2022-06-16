---
layout: post
title: Pandas Dataframe 특정 필드에 포함된 문자열 검색하기
category: Python
tag: Pandas
---

<table>
    <thead>
        <tr>
            <th>name</th>
            <th>age</th>
            <th>gender</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>kim taeju</td>
            <td>30</td>
            <td>male</td>
        </tr>
        <tr>
            <td>lee jungjae</td>
            <td>40</td>
            <td>male</td>
        </tr>
        <tr>
            <td>kim yuna</td>
            <td>25</td>
            <td>female</td>
        </tr>
    </tbody>

----

위와 같은 Dataframe 에서 특정 필드에 원하는 Text가 포함된 row를 찾으려면 `field_name.str.contains` 에 찾고자하는 Text를 넘겨주면 된다.

{% highlight python %}
df[df.name.str.contains("kim")]
{% endhighlight %}