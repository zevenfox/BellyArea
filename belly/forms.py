# from django import forms
# from .models import *

# class ChoiceForm (forms.Form):
#     ch_colors = [('#ff0000', 'Red'), ('#O0ffOO', 'Green'),('#0000ff', 'Blue')]
    
#     color = forms.ChoiceField(
#     choices=ch_colors,
#     label='Color',
#     required = False,
#     widget = forms.Radioselect
#     )

#     ch_styles = [('<by>', 'Bold'), ('<i>', 'Italic'),
#                     ('<u>', 'Underline') ]

#     font_style = forms.MultiplecholceField(
#         choices = ch_styles,
#         label='Font Style',
#         required = False,
#         widget = forms.CheckboxselectMultiple
#     )

#     ch_sizes =[('14px', 'Small'), ('16px', 'Medium'),
#                 ( '20px', 'Large') ]
    
#     font_size = forms.ChoiceField(
#     choices=ch_sizes,
#     label='Font Size' ,
#     required=False,
#     widget=forms.Select
#     )

#     ch_families = [('Tahoma', 'Tahoma'), ('Arial', 'Arial'),
#                     ('Times New Roman', 'Times New Roman'),
#                     ('Microsoft Sans serif', 'Microsoft sans serif')]


#     font_family = forms.MultiplechoiceField(
#         choices=ch_families,
#         label='Font Family',
#         required=False,
#         widget=forms. SelectMultiple,
#     )

