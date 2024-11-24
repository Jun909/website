from django import forms
from .models import UserInfo
from django.utils.translation import gettext as _

class UserInfoForm(forms.ModelForm):
    HIGHEST_EDUCATION_CHOICES = [
        ('硕士','硕士'),
        ('博士','博士'),
        ('博士后','博士后'),
        ('其他','其他'),
    ]

    GENDER_CHOICES =[
        ('男', '男'),
        ('女', '女'),
    ]

    MAJOR_TYPE_CHOICES = [
        ('哲学', '哲学'),
        ('经济学','经济学'),
        ('法学','法学'),
        ('教育学','教育学'),
        ('文学','文学'),
        ('历史学','历史学'),
        ('理学','理学'),
        ('工学','工学'),
        ('农学','农学'),
        ('医学','医学'),
        ('军事学','军事学'),
        ('管理学','管理学'),
        ('艺术学','艺术学'),
    ]

    EXPERIENCE_ABROAD_CHOICE = [
        ('有','有'),
        ('没有','没有'),
    ]

    TARGET_WORKING_PLACE = [
        ('华南','华南'),
        ('华北','华北'),
        ('华中','华中'),
        ('西南','西南'),
        ('西北','西北'),
        ('东北','东北'),
        ('华东','华东'),
        ('地区不限（默认所有城市都可接受）','地区不限（默认所有城市都可接受)'),

    ]

    TYPE_OF_JOB = [
        ('公办高校','公办高校'),
        ('民办高校','民办高校'),
        ('课题组','课题组'),
        ('科研机构','科研机构'),
        ('国企央企','国企央企'),
        ('私企','私企'),
        ('事业单位','事业单位'),
        ('医院','医院'),
        ('中小学','中小学'),
        ('幼儿园','幼儿园'),
        ('其他','其他'),

    ]

    JOB_POSITION_WANTED = [
        ('教学教研岗','教学教研岗'),
        ('行政管理岗','行政管理岗'),
        ('辅导员岗','辅导员岗'),
        ('研究/技术岗','研究/技术岗'),
        ('企业岗','企业岗'),
        ('博士后','博士后'),
    ]

    POLITICAL_INFO = [
        ('党员','党员'),
        ('预备党员','预备党员'),
        ('团员','团员'),
        ('群众','群众'),
    ]

    HIGHEST_TITLE_ACHIEVED = [
        ('初级','初级'),
        ('中级','中级'),
        ('副高','副高'),
        ('正高','正高'),
        ('无','无'),
    ]


    highest_education = forms.ChoiceField(choices=HIGHEST_EDUCATION_CHOICES, widget= forms.RadioSelect, label= "您的最高学历（含在读）:")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='您的性别：')
    major_type = forms.ChoiceField(choices=MAJOR_TYPE_CHOICES,widget=forms.RadioSelect, label= '您的学科门类是：')
    experience_abroad = forms.ChoiceField(choices=EXPERIENCE_ABROAD_CHOICE, widget=forms.RadioSelect, label= '您是否有海外的正式工作经历：')
    target_working_place = forms.MultipleChoiceField(choices=TARGET_WORKING_PLACE, widget=forms.CheckboxSelectMultiple, label = '您的意向求职地区:【多选题】')
    type_of_job = forms.MultipleChoiceField(choices=TYPE_OF_JOB, widget=forms.CheckboxSelectMultiple, label='您的意向求职单位类型：【多选题】')
    job_position_wanted = forms.MultipleChoiceField(choices=JOB_POSITION_WANTED, widget=forms.CheckboxSelectMultiple, label='您的意向岗位类型：【多选题】')
    time_of_graduation = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), label='您的毕业时间：')
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), label='您的出生日期：')
    political_info = forms.ChoiceField(choices=POLITICAL_INFO, widget=forms.RadioSelect, label= '您的政治面貌：')
    highest_title_achieved = forms.ChoiceField(choices=HIGHEST_TITLE_ACHIEVED, widget=forms.RadioSelect, label= '您获评的最高称职：')


    class Meta:

        model = UserInfo
        fields = ["name", "highest_education", "gender", "major_type", "major", "university", "experience_abroad", "target_working_place",
                  "type_of_job", "job_position_wanted", "email", "time_of_graduation", "birthdate", "political_info", "highest_title_achieved", "resume" ]
        labels = {
            'name' : '您的姓名：',
            'highest_education' : '您的最高学历（含在读）：',
            'gender' : '您的性别：',
            'major_type' : '您的学科门类是：',
            'major' : '您的专业：',
            'university' : '您的毕业院校（最高学历）：',
            'experience_abroad':'您是否有海外的正式工作经历：',
            'target_working_place' : '您的意向求职地区:【多选题】',
            'type_of_job': '您的意向求职单位类型：【多选题】',
            'job_position_wanted' : '您的意向岗位类型：【多选题】',
            'email': '您的邮箱地址：',
            'time_of_graduation': '您的毕业时间：',
            'birthdate': '您的出生日期：',
            'political_info': '您的政治面貌：',
            'highest_title_achieved': '您获评的最高称职：',
            'resume': '您的简历：'

        }