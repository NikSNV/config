from django import forms
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.Form):
    to_emails = forms.CharField(label='Получатели', widget=forms.TextInput(attrs={'size': 75,
                                                                                  'placeholder': 'Вводите EMAIL получателей через ПРОБЕЛ!'}),
                                required=True)
    subject = forms.CharField(label='Тема', required=True, widget=forms.TextInput(attrs={'size': 80}))
    message = forms.CharField(label='Сообщение', widget=CKEditorWidget(), required=True)
    # message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'rows': 4, 'cols': 100}), required=True)
