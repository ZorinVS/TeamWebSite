from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Иван Иванов"
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "placeholder": "you@example.com"
        })
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={
            "placeholder": "Напишите, чем мы можем помочь",
            "rows": 5
        })
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Имя не должно содержать цифры.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) < 10:
            raise forms.ValidationError("Пожалуйста, уточните ваше сообщение подробнее.")
        return message
