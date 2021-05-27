import graphene
from django.conf import settings
from graphene_django import DjangoObjectType

from .models import Blog, BlogCounts, Tag
from django.contrib.auth.models import User
from accounts.models import Profile


class UserType(DjangoObjectType):
    class Meta:
        model = User


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog


class BlogCountsType(DjangoObjectType):
    class Meta:
        model = BlogCounts


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(graphene.ObjectType):
    all_posts = graphene.List(BlogType)
    author_by_username = graphene.Field(UserType, username=graphene.String())
    post_by_slug = graphene.Field(BlogType, slug=graphene.String())
    posts_by_author = graphene.List(BlogType, username=graphene.String())
    posts_by_tag = graphene.List(BlogType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return (
            Blog.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            Blog.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            Blog.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            Blog.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )

    def resolve_author_by_username(root, info, username):
        return User.objects.select_related("profile").get(
            profile__user__username=username
        )


schema = graphene.Schema(query=Query)
