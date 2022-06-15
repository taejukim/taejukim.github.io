# from skill_decorators import advanced, intermediate, basic


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