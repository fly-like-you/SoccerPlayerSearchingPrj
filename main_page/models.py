from django.db import models


class Team(models.Model): # 기존에서 팀id를 pk로 받겠습니다.
    teamName = models.CharField(max_length=50)
    coachName = models.CharField(max_length=10)
    homeStadium = models.CharField(max_length=20)
    region = models.CharField(max_length=10)
    rank = models.IntegerField()

    head_image = models.ImageField(upload_to='main_page/images/%Y/%m/%d', blank=True)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL, blank=True,db_column='slug')        # 외래키키
    def __str__(self):
        return self.teamName

    def get_absolute_url(self):
        return f'/main_page/category/{self.category.slug}/'

class Category(models.Model): # 팀별 카테고리 생성
    categoryName = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="organize", unique=True)  # 카테고리 이름
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True) # slug 필드는 사람이 읽을 수 있는 텍스트로 고유 url을 만들때 사용

    def __str__(self):
        return str(self.categoryName)

    def get_absolute_url(self):
        return f'/main_page/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories' # 카테고리 이름 변경





class Player(models.Model):

    name = models.CharField(max_length=10)
    position = models.CharField(max_length=5)
    pass_success_rate = models.IntegerField()
    shoot_success_rate = models.IntegerField()
    height = models.IntegerField(default=170)
    weight = models.IntegerField(default=60)
    nationality = models.CharField(default="kor", max_length=10)
    birthdate = models.DateField(blank=True, null=True, default='2000-01-01')
    jersey_number = models.IntegerField(blank=True, null=True)


    head_image = models.ImageField(upload_to='main_page/images/%Y/%m/%d', blank=True)

    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)        # 외래키키

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/main_page/{self.pk}/'
