from django.db import models
from fndds.models import Food, Weight


class Subject(models.Model):
    name = models.TextField(primary_key=True, max_length=7)

    def __str__(self):
        return self.name


class Meal(models.Model):
    id = models.TextField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    subjectid = models.ForeignKey(Subject,
                                  blank=True,
                                  null=True,
                                  related_name='subs_meals',
                                  on_delete=models.SET_NULL)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id


class Image(models.Model):
    path = models.TextField()
    time = models.TextField(blank=True, null=True)
    mealid = models.ForeignKey(Meal,
                               blank=True,
                               null=True,
                               related_name='meals_images',
                               on_delete=models.SET_NULL)
    subjectid = models.ForeignKey(Subject,
                                  blank=True,
                                  null=True,
                                  related_name='subs_images',
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return self.path


class T1DFood(models.Model):
    meal = models.ForeignKey(Meal,
                              on_delete=models.DO_NOTHING,
                              related_name="t1d_meals_foods",
                              blank=True,
                              null=True)
    food = models.ForeignKey(Food,
                             on_delete=models.DO_NOTHING,
                             related_name="t1d_foods_in_meal")


    def __str__(self):
        return f'{self.meal} {self.food}'


class T1DServing(models.Model):
    food = models.ForeignKey(T1DFood,
                             on_delete=models.CASCADE,)
    servingSize = models.ForeignKey(Weight,
                                    related_name="t1ds_portion_sizes",
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL)
    taken_serving = models.FloatField(blank=True, null=True)
    returned_serving = models.FloatField(blank=True, null=True)