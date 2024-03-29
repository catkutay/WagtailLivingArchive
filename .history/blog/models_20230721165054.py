from django.contrib.auth.models import User
from django.db import models
from django.template.response import TemplateResponse
from djangokeys import DjangoKeys
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField

# from mirage import fields
from wagtail.core.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import PAGE_TEMPLATE_VAR
from wagtailgmaps.edit_handlers import MapFieldPanel
from wagtailvideos.edit_handlers import VideoChooserPanel

keys = DjangoKeys("./livingarchive/settings/.env")


class BlogListingPage(Page):
    """Listing page list all the blog detail pages"""

    template = "blog/blog_listing_page.html"
    """to limit only 1 home page"""
    max_count = 1
    # get google maps api key from .env
    api_key = keys.str("API_KEY")

    # to get detail from blog detail page

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context"""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = (
            BlogDetailPage.objects.live().all().order_by("-first_published_at")
        )

        return context


class LinkBlock(StructBlock):
    title = CharBlock(required=True, help_text="Enter the link title")
    url = CharBlock(required=True, help_text="Enter the link URL")
    document = DocumentChooserBlock(
        required=False, help_text="Choose a document for this link"
    )


class BlogDetailPage(Page):
    """Blog detail page"""

    # base_form_class = CustomPageForm
    # edit_handler = CustomEditView

    password_required_template = "blog/password_required.html"
    template = "blog/blog_detail_page.html"
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    video = models.ForeignKey(
        "wagtailvideos.Video",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    # Return a hiding version of self.email

    email = User(Page.owner).email.replace("@", " at ")

    address = models.CharField(max_length=255, null=True)

    links = StreamField(
        [
            ("link", LinkBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        ImageChooserPanel("image"),
        VideoChooserPanel("video"),
        FieldPanel("body", classname="full"),
        MapFieldPanel("address", latlng=True, zoom=4),
        StreamFieldPanel("links"),
    ]

    # def get_template(self, request, *args, **kwargs):
    #     tester = self.permissions_for_user(request.user)
    #     # if self.permissions_for_user(request.user):
    #     #     return 'blog/password_required.html'
    #     # Check if the user has permission to view
    #     # print(self.get_view_restrictions())
    #     # can_view = permissions.can_view()
    #     # blog_post = self.specific
    #     # print(blog_post.serve(request))
    #     # return blog_post.serve(request)
    #     # print(BlogDetailPage.objects.private())
    #     return self.template

    def get_context(self, request, *args, **kwargs):
        context = {
            PAGE_TEMPLATE_VAR: self,
            "self": self,
            "request": request,
        }

        if self.context_object_name:
            context[self.context_object_name] = self
        context["accept"] = kwargs["accept"]
        return context

    def serve(self, request, *args, **kwargs):
        if "accept" not in kwargs:
            kwargs["accept"] = True
        request.is_preview = False

        return TemplateResponse(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs),
        )
