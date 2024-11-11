from django import forms
from .models import UserInfo
from django.utils.translation import gettext as _

class UserInfoForm(forms.ModelForm):
    HIGHEST_EDUCATION_CHOICES = [
        ('master','硕士'),
        ('phd','博士'),
        ('postdoc','博士后'),
        ('other','其他'),
    ]

    GENDER_CHOICES =[
        ('male', '男'),
        ('female', '女'),
    ]

    MAJOR_TYPE_CHOICES = [
        ('philosophy', '哲学'),
        ('economic','经济学'),
        ('law','法学'),
        ('education','教育学'),
        ('literature','文学'),
        ('history','历史学'),
        ('science','理学'),
        ('engineering','工学'),
        ('agronomy','农学'),
        ('medicine','医学'),
        ('military science','军事学'),
        ('management','管理学'),
        ('art','艺术学'),
    ]

    EXPERIENCE_ABROAD_CHOICE = [
        ('yes','有'),
        ('no','没有'),
    ]


    highest_education = forms.ChoiceField(choices=HIGHEST_EDUCATION_CHOICES, widget= forms.RadioSelect, label= "您的最高学历（含在读）:")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='您的性别：')
    major_type = forms.ChoiceField(choices=MAJOR_TYPE_CHOICES,widget=forms.RadioSelect, label= '您的学科门类是：')
    experience_abroad = forms.ChoiceField(choices=EXPERIENCE_ABROAD_CHOICE, widget=forms.RadioSelect, label= '您是否有海外的正式工作经历：')

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

        }