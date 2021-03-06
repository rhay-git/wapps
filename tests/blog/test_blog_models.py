import pytest

from pytest_factoryboy import LazyFixture

from wapps.blog.models import Blog, BlogPost

from wapps.pytest import assert_can_create_at, assert_can_not_create_at
from wapps.pytest import assert_allowed_subpage_types, assert_allowed_parent_types


@pytest.mark.django_db
def test_blog_hierarchy_restrictions(blog, site):
    assert_allowed_subpage_types(blog, [BlogPost])
    assert_can_create_at(site.root_page.__class__, Blog)
    assert_can_not_create_at(BlogPost, Blog)


@pytest.mark.django_db
def test_blogpost_hierarchy_restrictions(blog_post, site):
    assert_allowed_parent_types(blog_post, [Blog])
    assert_can_not_create_at(site.root_page.__class__, BlogPost)
    assert_can_create_at(Blog, BlogPost)


@pytest.mark.django_db
@pytest.mark.parametrize('blog_post__parent', [LazyFixture('blog')])
def test_blogpost_parent_blog(blog, blog_post):
    assert isinstance(blog_post.blog, Blog)
    assert blog_post.blog == blog
