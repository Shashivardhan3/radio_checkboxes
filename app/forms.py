from django import forms

g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('django','DJANGO'),('api',('API')),('selenium','SELENIUM')]


class RegistrtionForm(forms.Form):
    Name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
    # gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

