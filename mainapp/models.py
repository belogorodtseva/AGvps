from django.db import models
#################################################################### SERVICES #####

class Architects_supervision(models.Model):
    name_en = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    name_ua = models.CharField(max_length=50)
    description_en = models.CharField(max_length=300, default='some string')
    description_ru = models.CharField(max_length=300, default='some string')
    description_ua = models.CharField(max_length=300, default='some string')
    terms_name_en = models.CharField(max_length=100)
    terms_name_ru = models.CharField(max_length=100)
    terms_name_ua = models.CharField(max_length=100)
    terms_en = models.CharField(max_length=100)
    terms_ru = models.CharField(max_length=100)
    terms_ua = models.CharField(max_length=100)
    cost_name_en = models.CharField(max_length=100)
    cost_name_ru = models.CharField(max_length=100)
    cost_name_ua = models.CharField(max_length=100)
    cost_en = models.CharField(max_length=100)
    cost_ru = models.CharField(max_length=100)
    cost_ua = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))

class Paragraphs_AS(models.Model):
    paragraph_en = models.CharField(max_length=300, default='some string')
    paragraph_ru = models.CharField(max_length=300, default='some string')
    paragraph_ua = models.CharField(max_length=300, default='some string')


    def __str__(self):
        return self.paragraph_en

class Architecture(models.Model):
    name_en = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    name_ua = models.CharField(max_length=50)
    description_en = models.CharField(max_length=300, default='some string')
    description_ru = models.CharField(max_length=300, default='some string')
    description_ua = models.CharField(max_length=300, default='some string')
    terms_name_en = models.CharField(max_length=100)
    terms_name_ru = models.CharField(max_length=100)
    terms_name_ua = models.CharField(max_length=100)
    terms_en = models.CharField(max_length=100)
    terms_ru = models.CharField(max_length=100)
    terms_ua = models.CharField(max_length=100)
    cost_name_en = models.CharField(max_length=100)
    cost_name_ru = models.CharField(max_length=100)
    cost_name_ua = models.CharField(max_length=100)
    cost_en = models.CharField(max_length=100)
    cost_ru = models.CharField(max_length=100)
    cost_ua = models.CharField(max_length=100)
    schematic_desing_name_en =  models.CharField(max_length=100)
    schematic_desing_name_ru =  models.CharField(max_length=100)
    schematic_desing_name_ua =  models.CharField(max_length=100)
    desing_development_name_en =  models.CharField(max_length=100)
    desing_development_name_ru =  models.CharField(max_length=100)
    desing_development_name_ua =  models.CharField(max_length=100)
    construction_documents_name_en =  models.CharField(max_length=100)
    construction_documents_name_ru =  models.CharField(max_length=100)
    construction_documents_name_ua =  models.CharField(max_length=100)
    construction_documents_description_en = models.CharField(max_length=100, default='description')
    construction_documents_description_ru = models.CharField(max_length=100, default='description')
    construction_documents_description_ua = models.CharField(max_length=100, default='description')

    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))

class Paragraphs_Arch_SD(models.Model):
    paragraph_en = models.CharField(max_length=300, default='some string')
    paragraph_ru = models.CharField(max_length=300, default='some string')
    paragraph_ua = models.CharField(max_length=300, default='some string')


    def __str__(self):
        return self.paragraph_en

class Paragraphs_Arch_DD(models.Model):
    paragraph_en = models.CharField(max_length=300, default='some string')
    paragraph_ru = models.CharField(max_length=300, default='some string')
    paragraph_ua = models.CharField(max_length=300, default='some string')


    def __str__(self):
        return self.paragraph_en

class Paragraphs_Arch_CD(models.Model):
    paragraph_en = models.CharField(max_length=300, default='some string')
    paragraph_ru = models.CharField(max_length=300, default='some string')
    paragraph_ua = models.CharField(max_length=300, default='some string')


    def __str__(self):
        return self.paragraph_en

