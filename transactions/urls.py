from django.urls import path
from .views import sign_up_view,  feed_stray_view, get_total_fed_view

urlpatterns = [
    path(
        "sign_up/",
        sign_up_view.sign_up,
        name="sign_up_view"
    ),
    path(
        "feed/<uuid:company_uuid>/",
        feed_stray_view.feed_stray,
        name="product_detail_view",
    ),
    path(
        "total_strays_fed/<uuid:company_uuid>/",
        get_total_fed_view.get_total_fed_by_company,
        name="get_total_fed_by_company",
    ),
    path(
        "total_strays_fed/",
        get_total_fed_view.get_total_fed,
        name="get_total_fed",
    ),
]
