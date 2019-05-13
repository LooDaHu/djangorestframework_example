from django.db import models
from django.utils.timezone import utc
from datetime import datetime

'''
Be careful, model 2 is before model 1, due to we have a foreign key that related to model 2
 at model 1
'''


class Model2(models.Model):
    # The primary key of model 2
    model2_id = models.AutoField(primary_key=True, db_column='Model2Id')
    model2_int = models.IntegerField(db_column='Model2Int', default=1)

    def __int__(self):
        return self.model2_id


# Create your models here.
class Model1(models.Model):
    # Create primary key first.
    model1_id = models.AutoField(primary_key=True, db_column='Model1Id')

    # An example of integer field.
    model1_int = models.IntegerField(db_column='Model1Int', default=1)

    # An example of datetime field.
    model1_datetime = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc),
                                           db_column='Model1DateTime')

    # You can also use auto_now_add, which default will be the datetime of creating item
    '''
     Tip: add_now = True, once the item is accessed, 
     the datetime will be updated automatically to the datetime of accessing
    '''
    # model1_datetime = models.DateTimeField(auto_now_add=True, db_column='Model1DateTime')

    # An example of text field.
    model1_text = models.TextField(db_column='Model1Text')

    # An example of text field.
    model2_id = models.ForeignKey(Model2, on_delete=models.CASCADE, db_column='Model2Id')

    def __int__(self):
        return self.model1_id
