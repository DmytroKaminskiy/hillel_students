from django import forms

from students.models import Student


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'password',
            'phone',
        )

    def clean_phone(self):  # clean_ + field
        phone = self.cleaned_data['phone']
        cleaned_phone = ''.join(i for i in phone if i.isdigit())
        return cleaned_phone

    # start end
    # def clean(self):
    #     pass

    # def save(self, commit=True):
    #     pass
