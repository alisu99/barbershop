from django.urls import path
from .views import processar_pagamento

urlpatterns = [
    path('processar_pagamento/', processar_pagamento, name='processar_pagamento'),
]
