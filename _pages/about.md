---
layout: page
title: About me
---

{% highlight python%}
class MyProfile:
    
    def __init__(self) -> None:
        self.name: str = 'Taeju Kim'
        self.year_of_birth: int = 1987
        self.gender: str = 'male'
    
    def work_history(self) -> list:
        return [
            {
                'compan_name:':'NHN SOFT',
                'job_position':'Cloud Service QA(Manager)',
                'status':'current_work'
            },
            {
                'company_name':'LG Electronics', 
                'job_position':'TV SW QA',
                'status':'retire'
            }
        ]
        
    def contacts(self) -> dict:
        return {
            'email':'iam@taeju.kim',
            'github':'https://github.com/taejukim'
        }

{% endhighlight %}

## 안녕하세요!

SW QA엔지니어 김태주 입니다.

현재는 클라우드 서비스 QA로 일하고 있고 주로 자동화 Test 업무를 맡고 있습니다.

Linux, Python, JAVA, Testing Skill 등의 내용을 포스팅하고 있습니다.


감사합니다!
