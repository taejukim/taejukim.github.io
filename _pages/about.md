---
layout: page
title: About me
---


{% highlight python%}
from skill_decorators import advanced, intermediate, basic

class MyProfile:
    
    def __init__(self) -> None:
        self.name: str = 'Taeju Kim'
        self.year_of_birth: int = 1987
        self.gender: str = 'male'

    def get_study(self) -> dict:
        return {
            'major':'Information and Communication Engineering',
            'certificate':['ISTQB','Engineer Information Processing(정보처리기사)']
        }
    
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


class MySkill(MyProfile):

    def qa_skills(self) -> dict:

    
    def languages(self) -> dict:
        return {
            'advenced':['python','java'],
            'intermediate':['javascript','html','css'],
            'basic':['SQL','shellscript','typescript','groovy']
        }
    
    def libraries(self) -> dict:
        return {
            'advenced':['selenium','django', 'pandas'],
            'intermediate': ['fastapi', 'appium'],
            'basic':['testcafe']
        }

    def others(self) -> dict:
        return {
            'advanced':[]
        }
{% endhighlight %}

## 안녕하세요!

SW QA엔지니어 김태주 입니다.

현재는 클라우드 서비스 QA로 일하고 있고 주로 자동화 Test 업무를 맡고 있습니다.

Linux, Python, JAVA, Testing Skill 등의 내용을 포스팅하고 있습니다.



[iam@taeju.kim](mailto:iam@taeju.kim)

감사합니다!