class Interior_design(models.Model):
    name_en = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    name_ua = models.CharField(max_length=50)
    description_en = models.CharField(max_length=300, default='some string')
    description_ru = models.CharField(max_length=300, default='some string')
    description_ua = models.CharField(max_length=300, default='some string')
    paragraphs_name_en = models.CharField(max_length=100)
    paragraphs_name_ru = models.CharField(max_length=100)
    paragraphs_name_ua = models.CharField(max_length=100)
    terms_name_en = models.CharField(max_length=100)
    terms_name_ru = models.CharField(max_length=100)
    terms_name_ua = models.CharField(max_length=100)
    terms_en = models.CharField(max_length=100)
    terms_ru = models.CharField(max_length=100)
    terms_ua = models.CharField(max_length=100)
    cost_name_en = models.CharField(max_length=100)
    cost_name_ru = models.CharField(max_length=100)
    cost_name_ua = models.CharField(max_length=100)
    cost_en = models.CharField(max_length=100)
    cost_ru = models.CharField(max_length=100)
    cost_ua = models.CharField(max_length=100)


    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))

class Paragraphs_ID(models.Model):
    paragraph_en = models.CharField(max_length=300, default='some string')
    paragraph_ru = models.CharField(max_length=300, default='some string')
    paragraph_ua = models.CharField(max_length=300, default='some string')


    def __str__(self):
        return self.paragraph_en

class Product_design(models.Model):
    name_en = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    name_ua = models.CharField(max_length=50)
    description_en = models.CharField(max_length=300, default='some string')
    description_ru = models.CharField(max_length=300, default='some string')
    description_ua = models.CharField(max_length=300, default='some string')
    paragraphs_name_en = models.CharField(max_length=100)
    paragraphs_name_ru = models.CharField(max_length=100)
    paragraphs_name_ua = models.CharField(max_length=100)
    terms_name_en = models.CharField(max_length=100)
    terms_name_ru = models.CharField(max_length=100)
    terms_name_ua = models.CharField(max_length=100)
    terms_en = models.CharField(max_length=100)
    terms_ru = models.CharField(max_length=100)
    terms_ua = models.CharField(max_length=100)
    cost_name_en = models.CharField(max_length=100)
    cost_name_ru = models.CharField(max_length=100)
    cost_name_ua = models.CharField(max_length=100)
    cost_en = models.CharField(max_length=100)
    cost_ru = models.CharField(max_length=100)
    cost_ua = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))

class Paragraphs_PD(models.Model):
    paragraph_en = models.CharField(max_length=300, default='some string')
    paragraph_ru = models.CharField(max_length=300, default='some string')
    paragraph_ua = models.CharField(max_length=300, default='some string')


    def __str__(self):
        return self.paragraph_en


############################################################################## PROJECTS #######

class Arch_projects(models.Model):
    name_en = models.CharField(max_length=300)
    name_ru = models.CharField(max_length=300)
    name_ua = models.CharField(max_length=300)
    description_en = models.CharField(max_length=600)
    description_ru = models.CharField(max_length=600)
    description_ua = models.CharField(max_length=600)
    mainimg = models.FileField(null=True)

    side = models.CharField(max_length=20, default='L')
    number = models.IntegerField(default='1')

    def __str__(self):
        return '%s - %s' % (str(self.name_en), str(self.number))


class Arch_photo(models.Model):
    archimg = models.FileField(null=True)
    project = models.ForeignKey(Arch_projects)

    def __str__(self):
        return str(self.project)

class Design_projects(models.Model):
    name_en = models.CharField(max_length=300)
    name_ru = models.CharField(max_length=300)
    name_ua = models.CharField(max_length=300)
    description_en = models.CharField(max_length=600)
    description_ru = models.CharField(max_length=600)
    description_ua = models.CharField(max_length=600)
    mainimg = models.FileField(null=True)
    side = models.CharField(max_length=20, default='L')
    number = models.IntegerField(default='1')

    def __str__(self):
        return '%s - %s' % (str(self.name_en), str(self.number))


class Design_photo(models.Model):
    designimg = models.FileField(null=True)
    project = models.ForeignKey(Design_projects)

    def __str__(self):
        return str(self.project)
