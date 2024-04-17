from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def timepassed(self):
        # delta = timezone.now() - self.created_at
        # return delta.days, delta.seconds//3600, (delta.seconds//60)%60
    
        time_difference = timezone.now() - self.created_at
        total_seconds = int(time_difference.total_seconds())
        
        days = total_seconds // (24*60*60)
        total_seconds %= (24*60*60)
    
        hours = total_seconds // (60*60)
        total_seconds %= (60*60)
    
        minutes = total_seconds // 60
    
        return f"{days} days, {hours} hours, {minutes} minutes"
    
    
    def user_attributes(self):
        return {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'date_joined': self.user.date_joined,
            'last_login': self.user.last_login,
            'is_active': self.user.is_active,
            'is_staff': self.user.is_staff,
            'is_superuser': self.user.is_superuser,
            'groups': [group.name for group in self.user.groups.all()],
            'user_permissions': [perm.codename for perm in self.user.user_permissions.all()],
            'todos': [todo.title for todo in self.user.todo_set.all()],
        }