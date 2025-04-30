# Activate your virtual environment
# source venv/bin/activate 

# Or on windows: 
# venv\Scripts\activate 

# Navigate to your project folder: 
# cd your_project_folder 

# Run the server: 
# python manage.py chabgepassword your_superuser_username 

# Example: 

# python manage.py changepassword admin

# Method - 2: Use the Django Shell
# python manage.py shell 

# Then run the following code: 
# from django.contrib.auth import get_user_model
# User = get_user_model()
# user = User.objects.get(username='admin')
# user.set_password("new_secure_password")
# user.save()

# exit()

# Method - 3: Use the Django Admin (if you`re logged in)
# Go to your Django admin page, usually at http://127.0.0.1:8000/admin/.

# Log in with your current credentials.

# Click on Users.

# Find your superuser account and click on it.

# Scroll down to the “Password” section and click "this form" under the "Raw passwords are not stored..." message.

# Enter your new password twice and save.

# Bonus : Forgot Your SuperUser Username ?
# python manage.py shell
#  and then type: 
# from django.contrib.auth import get_user_model

# User = get_user_model()

# for user in User.objects.all():
#     print(user.username)

