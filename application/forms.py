from django import forms
from .models import UserInfo
from django.utils.translation import gettext as _

class UserInfoForm(forms.ModelForm):
    class Meta:

        model = UserInfo
        fields = ["name", "highest_education", "gender", "major", "university", "experience_abroad", "target_working_place",
                  "type_of_job", "job_position_wanted", "email", "time_of_graduation", "birthdate", "political_info", "highest_title_achieved", "resume" ]
        labels = {
            'name' : '姓名'
        }