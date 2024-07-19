from django.db import models


class Item(models.Model):
        first_name = models.CharField(max_length=100, default="")
        middle_name = models.CharField(max_length=100, default="")
        last_name = models.CharField(max_length=100, default="")
        phone = models.CharField(max_length=100, default="")
        email = models.EmailField(max_length=100, default="")
        date_of_birth = models.CharField(max_length=100, default="")
        place_of_birth = models.CharField(max_length=100, default="")
        sex = models.CharField(max_length=100, default="")
        civil_status = models.CharField(max_length=100, default="")
        height = models.CharField(max_length=100, default="")
        weight = models.CharField(max_length=100, default="")
        blood_type = models.CharField(max_length=100, default="")
        gsis_id = models.CharField(max_length=100, default="")
        pag_ibig_id = models.CharField(max_length=100, default="")
        philhealt_id = models.CharField(max_length=100, default="")
        sss_no = models.CharField(max_length=100, default="")
        tin_no = models.CharField(max_length=100, default="")
        agency_employee = models.CharField(max_length=100, default="")
        citizenship = models.CharField(max_length=100, default="")
        residential_address = models.CharField(max_length=100, default="")
        zip_code = models.CharField(max_length=100, default="")
        permanent_address = models.CharField(max_length=100, default="")
        zip_code = models.CharField(max_length=100, default="")
        
        def __str__(self):
            return self.first_name
    
    