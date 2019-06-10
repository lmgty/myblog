from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    用户表
    """
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, verbose_name="用户名")
    create_time = models.DateTimeField(auto_now_add=True)

    # 一对一
    blog = models.OneToOneField(to="Blog", to_field="nid", null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Blog(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, verbose_name="个人博客标题")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog站点"
        verbose_name_plural = verbose_name


class Tag(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name="标签名称")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="文章标题")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    comment_count = models.IntegerField(verbose_name="评论数", default=0)
    up_count = models.IntegerField(verbose_name="点赞数", default=0)
    down_count = models.IntegerField(verbose_name="踩数", default=0)

    user = models.ForeignKey(to="UserInfo", to_field="nid")
    tags = models.ManyToManyField(
        to="Tag",
        through="Article2Tag",
        through_fields=("article", "tag"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class ArticleDetail(models.Model):

    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.OneToOneField(to="Article", to_field="nid")

    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name


class Article2Tag(models.Model):
    """
    文章和标签的多对多关系表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid")
    tag = models.ForeignKey(to="Tag", to_field="nid")

    def __str__(self):
        return "{}-{}".format(self.article.title, self.tag.title)

    class Meta:
        unique_together = (("article", "tag"),)
        verbose_name = "文章-标签"
        verbose_name_plural = verbose_name


class ArticleUpDown(models.Model):
    """
    点赞表
    """
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="UserInfo", null=True)
    article = models.ForeignKey(to="Article", null=True)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = (("article", "user"),)
        verbose_name = "文章点赞"
        verbose_name_plural = verbose_name


class Comment(models.Model):

    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid")
    user = models.ForeignKey(to="UserInfo", to_field="nid")
    content = models.CharField(max_length=255, verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    parent_comment = models.ForeignKey("self", null=True, blank=True)

    def __str__(self):
        return self.content

    verbose_name = "评论"
    verbose_name_plural = verbose_name
