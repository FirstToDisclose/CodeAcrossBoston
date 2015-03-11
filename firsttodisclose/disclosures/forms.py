from django import forms

class SubmissionForm(forms.Form):
	title = forms.CharField(max_length=255)
	abstract = forms.CharField(required=False)
	abstract_file = forms.FileField(required=False)

	body = forms.CharField(required=False)
	body_file = forms.FileField(required=False)

	