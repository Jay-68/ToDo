from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter ToDo e.g. Delete junk files',
                                      'arial-label': 'Todo', 'aria-describeby': 'add-btn'}
                           ))
