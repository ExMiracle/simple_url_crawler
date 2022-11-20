from django.forms import forms, URLField


class URLForm(forms.Form):
    url = URLField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': "form-control"})
