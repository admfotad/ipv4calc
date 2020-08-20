from django import forms


IMP_CHOICES = (
    ('1', '255.255.255.254/31 '),
    ('2', '255.255.255.252/30 '),
    ('3', '255.255.255.248/29 '),
    ('4', '255.255.255.240/28 '),
    ('5', '255.255.255.224/27 '),
    ('6', '255.255.255.192/26 '),
    ('7', '255.255.255.128/25 '),
    ('8', '255.255.255.0/24 '),
    ('9', '255.255.254.0/23 '),
    ('10', '255.255.252.0/22 '),
    ('11', '255.255.248.0/21 '),
    ('12', '255.255.240.0/20 '),
    ('13', '255.255.224.0/19 '),
    ('14', '255.255.192.0/18 '),
    ('15', '255.255.128.0/17 '),
    ('16', '255.255.0.0/16 '),
    ('17', '255.254.0.0/15 '),
    ('18', '255.252.0.0/14 '),
    ('19', '255.248.0.0/13 '),
    ('20', '255.240.0.0/12 '),
    ('21', '255.224.0.0/11 '),
    ('22', '255.192.0.0/10 '),
    ('23', '255.128.0.0/9 '),
    ('24', '255.0.0.0/8 '),
)


class Calc(forms.Form):
    IPv4_address = forms.CharField(required=True, initial='192.168.0.1')
    Subnet_mask = forms.ChoiceField(choices=IMP_CHOICES, required=True, initial='255.255.255.0')
#    Content = forms.CharField(
#        required=True,
#        widget=forms.Textarea
#    )