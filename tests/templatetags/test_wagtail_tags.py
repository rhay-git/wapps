import pytest

from wapps.utils import get_image_url


@pytest.mark.django_db
def test_is_site_root(wrf, jinja, site, page):
    request = wrf.get('/')
    assert site.root_page != page
    assert jinja('{{ is_site_root(page) }}', request=request, page=site.root_page) == 'True'
    assert jinja('{{ is_site_root(page) }}', request=request, page=page) == 'False'
    assert jinja('{{ is_site_root(page) }}', page=site.root_page) == 'False'
    assert jinja('{{ is_site_root(page) }}', request=request, page=None) == 'False'


@pytest.mark.django_db
def test_imageurl(image, jinja):
    rendered = jinja('{{ imageurl(image, "original") }}', image=image)
    assert rendered == get_image_url(image, 'original')
