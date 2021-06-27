from django.forms.utils import ErrorList

class DivErrorList(ErrorList):
     def __str__(self):
         return self.as_divs()
     def as_divs(self):
         if not self: return ''
         return '<div class="errorlist">%s</div>' % ''.join(['<div class="alert alert-danger">%s</div>' % e for e in self])