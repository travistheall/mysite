from django.db import models


class Food(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    desc = models.CharField(max_length=184)
    wweia_cat_num = models.PositiveSmallIntegerField()
    wweia_cat_desc = models.CharField(max_length=48)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.desc


class Portion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=114)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Nutrient(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    tag = models.CharField(max_length=10)
    unit = models.CharField(max_length=7)
    decimals = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Subcode(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=63)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Derivation(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


#TODO: Add fndds_ingrednutval!
class Ingredient(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name="ingredients")
    seq_num = models.PositiveSmallIntegerField()
    code = models.IntegerField()
    name = models.CharField(max_length=134)
    amount = models.DecimalField(max_digits=8, decimal_places=4)
    measure = models.CharField(max_length=3)
    portion = models.ForeignKey('Portion', on_delete=models.CASCADE, related_name="ingredients")
    retention = models.PositiveSmallIntegerField()
    weight = models.IntegerField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Moisture(models.Model):
    food = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    change = models.SmallIntegerField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __int__(self):
        return self.change


class Description(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name="descriptions")
    seq_num = models.PositiveSmallIntegerField()
    desc = models.CharField(max_length=80)
    wweia_cat_desc = models.CharField(max_length=48)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.desc


class NutrientValue(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name="nutrient_values")
    nutrient = models.ForeignKey('Nutrient', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=8, decimal_places=3)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __int__(self):
        return self.value


class Weight(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name="food_weights")
    subcode = models.ForeignKey('Subcode', on_delete=models.CASCADE)
    seq_num = models.PositiveSmallIntegerField()
    portion = models.ForeignKey('Portion', on_delete=models.CASCADE, related_name="portion_weights")
    value = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __int__(self):
        return self.value

#TODO: Fix WeightSubCodeLink
#class WeightSubcodeLink(models.Model):
#    food = models.ForeignKey('Weight', on_delete=models.CASCADE)
#    subcode = models.ForeignKey('Subcode', on_delete=models.CASCADE)
#    start_date = models.DateField(auto_now=False, auto_now_add=False)
#    end_date = models.DateField(auto_now=False, auto_now_add=False)
