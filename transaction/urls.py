from django.urls import path, include
from . import views

urlpatterns = [
    path('upi/', views.UpiTransactionView.as_view()),
    path('online/', views.OnlineTransactionView.as_view()),
    path('loan/', views.LoanDetailView.as_view()),
    path('loan/<int:pk>/', views.LoanDetailSingleView.as_view()),
    path('fixed-deposit/', views.FixedDepositView.as_view()),
]



# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODE0MDQ0NiwiaWF0IjoxNzA3Mjc2NDQ2LCJqdGkiOiJiNGI2NThlN2JlNjk0ZTJmYmY1YzNmNjUwN2U4YmE5NyIsInVzZXJfaWQiOjN9.72Ly5NQ1zbLDmFjnQCi2a1xXKf897XKAQql9NMR-1Xk
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3NzA4NDQ2LCJpYXQiOjE3MDcyNzY0NDYsImp0aSI6ImU3OGFhZWJkYjgxYzQ0OTY5MjFjNDhjYzZlYTkzZDk1IiwidXNlcl9pZCI6M30.nUGFtc_lr3HaVoQgGsFExHiTBo1zJBdPjyxOE1eILFQ


    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODE2OTYzNCwiaWF0IjoxNzA3MzA1NjM0LCJqdGkiOiI2MjQ3MzFhNDUzMGI0OTMwOTJlN2QzMzczMWEwYWE3OCIsInVzZXJfaWQiOjR9.jCrQTOahmPtseNUW6MjaejcK6J7AFMg-BY4qq1pW3KI
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3NzM3NjM0LCJpYXQiOjE3MDczMDU2MzQsImp0aSI6ImViYmRiZTI2MmRhNDRlYzZhNTA0ZjYzYTkwMmViNTRjIiwidXNlcl9pZCI6NH0.TwJGQSfnzNwEQdDuhNulm5yp-THBkBPOHOdqfem9YYs