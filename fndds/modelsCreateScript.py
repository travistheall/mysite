import pandas as pd
from fndds.models import *

main = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_MainFoodDesc.xlsx')
for x in range(len(main)):
    Food(id=main["FoodCode"][x],
         desc=main["MainFoodDesc"][x],
         wweia_cat_num=main["WWEIACategoryNumber"][x],
         wweia_cat_desc=main["WWEIACategoryDesc"][x],
         start_date=main["StartDate"][x],
         end_date=main["EndDate"][x]).save()

port = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_FoodPortionDesc.xlsx')
for x in range(len(port)):
    Portion(id=port["PortionCode"][x],
            name=port["PortionDescription"][x],
            start_date=port["StartDate"][x],
            end_date=port["EndDate"][x]).save()

nut = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_NutDesc.xlsx')
for x in range(len(nut)):
    Nutrient(id=nut["NutrientCode"][x],
             name=nut["NutrientDesc"][x],
             tag=nut["Tagname"][x],
             unit=nut["Unit"][x],
             decimals=nut["Decimals"][x]).save()

subcode = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_SubcodeDesc.xlsx')
for x in range(len(subcode)):
    Subcode(id=subcode["Subcode"][x],
            name=subcode["SubcodeDesc"][x],
            start_date=subcode["StartDate"][x],
            end_date=subcode["EndDate"][x]).save()

deriv = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_DerivDesc.xlsx')
for x in range(len(deriv)):
    Derivation(id=deriv["DerivationCode"][x], name=deriv["DerivationDescription"][x]).save()

add = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_AddFoodDesc.xlsx')
for x in range(len(add)):
    Description(food=Food.objects.get(id=add["FoodCode"][x]),
                seq_num=add["SeqNum"][x],
                desc=add["AddFoodDesc"][x],
                start_date=add["StartDate"][x],
                end_date=add["EndDate"][x]).save()

nutVal = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_NutVal.xlsx')
for x in range(len(nutVal)):
    NutrientValue(food=Food.objects.get(id=nutVal["FoodCode"][x]),
                  nutrient=Nutrient.objects.get(id=nutVal["NutrientCode"][x]),
                  value=nutVal["NutrientValue"][x],
                  start_date=nutVal["StartDate"][x],
                  end_date=nutVal["EndDate"][x]).save()

weight = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_FoodWeights.xlsx')
for x in range(len(weight)):
    Weight(food=Food.objects.get(id=weight["FoodCode"][x]),
           seq_num=weight["SeqNum"][x],
           portion=Portion.objects.get(id=weight['PortionCode'][x]),
           subcode=Subcode.objects.get(id=weight["Subcode"][x]),
           value=weight["PortionWeight"][x],
           start_date=weight["StartDate"][x],
           end_date=weight["EndDate"][x]).save()

#for x in range(len(weight)):
#    if weight["Subcode"][x] > 0:
#        w = Weight.objects.get(food=Food.objects.get(id=weight["FoodCode"][x]),
#                               seq_num=weight["SeqNum"][x],
#                               portion=Portion.objects.get(id=weight['PortionCode'][x]),
#                               value=weight["PortionWeight"][x])
#        w.subcode.add(Subcode.objects.get(id=weight["Subcode"][x]))

#weightsublink = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_FoodSubcodeLinks.xlsx')
#for x in range(len(weightsublink)):
#    WeightSubcodeLink(food=Weight.objects.get(food=Food.objects.get(id=weightsublink["FoodCode"][x]),
#                      nutrient=Nutrient.objects.get(id=weightsublink["Subcode"][x]),
#                      start_date=weightsublink["StartDate"][x],
#                      end_date=weightsublink["EndDate"][x]).save()

ingred = pd.read_excel('D:/Database creation/mysite/fndds/modelData/fndds_Ingred.xlsx')
for x in range(len(ingred)):
    i = Ingredient(food=Food.objects.get(id=ingred["FoodCode"][x]),
                   seq_num=ingred["SeqNum"][x],
                   code=ingred["IngredCode"][x],
                   name=ingred["IngredDesc"][x],
                   amount=ingred["Amount"][x],
                   measure=ingred["Measure"][x],
                   portion=Portion.objects.get(id=ingred["PortionCode"][x]),
                   retention=ingred["RetentionCode"][x],
                   weight=ingred["IngredientWeight"][x],
                   start_date=ingred["StartDate"][x],
                   end_date=ingred["EndDate"][x]).save()
