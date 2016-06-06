from django import forms

class UserAnswerForm(forms.Form):
    answer = forms.CharField(label="Svar")
