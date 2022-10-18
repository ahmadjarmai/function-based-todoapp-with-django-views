from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model) :

    name =models.CharField(max_length =200)
    body =models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    completed =models.BooleanField(default=False)
    user =models.ForeignKey(User, on_delete=models.CASCADE, null =True)

    class Meta :
        ordering =['-created']

    def __Str__(self) :
        return self.name
