---
layout: post
title: Mysql 백업하기
category: DB
tag: Mysql
---

Mysql DB 백업을 하기 위해 `mysqldump`를 사용한다
  
기본적인 사용법은 아래와 같다.
{% highlight shell %}
mysqldump -u[username] -p[password] [db_name] > db.sql
{% endhighlight %}

여기에 `-h` 옵션으로 원격 Host를 넣어주면 원격 DB도 백업할 수 있다.

{% highlight shell %}
mysqldump -h [hostname] -u[username] -p[password] [db_name] > db.sql
{% endhighlight %}

특정 테이블만 백업할 때는 `db_name` 뒤에 table name을 넣어주면 된다.

{% highlight shell %}
mysqldump -h [hostname] -u[username] -p[password] [db_name] [table]> db.sql
{% endhighlight %}

복구는 아래처럼 하면된다.
{% highlight shell %}
mysql -u[username] -p[password] [dbname] < db.sql
{% endhighlight %}
